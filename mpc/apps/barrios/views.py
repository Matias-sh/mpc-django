from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def vista_barrios(request):
    barrios = Barrios.objects.all()
    context = {
        'barrios': barrios
    }
    return render(request, 'barrios/barrios.html', context)

def vista_nuevo_barrio(request):
    if request.method == 'POST':
        form = BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vista_barrios')
    else:
        form = BarrioForm()

    context = {
        'form': form
    }

    return render(request, 'barrios/nuevo_barrio.html', context)

def vista_editar_barrio(request, id):
    barrio = Barrios.objects.get(id=id)
    if request.method == 'POST':
        form = BarrioForm(request.POST, instance=barrio)
        if form.is_valid():
            form.save()
            return redirect('vista_barrios')
    else:
        form = BarrioForm(instance=barrio)

    context = {
        'form': form
    }

    return render(request, 'barrios/editar_barrio.html', context)

def vista_eliminar_barrio(request, id):
    barrio = Barrios.objects.get(id=id)
    barrio.delete()
    return redirect('vista_barrios')