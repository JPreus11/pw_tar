from django.shortcuts import render

def index(request):
    return render(request, 'ParaViajar/index.html')

def destinos(request):
    return render(request, 'ParaViajar/destinos.html')

def hoteles(request):
    return render(request, 'ParaViajar/hoteles.html')

def vuelos(request):
    return render(request, 'ParaViajar/vuelos.html')

def confirmar_reserva(request):
    return render(request, 'ParaViajar/confirmar_reserva.html')

def nosotros(request):
    return render(request, 'ParaViajar/nosotros.html')
