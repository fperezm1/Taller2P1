from rest_framework import viewsets
from .models import Distancia
from .serializers import DistanciaSerializer
from django.shortcuts import render, HttpResponse
import django.contrib.sites.requests
from rest_framework.compat import requests

class DistanciaViewSet(viewsets.ModelViewSet):
    queryset = Distancia.objects.all().order_by('-created')
    serializer_class = DistanciaSerializer

def distancia(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'cm', 'value': value}
            response = requests.post('http://127.0.0.1:8000/distancias/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/distancias/')
    # Convierte la respuesta en JSON
    distancia = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "distancia/distancia.html", {'distancias': distancia})