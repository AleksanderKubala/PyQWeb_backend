from PyQ.Circuit import Circuit

from pyq.pyqweb.Responses.CircuitGateResponse import CircuitGateResponse
from pyq.pyqweb.Responses.CircuitLayerResponse import CircuitLayerResponse
from pyq.pyqweb.Responses.CleanSlotResponse import CleanSlotResponse


class CircuitService(object):

    def __init__(self):
        self.circuit = Circuit()

    def get_circuit(self):
        size = self.get_register_size()
        state = self.get_register_state()
        layer_count = self.circuit.layer_count
        layers = list()
        for i in range(layer_count):
            layers.append((i, self.circuit.layers[i].get_gates()))
        layers = self.prepare_layer_response(layers)
        return size, state, layer_count, layers

    def createCircuit(self, request):
        self.circuit = Circuit(request.size, request.layerCount)
        for layer in request.layers:
            for gate in layer['gates']:
                self.circuit.add(gate['gate'], gate['qubits'], layer['step'], gate['controls'])
        self.circuit.set_register(request.state)
        return self.get_circuit()

    def reset(self):
        self.circuit = Circuit()
        return self.get_circuit()

    def add(self, request):
        result = self.circuit.add(request.gate, request.qubits, request.step, request.controls)
        added = self.prepare_layer_response(result.added)
        removed = self.prepare_removal_response(result.removed)
        return added, removed

    def remove(self, request):
        result = self.circuit.remove(request.qubits, request.step)
        removed = self.prepare_removal_response(result.removed)
        return removed

    def compute(self, request):
        return self.circuit.compute(request.time)

    def set_register(self, request):
        self.circuit.set_register(request.state)
        result = self.circuit.resize(request.size)
        return self.prepare_removal_response(result.removed)

    def get_results(self):
        return self.circuit.get_results()

    def get_register_size(self):
        return self.circuit.size

    def get_register_state(self):
        return self.circuit.current_state

    def prepare_layer_response(self, circuit_layers):
        layers = list()
        gates = list()
        for circuit_layer in circuit_layers:
            for circuit_gate in circuit_layer[1]:
                gates.append(CircuitGateResponse(circuit_gate.qubits, circuit_gate.basegate, circuit_gate.controls))
            layers.append(CircuitLayerResponse(circuit_layer[0], gates))
            gates = list()
        return layers

    def prepare_removal_response(self, circuit_layers):
        removed = list()
        for circuit_layer in circuit_layers:
            removed.append(CleanSlotResponse(circuit_layer[0], circuit_layer[1]))
        return removed


