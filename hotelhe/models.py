from django.db import models

# Create your models here.

class Turismo(models.Model):
    imagen = models.FileField(upload_to="")
    nombre = models.CharField(max_length=100)
    hora = models.CharField(max_length=100)
    precio = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=300)

    class Meta:
        db_table = "turismo"


class Habitacion(models.Model):
    nombrePersona = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    numeroPersonas = models.IntegerField()
    tipo = models.CharField(max_length=300)
    dias = models.IntegerField()

    class Meta:
        db_table = "habitaciones"