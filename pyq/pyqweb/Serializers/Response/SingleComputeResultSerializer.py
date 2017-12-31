from rest_framework import serializers

class SingleComputeResultSerializer(serializers.Serializer):
    amplitude = serializers.CharField(max_length=32)
    bits = serializers.CharField(max_length=32)
    probability = serializers.FloatField()