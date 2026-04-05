from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    InitiateDecisionView,
    EvaluateDynamicView,
    DecisionHistoryView,
    health_view,
)

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
    path("health/", health_view, name="health"),
    path("initiate/", InitiateDecisionView.as_view(), name="initiate"),
    path("evaluate/", EvaluateDynamicView.as_view(), name="evaluate"),
    path("history/", DecisionHistoryView.as_view(), name="history"),
]
