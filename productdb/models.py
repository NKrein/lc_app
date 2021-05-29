from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Tipo(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        txt = "{0} - {1}"
        return txt.format(self.codigo, self.nombre)


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    tipo = models.ForeignKey(Tipo, null=False, blank=False, on_delete=CASCADE)
    stock = models.CharField(max_length=10)
    precio = models.CharField(max_length=5)

    def mostrar_producto(self):
        txt = "{0} - Stock: {1} - Precio: {2}"
        return txt.format(self.nombre, self.stock, self.precio)

    def __str__(self):
        txt = "{0} - Stock: {1} - Precio: {2}"
        return txt.format(self.nombre, self.stock, self.precio)
