from django.db import models

class Oficinas(models.Model):
    codigo_oficina = models.IntegerField(primary_key= True,unique = True)
    ciudad = models.CharField(max_length=30)
    pais = models.CharField(max_length= 30)
    region = models.CharField(max_length=30)
    codigo_postal = models.CharField(max_length=30)
    telefono = models.IntegerField()
    linea_direccion1 = models.CharField(max_length=30)
    linea_direccion2  = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.ciudad)
