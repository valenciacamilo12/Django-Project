from django.db import models
from apps.empleados.models import Empleado
from django.utils.translation import ugettext as _

class Cliente(models.Model):
    codigo_cliente = models.AutoField(primary_key=True,unique=True)
    nombre_cliente = models.CharField(max_length=30)
    nombre_contacto = models.CharField(max_length=30)
    apellido_contacto = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    fax = models.IntegerField()
    linea_direccion1 = models.CharField(max_length=30)
    linea_direccion2 = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    codigo_postal = models.CharField(max_length=30, default=True)
    limite_credito = models.CharField(max_length=30, default=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre_cliente)

    class Meta:
        permissions = {
            ('is_uno', _('Usuario Uno')),
            ('is_dos', _('Usuario Dos')),
        }