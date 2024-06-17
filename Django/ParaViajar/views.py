from django.shortcuts import render
# Create your views here.
def index(request):
    context = {}
    return render(request, "pages/index.html", context)

def confirmar_reserva(request):
    context = {}
    return render(request, "pages/confirmar_reserva.html", context)

def destino(request):
    context = {}
    return render(request, "pages/destino.html", context)

def hoteles(request):
    context = {}
    return render(request, "pages/hoteles.html", context)

def nosotros(request):
    context = {}
    return render(request, "pages/nosotros.html", context)

def vuelos(request):
    context = {}
    return render(request, "pages/vuelos.html", context)

