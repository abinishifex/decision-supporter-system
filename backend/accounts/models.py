from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Add any custom fields here in the future
    # e.g., profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    # e.g., is_expert = models.BooleanField(default=False)

    def __str__(self):
        return self.username
