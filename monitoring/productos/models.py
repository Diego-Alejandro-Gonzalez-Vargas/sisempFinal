
from django.db import models


class Producto(models.Model):
    name = models.CharField(max_length=50)
    unidades = models.IntegerField()
    price = models.IntegerField()
    category = models.CharField(max_length=50)
    image = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.name)