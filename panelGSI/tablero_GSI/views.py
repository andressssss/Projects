from django.shortcuts import render
from rest_framework import generics
from tablero_GSI.models import Aplicaciones
from tablero_GSI.serializadores import AplicacionSerializer

class AplicacionList(generics.ListCreateAPIView):
    queryset = Aplicaciones.objects.all()
    serializer_class = AplicacionSerializer

class AplicacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aplicaciones.objects.all()
    serializer_class = AplicacionSerializer
