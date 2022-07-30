from django.db import models

# Create your models here.

class Cuota(models.Model):
    id_cuota_cliente = models.AutoField(primary_key=True)
    nro_cuota_cliente = models.IntegerField()
    tipo_cuota = models.CharField(max_length=40)
    cuota_total_pesos = models.DecimalField(max_digits=99999, decimal_places=2)
    cuota_mas_interes = models.DecimalField(max_digits=99999, decimal_places=2)
    porcentaje_gastos = models.DecimalField(max_digits=99999, decimal_places=2)
    gastos_pesos = models.DecimalField(max_digits=99999, decimal_places=2)
    porcentaje_interes = models.DecimalField(max_digits=99999, decimal_places=2)
    interes_pesos = models.DecimalField(max_digits=99999, decimal_places=2)
    detalle = models.CharField(max_length=500)
    observaciones = models.CharField(max_length=500)
    tipo_pago = models.CharField(max_length=40)


"""
class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    sexo = models.CharField(max_length=1)
    fecha_nac = models.DateField()
    detalle_persona = models.CharField(max_length=200)

class Barrio(models.Model):
    id_barrio = models.AutoField(primary_key=True)
    nombre_barrio = models.CharField(max_length=40)

class BarrioDet(models.Model):
    id_barrio_det = models.AutoField(primary_key=True)
    id_barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    mz = models.IntegerField()
    pc = models.IntegerField()

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    id_barrio_det = models.ForeignKey(BarrioDet, on_delete=models.CASCADE)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=20)
    constrasenia = models.CharField(max_length=30)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class TipoPago(models.Model):
    id_tipo_pago = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=15)

class Efectivo(models.Model):
    id_efectivo = models.AutoField(primary_key=True)
    descripcion = models.DecimalField(max_digits=9999, decimal_places=2)

class DetalleMinuta(models.Model):
    id_detalle_minuta = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)


class MinutaGeneral(models.Model):
    id_minuta_general = models.AutoField(primary_key=True)
    importe_minuta = models.DecimalField(max_digits=9999, decimal_places=2)
    diferencia = models.DecimalField(max_digits=9999, decimal_places=2)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_tipo_pago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    id_efectivo = models.ForeignKey(Efectivo, on_delete=models.CASCADE)
    id_detalle_minuta = models.ForeignKey(DetalleMinuta, on_delete=models.CASCADE)
"""