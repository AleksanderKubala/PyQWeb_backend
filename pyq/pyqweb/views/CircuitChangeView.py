from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pyq.pyqweb.Responses.CircuitChangeResponse import CircuitChangeResponse
from pyq.pyqweb.Responses.CircuitGateResponse import CircuitGateResponse
from pyq.pyqweb.Responses.CircuitLayerResponse import CircuitLayerResponse
from pyq.pyqweb.Responses.CleanSlotResponse import CleanSlotResponse

from pyq.pyqweb.Serializers.Request.AddGateRequestSerializer import AddGateRequestSerializer
from pyq.pyqweb.Serializers.Request.CleanSlotRequestSerializer import CleanSlotRequestSerializer
from pyq.pyqweb.Serializers.Response.CircuitChangeResponseSerializer import CircuitChangeResponseSerializer

from pyq.pyqweb.Services import circuit_service

class CircuitChangeView(APIView):

    def post(self, request):
        serializer = AddGateRequestSerializer(data=request.data)
        if serializer.is_valid():
            request = serializer.create(serializer.data)
            added, removed = circuit_service.add(request)
            response = CircuitChangeResponse(added, removed)
            serializer = CircuitChangeResponseSerializer(instance=response)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = CleanSlotRequestSerializer(data=request.data)
        if serializer.is_valid():
            request = serializer.create(serializer.data)
            removed = circuit_service.remove(request)
            response = CircuitChangeResponse(removed=removed)
            serializer = CircuitChangeResponseSerializer(instance=response)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

