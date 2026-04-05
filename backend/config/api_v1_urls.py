from django.urls import path, include

urlpatterns = [
    path("auth/", include("accounts.urls")),
    path("decisions/", include("decisioning.urls")),
    path("chat/", include("ai_assistant.urls")),
]
