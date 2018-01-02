from PyQ.GateInfoRegister import GateInfoRegister

class GateService(object):

    def get_gates(self):
        return GateInfoRegister.instance().register.values()
