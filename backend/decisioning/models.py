from django.db import models


class DecisionSession(models.Model):
    problem = models.TextField()
    category_id = models.CharField(max_length=100)
    category_name = models.CharField(max_length=255)
    category_payload = models.JSONField()
    options = models.JSONField()
    answers = models.JSONField()
    results = models.JSONField()
    recommendation = models.CharField(max_length=255)
    analysis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.category_name}: {self.recommendation}"
