from rest_framework import serializers
from .models import Team, Profile

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        medel = Team
        fields = ['id', 'member_count']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'user_name',
            'age',
            'mbti',
            'affiliations',
            'location',
            'participation_field'
        ]