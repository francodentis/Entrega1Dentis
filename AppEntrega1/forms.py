from django import forms

class EntregableFormularioSalon(forms.Form):
    salon=forms.CharField()
    ciudad=forms.CharField()
    capacidad=forms.IntegerField()
class EntregableFormularioVestidos(forms.Form):
    modelo=forms.CharField()
    color=forms.CharField()
    modista=forms.CharField()
    precio=forms.IntegerField()
class EntregableFormularioLunaDeMiel(forms.Form):
    destino=forms.CharField()
class BusquedaLunaDeMiel(forms.Form):
    destino=forms.CharField()