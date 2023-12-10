from django.db import models

# Create your models here.

class Aula(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class ReservaAula(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    nombre_reservante = models.CharField(max_length=100)
    email_reservante = models.EmailField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"Reserva en {self.aula.nombre} por {self.nombre_reservante}"