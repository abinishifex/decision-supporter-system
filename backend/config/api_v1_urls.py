from django.urls import path, include
from rest_framework.routers import DefaultRouter
from decisioning.views import CategoryViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("accounts.urls")),
    path("decisions/", include("decisioning.urls")),
    path("chat/", include("ai_assistant.urls")),
]
