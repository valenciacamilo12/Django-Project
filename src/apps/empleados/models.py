from django.db import models
from apps.oficinas.models import Oficinas
from apps.clientes.models import Cliente

class Empleado(models.Model):
    codigo_empleado = models.IntegerField(primary_key=True,unique=True)
    nombre = models.CharField(max_length=30)
    apellido1 = models.CharField(max_length=30)
    apellido2 = models.CharField(max_length=30)
    extencion = models.IntegerField()
    email = models.CharField(max_length=30)
    codigo_oficina = models.IntegerField()
    codigo_jefe = models.IntegerField()
    puesto = models.CharField(max_length=30)
    oficina = models.ForeignKey(Oficinas, on_delete=models.CASCADE, null=True, blank = True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank = True)

    def __str__(self):
        return '{}'.format(self.nombre)

