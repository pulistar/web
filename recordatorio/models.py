from django.db import models


class Recordatorio(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()

    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.titulo
