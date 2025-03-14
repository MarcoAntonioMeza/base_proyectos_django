from django.contrib import admin

# Register your models here.

from apps.clientes.models import Cliente, DireccionClientes
admin.site.register(Cliente)