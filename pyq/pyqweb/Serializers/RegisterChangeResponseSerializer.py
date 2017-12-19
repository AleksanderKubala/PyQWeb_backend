from rest_framework import serializers
from pyq.pyqweb.Serializers.CircuitChangeResponseSerializer import CircuitChangeResponseSerializer

class RegisterChangeResponseSerializer(serializers.Serializer):
    changes = CircuitChangeResponseSerializer()
    size = serializers.IntegerField()
    state = serializers.IntegerField()