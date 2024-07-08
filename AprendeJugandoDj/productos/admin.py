from django.contrib import admin
from .models import (Categoria)
from .models import (subCategoria)
from .models import (Producto)

# Register your models here.
admin.site.register(Categoria)
admin.site.register(subCategoria)
admin.site.register(Producto)