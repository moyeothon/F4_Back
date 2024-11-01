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

class LoginSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Profile
        fields = ['id', 'user_name', 'birth_date', 'age', 'mbti', 'affiliations', 'location', 'participation_field', 'team']
        extra_kwargs = {
            'age': {'required': False},
            'mbti': {'required': False},
            'affiliations': {'required': False},
            'location': {'required': False},
            'participation_field': {'required': False},
        }
