from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('minuta_caja/', views.minuta_caja, name="minuta_caja"),
    path('ing_mont_barrio/', views.ing_mont_barrio, name="ing_mont_barrio"),
    path('legajo_cliente/', views.legajo_cliente, name="legajo_cliente"),
    path('registrarCuota/', views.registrarCuota),
    path('legajo_cliente/edicionCuota/<id_cuota_cliente>', views.edicionCuota),
    path('editarCuota/', views.editarCuota),
    path('legajo_cliente/eliminarCuota/<id_cuota_cliente>', views.eliminarCuota),
    path('nuevo_cliente/', views.nuevo_cliente, name="nuevo_cliente"),
    path('nuevo_barrio/', views.nuevo_barrio, name="nuevo_barrio"),
]