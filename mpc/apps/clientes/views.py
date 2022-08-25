from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def vista_clientes(request):
    clientes = Clientes.objects.all()
    context = {
        'clientes': clientes
    }
    return render(request, 'clientes/clientes.html', context)

def vista_crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vista_clientes')
    else:
        form = ClienteForm()

    context = {
        'form': form
    }

    return render(request, 'clientes/nuevo_cliente.html', context)

def vista_editar_cliente(request, id):
    cliente = Clientes.objects.get(id_cliente=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('vista_cliente')
    else:
        form = ClienteForm()

    context = {
        'form': form
    }

    return render(request, 'clientes/editar_cliente.html', context)

def vista_eliminar_cliente(request, id):
    cliente = Clientes.objects.get(id_cliente=id)
    cliente.delete()
    return redirect('vista_clientes')