from rest_framework import serializers
from .models import Team, Profile, ProfileQuestionAnswer

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'team_name', 'member_count', 'rules', 'goals']
        extra_kwargs = {
            'rules': {'required': False},
            'goals': {'required': False},
        }
class ProfileSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    class Meta:
        model = Profile
        fields = [
            'id',
            'role',
            'user_name',
            'birth_date',
            'profile_image',
            'phone',
            'email',
            'github_address',
            'participation_field',
            'location',
            'affiliations',
            'mbti',
            'stack',
            'preferred_os',
            'editor_mode',
            'work_environment',
            'collaboration_environment',
            'focus_time',
            'project_style',
            'communication_style',
            'team',
        ]

class LoginSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Profile
        fields = [
            'id', 
            'user_name',
            'role',
            'birth_date', 
            'mbti', 
            'affiliations', 
            'location', 
            'participation_field', 
            'team',
            'preferred_os',  
            'editor_mode', 
            'work_environment', 
            'collaboration_environment', 
            'focus_time', 
            'project_style', 
            'communication_style'
        ]
        extra_kwargs = {
            'role': {'required': False},
            'mbti': {'required': False},
            'affiliations': {'required': False},
            'location': {'required': False},
            'participation_field': {'required': False},
            'team': {'required': False},
            'preferred_os': {'required': False},
            'editor_mode': {'required': False},
            'work_environment': {'required': False},
            'collaboration_environment': {'required': False},
            'focus_time': {'required': False},
            'project_style': {'required': False},
            'communication_style': {'required': False},
        }

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'phone',
            'email',
            'github_address',
            'participation_field',
            'location',
            'affiliations',
            'mbti',
            'stack',
            'preferred_os',
            'editor_mode',
            'work_environment',
            'collaboration_environment',
            'focus_time',
            'project_style',
            'communication_style'
        ]
        extra_kwargs = {field: {'required': False} for field in fields}

class ProfileQuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileQuestionAnswer
        fields = ['profile', 'question_id', 'answer_id']