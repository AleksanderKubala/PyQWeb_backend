from rest_framework import serializers
from pyq.pyqweb.Requests.ResizeRequest import ResizeRequest

class ResizeRequestSerializer(serializers.Serializer):
    size = serializers.IntegerField()

    def create(self, validated_data):
        return ResizeRequest(**validated_data)