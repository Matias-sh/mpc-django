from django.db import models

# Create your models here.
   

class Persona(models.Model):
    opciones_sexo = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=opciones_sexo)
    fecha_nac = models.DateField()
    detalle_persona = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre + " " + self.apellido

class DueñoBarrio(models.Model):
    id_dueño_barrio = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    detalle_dueño_barrio = models.CharField(max_length=200)

    def __str__(self):
        return self.persona.nombre + " " + self.persona.apellido

class Barrio(models.Model):
    id_barrio = models.AutoField(primary_key=True)
    nombre_barrio = models.CharField(max_length=40, null=True)
    detalle_barrio = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nombre_barrio

class BarrioDueñoDet(models.Model):
    id_barrio_det = models.AutoField(primary_key=True)
    id_barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    id_dueño_barrio = models.ForeignKey(DueñoBarrio, on_delete=models.CASCADE)
    mz = models.IntegerField()
    pc = models.IntegerField()

    def __str__(self):
        return self.id_barrio.nombre_barrio + " " + self.id_dueño_barrio.persona.nombre + " " + self.id_dueño_barrio.persona.apellidos

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    telefono = models.IntegerField()
    email = models.CharField(max_length=100, null=True)
    detalle_cliente = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.id_persona.nombre + " " + self.id_persona.apellido

class ClienteBarrio(models.Model):
    id_cliente_barrio = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    cant_cuotas = models.IntegerField()

    def __str__(self):
        return self.id_cliente.id_persona.nombre + " " + self.id_cliente.id_persona.apellido + " Barrio:" + self.id_barrio.nombre_barrio

class TpoCuota(models.Model):
    id_tpo_cuota = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.descripcion

class TpoPago(models.Model):
    id_tpo_pago = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.descripcion

""" Modelo de formulario de guardar una cuota """
class ClienteBarrioCuotas(models.Model):
    id_cliente_barrio_cuotas = models.AutoField(primary_key=True)
    id_cliente_barrio = models.ForeignKey(ClienteBarrio, on_delete=models.CASCADE)
    nro_cuota = models.IntegerField()
    id_tpo_cuota = models.ForeignKey(TpoCuota, on_delete=models.CASCADE, null=True)
    cuota_total_pesos = models.DecimalField(max_digits=99999, decimal_places=2)
    cuota_mas_interes = models.DecimalField(max_digits=99999, decimal_places=2)
    porcentaje_gastos = models.DecimalField(max_digits=99999, decimal_places=2)
    gastos_pesos = models.DecimalField(max_digits=99999, decimal_places=2)
    porcentaje_interes = models.DecimalField(max_digits=99999, decimal_places=2)
    interes_pesos = models.DecimalField(max_digits=99999, decimal_places=2)
    detalle = models.CharField(max_length=500, null=True)
    observaciones = models.CharField(max_length=500, null=True)
    id_tpo_pago = models.ForeignKey(TpoPago, on_delete=models.CASCADE, null=True)
    detalle_cliente_barrio_det = models.CharField(max_length=200)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.TextField(max_length=20)
    constrasenia = models.CharField(max_length=30, null=True )
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Efectivo(models.Model):
    id_efectivo = models.AutoField(primary_key=True)
    descripcion = models.DecimalField(max_digits=9999, decimal_places=2)