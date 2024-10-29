from django.urls import path
from inicio.views import inicio, creacion_casa, crear_casa, buscar_casa

app_name = "inicio"

urlpatterns = [
    path ("", inicio, name="inicio"),
    path ("creacion-casa/<ubicacion>/<ambientes>/<precio>", creacion_casa, name="creacion_casa"),
    path ("crear-casa/", crear_casa, name= "crear_casa"),
    path ("buscar-casa/", buscar_casa, name="buscar_casa" )
]