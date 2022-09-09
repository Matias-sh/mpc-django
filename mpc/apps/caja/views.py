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
        if form.is_valid():
            form.save()
            return redirect('vista_caja')
    else:
        form = CajaForm()

    context = {
        'form': form,
    }

    return render(request, 'caja/formulario_caja2.html', context)
