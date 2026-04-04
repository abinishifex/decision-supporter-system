from rest_framework import serializers
from .models import Category, Question, AllowedAnswer, DecisionSession


class AllowedAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllowedAnswer
        fields = ["label", "value"]


class QuestionSerializer(serializers.ModelSerializer):
    options = AllowedAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "text", "order", "options"]


class CategorySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "description", "icon", "questions"]


class EvaluateDecisionSerializer(serializers.Serializer):
    problem = serializers.CharField(min_length=6)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    options = serializers.ListField(child=serializers.CharField(min_length=1), min_length=2)
    answers = serializers.DictField()
