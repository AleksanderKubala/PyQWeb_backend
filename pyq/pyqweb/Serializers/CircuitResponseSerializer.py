from rest_framework import serializers
from .CircuitLayerResponseSerializer import CircuitLayerResponseSerializer

class CircuitResponseSerializer(serializers.Serializer):

    size = serializers.IntegerField()
    state = serializers.IntegerField()
    layerCount = serializers.IntegerField()
    layers = CircuitLayerResponseSerializer(many=True)
