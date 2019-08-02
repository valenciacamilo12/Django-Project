from django.db import models
from apps.clientes.models import Cliente

class Producto(models.Model):
    codigo_producto = models.IntegerField(primary_key=True,unique=True)
    nombre = models.CharField(max_length=30)
    gama = models.CharField(max_length=30)
    dimensiones = models.CharField(max_length=30)
    proveedor = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    cantidad_stock = models.IntegerField()
    precio_venta = models.CharField(max_length=30)
    precio_proveedor  = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.nombre)



class Pedidos(models.Model):
    codigo_pedido = models.IntegerField(primary_key=True,unique=True)
    fecha_pedido = models.DateField()
    fecha_esparada = models.DateField()
    fecha_entrega = models.DateField()
    estado = models.CharField(max_length=40)
    comentarios = models.CharField(max_length=60)
    codigo_cliente = models.ForeignKey(Cliente, null = True, on_delete= models.CASCADE, blank = True)


    def __str__(self):
        return '{}'.format(self.fecha_pedido)


class Pagos(models.Model):
    codigo_cliente = models.ForeignKey(Cliente, null = True, on_delete=models.CASCADE, blank = True)
    forma_pago = models.CharField(max_length=30)
    id_transaccion =  models.IntegerField(primary_key=True,unique = True)
    fecha_pago = models.DateField()
    cantidad  = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.id_transaccion)