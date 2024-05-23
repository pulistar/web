from django.db import models


class Actividad(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
    duracion = models.DurationField()
    TIPO_CHOICES = [
        ('ejercicio', 'Ejercicio'),
        ('dieta', 'Dieta'),
        ('hidratacion', 'Hidratación'),
    ]
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)


    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.titulo
