import json

from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import DecisionSession
from .services import build_chat_response, evaluate_decision, validate_decision_payload


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
        normalized = validate_decision_payload(payload)
        evaluation = evaluate_decision(
            normalized["problem"],
            normalized["category"],
            normalized["options"],
            normalized["answers"],
        )
        session = DecisionSession.objects.create(
            problem=normalized["problem"],
            category_id=normalized["category"]["id"],
            category_name=normalized["category"]["name"],
            category_payload=normalized["category"],
            options=normalized["options"],
            answers=normalized["answers"],
            results=evaluation["results"],
            recommendation=evaluation["recommendedOption"],
            analysis=evaluation["analysis"],
        )
    except ValueError as exc:
        return JsonResponse({"error": str(exc)}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Request body must be valid JSON."}, status=400)

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
def chat_view(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    try:
        payload = json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "Request body must be valid JSON."}, status=400)

    message = str(payload.get("message", "")).strip()
    if not message:
        return JsonResponse({"error": "Message is required."}, status=400)

    return JsonResponse({"reply": build_chat_response(message)})
