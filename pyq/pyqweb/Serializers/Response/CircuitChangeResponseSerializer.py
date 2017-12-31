from rest_framework import serializers

from pyq.pyqweb.Serializers.Request.AddGateRequestSerializer import AddGateRequestSerializer
from pyq.pyqweb.Serializers.Request.CleanSlotRequestSerializer import CleanSlotRequestSerializer


class CircuitChangeResponseSerializer(serializers.Serializer):
    added = AddGateRequestSerializer(many=True)
    removed = CleanSlotRequestSerializer(many=True)

