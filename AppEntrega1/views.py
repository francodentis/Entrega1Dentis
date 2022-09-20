from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega1.forms import *
from AppEntrega1.models import *

# Create your views here.
def inicio(request):
    return render(request,"AppEntrega1/inicio.html")

def salones(request):
    if request.method == "POST":
        SalonesFormulario = EntregableFormularioSalon(request.POST)
        print(SalonesFormulario)
        if SalonesFormulario.is_valid:
            informacion = SalonesFormulario.cleaned_data
            salon=Salones(salon=informacion['salon'],ciudad=informacion['ciudad'],capacidad=informacion['capacidad'])
            salon.save()
            return render(request,"AppEntrega1/inicio.html")
    else:
        SalonesFormulario = EntregableFormularioSalon()
    return render(request,"AppEntrega1/salones.html",{"SalonesFormulario":SalonesFormulario})
    return render(request,"AppEntrega1/salones.html")

def vestidos(request):
    if request.method == "POST":
        VestidosFormulario = EntregableFormularioVestidos(request.POST)
        print(VestidosFormulario)
        if VestidosFormulario.is_valid:
            informacion = VestidosFormulario.cleaned_data
            vestidos=Vestidos(modelo=informacion['modelo'],color=informacion['color'],modista=informacion['modista'],precio=informacion['precio'])
            vestidos.save()
            return render(request,"AppEntrega1/inicio.html")
    else:
        VestidosFormulario = EntregableFormularioVestidos()
    return render(request,"AppEntrega1/vestidos.html",{"VestidosFormulario":VestidosFormulario})

def lunademiel(request):
    if request.method == "POST":
        LunaDeMielFormulario = EntregableFormularioLunaDeMiel(request.POST)
        print(LunaDeMielFormulario)
        if LunaDeMielFormulario.is_valid:
            informacion = LunaDeMielFormulario.cleaned_data
            destino=LunaDeMiel(destino=informacion['destino'])
            destino.save()
            return render(request,"AppEntrega1/inicio.html")
    else:
        LunaDeMielFormulario = EntregableFormularioLunaDeMiel()
    return render(request,"AppEntrega1/lunademiel.html",{"LunaDeMielFormulario":LunaDeMielFormulario})

def busquedasalones(request):
    return render(request,"AppEntrega1/busquedasalones.html")

def resultadobusqueda(request):
    return render(request,"AppEntrega1/resultadobusqueda.html")

def buscar(request):
    if request.GET['ciudad']:
        ciudad = request.GET['ciudad']
        salones = Salones.objects.filter(ciudad__icontains=ciudad)
        return render(request,"AppEntrega1/resultadobusqueda.html",{"ciudad":ciudad, "salones":salones})
    else:
        respuesta = "No enviaste datos"
    return render(request,"AppEntrega1/resultadobusqueda.html",{"respuesta":respuesta})
    

def contacto(request):
    return render(request,"AppEntrega1/contacto.html")