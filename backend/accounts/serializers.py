import os
from rest_framework import serializers
from .models import User
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "date_joined")
        read_only_fields = ("id", "date_joined")


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "first_name", "last_name")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            is_active=True,  # Account inactive until verified
        )

        # Generate token and uid
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        # Build verification URL
        frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")
        verification_link = f"{frontend_url}/verify-email/{uid}/{token}"

        # Send email (fail silently so a bad provider doesn't crash registration)
        try:
            if getattr(settings, 'RESEND_API_KEY', None):
                import json
                from urllib.request import Request, urlopen

                # Resend API Payload
                url = "https://api.resend.com/emails"
                headers = {
                    "Authorization": f"Bearer {settings.RESEND_API_KEY}",
                    "Content-Type": "application/json",
                }
                data = {
                    "from": settings.DEFAULT_FROM_EMAIL,
                    "to": [user.email],
                    "subject": "Verify your Decision Supporter Account",
                    "html": f"<p>Hi {user.username},</p><p>Please verify your email by clicking the link below:</p><p><a href='{verification_link}'>{verification_link}</a></p><p>Thank you!</p>"
                }

                req = Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
                with urlopen(req) as response:
                    if response.getcode() == 200 or response.getcode() == 201:
                        print(f"SUCCESS [Resend API]: Email sent to {user.email}")
                    else:
                        print(f"WARNING [Resend API]: Unexpected response code {response.getcode()}")
            else:
                # Traditional Fallback (SMTP/Console)
                send_mail(
                    subject="Verify your Decision Supporter Account",
                    message=f"Hi {user.username},\n\nPlease verify your email by clicking the link below:\n\n{verification_link}\n\nThank you!",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],
                )
        except Exception as e:
            error_body = ""
            if hasattr(e, 'read'):
                try:
                    error_body = f" - Body: {e.read().decode('utf-8')}"
                except:
                    pass
            print(f"ERROR [Email System]: Failed to send email via any method: {str(e)}{error_body}")


        return user
