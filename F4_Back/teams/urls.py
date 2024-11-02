from django.urls import path
from .views import TeamCreateAPIView, TeamJoinAPIView, TeamUpdateAPIView, TeamDetailAPIView, ProfileCreateAPIView, ProfileDetailAPIView, TeamLoginOrRegisterAPIView, TeamProfilesAPIView, ProfileUpdateAPIView, ProfileQuestionAnswerCreateAPIView

urlpatterns = [

    # 팀 생성
    path('teams/', TeamCreateAPIView.as_view(), name='team-create'),

    # 팀 참여
    path('teams/<uuid:team_id>/join/', TeamJoinAPIView.as_view(), name='team-join'),

    # 팀 정보 업데이트
    path('teams/<uuid:team_id>/', TeamUpdateAPIView.as_view(), name='team-update'),

    # 팀 정보 조회
    path('teams/<uuid:team_id>/', TeamDetailAPIView.as_view(), name='team-detail'),

    #팀원 정보 전체 조회
    path('teams/<uuid:team_id>/profiles/', TeamProfilesAPIView.as_view(), name='team-profiles'),

    # 프로필 생성
    path('teams/<uuid:team_id>/profile/', ProfileCreateAPIView.as_view(), name='profile-create'),

    # 프로필 업데이트
    path('teams/<uuid:team_id>/profile/<int:profile_id>/update/', ProfileUpdateAPIView.as_view(), name='profile-update'),

    # 프로필 조회
    path('teams/<uuid:team_id>/profile/<int:profile_id>/', ProfileDetailAPIView.as_view(), name='profile-detail'),

    #로그인
    path('teams/<uuid:team_id>/login/', TeamLoginOrRegisterAPIView.as_view(), name="login"),

    path('teams/<uuid:team_id>/profiles/<int:profile_id>/answers/', ProfileQuestionAnswerCreateAPIView.as_view(), name='profile-question-answer-create'),
]