from django.db import models

# Create your models here.


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=15)
    stock = models.CharField(max_length=10)
    precio = models.CharField(max_length=5)

    def mostrar_producto(self):
        txt = "{0} - Stock: {1} - Precio: {2}"
        return txt.format(self.nombre, self.stock, self.precio)

    def __str__(self):
        txt = "{0} - Stock: {1} - Precio: {2}"
        return txt.format(self.nombre, self.stock, self.precio)
