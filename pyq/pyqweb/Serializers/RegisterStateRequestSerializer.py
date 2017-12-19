from rest_framework import serializers
from pyq.pyqweb.Requests.RegisterStateRequest import RegisterStateRequest

class RegisterStateRequestSerializer(serializers.Serializer):
    state = serializers.IntegerField()

    def create(self, validated_data):
        return RegisterStateRequest(**validated_data)
