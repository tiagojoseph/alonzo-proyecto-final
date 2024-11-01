from django.urls import path
from inicio import views

app_name = "inicio"

urlpatterns = [
    path ("", views.inicio, name="inicio"),
    path ("creacion-casa/<ubicacion>/<ambientes>/<precio>", views.creacion_casa, name="creacion_casa"),
    path ("crear-casa/", views.crear_casa, name= "crear_casa"),
    path ("buscar-casa/", views.buscar_casa, name="buscar_casa" ),
    path ("about-me", views.about_me, name= "about_me" ),
    path ("casas/crear/", views.CrearCasa.as_view(), name= "crear_casa_nueva"),
    path ("casas/", views.ListadoCasas.as_view(), name="listado_casas"),
    path ("casas/<int:pk>/", views.VerCasa.as_view() , name="ver_casa"),
    path ("casas/<int:id_casa>/eliminar", views.eliminar_casa, name="eliminar_casa"),
    path ("casas/<int:id_casa>/editar", views.editar_casa , name="editar_casa")
    
      ]