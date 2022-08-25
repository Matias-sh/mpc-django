from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_personas, name='vista_personas'),
    path('nueva_persona/', views.vista_nueva_persona, name='nueva_persona'),
    path('editar_persona/<int:id>/', views.vista_editar_persona, name='editar_persona'),
    path('eliminar_persona/<int:id>/', views.vista_eliminar_persona, name='eliminar_persona'),
]