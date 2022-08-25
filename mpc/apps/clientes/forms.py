from xml.dom.minidom import Attr
from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:

        model = Clientes
        
        fields = '__all__'

        widgets = {
            'id_persona': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el numero de telefono'})
        }

        labels = {
            'id_persona': 'Nombre de la Persona:',
            'telefono': 'Numero de telefono:'
        }