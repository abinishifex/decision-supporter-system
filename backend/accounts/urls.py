from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, MeView, VerifyEmailView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="auth_register"),
    path("verify-email/<str:uidb64>/<str:token>/", VerifyEmailView.as_view(), name="auth_verify_email"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", MeView.as_view(), name="auth_me"),
]
