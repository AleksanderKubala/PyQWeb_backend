from rest_framework import serializers
from pyq.pyqweb.Serializers.SingleComputeResultSerializer import SingleComputeResultSerializer


class ComputeResponseSerializer(serializers.Serializer):
    results = SingleComputeResultSerializer(many=True)