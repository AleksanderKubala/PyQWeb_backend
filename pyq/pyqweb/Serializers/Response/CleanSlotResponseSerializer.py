from rest_framework import serializers

from pyq.pyqweb.Responses.CleanSlotResponse import CleanSlotResponse

class CleanSlotResponseSerializer(serializers.Serializer):
    step = serializers.IntegerField()
    qubits = serializers.ListField()