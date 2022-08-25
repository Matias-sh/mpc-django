from django import forms
from django.forms import ModelForm
from .models import *

class DuenioBarrioForm(forms.ModelForm):
    class Meta:

        model = DueniosBarrios

        fields = '__all__'

        widgets = {
            'id_persona': forms.Select(attrs={'class': 'form-control'}),
            'detalle_duenio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del Dueño'})
        }

        labels = {
            'id_persona': 'Nombre de la Persona',
            'detalle_duenio': 'Detalle del Dueño'
        }