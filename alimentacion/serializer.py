from rest_framework import serializers
from .models import Alimentacion

class AlimentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentacion
        fields = '__all__'
