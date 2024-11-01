from rest_framework import serializers
from .models import Test, Choice, TestAnswer

# Choice Serializer
class ChoiceSerializer(serializers.ModelSerializer):
    choice_id = serializers.IntegerField(source='id')
    choice_text = serializers.CharField()

    class Meta:
        model = Choice
        fields = ['choice_id', 'choice_text']

# Test Serializer (질문과 선택지를 함께 반환)
class TestSerializer(serializers.ModelSerializer):
    test_id = serializers.IntegerField(source='id')
    test_text = serializers.CharField()
    choices = ChoiceSerializer(many=True)
    
    class Meta:
        model = Test
        fields = ['test_id', 'test_text', 'choices']

# TestAnswer Serializer (사용자의 응답을 저장)
class TestAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAnswer
        fields = ['profile', 'test', 'choice']