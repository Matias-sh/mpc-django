from django.shortcuts import render, redirect
from .forms import *
# Create your views here.

def vista_personas(request):
    personas = Personas.objects.all()
    context = {
        'personas': personas,
    }
    return render(request, 'personas/personas.html', context)

def vista_nueva_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vista_personas')
    else:
        form = PersonaForm()
    
    context = {
        'form': form
    }

    return render(request, 'personas/nueva_persona.html', context)

def vista_editar_persona(request, id):
    persona = Personas.objects.get(id_persona=id)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('vista_personas')
    else:
        form = PersonaForm(instance=persona)
    
    context = {
        'form': form
    }

    return render(request, 'personas/editar_persona.html', context)

def vista_eliminar_persona(request, id):
    persona = Personas.objects.get(id_persona=id)
    persona.delete()
    return redirect('vista_personas')