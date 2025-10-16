from rest_framework import serializers
from .models import Dueno, Vehiculo

class DuenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dueno
        fields = ['id', 'nombre', 'numero_licencia']

class VehiculoSerializer(serializers.ModelSerializer):
    # lectura anidada: devolver datos del dueño
    dueno = DuenoSerializer(read_only=True)
    # escritura: aceptar dueno_id para crear/actualizar
    dueno_id = serializers.PrimaryKeyRelatedField(
        queryset=Dueno.objects.all(),
        source='dueno',
        write_only=True
    )

    class Meta:
        model = Vehiculo
        fields = ['id', 'marca', 'modelo', 'anio', 'dueno', 'dueno_id', 'creado_en']
        read_only_fields = ['creado_en']
