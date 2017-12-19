from rest_framework import serializers
from pyq.pyqweb.Serializers.AddGateRequestSerializer import AddGateRequestSerializer
from pyq.pyqweb.Serializers.CleanSlotRequestSerializer import CleanSlotRequestSerializer

class CircuitChangeResponseSerializer(serializers.Serializer):
    added = AddGateRequestSerializer(many=True)
    removed = CleanSlotRequestSerializer(many=True)

