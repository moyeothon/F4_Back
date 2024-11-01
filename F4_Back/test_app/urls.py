from django.urls import path
from .views import TestListAPIView, TestDetailAPIView, TestAnswerCreateAPIView, TestAnswerListAPIView

urlpatterns = [
    # 전체 질문 목록 조회
    path('tests/', TestListAPIView.as_view(), name='test-list'),
    # 특정 질문 ID 조회
    path('tests/<int:pk>/', TestDetailAPIView.as_view(), name='test-detail'),
    # 사용자 응답 저장
    path('tests/answer/', TestAnswerCreateAPIView.as_view(), name='test-answer'),
    # 특정 사용자 응답 조회
    path('tests/answers/<int:profile_id>/', TestAnswerListAPIView.as_view(), name='test-answer-user'),
    # 특정 팀의 팀원 응답 조회
    # path('api/tests/answers/team/<int:team_id>/', .as_view(), name='team-answers'),
]

