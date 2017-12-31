from rest_framework import serializers
from pyq.pyqweb.Requests.RegisterRequest import RegisterRequest

class RegisterRequestSerializer(serializers.Serializer):
    size = serializers.IntegerField()
    state = serializers.IntegerField()

    def create(self, validated_data):
        return RegisterRequest(**validated_data)

    def update(self, instance, validated_data):
        instance.size = validated_data.get('size', instance.size)
        instance.state = validated_data.get('state', instance.state)
        return instance
