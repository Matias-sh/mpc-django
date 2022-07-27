from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'minutas/index.html')

def minuta_caja(request):
    return render(request, 'minutas/minuta_caja.html')

def ing_mont_barrio(request):
    return render(request, 'minutas/ing_mont_barrio.html')

def legajo_cliente(request):
    return render(request, 'minutas/legajo_cliente.html')