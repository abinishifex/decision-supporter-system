import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST


def _parse_json(request):
    try:
        return json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return None


def _serialize_user(user):
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "firstName": user.first_name,
        "lastName": user.last_name,
    }


@csrf_exempt
@require_POST
def register_view(request):
    payload = _parse_json(request)
    if payload is None:
        return JsonResponse({"error": "Invalid JSON payload."}, status=400)

    username = (payload.get("username") or "").strip()
    email = (payload.get("email") or "").strip()
    password = payload.get("password") or ""

    if len(username) < 3:
        return JsonResponse({"error": "Username must be at least 3 characters."}, status=400)
    if not email:
        return JsonResponse({"error": "Email is required."}, status=400)
    if len(password) < 6:
        return JsonResponse({"error": "Password must be at least 6 characters."}, status=400)
    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "Username already exists."}, status=400)
    if User.objects.filter(email=email).exists():
        return JsonResponse({"error": "Email already exists."}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)
    login(request, user)
    return JsonResponse({"user": _serialize_user(user)}, status=201)


@csrf_exempt
@require_POST
def login_view(request):
    payload = _parse_json(request)
    if payload is None:
        return JsonResponse({"error": "Invalid JSON payload."}, status=400)

    username = (payload.get("username") or "").strip()
    password = payload.get("password") or ""

    if not username or not password:
        return JsonResponse({"error": "Username and password are required."}, status=400)

    user = authenticate(request, username=username, password=password)
    if user is None:
        return JsonResponse({"error": "Invalid username or password."}, status=401)

    login(request, user)
    return JsonResponse({"user": _serialize_user(user)})


@csrf_exempt
@require_POST
def logout_view(request):
    logout(request)
    return JsonResponse({"success": True})


@require_GET
def me_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"user": None}, status=401)
    return JsonResponse({"user": _serialize_user(request.user)})

