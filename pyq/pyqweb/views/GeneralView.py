from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pyq.pyqweb.Responses.CircuitChangeResponse import CircuitChangeResponse
from pyq.pyqweb.Responses.ComputeResponse import ComputeResponse
from pyq.pyqweb.Responses.RegisterResponse import RegisterResponse
from pyq.pyqweb.Serializers.Request.AddGateRequestSerializer import AddGateRequestSerializer
from pyq.pyqweb.Serializers.Request.CleanSlotRequestSerializer import CleanSlotRequestSerializer
from pyq.pyqweb.Serializers.Request.ComputeRequestSerializer import ComputeRequestSerializer
from pyq.pyqweb.Serializers.Response.CircuitChangeResponseSerializer import CircuitChangeResponseSerializer
from pyq.pyqweb.Serializers.Response.ComputeResponseSerializer import ComputeResponseSerializer
from pyq.pyqweb.Serializers.Response.RegisterResponseSerializer import RegisterResponseSerializer
from pyq.pyqweb.Services import circuit_service


@api_view(['POST'])
def add_gate(request):
    serializer = AddGateRequestSerializer(data=request.data)
    if serializer.is_valid():
        request = serializer.create(serializer.data)
        changes = circuit_service.add(request)
        response = CircuitChangeResponse(changes)
        serializer = CircuitChangeResponseSerializer(instance=response)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def clean_slots(request):
    serializer = CleanSlotRequestSerializer(data=request.data)
    if serializer.is_valid():
        request = serializer.create(serializer.data)
        changes = circuit_service.remove(request)
        response = CircuitChangeResponse(changes)
        serializer = CircuitChangeResponseSerializer(instance=response)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
