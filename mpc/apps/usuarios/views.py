from django.shortcuts import render

# Create your views here.

def vista_usuarios(request):
    return render(request, 'vista_usuarios.html')