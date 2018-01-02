from rest_framework.response import Response
from rest_framework.views import APIView

from pyq.pyqweb.Responses.CircuitGateResponse import CircuitGateResponse
from pyq.pyqweb.Responses.CircuitLayerResponse import CircuitLayerResponse
from pyq.pyqweb.Responses.CircuitResponse import CircuitResponse
from pyq.pyqweb.Serializers.Response.CircuitResponseSerializer import CircuitResponseSerializer
from pyq.pyqweb.Services import circuit_service

class CircuitView(APIView):

    def get(self, request):
        size, state, layer_count, layers = circuit_service.get_circuit()
        response = CircuitResponse(size, state, layer_count, layers)
        serializer = CircuitResponseSerializer(instance=response)
        return Response(serializer.data)


