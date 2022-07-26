from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'minutas/index.html')

def minutas(request):
    return render(request, 'minutas/minutas.html')

def ing_mont_barrio(request):
    return render(request, 'minutas/ing_mont_barrio.html')