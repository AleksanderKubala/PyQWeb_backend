from django.db import models
from .Circuit import Circuit
from .GateSignature import GateSignature

class Gate(models.Model):
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    signature = models.ForeignKey(GateSignature, on_delete=models.CASCADE)
    layer = models.PositiveIntegerField()
    qubit = models.PositiveIntegerField()
    size = models.PositiveIntegerField()
    controls = models.CharField(max_length=32)
