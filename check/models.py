from django.db import models

class MiModelo(models.Model):
    valor = models.BooleanField(default=False)
    nombre = models.CharField(max_length=20,null=True, blank=True)

