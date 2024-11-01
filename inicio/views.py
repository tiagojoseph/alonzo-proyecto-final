from django.shortcuts import render, redirect
from inicio.models import Casa
from inicio.forms import CrearCasaFromulario, BuscarCasaFormulario, EdicionCasa
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

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




class CrearCasa (CreateView):
    model= Casa
    template_name= "inicio/crear_casa_nueva.html"
    success_url = reverse_lazy("inicio:listado_casas")
    fields = ["ubicacion", "ambientes", "precio"]

class ListadoCasas(ListView):
    model = Casa
    template_name= "inicio/listado_casas.html"  
    context_object_name = "casas" 


def eliminar_casa (request, id_casa):
    casa = Casa.objects.get(id=id_casa)
    casa.delete()
    return redirect ("inicio:listado_casas")

def editar_casa(request, id_casa):

    casa = Casa.objects.get(id=id_casa)

    formulario = EdicionCasa(initial={"ubicacion": casa.ubicacion, "ambientes": casa.ambientes, "precio": casa.precio } )
    if request.method == "POST":
        formulario = EdicionCasa (request.POST) 
        if formulario.is_valid():
            casa.ubicacion = formulario.cleaned_data ["ubicacion"]
            casa.ambientes = formulario.cleaned_data ["ambientes"]
            casa.precio = formulario.cleaned_data ["precio"]

            casa.save()
            return redirect ("inicio:listado_casas")
        
    return render (request, "inicio/editar_casa.html", { "form": formulario, "casa" : casa })


class VerCasa(DetailView):
    model = Casa 
    template_name = "inicio/ver_casa.html"