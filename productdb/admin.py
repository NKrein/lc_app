from django.contrib import admin
from productdb.models import *

# Register your models here.


class Clientes_view(admin.ModelAdmin):
    list_display = ("nombre", "telefono", "direccion")
    search_fields = ("nombre",)


class Pedidos_view(admin.ModelAdmin):
    list_display = ("fecha", "cliente", "estado")
    list_filter = ("fecha", "estado")
    date_hierarchy = "fecha"


admin.site.register(Tipo)
admin.site.register(Cliente, Clientes_view)
admin.site.register(Pedido, Pedidos_view)
admin.site.register(Producto)
