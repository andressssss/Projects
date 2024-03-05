from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import AplicacionSerializer, lineabaseSerializer

class AplicacionViewSet(viewsets.ModelViewSet):
    serializer_class = AplicacionSerializer
    queryset = Aplicaciones.objects.all()

class lineabaseViewSet(viewsets.ModelViewSet):
    serializer_class = lineabaseSerializer
    queryset = lineabase.objects.all()
