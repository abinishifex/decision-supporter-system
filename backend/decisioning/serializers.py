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


# --- Dynamic Discovery (Role 4) ---

class InitiateDecisionSerializer(serializers.Serializer):
    problem = serializers.CharField(min_length=10)
    options = serializers.ListField(child=serializers.CharField(min_length=1), min_length=2)
    category_id = serializers.IntegerField(required=False, allow_null=True)


class EvaluateDynamicSerializer(serializers.Serializer):
    session_id = serializers.IntegerField()
    # answers: { "question_id": "A/B/C/D/E" }
    answers = serializers.DictField()

class DecisionSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecisionSession
        fields = [
            "id", "problem", "category", "options", "dynamic_questions", "answers", 
            "results", "recommendation", "analysis_summary", "analysis_pros", "analysis_cons", "status", "created_at"
        ]
        read_only_fields = ["id", "created_at", "results", "recommendation", "analysis_summary", "analysis_pros", "analysis_cons"]
