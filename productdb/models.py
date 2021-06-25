from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField

# Create your models here.


class Tipo(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        txt = "{0} - {1}"
        return txt.format(self.codigo, self.nombre)


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        txt = "{0} - Tel.: {1}"
        return txt.format(self.nombre, self.telefono)


class Pedido(models.Model):
    nro = models.AutoField(primary_key=True)
    fecha = DateField(auto_now=True)
    cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=CASCADE)
    estado = models.BooleanField(default=False)

    def __str__(self):
        txt = "{0} - Estado: {1}"
        return txt.format(self.cliente, self.estado)


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    tipo = models.ForeignKey(Tipo, null=False, blank=False, on_delete=CASCADE)
    stock = models.CharField(max_length=10)
    precio = models.CharField(max_length=5)

    def __str__(self):
        txt = "{0} - Stock: {1} - Precio: {2}"
        return txt.format(self.nombre, self.stock, self.precio)
