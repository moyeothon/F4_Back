from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team, Profile
# from questions.models import Question
from .serializers import TeamSerializer, ProfileSerializer
from django.shortcuts import get_object_or_404

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
            profile_serializer.save()
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
            serializer.save()
            return Response({"Profile_id": serializer.data["id"], "message": "Profile created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetailAPIView(APIView):
    def get(self, request, team_id, profile_id):
        profile = get_object_or_404(Profile, id=profile_id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)





