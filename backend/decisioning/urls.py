from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import decision_detail_view, evaluate_view, health_view, CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path("", include(router.urls)),
    path("health/", health_view, name="health"),
    path("decisions/evaluate/", evaluate_view, name="evaluate"),
    path("decisions/<int:decision_id>/", decision_detail_view, name="decision-detail"),
]

