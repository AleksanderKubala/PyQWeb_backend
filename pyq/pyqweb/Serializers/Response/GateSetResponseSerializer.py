from rest_framework import serializers

from .GateInfoResponseSerializer import GateInfoResponseSerializer

class GateSetResponseSerializer(serializers.Serializer):
    gates = GateInfoResponseSerializer(many=True)