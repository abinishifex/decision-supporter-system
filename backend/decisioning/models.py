from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="questions")
    text = models.CharField(max_length=500)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.text[:50]}..."


class AllowedAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    label = models.CharField(max_length=255)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.label} ({self.value})"


class DecisionSession(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="decision_sessions")
    problem = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    options = models.JSONField(default=list)
    answers = models.JSONField(default=dict)
    dynamic_questions = models.JSONField(null=True, blank=True)
    results = models.JSONField(null=True, blank=True)

    recommendation = models.CharField(max_length=255, null=True, blank=True)

    # Split analysis fields
    analysis_summary = models.TextField(null=True, blank=True)
    analysis_pros = models.TextField(null=True, blank=True)
    analysis_cons = models.TextField(null=True, blank=True)

    STATUS_CHOICES = [
        ("initiated", "Initiated"),
        ("evaluated", "Evaluated"),
        ("completed", "Completed"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="initiated")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Decision {self.id} by {self.user}"
