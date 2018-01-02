from rest_framework import serializers
from pyq.pyqweb.Requests.AddGateRequest import AddGateRequest

class AddGateRequestSerializer(serializers.Serializer):
    gate = serializers.CharField(max_length=32)
    step = serializers.IntegerField()
    qubits = serializers.ListField()
    controls = serializers.ListField()

    def create(self, validated_data):
        return AddGateRequest(**validated_data)

    def update(self, instance, validated_data):
        instance.gate = validated_data.get('gate', instance.basegate)
        instance.step = validated_data.get('step', instance.step)
        instance.qubits = validated_data.get('qubits', instance.qubits)
        instance.controls = validated_data.get('controls', instance.controls)
        return instance