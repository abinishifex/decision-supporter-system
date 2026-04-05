from rest_framework import serializers

class DecisionStartSerializer(serializers.Serializer):
    problem = serializers.CharField(max_length=500)
    options = serializers.ListField(
        child=serializers.CharField(max_length=200),
        min_length=2
    )