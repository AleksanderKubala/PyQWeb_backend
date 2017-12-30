from PyQ.Circuit import Circuit

from pyq.pyqweb.Requests.AddGateRequest import AddGateRequest
from pyq.pyqweb.Requests.CleanSlotRequest import CleanSlotRequest

class CircuitService(object):

    def __init__(self):
        self.circuit = Circuit()

    def get_circuit(self):
        size = self.get_circuit_size()
        state = self.get_register_state()
        layer_count = self.circuit.layer_count


    def add(self, request):
        result = self.circuit.add(request.gate, request.qubits, request.layer, request.controls)
        return self._generate_changes_results(result)

    def remove(self, request):
        result = self.circuit.remove(request.qubits, request.layer)
        return self._generate_changes_results(result)

    def compute(self, request):
        return self.circuit.compute(request.time)

    def set_circuit_size(self, new_size):
        result = self.circuit.resize(new_size)
        return self._generate_changes_results(result)

    def set_register_state(self, state):
        self.circuit.set_register(state)
        return self.get_register_state()

    def get_results(self):
        return self.circuit.get_results()

    def get_circuit_size(self):
        return self.circuit.size

    def get_register_state(self):
        return self.circuit.current_state

    def _generate_changes_results(self, result):
        for i in range(len(result.added)):
            addition = (result.added[i])
            result.added[i] = AddGateRequest(addition[1].basegate, addition[1].qubits, addition[0], addition[1].controls)
        for i in range(len(result.removed)):
            removal = (result.removed[i])
            result.removed[i] = CleanSlotRequest(removal[0], removal[1])
        return result

    def _generate_compute_results(self, results):
        pass
