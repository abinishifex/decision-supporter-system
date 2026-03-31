from rest_framework import serializers
from .models import Category, Question, AllowedAnswer, DecisionSession

class AllowedAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllowedAnswer
        fields = ['label', 'value']

class QuestionSerializer(serializers.ModelSerializer):
    options = AllowedAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'order', 'options']

class CategorySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'icon', 'questions']

class DecisionSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecisionSession
        fields = [
            'id', 'problem', 'category', 'options', 'answers', 
            'results', 'recommendation', 'analysis', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

class EvaluateDecisionSerializer(serializers.Serializer):
    problem = serializers.CharField(min_length=6)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    options = serializers.ListField(
        child=serializers.CharField(min_length=1),
        min_length=2,
    )
    answers = serializers.DictField()

    def validate(self, data):
        category = data['category_id']
        options = data['options']
        raw_answers = data.get('answers', {})

        # Build validation map from DB
        questions = category.questions.prefetch_related('options')
        question_ids = {str(q.id) for q in questions}
        valid_values = {
            str(q.id): {opt.value for opt in q.options.all()}
            for q in questions
        }

        normalized_answers = {}
        for option_index in range(len(options)):
            option_key = str(option_index)
            option_answers = raw_answers.get(option_key)
            if not isinstance(option_answers, dict):
                raise serializers.ValidationError(f"Missing answers for option {option_index + 1}.")

            normalized_option = {}
            for qid in question_ids:
                raw_value = option_answers.get(qid)
                if raw_value is None:
                    raise serializers.ValidationError(f"Question {qid} is unanswered for option {option_index + 1}.")
                try:
                    value = int(raw_value)
                except (TypeError, ValueError):
                    raise serializers.ValidationError(f"Question {qid} has an invalid answer value.")
                
                if value not in valid_values[qid]:
                    raise serializers.ValidationError(f"Question {qid} has an unsupported answer value.")
                
                normalized_option[qid] = value
            
            normalized_answers[option_key] = normalized_option

        data['answers'] = normalized_answers
        return data
