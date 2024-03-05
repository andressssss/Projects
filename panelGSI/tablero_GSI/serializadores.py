from rest_framework import serializers
from tablero_GSI.models import Aplicaciones

class AplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aplicaciones
        fields = ('id', 'identificacion', 'codigo', 'nombre', 'nombreSV')
