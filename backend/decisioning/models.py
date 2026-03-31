from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    icon = models.CharField(max_length=100, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    category = models.ForeignKey(Category, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text

class AllowedAnswer(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.label} ({self.value})"


class DecisionSession(models.Model):
    problem = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    options = models.JSONField()
    answers = models.JSONField()
    results = models.JSONField()
    recommendation = models.CharField(max_length=255)
    analysis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.problem}: {self.recommendation}"
