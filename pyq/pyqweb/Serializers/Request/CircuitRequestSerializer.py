from rest_framework import serializers

from pyq.pyqweb.Requests.CircuitRequest import CircuitRequest
from pyq.pyqweb.Serializers.Request.CircuitLayerRequestSerializer import CircuitLayerRequestSerializer


class CircuitRequestSerializer(serializers.Serializer):

    size = serializers.IntegerField()
    state = serializers.IntegerField()
    layerCount = serializers.IntegerField()
    layers = CircuitLayerRequestSerializer(many=True)

    def create(self, validated_data):
        return CircuitRequest(**validated_data)

    def update(self, instance, validated_data):
        instance.size = validated_data.get('size', instance.size)
        instance.state = validated_data.get('state', instance.state)
        instance.layerCount = validated_data.get('layerCount', instance.layerCount)
        instance.layers = validated_data.get('layers', instance.layers)
        return instance
