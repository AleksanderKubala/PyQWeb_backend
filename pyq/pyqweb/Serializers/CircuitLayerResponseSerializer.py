from rest_framework import serializers
from .CircuitGateResponseSerializer import CircuitGateResponseSerializer

class CircuitLayerResponseSerializer(serializers.Serializer):

    step = serializers.IntegerField()
    gates = CircuitGateResponseSerializer(many=True)
