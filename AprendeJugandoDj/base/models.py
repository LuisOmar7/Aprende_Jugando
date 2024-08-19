from django.db import models

# Create your models here.
class Comentario(models.Model):
    email = models.EmailField(max_length=254)
    mensaje = models.TextField()
    created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado") 
    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]

    def _str_(self):
        return self.mensaje
    #Indica que se mostrára el mensaje como valor en la tabla