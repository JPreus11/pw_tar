from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso.")
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'pages/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Has iniciado sesión como {username}.")
                return redirect('index')
            else:
                messages.error(request,"Usuario o contraseña inválidos.")
        else:
            messages.error(request,"Usuario o contraseña inválidos.")
    form = AuthenticationForm()
    return render(request, 'pages/login.html', {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('index')

def index(request):
    context = {}
    return render(request, "pages/index.html", context)


def confirmar_reserva(request):
    success_message = ''
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = 'La reserva se ha realizado con éxito.'
            return render(request, 'pages/confirmar_reserva.html', {'form': ReservaForm(), 'success_message': success_message})
    else:
        form = ReservaForm()
    return render(request, 'pages/confirmar_reserva.html', {'form': form, 'success_message': success_message})

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

def avion_de_compras(request):
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'pages/avion_de_compras.html', context)

def update_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('avion_de_compras')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'pages/update.html', {'form': form})

def delete_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        return redirect('avion_de_compras')
    return render(request, 'pages/delete.html', {'reserva': reserva})

def Ofertas(request):
    context = {}
    return render(request, "pages/Ofertas.html", context)
