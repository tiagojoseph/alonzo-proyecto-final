from django.shortcuts import render
from inicio.models import Casa

def inicio (request):
    return render (request, "inicio/index.html")

def creacion_casa (request, ubicacion, ambientes, precio):

    casa = Casa (ubicacion = ubicacion, ambientes = ambientes, precio = precio)
    casa.save()
    return render (request, "inicio/creacion_casa.html", {"casa": casa})

def crear_casa (request):
    return render (request, "inicio/crear_casa.html", {"casa": ""})

def buscar_casa (request):
    return render (request, "inicio/buscar_casa.html", {"casa": ""})