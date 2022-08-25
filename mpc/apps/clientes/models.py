from django.db import models
from apps.personas.models import Personas

# Create your models here.

class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Personas, on_delete=models.CASCADE)
    telefono = models.IntegerField()
