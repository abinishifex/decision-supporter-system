from django.urls import path

from .views import chat_view, decision_detail_view, evaluate_view, health_view


urlpatterns = [
    path("health/", health_view, name="health"),
    path("decisions/evaluate/", evaluate_view, name="evaluate"),
    path("decisions/<int:decision_id>/", decision_detail_view, name="decision-detail"),
    path("chat/", chat_view, name="chat"),
]
