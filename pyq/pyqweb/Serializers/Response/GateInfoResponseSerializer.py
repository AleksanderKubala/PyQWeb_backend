from rest_framework import serializers

class GateInfoResponseSerializer(serializers.Serializer):
    signature = serializers.CharField(max_length=32)
    multi = serializers.BooleanField()