from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('confirmar-reserva/', views.confirmar_reserva, name='confirmar_reserva'),
    path('destino/', views.destino, name='destino'),
    path('hoteles/', views.hoteles, name='hoteles'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('vuelos/', views.vuelos, name='vuelos'),
    path('avion-de-compras/', views.avion_de_compras, name='avion_de_compras'),
    path('update-reserva/<int:pk>/', views.update_reserva, name='update_reserva'),
    path('delete-reserva/<int:pk>/', views.delete_reserva, name='delete_reserva'),
    path('Ofertas/', views.Ofertas, name='Ofertas'),
]
