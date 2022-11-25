from django.urls import path
from . import views

urlpatterns = [
    path('', views.caja, name='vista_caja'),
    path('formulario_caja/', views.formulario_caja, name='formulario_caja'),
]