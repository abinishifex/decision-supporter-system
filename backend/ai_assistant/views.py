from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ChatView(APIView):
    """
    POST /api/v1/chat/
    Placeholder for the AI-powered Decision Coach.
    """

    def post(self, request):
        return Response(
            {"reply": "The AI Decision Coach is currently being implemented."},
            status=status.HTTP_200_OK,
        )
