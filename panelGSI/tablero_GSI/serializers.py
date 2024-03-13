from rest_framework import serializers
from .models import lineabase, CMDB, llave, eventos, CMDBvsEventos, LineabasevsEventos, CMDBvsLineabase, EventosvsLineabase, LineabasevsCMDB, EventosvsCMDB

class lineabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = lineabase
        fields = '__all__'

class CMDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMDB
        fields = '__all__'

class llaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = llave
        fields = '__all__'

class eventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = eventos
        fields = '__all__'

class CMDBvsEventosSerializer(serializers.ModelSerializer):

    class Meta:
        model = CMDBvsEventos
        fields = '__all__'

class LineabasevsEventosSerializer(serializers.ModelSerializer):

    class Meta:
        model = LineabasevsEventos
        fields = '__all__'

class CMDBvsLineabaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = CMDBvsLineabase
        fields = '__all__'

class EventosvsLineabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventosvsLineabase
        fields = '__all__'

class EventosvsCMDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventosvsCMDB
        fields = '__all__'

class LineabasevsCMDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineabasevsCMDB
        fields = '__all__'