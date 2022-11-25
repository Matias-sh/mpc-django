from django import forms
from .models import *

class CajaForm(forms.ModelForm):
    class Meta:

        model = General

        fields = (
            'id_general',
            'dv1_m',
            'dv1_ga',
            'dv1_tar',
            'dv1_ga_tar',
            'dv2_m',
            'dv2_ga',
            'dv2_tar',
            'dv2_ga_tar',
            'rigo_m',
            'rigo_ga',
            'rigo_tar',
            'rigo_ga_tar',
            'si_m',
            'si_ga',
            'si_tar',
            'si_ga_tar',
            'si2_m',
            'si2_ga',
            'si2_tar',
            'si2_ga_tar',
            'der_m',
            'der_ga',
            'der_tar',
            'der_ga_tar',
            'dea_m',
            'dea_ga',
            'dea_tar',
            'dea_ga_tar',
            'dee_m',
            'dee_ga',
            'dee_tar',
            'dee_ga_tar',
            'sa_m',
            'sa_ga',
            'sa_tar',
            'sa_ga_tar',
            'ceto_m',
            'ceto_ga',
            'ceto_tar',
            'ceto_ga_tar',
            'gara_m',
            'gara_ga',
            'gara_tar',
            'gara_ga_tar',
            'apodaca_m',
            'apodaca_ga',
            'apodaca_tar',
            'apodaca_ga_tar',
            'total_m',
            'total_ga',
            'total_tar',
            'total_m_ga_tar',
            'total_ingresado',
        )

        widgets = {
            'dv1_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'dv1_m', 'onKeyUp': 'total_M()', 'value': '$'}),
            'dv1_ga': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'dv1_ga', 'onKeyUp': 'total_GA()'}),
            'dv1_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'dv1_tar', 'onKeyUp': 'total_TAR()'}),
            'dv1_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'dv1_ga_tar', 'onKeyUp': 'total_GA_TAR()'}),
            'dv2_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'dv2_m', 'onKeyUp': 'total_M()'}),
            'dv2_ga': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'dv2_ga', 'onKeyUp': 'total_GA()'}),
            'dv2_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'dv2_tar', 'onKeyUp': 'total_TAR()'}),
            'dv2_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'dv2_ga_tar', 'onKeyUp': 'total_GA_TAR()'}),
            'rigo_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'rigo_m', 'onKeyUp': 'total_M()'}),
            'rigo_ga': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'rigo_ga', 'onKeyUp': 'total_GA()'}),
            'rigo_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta','id': 'rigo_tar', 'onKeyUp': 'total_TAR()'}),
            'rigo_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'rigo_ga_tar', 'onKeyUp': 'total_GA_TAR()'}),
            'si_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'si_m', 'onKeyUp': 'total_M()'}),
            'si_ga': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'si_ga', 'onKeyUp': 'total_GA()'}),
            'si_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'si_tar', 'onKeyUp': 'total_TAR()'}),
            'si_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'si_ga_tar', 'onKeyUp': 'total_GA_TAR()'}),
            'si2_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'si2_m', 'onKeyUp': 'total_M()'}),
            'si2_ga': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'si2_ga', 'onKeyUp': 'total_GA()'}),
            'si2_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'si2_tar', 'onKeyUp': 'total_TAR()'}),
            'si2_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'si2_ga_tar', 'onKeyUp': 'total_GA_TAR()'}),
            'der_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'der_m', 'onKeyUp': 'total_M()'}),
            'der_ga': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'der_ga', 'onKeyUp': 'total_GA()'}),
            'der_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'der_tar', 'onKeyUp': 'total_TAR()'}),
            'der_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'der_ga_tar', 'onKeyUp': 'total_GA_TAR()'}),
            'dea_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'dea_m', 'onKeyUp': 'total_M()'}),
            'dea_ga': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'dea_ga', 'onKeyUp': 'total_GA()'}),
            'dea_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'dea_tar', 'onKeyUp': 'total_TAR()'}),
            'dea_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'dea_ga_tar', 'onKeyUp': 'total_GA_TAR()'}),
            'dee_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'dee_m', 'onKeyUp': 'total_M()'}),
            'dee_ga': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'dee_ga', 'onKeyUp': 'total_GA()'}),
            'dee_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'dee_tar', 'onKeyUp': 'total_TAR()'}),
            'dee_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'dee_ga_tar', 'onKeyUp': 'total_GA_TAR()'}),
            'sa_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'sa_m', 'onKeyUp': 'total_M()'}),
            'sa_ga': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'sa_ga', 'onKeyUp': 'total_GA()'}),
            'sa_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'sa_tar', 'onKeyUp': 'total_TAR()'}),
            'sa_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'sa_ga_tar', 'onKeyUp': 'total_GA_TAR()'}),
            'ceto_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'ceto_m', 'onKeyUp': 'total_M()'}),
            'ceto_ga': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'ceto_ga', 'onKeyUp': 'total_GA()'}),
            'ceto_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'ceto_tar', 'onKeyUp': 'total_TAR()'}),
            'ceto_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'ceto_ga_tar', 'onKeyUp': 'total_GA_TAR()'}),
            'gara_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'gara_m', 'onKeyUp': 'total_M()'}),
            'gara_ga': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'gara_ga', 'onKeyUp': 'total_GA()'}),
            'gara_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'gara_tar', 'onKeyUp': 'total_TAR()'}),
            'gara_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'gara_ga_tar', 'onKeyUp': 'total_GA_TAR()'}),
            'apodaca_m': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'apodaca_m', 'onKeyUp': 'total_M()'}),
            'apodaca_ga': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'apodaca_ga', 'onKeyUp': 'total_GA()'}),
            'apodaca_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'apodaca_tar', 'onKeyUp': 'total_TAR()'}),
            'apodaca_ga_tar': forms.NumberInput(attrs={'class': 'form-control form-caja-minuta', 'id': 'apodaca_ga_tar', 'onKeyUp': 'total_GA_TAR()'}),
            'total_m': forms.NumberInput(attrs={'id': 'invi_total_m', 'readonly':'true', 'hidden': 'true'}),
            'total_ga': forms.NumberInput(attrs={'id': 'invi_total_ga', 'readonly':'true', 'hidden': 'true'}),
            'total_tar': forms.NumberInput(attrs={'id': 'invi_total_tar', 'readonly':'true', 'hidden': 'true'}),
            'total_m_ga_tar': forms.NumberInput(attrs={'id': 'invi_total_m_ga_tar', 'readonly':'true', 'hidden': 'true'}),
            'total_ingresado': forms.NumberInput(attrs={'id': 'invi_total_ingresado', 'readonly':'true', 'hidden': 'true'}),
            ### Fin inputs del form minuta
            
        }
        
        labels = {

        }

class MinDetForm(forms.ModelForm):
    class Meta:
        model = MinDet

        fields = (
            'codigo',
            'detalle',
            'especificacion',
            'monto',
        )

        widgets = {
            'codigo': forms.TextInput(attrs={'id': 'td-det-0', 'onkeyup': 'cod_DET(this)'}),
            'detalle': forms.TextInput(attrs={'class': 'form-caja-minuta', 'id': 'det-det-1', 'readonly': 'true'}),
            'especificacion': forms.TextInput(attrs={'class': 'form-caja-minuta esp-det'}),
            'monto': forms.NumberInput(attrs={'class': 'form-caja-minuta mont-det'}),
        }