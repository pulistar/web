
   
from rest_framework import viewsets
from .models import Actividad
from .serializer import ActividadSerializer

class ActividadView(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()  # Línea corregida
    serializer_class = ActividadSerializer
