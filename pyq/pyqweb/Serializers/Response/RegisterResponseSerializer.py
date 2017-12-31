from rest_framework import serializers

from pyq.pyqweb.Serializers.Response.CircuitChangeResponseSerializer import CircuitChangeResponseSerializer


class RegisterResponseSerializer(serializers.Serializer):
    changes = CircuitChangeResponseSerializer()
    size = serializers.IntegerField()
    state = serializers.IntegerField()
