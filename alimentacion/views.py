from django.shortcuts import render
from rest_framework import viewsets
from .serializer import AlimentacionSerializer
from .models import Alimentacion

class AlimentacionView(viewsets.ModelViewSet):
    serializer_class = AlimentacionSerializer
    queryset = Alimentacion.objects.all()

    


    


