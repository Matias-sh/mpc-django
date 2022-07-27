from django import forms
from .models import *

class LegajoClienteForm(forms.Form):
    """
    class Meta:
        model =

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
            'apellido': forms.CharField()
            'nombre': forms.CharField()
            'documento': forms.IntegerField()
            'barrio': forms.CharField()
            'mz': forms.CharField()
            'pc': forms.CharField()
            'actualizacion': forms.CharField()
            'aviso': forms.CharField()
            'fecha_legajo_cliente': forms.DateField()
            'total': forms.DecimalField()
        }    
    """

class AltaPagoForm(forms.Form):
    """
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