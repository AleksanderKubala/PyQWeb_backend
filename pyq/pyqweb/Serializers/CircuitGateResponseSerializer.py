from rest_framework import serializers

class CircuitGateResponseSerializer(serializers.Serializer):

    gate = serializers.CharField(max_length=32)
    qubits = serializers.ListField()
    controls = serializers.ListField()
