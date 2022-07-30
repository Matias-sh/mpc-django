from tkinter import Widget
from django import forms
from .models import *
"""
class CuotaClienteForm(forms.Form):

    class Meta:
        model = CuotaCliente

        fields = '__all__'

        widgets = {
            'nro_cuota_cliente': forms.NumberInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'tipo_cuota': forms.TextInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'cuota_total_pesos': forms.NumberInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'cuota_mas_interes': forms.NumberInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'porcentaje_gastos': forms.NumberInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'gastos pesos': forms.NumberInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'porcentaje_interes': forms.NumberInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'interes_pesos': forms.NumberInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'detalle': forms.TextInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'observaciones': forms.TextInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'tipo_pago': forms.TextInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            
        }
"""

"""
class LegajoClienteForm(forms.Form):
    
    class Meta:
        model = BarrioDet

        fields = [
            'apellido',
            'nombre',
            'barrio',
            'mz',
            'pc',
            'actualizacion',
            'aviso',
            'fecha_legajo_cliente',
            'total'
        ]
        widgets = {
            'apellido': forms.CharField(),
            'nombre': forms.CharField(),
            'documento': forms.IntegerField(),
            'barrio': forms.CharField(),
            'mz': forms.CharField(),
            'pc': forms.CharField(),
            'actualizacion': forms.CharField(),
            'aviso': forms.CharField(),
            'fecha_legajo_cliente': forms.DateField(),
            'total': forms.DecimalField()
        }    

class AltaPagoForm(forms.Form):
    class Meta:
        model = 

        fields = [
            'nro_cuota',
            'tipo',
            'cuota_total',
            'cuota_mas_interes',
            'porc_gastos',
            'gastos',
            'porc_interes',
            'interes',
            'detalle',
            'observaciones',
            'tipo_pago',
        ]
"""