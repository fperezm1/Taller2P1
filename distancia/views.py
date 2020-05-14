from rest_framework import viewsets
from django.shortcuts import render, HttpResponse
import django.contrib.sites.requests
from rest_framework.compat import requests

def distancia(request):
    # Verifica si hay un parámetro codigo en la petición GET
    if 'codigo' and 'longitud' and 'latitud' and 'terreno' and 'area' in request.GET:
        codigo = request.GET['codigo']
        longitud = request.GET['longitud']
        latitud = request.GET['latitud']
        terreno = request.GET['terreno']
        area = request.GET['area']
        # Verifica si el area no esta vacio
        if codigo and longitud and latitud and terreno and area:
            # Crea el json para realizar la petición POST al Web Service
            args = {'codigo': codigo, 'longitud': longitud, 'latitud': latitud, 'terreno': terreno, 'area': area}
            response = requests.post('http://127.0.0.1:8000/distancias/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/distancias/')
    # Convierte la respuesta en JSON
    distancia = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "distancia/distancia.html", {'distancias': distancia})