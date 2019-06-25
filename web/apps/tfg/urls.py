from django.urls import path
from .views import crearPeticion

urlpatterns = [
    path('crear_peticion/',crearPeticion, name = 'crear_peticion')
]