from rest_framework import serializers
from pyq.pyqweb.Requests.CleanSlotRequest import CleanSlotRequest

class CleanSlotRequestSerializer(serializers.Serializer):
    layer = serializers.IntegerField()
    qubits = serializers.ListField()

    def create(self, validated_data):
        return CleanSlotRequest(**validated_data)

    def update(self, instance, validated_data):
        instance.layer = validated_data.get('layer', instance.layer)
        instance.qubits = validated_data.get('qubits', instance.qubits)
        return instance

