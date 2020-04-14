from rest_framework import serializers
from .models import Distancia

class DistanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distancia
        fields = ('id', 'type', 'value')