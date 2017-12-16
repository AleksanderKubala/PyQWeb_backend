from django.db import models

class GateSignature(models.Model):
    signature = models.CharField(max_length=32)
