import json

from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import DecisionSession, Category
from .services import evaluate_decision
from rest_framework import viewsets, mixins
from .serializers import CategorySerializer, EvaluateDecisionSerializer


class CategoryViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    Exposes GET /api/v1/decisions/categories/ and GET /api/v1/decisions/categories/<id>/
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def health_view(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    return JsonResponse({"status": "ok"})


@csrf_exempt
def evaluate_view(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    try:
        payload = json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "Request body must be valid JSON."}, status=400)

    serializer = EvaluateDecisionSerializer(data=payload)
    if not serializer.is_valid():
        return JsonResponse({"error": serializer.errors}, status=400)

    validated = serializer.validated_data

    try:
        evaluation = evaluate_decision(
            validated["problem"],
            validated["category_id"],
            validated["options"],
            validated["answers"],
        )
        session = DecisionSession.objects.create(
            problem=validated["problem"],
            category=validated["category_id"],
            options=validated["options"],
            answers=validated["answers"],
            results=evaluation["results"],
            recommendation=evaluation["recommendedOption"],
            analysis=evaluation["analysis"],
        )
    except Exception as exc:
        return JsonResponse({"error": str(exc)}, status=500)

    evaluation["decisionId"] = session.id
    return JsonResponse(evaluation, status=201)


def decision_detail_view(request, decision_id):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    try:
        session = DecisionSession.objects.get(pk=decision_id)
    except DecisionSession.DoesNotExist:
        return JsonResponse({"error": "Decision session not found."}, status=404)

    return JsonResponse(
        {
            "decisionId": session.id,
            "problem": session.problem,
            "category": session.category.id if session.category else None,
            "options": session.options,
            "answers": session.answers,
            "results": session.results,
            "recommendedOption": session.recommendation,
            "analysis": session.analysis,
            "createdAt": session.created_at.isoformat(),
        }
    )
