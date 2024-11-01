from django.urls import path
from .views import GPTAPIView

urlpatterns = [
    path('gpt/ask/', GPTAPIView.as_view(), name='gpt-ask'),  # POST 요청으로 질문을 보낼 URL
]