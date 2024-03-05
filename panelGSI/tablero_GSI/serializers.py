from rest_framework import serializers
from .models import Aplicaciones, lineabase

class AplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aplicaciones
        fields = '__all__'

class lineabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = lineabase
        fields = '__all__'
