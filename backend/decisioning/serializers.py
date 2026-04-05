from rest_framework import serializers
from .models import DecisionSession

class DecisionSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecisionSession
        fields = ['id', 'problem', 'category', 'options', 'answers',
          'dynamic_questions', 'results', 'recommendation',
          'analysis_summary', 'analysis_pros', 'analysis_cons',  
          'status', 'created_at']
        read_only_fields = ['id', 'created_at', 'results', 'recommendation', 'analysis']