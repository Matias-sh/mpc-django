from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_clientes, name='vista_clientes'),
    path('nuevo_cliente/', views.vista_crear_cliente, name='nuevo_cliente'),
    path('editar_cliente/<int:id>/', views.vista_editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/<int:id>/', views.vista_eliminar_cliente, name='eliminar_cliente'),
]