from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

class GPRAPIView(APIView):
    def post(self, request):
        user_input = request.data.get("question")

        if not user_input:
            return Response({'error': "질문이 필요합니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            response = openai.Completion.create(
                engine ="text-davinci-003",
                prompt=user_input,
                max_tokens=100,
                temperature=0.5,
            )

            answer = response.choices[0].text.strip()
            return Response({"answer": answer}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
