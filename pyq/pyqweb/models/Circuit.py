from django.db import models

class Circuit(models.Model):
    name = models.CharField(max_length=32)
    size = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
