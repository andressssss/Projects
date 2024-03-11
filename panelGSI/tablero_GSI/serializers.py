from rest_framework import serializers
from .models import lineabase, CMDB, llave, eventos, CMDBvsEventos, LineabasevsEventos

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