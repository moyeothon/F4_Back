from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team, Profile
# from questions.models import Question
from .serializers import TeamSerializer, ProfileSerializer, LoginSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken

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
            # 회원가입 및 로그인 처리
            login_serializer = LoginSerializer(data={"team": team.id, "user_name": name, "birth_date": dob})
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