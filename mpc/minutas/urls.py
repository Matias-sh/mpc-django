from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('minutas/', views.minutas, name="minutas"),
    path('ing_mont_barrio/', views.ing_mont_barrio, name="ing_mont_barrio")
]