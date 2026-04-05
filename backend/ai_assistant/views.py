from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import build_chat_response


class ChatView(APIView):
    """
    POST /api/chat/
    Accepts { "message": "..." } and returns a Groq AI response.
    """
    def post(self, request):
        message = str(request.data.get("message", "")).strip()
        if not message:
            return Response({"error": "Message is required."}, status=status.HTTP_400_BAD_REQUEST)

        reply = build_chat_response(message)
        return Response({"reply": reply}, status=status.HTTP_200_OK)
