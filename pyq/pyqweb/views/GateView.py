from rest_framework.response import Response
from rest_framework.views import APIView

from pyq.pyqweb.Responses.GateSetResponse import GateSetResponse
from pyq.pyqweb.Responses.GateInfoResponse import GateInfoResponse
from pyq.pyqweb.Serializers.Response.GateSetResponseSerializer import GateSetResponseSerializer
from pyq.pyqweb.Services import gate_service


class GateView(APIView):

    def get(self, request, format=None):
        gateset = gate_service.get_gates()
        modified_gateset = list()
        for gate in gateset:
            if gate.basic is True:
                modified_gateset.append(GateInfoResponse(gate.signature.gatename, gate.multi))
        response = GateSetResponse(modified_gateset)
        serializer = GateSetResponseSerializer(instance=response)
        return Response(serializer.data)

