from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer

# Create your views here.
class QuestionListAPIView(APIView):
    def get(self, request):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AnswerCreateAPIView(APIView):
    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Answer saved successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAnswerListAPIView(APIView):
    def get(self, request, user_id):
        answers = Answer.objects.filter(user_name=user_id)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)