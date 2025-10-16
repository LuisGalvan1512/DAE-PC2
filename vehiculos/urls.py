from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DuenoViewSet, VehiculoViewSet

router = DefaultRouter()
router.register(r'duenos', DuenoViewSet, basename='dueno')
router.register(r'vehiculos', VehiculoViewSet, basename='vehiculo')

urlpatterns = [
    path('', include(router.urls)),
]
