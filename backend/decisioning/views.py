from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import DecisionSession
from .serializers import DecisionSessionSerializer
from .services import generate_dynamic_questions, evaluate_dynamic_decision, validate_decision_payload

class DecisionSessionViewSet(viewsets.ModelViewSet):
    serializer_class = DecisionSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DecisionSession.objects.filter(user=self.request.user).order_by('-created_at')

    @action(detail=False, methods=['post'])
    def initiate(self, request):
        """
        STEP 1: POST /api/decisions/initiate/
        Takes problem/category and returns questions.
        """
        normalized = validate_decision_payload(request.data)
        questions = generate_dynamic_questions(
            normalized["problem"], 
            normalized["category"]
        )
        return Response(questions, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def evaluate(self, request):
        """
        STEP 2: POST /api/decisions/evaluate/
        Takes problem, category, options, and answers; saves to DB.
        """
        try:
            data = request.data
            evaluation = evaluate_dynamic_decision(
                data["problem"],
                data["category"],
                data["options"],
                data["answers"]
            )

            decision = DecisionSession.objects.create(
                user=request.user,
                problem=data["problem"],
                category=data["category"],
                options=data["options"],
                answers=data["answers"],
                results=evaluation["results"],
                recommendation=evaluation["recommendedOption"],
                analysis_summary=evaluation.get("summary", ""),
                analysis_pros=evaluation.get("pros", ""),
                analysis_cons=evaluation.get("cons", "")
            )

            evaluation["decisionId"] = decision.id
            return Response(evaluation, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({"error": f"Missing field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)