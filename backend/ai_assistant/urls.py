# from django.urls import path
# from .views import ChatView

# urlpatterns = [
#     path("", ChatView.as_view(), name="chat"),
# ]

from django.urls import path
from .views import start_decision, test_view

urlpatterns = [
    path('start-decision/', start_decision),
    path('test/', test_view),
]