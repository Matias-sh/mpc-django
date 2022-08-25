from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_clientes, name='vista_clientes'),
]