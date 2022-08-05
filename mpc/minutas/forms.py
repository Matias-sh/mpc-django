from django import forms
from .models import *

class CuotaClienteForm(forms.ModelForm):

    class Meta:
        model = ClienteBarrioCuotas

        fields = '__all__'

        widgets = {
            'id_cliente_barrio_det': forms.Select(attrs={'class': 'form-control', 'label': 'Cliente'}),
            'nro_cuota': forms.NumberInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'tipo_cuota': forms.Select(attrs={'class': 'form-control'}),
            'cuota_total_pesos': forms.NumberInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'cuota_mas_interes': forms.NumberInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'porcentaje_gastos': forms.NumberInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'gastos pesos': forms.NumberInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'porcentaje_interes': forms.NumberInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'interes_pesos': forms.NumberInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'detalle': forms.TextInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'observaciones': forms.TextInput(attrs={"placeholder": "Ingrese el numero de cuota de cliente", "class": "form-control"}),
            'tipo_pago': forms.Select(attrs={'class': 'form-control'}),
            
        }



class PersonaForm(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={"placeholder": "Ingrese el nombre", "class": "form-control"}),
            'apellido': forms.TextInput(attrs={"placeholder": "Ingrese el apellido", "class": "form-control"}),
            'dni': forms.NumberInput(attrs={"placeholder": "Ingrese el dni", "class": "form-control"}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'fecha_nac': forms.DateInput(attrs={"placeholder": "Ingrese la fecha de nacimiento", "class": "form-control"}),
            'detalle_persona': forms.TextInput(attrs={"placeholder": "Ingrese el detalle", "class": "form-control"}),
        }

class NuevoClienteForm(forms.ModelForm):
    
        class Meta:
            model = ClienteBarrio

            fields = '__all__'

            widgets = {
                'id_persona': forms.Select(attrs={'class': 'form-control'}),
                'telefono': forms.NumberInput(attrs={"placeholder": "Ingrese el telefono", "class": "form-control"}),
                'email': forms.EmailInput(attrs={"placeholder": "Ingrese el email", "class": "form-control"}),
                'detalle_cliente': forms.TextInput(attrs={"placeholder": "Ingrese el detalle", "class": "form-control"}),
            }

class NuevoDueñoBarrioForm(forms.ModelForm):
    class Meta:
        model = DueñoBarrio
        fields = '__all__'
        widgets = {
            'id_persona': forms.Select(attrs={'class': 'form-control'}),
            'detalle_barrio': forms.TextInput(attrs={"placeholder": "Ingrese el detalle", "class": "form-control"}),
        }

class NuevoBarrioForm(forms.ModelForm):
    class Meta:
        model = Barrio
        fields = '__all__'
        widgets = {
            'nombre_barrio': forms.TextInput(attrs={"placeholder": "Ingrese el nombre del barrio", "class": "form-control"}),
            'detalle_barrio': forms.TextInput(attrs={"placeholder": "Ingrese el detalle", "class": "form-control"}),
        }

class ClienteBarrioForm(forms.ModelForm):
    class Meta:
        model = ClienteBarrio
        fields = '__all__'
        widgets = {
            'id_cliente': forms.Select(attrs={'class': 'form-control'}),
            'id_barrio': forms.Select(attrs={'class': 'form-control'}),
            'cant_cuotas': forms.NumberInput(attrs={"placeholder": "Ingrese el numero de cuotas de cliente", "class": "form-control"}),
        }
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