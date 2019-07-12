from django.urls import path
from .views import ListarNoticias

urlpatterns = [
    # path('crear_peticion/',CrearPeticion, name = 'crear_peticion'), #dirección barra de dirección, código que se va a ejecutar, identificador de la url
    path('listar_noticias/', ListarNoticias, name= 'listar_noticias')
    # path('listar_noticias/', BuscarNoticia, name = "listar_noticias")
]