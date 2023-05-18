from django.db import models
from productos.models import Producto
from proveedores.models import Proveedor

class Pedido(models.Model):
    products = models.ArrayField(models.ForeignKey(Producto, on_delete=models.CASCADE))
    unidades = models.ArrayField(models.IntegerField())
    provider = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fechaEntrega = models.DateField()
    fechaPedido = models.DateField()

    def __str__(self):
        return '%s %s' % (self.products, self.unidades)