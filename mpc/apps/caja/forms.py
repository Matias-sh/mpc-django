from django import forms
from .models import *

class CajaForm(forms.ModelForm):
    class Meta:

        model = General

        fields = '__all__'

        widgets = {
            'dv1_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta'}),
            'dv1_ga': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'dv1_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'dv1_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'dv2_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta'}),
            'dv2_ga': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'dv2_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'dv2_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'rigo_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta'}),
            'rigo_ga': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'rigo_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'rigo_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'si_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta'}),
            'si_ga': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'si_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'si_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'si2_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta'}),
            'si2_ga': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'si2_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'si2_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'der_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta'}),
            'der_ga': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'der_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'der_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'dea_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta'}),
            'dea_ga': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'dea_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'dea_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'dee_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta'}),
            'dee_ga': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'dee_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'dee_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'sa_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta'}),
            'sa_ga': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'sa_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'sa_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'ceto_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta'}),
            'ceto_ga': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'ceto_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
            'ceto_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja'}),
        }
        
        labels = {

        }