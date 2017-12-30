from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pyq.pyqweb.Serializers.ResizeRequestSerializer import ResizeRequestSerializer
from pyq.pyqweb.Serializers.RegisterChangeResponseSerializer import RegisterChangeResponseSerializer
from pyq.pyqweb.Responses.RegisterChangeResponse import RegisterChangeResponse

from pyq.pyqweb.Services import circuit_service

class CircuitSizeView(APIView):

    def get(self, request):
        changes = None
        size = circuit_service.get_register_size()
        state = circuit_service.get_register_state()
        response = RegisterChangeResponse(state, size, changes)
        serializer = RegisterChangeResponseSerializer(instance=response)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResizeRequestSerializer(data=request.data)
        if serializer.is_valid():
            request = serializer.create(serializer.data)
            changes = circuit_service.resize_circuit(request.size)
            size = circuit_service.get_register_size()
            state = circuit_service.get_register_state()
            response = RegisterChangeResponse(state, size, changes)
            serializer = RegisterChangeResponseSerializer(instance=response)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
