from rest_framework import serializers
from pyq.pyqweb.Requests.CleanSlotRequest import CleanSlotRequest

class CleanSlotRequestSerializer(serializers.Serializer):
    step = serializers.IntegerField()
    qubits = serializers.ListField()

    def create(self, validated_data):
        return CleanSlotRequest(**validated_data)

    def update(self, instance, validated_data):
        instance.step = validated_data.get('step', instance.step)
        instance.qubits = validated_data.get('qubits', instance.qubits)
        return instance

