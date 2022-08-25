from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_dueniosBarrios, name='vista_dueniosBarrios'),
    path('nuevo_duenio/', views.vista_nuevo_duenioBarrio, name='nuevo_duenio'),
    path('editar_duenio/<int:id>/', views.vista_editar_duenioBarrio, name='editar_duenio'),
    path('eliminar_duenio/<int:id>/', views.vista_eliminar_duenio, name='eliminar_duenio')
]