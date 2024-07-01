from django.db import models

# Create your models here. admin: contraseña
class Reserva(models.Model):
    nombre = models.CharField(max_length=255, blank=False, null=False)
    apellido = models.CharField(max_length=255, blank=False, null=False)
    rut = models.CharField(max_length=10, blank=False, null=False)
    correo = models.CharField(max_length=255, blank=False, null=False)
    telefono = models.CharField(max_length=9, blank=False, null=False)
    emergencia = models.CharField(max_length=9, blank=False, null=False)
    servicio_adicional = models.CharField(max_length=255, blank=False, null=False)
    id_genero = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero')
    id_discapacidad = models.ForeignKey('Discapacidad', on_delete=models.CASCADE, db_column='idDiscapacidad')
    id_asistencia = models.ForeignKey('Asistencia', on_delete=models.CASCADE, db_column='idAsistencia')
    id_mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE, db_column='idMascota')
    id_eadicional = models.ForeignKey('EAdicional', on_delete=models.CASCADE, db_column='idEAdicional')
    id_asiento = models.ForeignKey('Asiento', on_delete=models.CASCADE, db_column='idAsiento')
    id_seguro = models.ForeignKey('Seguro', on_delete=models.CASCADE, db_column='idSeguro')
    id_hpremiun = models.ForeignKey('HPremiun', on_delete=models.CASCADE, db_column='idHPremiun')
    id_apremiun = models.ForeignKey('APremiun', on_delete=models.CASCADE, db_column='idAPremiun')

class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    nombre_genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre_genero
    
class Discapacidad(models.Model):
    id_discapacidad = models.AutoField(db_column='idDiscapacidad', primary_key=True)
    nombre_discapacidad = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre_discapacidad
    
class Asistencia(models.Model):
    id_asistencia = models.AutoField(db_column='idAsistencia', primary_key=True)
    nombre_asistencia = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre_asistencia
    
class Mascota(models.Model):
    id_mascota = models.AutoField(db_column='idMascota', primary_key=True)
    nombre_mascota = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre_mascota

class EAdicional(models.Model):
    id_eadicional = models.AutoField(db_column='idEAdicional', primary_key=True)
    nombre_eadicional = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre_eadicional
    
class Asiento(models.Model):
    id_asiento = models.AutoField(db_column='idAsiento', primary_key=True)
    nombre_asiento = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre_asiento
    
class Seguro(models.Model):
    id_seguro = models.AutoField(db_column='idSeguro', primary_key=True)
    nombre_seguro = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre_seguro
    
class HPremiun(models.Model):
    id_hpremiun = models.AutoField(db_column='idHPremiun', primary_key=True)
    nombre_hpremiun = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre_hpremiun
    
class APremiun(models.Model):
    id_apremiun = models.AutoField(db_column='idAPremiun', primary_key=True)
    nombre_apremiun = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre_apremiun