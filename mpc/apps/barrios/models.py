from django.db import models
from apps.dueniosBarrios.models import DueniosBarrios

# Create your models here.

class Barrios(models.Model):
    id_barrio = models.AutoField(primary_key=True)
    id_dueniobarrio = models.ForeignKey(DueniosBarrios, on_delete=models.CASCADE)
    nombre_barrio = models.CharField(max_length=50)
    