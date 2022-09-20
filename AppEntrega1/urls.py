from django.urls import path
from AppEntrega1 import views


urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('salones',views.salones,name="Salones"),
    path('vestidos',views.vestidos,name="Vestidos"),
    path('lunademiel',views.lunademiel,name="LunaDeMiel"),
    path('contacto',views.contacto,name="Contacto"),
    path('busquedasalones',views.busquedasalones,name="BusquedaSalones"),
    path('resultadobusqueda',views.busquedasalones,name="ResultadoBusqueda"),
    path('buscar/',views.buscar),
]