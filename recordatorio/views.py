from django.shortcuts import render
from rest_framework import viewsets
from .serializer import RecordatorioSerializer
from .models import Recordatorio

class RecordatorioView(viewsets.ModelViewSet):
    serializer_class = RecordatorioSerializer
    queryset = Recordatorio.objects.all()

    
  