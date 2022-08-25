from django import forms
from django.forms import ModelForm
from .models import *


class BarrioForm(forms.ModelForm):
    class Meta:
        model = Barrios

        fields = '__all__'

        widgets = {
            'id_dueniobarrio': forms.Select(attrs={'class': 'form-control'}),
            'nombre_barrio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte el nombre del barrio'}),
        }
        labels = {
            'id_dueniobarrio': 'Dueño del Barrio',
            'nombre_barrio': 'Nombre del Barrio'
        }