from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team, Profile
# from questions.models import Question
from .serializers import TeamSerializer, ProfileSerializer, LoginSerializer, ProfileUpdateSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

class TeamCreateAPIView(APIView):
    def post(self,request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"team_id": serializer.data["id"]}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeamJoinAPIView(APIView):
    def post(self, request, team_id):
        team = get_object_or_404(Team, id=team_id)
        profile_serializer = ProfileSerializer(data=request.data)
        if profile_serializer.is_valid():
            profile_serializer.save(team=team)
            return Response({"message": "Profile created successfully"}, status=status.HTTP_201_CREATED)
        return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeamUpdateAPIView(APIView):
    def put(self, request, team_id):
        team = get_object_or_404(Team, id=team_id)
        serializer = TeamSerializer(team, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "Team information updated successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeamDetailAPIView(APIView):
    def get(self, request, team_id):
        team = get_object_or_404(Team, id=team_id)
        serializer = TeamSerializer(team)
        return Response(serializer.data)
    
class ProfileCreateAPIView(APIView):
    def post(self, request, team_id):
        team = get_object_or_404(Team, id=team_id)
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(team=team)
            return Response({"Profile_id": serializer.data["id"], "message": "Profile created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetailAPIView(APIView):
    def get(self, request, team_id, profile_id):
        profile = get_object_or_404(Profile, id=profile_id, team_id=team_id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

class TeamLoginOrRegisterAPIView(APIView):
    def post(self, request, team_id):
        team = get_object_or_404(Team, id=team_id)
        name = request.data.get("name")
        dob = request.data.get("dob")

        # 팀 내에서 이름과 생년월일로 사용자 조회
        profile = Profile.objects.filter(team=team, user_name=name, birth_date=dob).first()

        if profile:
            # 로그인 성공, 토큰 발급
            refresh = RefreshToken.for_user(profile)
            return Response({
                "message": "Login successful",
                "profile_id": profile.id,
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            }, status=status.HTTP_200_OK)
        else:
            # 새로운 프로필이 팀의 첫 번째 프로필인지 확인
            is_leader = not Profile.objects.filter(team=team).exists()

            # 회원가입 및 로그인 처리
            login_serializer = LoginSerializer(data={
                "team": team.id, 
                "user_name": name, 
                "birth_date": dob, 
                "role": "team leader" if is_leader else "member"
                })
            if login_serializer.is_valid():
                profile = login_serializer.save()

                # 토큰 발급
                refresh = RefreshToken.for_user(profile)
                return Response({
                    "message": "Registered and logged in",
                    "profile_id": login_serializer.data["id"],
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh)
                }, status=status.HTTP_201_CREATED)
            return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#팀원 정보 전체 조회
class TeamProfilesAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        return Profile.objects.filter(team__id=team_id)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # 각 팀원의 프로필이 완전히 입력되었는지 확인
        all_complete = all(
            profile.user_name and profile.birth_date and profile.phone and profile.email and profile.github_address
            and profile.participation_field and profile.location and profile.affiliations and profile.mbti and profile.stack
            and profile.preferred_os and profile.editor_mode and profile.work_environment and profile.collaboration_environment
            and profile.focus_time and profile.project_style and profile.communication_style
            for profile in queryset
        )
        
        # 기존 프로필 데이터와 함께 all_complete 값을 추가하여 응답
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "profiles": serializer.data,
            "all_complete": all_complete
        })
    

class ProfileUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # 현재 로그인한 사용자 프로필 반환
        return Profile.objects.get(id=self.request.user.profile.id)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        # 유효성 검사 및 저장
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)