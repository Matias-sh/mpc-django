from django.shortcuts import render

# Create your views here.

def vista_clientes(request):
    return render(request, 'clientes.html')