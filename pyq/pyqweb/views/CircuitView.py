from rest_framework.views import APIView
from rest_framework.response import Response
from pyq.pyqweb.Serializers.CircuitResponseSerializer import CircuitResponseSerializer
from pyq.pyqweb.Responses.CircuitResponse import CircuitResponse
from pyq.pyqweb.Responses.CircuitLayerResponse import CircuitLayerResponse
from pyq.pyqweb.Responses.CircuitGateResponse import CircuitGateResponse

from pyq.pyqweb.Services import circuit_service

class CircuitView(APIView):

    def get(self, request):
        size, state, layer_count, circuit_layers = circuit_service.get_circuit()
        layers = list()
        gates = list()
        for circuit_layer in circuit_layers:
            for circuit_gate in circuit_layer[1]:
                gates.append(CircuitGateResponse(circuit_gate.qubits, circuit_gate.basegate, circuit_gate.controls))
            layers.append(CircuitLayerResponse(circuit_layer[0], gates))
            gates = list()
        response = CircuitResponse(size, state, layer_count, layers)
        serializer = CircuitResponseSerializer(instance=response)
        return Response(serializer.data)


