from django.shortcuts import render
from rest_framework import viewsets
from .models import lineabase, eventos, CMDB, llave, CMDBvsEventos, LineabasevsEventos, CMDBvsLineabase, EventosvsLineabase, LineabasevsCMDB, EventosvsCMDB
from .serializers import lineabaseSerializer, eventosSerializer, CMDBSerializer, llaveSerializer, CMDBvsEventosSerializer, LineabasevsEventosSerializer, CMDBvsLineabaseSerializer, EventosvsLineabaseSerializer, LineabasevsCMDBSerializer, EventosvsCMDBSerializer

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

class CMDBvsLineabaseViewSet(viewsets.ModelViewSet):
    serializer_class = CMDBvsLineabaseSerializer
    queryset = CMDBvsLineabase.objects.all()

class EventosvsLineabaseViewSet(viewsets.ModelViewSet):
    serializer_class = EventosvsLineabaseSerializer
    queryset = EventosvsLineabase.objects.all()

class LineabasevsCMDBViewSet(viewsets.ModelViewSet):
    serializer_class = LineabasevsCMDBSerializer
    queryset = LineabasevsCMDB.objects.all()

class EventosvsCMDBViewSet(viewsets.ModelViewSet):
    serializer_class = EventosvsCMDBSerializer
    queryset = EventosvsCMDB.objects.all()
