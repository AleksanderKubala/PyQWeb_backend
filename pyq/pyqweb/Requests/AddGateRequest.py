
class AddGateRequest(object):

    def __init__(self, gate, qubits, layer, controls):
        self.gate = gate
        self.qubits = qubits
        self.layer = layer
        self.controls = controls
