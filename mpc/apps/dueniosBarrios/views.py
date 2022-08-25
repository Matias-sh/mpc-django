from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def vista_dueniosBarrios(request):
    duenios = DueniosBarrios.objects.all()
    context = {
        'duenios': duenios
    }
    return render(request, 'dueniosBarrios/duenios_barrios.html', context)

def vista_nuevo_duenioBarrio(request):
    if request.method == 'POST':
        form = DuenioBarrioForm(request.POST)
        if form.is_valid():
            form.save()
            print('si es valido')
            return redirect('vista_dueniosBarrios')
    else:
        form = DuenioBarrioForm()

    context = {
        'form': form
    }

    return render(request, 'dueniosBarrios/nuevo_duenio.html', context)

def vista_editar_duenioBarrio(request, id):
    duenio = DueniosBarrios.objects.get(id_dueniobarrio=id)
    if request.method == 'POST':
        form = DuenioBarrioForm(request.POST, instance=duenio)
        if form.is_valid():
            form.save()
            return redirect('vista_dueniosBarrios')
    else:
        form = DuenioBarrioForm()

    context = {
        'form': form
    }

    return render(request, 'dueniosBarrios/editar_duenio.html', context)

def vista_eliminar_duenio(request, id):
    duenio = DueniosBarrios.objects.get(id_dueniobarrio=id)
    duenio.delete()
    return redirect(vista_dueniosBarrios)