from django import forms
from django.forms import ModelForm
from .models import *

class PersonaForm(ModelForm):
    class Meta:
        model = Personas
        fields = ['nombre', 'apellido', 'edad', 'telefono', 'email', 'domicilio']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'Email',
            'domicilio': 'Domicilio',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'domicilio': forms.Textarea(attrs={'class': 'form-control'}),
        }