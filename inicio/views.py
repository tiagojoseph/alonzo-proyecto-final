from django.shortcuts import render, redirect
from inicio.models import Casa
from inicio.forms import CrearCasaFromulario, BuscarCasaFormulario

def inicio (request):
    return render (request, "inicio/index.html")

def creacion_casa (request, ubicacion, ambientes, precio):

    casa = Casa (ubicacion = ubicacion, ambientes = ambientes, precio = precio)
    casa.save()
    return render (request, "inicio/creacion_casa.html", {"casa": casa})

def crear_casa (request):

    print ('Request', request)
    print ('Get', request.GET)
    print ('Post', request.POST)

    formulario = CrearCasaFromulario()

    if request.method == 'POST':

        formulario = CrearCasaFromulario (request.POST)
        if formulario.is_valid():
            data= formulario.cleaned_data
            casa = Casa (ubicacion=data.get("ubicacion"), ambientes=data.get("ambientes"), precio=data.get("precio"))
            casa.save()
            return redirect ("inicio:buscar_casa")
    

    return render (request, "inicio/crear_casa.html", {"form": formulario})

def buscar_casa (request):

    formulario = BuscarCasaFormulario(request.GET)
    if formulario.is_valid():
        ubicacion = formulario.cleaned_data.get("ubicacion")
        precio = formulario.cleaned_data.get("precio")
        casas = Casa.objects.filter(ubicacion__icontains=ubicacion, precio__icontains= precio)
    

    return render (request, "inicio/buscar_casa.html", {"casas": casas, "form" : formulario})

def about_me (request):
    return render (request, "inicio/sobre_mi.html")