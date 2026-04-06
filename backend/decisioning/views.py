import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from .models import DecisionSession
from .services import build_chat_response, evaluate_decision, validate_decision_payload


def _parse_json(request):
    try:
        return json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return None


@require_GET
def health_view(request):
    return JsonResponse({"status": "ok"})


@csrf_exempt
@require_POST
def evaluate_view(request):
    payload = _parse_json(request)
    if payload is None:
        return JsonResponse({"error": "Invalid JSON payload."}, status=400)

    try:
        validated = validate_decision_payload(payload)
        evaluation = evaluate_decision(
            problem=validated["problem"],
            category=validated["category"],
            options=validated["options"],
            answers=validated["answers"],
        )
    except ValueError as exc:
        return JsonResponse({"error": str(exc)}, status=400)

    session = DecisionSession.objects.create(
        problem=validated["problem"],
        category_id=validated["category"]["id"],
        category_name=validated["category"]["name"],
        category_payload=validated["category"],
        options=validated["options"],
        answers=validated["answers"],
        results=evaluation["results"],
        recommendation=evaluation["recommendedOption"],
        analysis=evaluation["analysis"],
    )

    return JsonResponse(
        {
            **evaluation,
            "decisionId": session.id,
        }
    )


@require_GET
def decision_detail_view(request, pk):
    session = get_object_or_404(DecisionSession, pk=pk)
    return JsonResponse(
        {
            "id": session.id,
            "problem": session.problem,
            "category": session.category_payload,
            "options": session.options,
            "answers": session.answers,
            "results": session.results,
            "recommendedOption": session.recommendation,
            "analysis": session.analysis,
            "createdAt": session.created_at.isoformat(),
        }
    )


@csrf_exempt
@require_POST
def chat_view(request):
    payload = _parse_json(request)
    if payload is None:
        return JsonResponse({"error": "Invalid JSON payload."}, status=400)

    message = payload.get("message")
    if not isinstance(message, str):
        return JsonResponse({"error": "Message is required."}, status=400)

    return JsonResponse({"reply": build_chat_response(message)})

