from pyq.pyqweb.Responses.CircuitChangeResponse import CircuitChangeResponse

class RegisterResponse(object):

    def __init__(self, state, size, removed):
        self.changes = CircuitChangeResponse(removed=removed)
        self.state = state
        self.size = size
