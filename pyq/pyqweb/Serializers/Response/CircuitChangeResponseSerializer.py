from rest_framework import serializers

from pyq.pyqweb.Serializers.Response.CircuitLayerResponseSerializer import CircuitLayerResponseSerializer
from pyq.pyqweb.Serializers.Response.CleanSlotResponseSerializer import CleanSlotResponseSerializer


class CircuitChangeResponseSerializer(serializers.Serializer):
    added = CircuitLayerResponseSerializer(many=True)
    removed = CleanSlotResponseSerializer(many=True)

