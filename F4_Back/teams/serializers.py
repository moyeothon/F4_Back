from rest_framework import serializers
from .models import Team, Profile

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'member_count']

class ProfileSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    class Meta:
        model = Profile
        fields = [
            'id',
            'user_name',
            'birth_date',
            'age',
            'mbti',
            'affiliations',
            'location',
            'participation_field',
            'team'
        ]