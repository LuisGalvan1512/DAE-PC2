from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Dueno, Vehiculo
from .serializers import DuenoSerializer, VehiculoSerializer

class DuenoViewSet(viewsets.ModelViewSet):

    queryset = Dueno.objects.all()
    serializer_class = DuenoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'numero_licencia']
    ordering_fields = ['nombre', 'numero_licencia']


class VehiculoViewSet(viewsets.ModelViewSet):

    queryset = Vehiculo.objects.select_related('dueno').all()
    serializer_class = VehiculoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['marca', 'modelo', 'anio', 'dueno__nombre']
    filterset_fields = ['marca', 'modelo', 'anio', 'dueno']
    ordering_fields = ['creado_en', 'marca', 'anio']
