from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    InitiateDecisionView,
    EvaluateDynamicView,
    DecisionHistoryView,
    DecisionSessionViewSet,
    health_view,
)
# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r'decisions', DecisionSessionViewSet, basename='decision')
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
    path("health/", health_view, name="health"),
    path("initiate/", InitiateDecisionView.as_view(), name="initiate"),
    path("evaluate/", EvaluateDynamicView.as_view(), name="evaluate"),
    path("history/", DecisionHistoryView.as_view(), name="history"),
]
