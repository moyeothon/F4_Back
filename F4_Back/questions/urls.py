from django.urls import path
from .views import QuestionListAPIView, AnswerCreateAPIView, UserAnswerListAPIView

urlpatterns = [
    # 질문 가져오기, 질문 추가하기
    path('questions/', QuestionListAPIView.as_view(), name='question-list'),

    # 응답 저장
    path('questions/answer/', AnswerCreateAPIView.as_view(), name='answer-create'),

    # 응답 기록
    path('questions/answers/<str:user_id>/', UserAnswerListAPIView.as_view(), name='user-answer-list'),
]