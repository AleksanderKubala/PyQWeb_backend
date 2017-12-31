from rest_framework.response import Response
from rest_framework.views import APIView

from pyq.pyqweb.Responses.GateSetResponse import GateSetResponse
from pyq.pyqweb.Serializers.Response.GateSetResponseSerializer import GateSetResponseSerializer
from pyq.pyqweb.Services import gate_service


class GateView(APIView):

    def get(self, request, format=None):
        gateset = gate_service.get_gates()
        response = GateSetResponse(gateset)
        serializer = GateSetResponseSerializer(instance=response)
        return Response(serializer.data)

