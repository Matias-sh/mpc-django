from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'minutas/index.html')

def minuta_caja(request):
    return render(request, 'minutas/minuta_caja.html')

def ing_mont_barrio(request):
    return render(request, 'minutas/ing_mont_barrio.html')

def nuevo_barrio(request):
    if request.method == 'POST':
        form = BarrioForm(data=request.POST)
        if form.is_valid():
            form_s = form.save(commit=False)
            form_s.save()
            return redirect('nuevo_barrio')
    else:
        form = BarrioForm()

    barriosListados = Barrio.objects.all()
    context = {
        'form': form,
        'barrio': barriosListados
    }
    
    return render(request, 'minutas/nuevo_barrio.html', context)

def nuevo_cliente(request):
    if request.method == 'POST':
        form = NuevoClienteForm(data=request.POST)
        if form.is_valid():
            form_s = form.save(commit=False)
            form_s.save()
            return redirect('nuevo_cliente')
    else:
        form = NuevoClienteForm()

    clientesListados = Cliente.objects.all()
    context = {
        'form': form,
        'cliente': clientesListados
    }
    
    return render(request, 'minutas/nuevo_cliente.html', context)

def legajo_cliente(request):
    if request.method == 'POST':
        form = CuotaClienteForm(data=request.POST)
        if form.is_valid():
            form_s = form.save(commit=False)
            form_s.save()
            return redirect('legajo_cliente')
    else:
        form = CuotaClienteForm()

    cuotasListadas = ClienteBarrioCuotas.objects.all()
    context = {
        'form': form,
        'cuota': cuotasListadas
    }
    
    return render(request, 'minutas/legajo_cliente.html', context)

def registrarCuota(request):
    nro_cuota = request.POST['txtNroCuotaCliente']
    tipo_cuota = request.POST['txtTipoCuota']
    cuota_total_pesos = request.POST['txtCuotaTotalPesos']
    cuota_mas_interes = request.POST['txtCuotaMasInteres']
    porcentaje_gastos = request.POST['txtPorcentajeGastos']
    gastos_pesos = request.POST['txtGastosPesos']
    porcentaje_interes = request.POST['txtPorcentajeInteres']
    interes_pesos = request.POST['txtInteresPesos']
    detalle = request.POST['txtDetalle']
    observaciones = request.POST['txtObservaciones']
    tipo_pago = request.POST['txtTipoPago']

    cuota = ClienteBarrioCuotas.objects.create(
        nro_cuota_cliente=nro_cuota_cliente,
        tipo_cuota=tipo_cuota,
        cuota_total_pesos=cuota_total_pesos,
        cuota_mas_interes=cuota_mas_interes,
        porcentaje_gastos=porcentaje_gastos,
        gastos_pesos=gastos_pesos,
        porcentaje_interes=porcentaje_interes,
        interes_pesos=interes_pesos,
        detalle=detalle,
        observaciones=observaciones,
        tipo_pago=tipo_pago
        )
    messages.success(request, '¡Cuota registrada!')
    return redirect('legajo_cliente')


def edicionCuota(request, id_cuota_cliente):
    cuota = Cuota.objects.get(id_cuota_cliente=id_cuota_cliente)
    return render(request, "minutas/edicionCuota.html", {"cuota": cuota})


def editarCuota(request):
    id_cuota_cliente = request.POST['txtCodigo']
    nro_cuota_cliente = request.POST['txtNroCuotaCliente']
    tipo_cuota = request.POST['txtTipoCuota']
    cuota_total_pesos = request.POST['txtCuotaTotalPesos']
    cuota_mas_interes = request.POST['txtCuotaMasInteres']
    porcentaje_gastos = request.POST['txtPorcentajeGastos']
    gastos_pesos = request.POST['txtGastosPesos']
    porcentaje_interes = request.POST['txtPorcentajeInteres']
    interes_pesos = request.POST['txtInteresPesos']
    detalle = request.POST['txtDetalle']
    observaciones = request.POST['txtObservaciones']
    tipo_pago = request.POST['txtTipoPago']

    cuota = Cuota.objects.get(id_cuota_cliente=id_cuota_cliente)
    cuota.nro_cuota_cliente=nro_cuota_cliente
    cuota.tipo_cuota=tipo_cuota
    cuota.cuota_total_pesos=cuota_total_pesos
    cuota.cuota_mas_interes=cuota_mas_interes
    cuota.porcentaje_gastos=porcentaje_gastos
    cuota.gastos_pesos=gastos_pesos
    cuota.porcentaje_interes=porcentaje_interes
    cuota.interes_pesos=interes_pesos
    cuota.detalle=detalle
    cuota.observaciones=observaciones
    cuota.tipo_pago=tipo_pago
    cuota.save()

    messages.success(request, '¡Cuota actualizado!')

    return redirect('legajo_cliente')


def eliminarCuota(request, id_cuota_cliente):
    cuota = Cuota.objects.get(id_cuota_cliente=id_cuota_cliente)
    cuota.delete()

    messages.success(request, '¡Cuota eliminado!')

    return redirect('legajo_cliente')
