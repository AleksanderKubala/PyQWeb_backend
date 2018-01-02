
class CircuitChangeResponse(object):

    def __init__(self, added = None, removed = None):
        self.added = added if added is not None else []
        self.removed = removed if removed is not None else []
