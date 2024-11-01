# survey/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Test, TestAnswer
from .serializers import TestSerializer, TestAnswerSerializer

# 전체 질문 목록 조회
class TestListAPIView(APIView):
    def get(self, request):
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 특정 질문 ID로 질문과 선택지 가져오기
class TestDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            test = Test.objects.get(pk=pk)
            serializer = TestSerializer(test)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Test.DoesNotExist:
            return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)

# 사용자 응답 저장
class TestAnswerCreateAPIView(APIView):
    def post(self, request):
        serializer = TestAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# 특정 사용자의 모든 응답 조회
class TestAnswerListAPIView(APIView):
    def get(self, request, profile_id):
        # 특정 사용자의 모든 TestAnswer 객체를 조회
        testanswers = TestAnswer.objects.filter(profile__id=profile_id)
        if testanswers.exists():
            serializer = TestAnswerSerializer(testanswers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
