from django.contrib import admin
from .models import (Categoria)
from .models import (subCategoria)
from .models import (Producto)

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Categoria, AdministrarModelo)
admin.site.register(subCategoria, AdministrarModelo)
admin.site.register(Producto, AdministrarModelo)