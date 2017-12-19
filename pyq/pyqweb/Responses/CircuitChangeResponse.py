
class CircuitChangeResponse(object):

    def __init__(self, changes=None):
        self.added = changes.added if changes is not None else []
        self.removed = changes.removed if changes is not None else []
