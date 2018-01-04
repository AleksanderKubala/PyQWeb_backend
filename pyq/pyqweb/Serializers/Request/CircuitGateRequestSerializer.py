from rest_framework import serializers

from pyq.pyqweb.Requests.CircuitGateRequest import CircuitGateRequest


class CircuitGateRequestSerializer(serializers.Serializer):

    gate = serializers.CharField(max_length=32)
    qubits = serializers.ListField()
    controls = serializers.ListField()

    def create(self, validated_data):
        return CircuitGateRequest(**validated_data)

    def update(self, instance, validated_data):
        instance.gate = validated_data.get('gate', instance.gate)
        instance.qubits = validated_data.get('qubits', instance.qubits)
        instance.controls = validated_data.get('controls', instance.controls)
        return instance
