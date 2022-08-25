from django.db import models

from apps.personas.models import Personas

# Create your models here.

class DueniosBarrios(models.Model):
    id_dueniobarrio = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Personas, on_delete=models.CASCADE)
    detalle_duenio = models.TextField()

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.id_persona.nombre, self.id_persona.apellido)
