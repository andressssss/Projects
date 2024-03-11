from django.shortcuts import render
from rest_framework import viewsets
from .models import lineabase, eventos, CMDB, llave, CMDBvsEventos, LineabasevsEventos
from .serializers import lineabaseSerializer, eventosSerializer, CMDBSerializer, llaveSerializer, CMDBvsEventosSerializer, LineabasevsEventosSerializer

class lineabaseViewSet(viewsets.ModelViewSet):
    serializer_class = lineabaseSerializer
    queryset = lineabase.objects.all()

class eventosViewSet(viewsets.ModelViewSet):
    serializer_class = eventosSerializer
    queryset = eventos.objects.all()

class CMDBViewSet(viewsets.ModelViewSet):
    serializer_class = CMDBSerializer
    queryset = CMDB.objects.all()

class llaveViewSet(viewsets.ModelViewSet):
    serializer_class = llaveSerializer
    queryset = llave.objects.all()

class CMDBvsEventosViewSet(viewsets.ModelViewSet):
    serializer_class = CMDBvsEventosSerializer
    queryset = CMDBvsEventos.objects.all()

class LineabasevsEventosViewSet(viewsets.ModelViewSet):
    serializer_class = LineabasevsEventosSerializer
    queryset = LineabasevsEventos.objects.all()
