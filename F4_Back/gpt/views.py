from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai
from django.conf import settings
import os

openai.api_key = settings.OPENAI_API_KEY
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_message(filename):
    file_path = os.path.join(BASE_DIR, 'gpt', filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
system_content = load_message("system_message.txt")
user_content = load_message("user_message.txt")
assistant_content_example = load_message("assistant_message.txt")
class GPTAPIView(APIView):
    def post(self, request):
        user_content = request.data.get("user_content")

        if not user_content:
            return Response({'error': "내용이 필요합니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            response = openai.ChatCompletion.create(
                model ="gpt-3.5-turbo",
                messages = [
                    {"role":"system", "content": system_content},
                    {"role":"user", "content": user_content},
                    {"role":"assistant", "content": assistant_content_example}
                ],
                max_tokens=500,
                temperature=0.7
            )

            answer = response.choices[0].message['content']
            return Response({"answer": answer}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
