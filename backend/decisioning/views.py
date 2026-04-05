from django.http import JsonResponse
from rest_framework import viewsets, mixins, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from .models import DecisionSession, Category
from .serializers import (
    CategorySerializer,
    InitiateDecisionSerializer,
    EvaluateDynamicSerializer,
    DecisionSessionSerializer,
)
from .services import (
    generate_dynamic_questions,
    evaluate_dynamic_decision,
)


class CategoryViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    Exposes GET /api/v1/decisions/categories/ and GET /api/v1/decisions/categories/<id>/
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class InitiateDecisionView(APIView):
    """
    POST /api/v1/decisions/initiate/
    Role 4: Handles the first step of Dynamic Discovery by generating custom questions.
    """
    permission_classes = [AllowAny] # Change to IsAuthenticated if needed

    def post(self, request):
        serializer = InitiateDecisionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        try:
            # Fetch category context if provided
            category_name = "General"
            category_obj = None
            if data.get("category_id"):
                try:
                    category_obj = Category.objects.get(pk=data["category_id"])
                    category_name = category_obj.name
                except Category.DoesNotExist:
                    pass

            # Call Gemini to get dynamic questions
            questions = generate_dynamic_questions(data["problem"], data["options"], category_name)
            
            # Save the session to track progress
            session = DecisionSession.objects.create(
                problem=data["problem"],
                options=data["options"],
                category=category_obj,
                dynamic_questions=questions,
                status="initiated"
            )
            
            return Response({
                "session_id": session.id,
                "category": category_name,
                "questions": questions
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EvaluateDynamicView(APIView):
    """
    POST /api/v1/decisions/evaluate/
    Role 4: Finalizes the dynamic discovery with a weighted Gemini evaluation.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = EvaluateDynamicSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        try:
            # Retrieve the session
            session = DecisionSession.objects.get(pk=data["session_id"])
            if session.status == "completed":
                return Response({"error": "This decision has already been completed."}, status=status.HTTP_400_BAD_REQUEST)

            # Call Gemini for final analysis
            evaluation = evaluate_dynamic_decision(
                session.problem,
                session.options,
                session.dynamic_questions,
                data["answers"]
            )
            
            # Update and complete the session
            session.answers = data["answers"]
            session.results = evaluation["results"]
            session.recommendation = evaluation["recommendedOption"]
            session.analysis_summary = evaluation["summary"]
            session.status = "completed"
            session.save()
            
            return Response(DecisionSessionSerializer(session).data, status=status.HTTP_200_OK)
            
        except DecisionSession.DoesNotExist:
            return Response({"error": "Session not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DecisionHistoryView(generics.ListAPIView):
    """
    GET /api/v1/decisions/history/
    Retrieve previous decision sessions.
    """
    serializer_class = DecisionSessionSerializer
    permission_classes = [AllowAny] # In production, this should be IsAuthenticated
    queryset = DecisionSession.objects.all()

def health_view(request):
    return JsonResponse({"status": "ok"})
