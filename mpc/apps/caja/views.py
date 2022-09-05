from django.shortcuts import render
from .forms import *

# Create your views here.

def caja(request):
    tabla_general = General.objects.all()
    context = {
        'tabla_general': tabla_general
    }
    return render(request, 'caja/caja.html', context)

def formulario_caja(request):
    if request.method == 'POST':
        form = CajaForm(request.POST)
        form2 = DetMinutaForm(request.POST)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect('vista_caja')
    else:
        form = CajaForm()
        form2 = DetMinutaForm()

    context = {
        'form': form,
        'form2': form2
    }

    return render(request, 'caja/cajona.html', context)
