from rest_framework import serializers

from pyq.pyqweb.Requests.CircuitLayerRequest import CircuitLayerRequest
from pyq.pyqweb.Serializers.Request.CircuitGateRequestSerializer import CircuitGateRequestSerializer


class CircuitLayerRequestSerializer(serializers.Serializer):

    step = serializers.IntegerField()
    gates = CircuitGateRequestSerializer(many=True)

    def create(self, validated_data):
        return CircuitLayerRequest(**validated_data)

    def update(self, instance, validated_data):
        instance.step = validated_data.get('step', instance.step)
        instance.gates = validated_data.get('gates', instance.gates)
        return instance
