
class CircuitGateRequest(object):

    def __init__(self, qubits, gate, controls):
        self.qubits = qubits
        self.gate = gate
        self.controls = controls
