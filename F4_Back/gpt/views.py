from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY


