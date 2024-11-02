from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai
from django.conf import settings
import os
from  teams.models import ProfileQuestionAnswer
from teams.serializers import ProfileQuestionAnswerSerializer
from rest_framework.permissions import AllowAny

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
    permission_classes = [AllowAny]

    def get(self, request, team_id):
        queryset = ProfileQuestionAnswer.objects.filter(team_id=team_id)

        serializer = ProfileQuestionAnswerSerializer(queryset, many=True)
        data = serializer.data
        
        data_str = str(data)
        prompt = f"{system_content}\nUser input: {user_content}\nAssistant example: {assistant_content_example}\nUser data:\n{data}"

        # ChatCompletion 용 메시지 생성
        messages = [
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": assistant_content_example},
            {"role": "user", "content": f"User data:\n{data}"}
        ]
        try:
            response = openai.chat.completions.create(
                # model="gpt-4",
                model ="gpt-3.5-turbo",
                # model="text-davinci-003",  # GPT-3 모델 지정
                # messages = [
                #     {"role":"system", "content": system_content},
                #     {"role":"user", "content": user_content},
                #     {"role":"assistant", "content": assistant_content_example}
                # ],
                # prompt=prompt,
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )

            # answer = response.choices[0].message['content']
            # return Response({"answer": answer}, status=status.HTTP_200_OK)
            answer = response.choices[0].message.content.strip()
            return Response({"answer": answer}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
