from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_barrios, name='vista_barrios'),
    path('nuevo_barrio/', views.vista_nuevo_barrio, name='nuevo_barrio'),
    path('editar_barrio/<int:id>/', views.vista_editar_barrio, name='editar_barrio'),
    path('eliminar_barrio/<int:id>/', views.vista_eliminar_barrio, name='eliminar_barrio')
]