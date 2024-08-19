from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
    imagen = models.ImageField(null=True,upload_to="fotoCat",verbose_name="FotoCat")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ["-created"]

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Clave')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria', related_name='productos')
    nombre = models.TextField()
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotos")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-created']

    def _str_(self):
        return self.nombre

class Opinion(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    comentario = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comentario