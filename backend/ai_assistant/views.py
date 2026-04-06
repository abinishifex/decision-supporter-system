from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_spectacular.utils import extend_schema
from drf_spectacular.types import OpenApiTypes

from .services import build_chat_response


class ChatView(APIView):
    """
    POST /api/chat/
    Accepts { "message": "..." } and returns a Google Gemini AI response.
    """
    permission_classes = (permissions.AllowAny,)

    @extend_schema(
        request=OpenApiTypes.OBJECT,
        responses={200: OpenApiTypes.OBJECT, 400: OpenApiTypes.OBJECT},
        description="Accepts { 'message': '...', 'history': [] } and returns a Gemini response."
    )
    def post(self, request):
        message = str(request.data.get("message", "")).strip()
        history = request.data.get("history", [])

        if not message:
            return Response({"error": "Message is required."}, status=status.HTTP_400_BAD_REQUEST)

        reply = build_chat_response(message, history)
        return Response({"reply": reply}, status=status.HTTP_200_OK)
