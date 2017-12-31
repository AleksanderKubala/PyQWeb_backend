from pyq.pyqweb.Responses.CircuitChangeResponse import CircuitChangeResponse

class RegisterResponse(object):

    def __init__(self, state, size, changes=None):
        self.changes = changes if changes is not None else CircuitChangeResponse()
        self.state = state
        self.size = size
