from django.urls import path
from .views import GPTAPIView

urlpatterns = [
    path('gpt/ask/<uuid:team_id>/', GPTAPIView.as_view(), name='gpt-ask'),
]