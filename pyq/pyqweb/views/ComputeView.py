from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# responses
from pyq.pyqweb.Responses.ComputeResponse import ComputeResponse

# serializers
from pyq.pyqweb.Serializers.Request.ComputeRequestSerializer import ComputeRequestSerializer
from pyq.pyqweb.Serializers.Response.ComputeResponseSerializer import ComputeResponseSerializer

from pyq.pyqweb.Services import circuit_service

class ComputeView(APIView):

    def post(self, request):
        serializer = ComputeRequestSerializer(data=request.data)
        if serializer.is_valid():
            request = serializer.create(serializer.data)
            results = circuit_service.compute(request)
            response = ComputeResponse(results)
            serializer = ComputeResponseSerializer(instance=response)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
