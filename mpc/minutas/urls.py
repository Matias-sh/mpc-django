from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('minuta_caja/', views.minuta_caja, name="minuta_caja"),
    path('ing_mont_barrio/', views.ing_mont_barrio, name="ing_mont_barrio"),
    path('legajo_cliente/', views.legajo_cliente, name="legajo_cliente")
]