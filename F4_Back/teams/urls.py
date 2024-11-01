from django.urls import path
from .views import TeamCreateAPIView, TeamJoinAPIView, TeamUpdateAPIView, TeamDetailAPIView, ProfileCreateAPIView, ProfileDetailAPIView

urlpatterns = [

    # 팀 생성
    path('teams/', TeamCreateAPIView.as_view(), name='team-create'),

    # 팀 참여
    path('teams/<uuid:team_id>/join/', TeamJoinAPIView.as_view(), name='team-join'),

    # 팀 정보 업데이트
    path('teams/<uuid:team_id>/', TeamUpdateAPIView.as_view(), name='team-update'),

    # 팀 정보 조회
    path('teams/<uuid:team_id>/', TeamDetailAPIView.as_view(), name='team-detail'),

    # 프로필 생성
    path('teams/<uuid:team_id>/profile/', ProfileCreateAPIView.as_view(), name='profile-create'),

    # 프로필 조회
    path('teams/<uuid:team_id>/profile/<int:profile_id>/', ProfileDetailAPIView.as_view(), name='profile-detail'),
]