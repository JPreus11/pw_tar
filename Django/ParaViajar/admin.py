from django.contrib import admin
from .models import Reserva, Genero, Discapacidad, Asistencia, Mascota, EAdicional, Asiento, Seguro, HPremiun, APremiun
# Register your models here.

admin.site.register(Reserva)
admin.site.register(Genero)
admin.site.register(Discapacidad)
admin.site.register(Asistencia)
admin.site.register(Mascota)
admin.site.register(EAdicional)
admin.site.register(Asiento)
admin.site.register(Seguro)
admin.site.register(HPremiun)
admin.site.register(APremiun)
