from django.urls import path
from ParaViajar import views

""" path('nombreURL',funcionVista,nombreDePagina) """

urlpatterns = [
    path("", views.index, name="index"),
    path("confirmar_reserva", views.confirmar_reserva, name="confirmar_reserva"),
    path("destino", views.destino, name="destino"),
    path("hoteles", views.hoteles, name="hoteles"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("vuelos", views.vuelos, name="vuelos"),
]
