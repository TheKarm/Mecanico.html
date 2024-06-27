from rest_framework import serializers
from .models import *

# SE USARA PARA TRANSFORMAR DATOS PYTHON A DATOS JSON
class TipoMecanicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMecanico
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class MecanicoSerializer(serializers.ModelSerializer):
    tipo = TipoMecanicoSerializer(read_only=True)
    genero = GeneroSerializer(read_only=True)

    class Meta:
        model = Mecanico
        fields = '__all__'