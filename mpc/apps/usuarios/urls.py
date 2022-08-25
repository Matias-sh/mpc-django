from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_usuarios, name='vista_usuarios'),
]