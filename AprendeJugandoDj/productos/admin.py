from django.contrib import admin
from .models import (Categoria)
from .models import (Producto)
from .models import Opinion

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Categoria, AdministrarModelo)
admin.site.register(Producto, AdministrarModelo)
admin.site.register(Opinion, AdministrarModelo)