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

def legajo_cliente(request):
    cuotasListadas = Cuota.objects.all()
    return render(request, 'minutas/legajo_cliente.html', {'cuota': cuotasListadas})

def registrarCuota(request):
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

    cuota = Cuota.objects.create(
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
