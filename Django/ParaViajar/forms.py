from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'nombre', 'apellido', 'rut', 'correo', 'telefono', 'emergencia', 
            'servicio_adicional', 'id_genero', 'id_discapacidad', 'id_asistencia', 
            'id_mascota', 'id_eadicional', 'id_asiento', 'id_seguro', 'id_hpremiun', 'id_apremiun'
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'rut': 'RUT',
            'correo': 'Correo Electrónico',
            'telefono': 'Teléfono',
            'emergencia': 'Contacto de Emergencia',
            'servicio_adicional': 'Servicio Adicional',
            'id_genero': 'Género',
            'id_discapacidad': 'Discapacidad',
            'id_asistencia': 'Asistencia',
            'id_mascota': 'Mascota',
            'id_eadicional': 'Equipaje Adicional',
            'id_asiento': 'Cambio de Asiento',
            'id_seguro': 'Seguro de Vuelo',
            'id_hpremiun': 'Habitación Premium',
            'id_apremiun': 'Alimentación Premium',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'emergencia': forms.TextInput(attrs={'class': 'form-control'}),
            'servicio_adicional': forms.TextInput(attrs={'class': 'form-control'}),
            'id_genero': forms.Select(attrs={'class': 'form-control'}),
            'id_discapacidad': forms.Select(attrs={'class': 'form-control'}),
            'id_asistencia': forms.Select(attrs={'class': 'form-control'}),
            'id_mascota': forms.Select(attrs={'class': 'form-control'}),
            'id_eadicional': forms.Select(attrs={'class': 'form-control'}),
            'id_asiento': forms.Select(attrs={'class': 'form-control'}),
            'id_seguro': forms.Select(attrs={'class': 'form-control'}),
            'id_hpremiun': forms.Select(attrs={'class': 'form-control'}),
            'id_apremiun': forms.Select(attrs={'class': 'form-control'}),
        }
