from rest_framework import serializers
from pyq.pyqweb.Requests.ComputeRequest import ComputeRequest

class ComputeRequestSerializer(serializers.Serializer):
    time = serializers.IntegerField()

    def create(self, validated_data):
        return ComputeRequest(**validated_data)