from django.shortcuts import render
from .models import Categoria
from .models import Producto

def categorias(request):
    categorias = Categoria.objects.all()

    return render(request, "productos/categorias.html",{'categorias':categorias})
# Create your views here.
def productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/productos.html", {'productos':productos})