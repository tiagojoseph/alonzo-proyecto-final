from django import forms 

class CrearCasaFromulario(forms.Form):
    ubicacion = forms.CharField (max_length=20)
    ambientes = forms.IntegerField ()
    precio = forms.CharField(max_length=20)

class BuscarCasaFormulario(forms.Form):
    ubicacion = forms.CharField (max_length=20, required=False)
    precio = forms.CharField (max_length=20, required=False)

class EdicionCasa(forms.Form):
    ubicacion = forms.CharField(max_length=20)
    ambientes = forms.IntegerField()
    precio = forms.CharField(max_length=20)