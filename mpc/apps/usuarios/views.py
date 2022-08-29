from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.

def login(request):
    return render(request, 'vista_usuarios.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.username
            messages.success(request, f'¡Usuario {username} registrado!')
            return redirect('inicio')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'usuarios/register.html', context)