from django.db import models
from productos.models import Producto
from proveedores.models import Proveedor
class Pedido(models.Model):
    products = models.ManyToManyField(Producto)
    unidades = models.CharField(max_length=255)
    provider = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fechaEntrega = models.DateField()
    fechaPedido = models.DateField()

    def unidades_as_list(self):
        return [int(x) for x in self.unidades.split(',')]

    def __str__(self):
        return '%s %s' % (self.products, self.unidades)