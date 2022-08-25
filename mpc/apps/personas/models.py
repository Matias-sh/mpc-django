from django.db import models

# Create your models here.

class Personas(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()

    def __str__(self):
        txt = '{0} {1}'
        return txt.format(self.nombre, self.apellido)