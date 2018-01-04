from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from pyq.pyqweb.Responses.CircuitResponse import CircuitResponse
from pyq.pyqweb.Serializers.Request.CircuitRequestSerializer import CircuitRequestSerializer
from pyq.pyqweb.Serializers.Response.CircuitResponseSerializer import CircuitResponseSerializer
from pyq.pyqweb.Services import circuit_service

class CircuitView(APIView):

    def get(self, request):
        size, state, layer_count, layers = circuit_service.get_circuit()
        response = CircuitResponse(size, state, layer_count, layers)
        serializer = CircuitResponseSerializer(instance=response)
        return Response(serializer.data)

    def post(self, request):
        serializer = CircuitRequestSerializer(data=request.data)
        if serializer.is_valid():
            request = serializer.create(serializer.data)
            size, state, layer_count, layers = circuit_service.createCircuit(request)
            response = CircuitResponse(size, state, layer_count, layers)
            serializer = CircuitResponseSerializer(instance=response)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request):
        size, state, layer_count, layers = circuit_service.reset()
        response = CircuitResponse(size, state, layer_count, layers)
        serializer = CircuitResponseSerializer(instance=response)
        return Response(serializer.data, status=status.HTTP_200_OK)




