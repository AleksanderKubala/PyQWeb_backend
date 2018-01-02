from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from pyq.pyqweb.Services import circuit_service

from pyq.pyqweb.Responses.RegisterResponse import RegisterResponse

from pyq.pyqweb.Serializers.Response.RegisterResponseSerializer import RegisterResponseSerializer
from pyq.pyqweb.Serializers.Request.RegisterRequestSerializer import RegisterRequestSerializer

class RegisterView(APIView):

    def get(self, request):
        changes = None
        size = circuit_service.get_register_size()
        state = circuit_service.get_register_state()
        response = RegisterResponse(state, size, changes)
        serializer = RegisterResponseSerializer(instance=response)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegisterRequestSerializer(data=request.data)
        if serializer.is_valid():
            request = serializer.create(serializer.data)
            removed = circuit_service.set_register(request)
            size = circuit_service.get_register_size()
            state = circuit_service.get_register_state()
            response = RegisterResponse(state, size, removed)
            serializer = RegisterResponseSerializer(instance=response)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
