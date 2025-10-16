from rest_framework import serializers
from .models import Dueno, Vehiculo

class DuenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dueno
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    dueno_nombre = serializers.CharField(source='dueno.nombre', read_only=True)

    class Meta:
        model = Vehiculo
        fields = ['id', 'marca', 'modelo', 'anio', 'dueno', 'dueno_nombre', 'creado_en']
