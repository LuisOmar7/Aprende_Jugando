from django.shortcuts import render, get_object_or_404
from .models import Categoria
from .models import Producto

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "productos/categorias.html",{'categorias':categorias})

def productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/productos.html", {'productos':productos})

def productoRev(request,pk):
    productos = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/productoRev.html', {'productos': productos})
