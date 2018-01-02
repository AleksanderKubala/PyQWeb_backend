
class AddGateRequest(object):

    def __init__(self, gate, qubits, step, controls):
        self.gate = gate
        self.qubits = qubits
        self.step = step
        self.controls = controls
