from rest_framework import serializers

class GateSetResponseSerializer(serializers.Serializer):
    signatures = serializers.ListField()