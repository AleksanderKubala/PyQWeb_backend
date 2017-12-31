from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from pyq.pyqweb.Serializers.AddGateRequestSerializer import AddGateRequestSerializer
from pyq.pyqweb.Serializers.CleanSlotRequestSerializer import CleanSlotRequestSerializer
from pyq.pyqweb.Serializers.CircuitChangeResponseSerializer import CircuitChangeResponseSerializer
from pyq.pyqweb.Serializers.ComputeRequestSerializer import ComputeRequestSerializer
from pyq.pyqweb.Serializers.ComputeResponseSerializer import ComputeResponseSerializer
from pyq.pyqweb.Serializers.RegisterStateRequestSerializer import RegisterStateRequestSerializer
from pyq.pyqweb.Serializers.RegisterChangeResponseSerializer import RegisterChangeResponseSerializer
from pyq.pyqweb.Responses.RegisterChangeResponse import RegisterChangeResponse
from pyq.pyqweb.Responses.CircuitChangeResponse import CircuitChangeResponse
from pyq.pyqweb.Responses.ComputeResponse import ComputeResponse

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

@api_view(['POST'])
def compute(request):
    serializer = ComputeRequestSerializer(data=request.data)
    if serializer.is_valid():
        request = serializer.create(serializer.data)
        results = circuit_service.compute(request)
        response = ComputeResponse(results)
        serializer = ComputeResponseSerializer(instance=response)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def set_state(request):
    serializer = RegisterStateRequestSerializer(data=request.data)
    if serializer.is_valid():
        request = serializer.create(serializer.data)
        state = circuit_service.set_register_state(request.state)
        size = circuit_service.get_circuit_size()
        response = RegisterChangeResponse(state, size)
        serializer = RegisterChangeResponseSerializer(instance=response)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
