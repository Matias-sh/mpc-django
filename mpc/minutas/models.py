from django.db import models

# Create your models here.

class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField()
    apellido = models.CharField()
    dni = models.IntegerField()
    sexo = models.CharField()
    fecha_nac = models.DateField()
    detalle_persona = models.CharField()

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField()
    constrasenia = models.CharField()
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class TipoPago(models.Model):
    id_tipo_pago = models.AutoField(primary_key=True)
    descripcion = models.CharField()

class Efectivo(models.Model):
    id_efectivo = models.AutoField(primary_key=True)
    descripcion = models.CharField()

class DetalleMinuta(models.Model):
    id_detalle_minuta = models.AutoField(primary_key=True)
    descripcion = models.CharField()


class MinutaGeneral(models.Model):
    id_minuta_general = models.AutoField(primary_key=True)
    importe_minuta = models.DecimalField()
    diferencia = models.DecimalField()
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_tipo_pago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    id_efectivo = models.ForeignKey(Efectivo, on_delete=models.CASCADE)
    id_detalle_minuta = models.ForeignKey(DetalleMinuta, on_delete=models.CASCADE)
