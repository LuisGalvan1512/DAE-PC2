from django.db import models

class Dueno(models.Model):
    nombre = models.CharField(max_length=150)
    numero_licencia = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.numero_licencia})"

class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.PositiveSmallIntegerField()
    dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE, related_name='vehiculos')
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado_en']

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"