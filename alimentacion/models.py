from django.db import models


class Alimentacion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
    tipo_comida = models.CharField(max_length=50, choices=[('desayuno', 'Desayuno'), ('almuerzo', 'Almuerzo'), ('cena', 'Cena')])
    calorias = models.IntegerField()

    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.nombre
