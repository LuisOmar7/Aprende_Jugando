from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria
from .models import Producto
from .models import Opinion
from .forms import OpinionForm 

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "productos/categorias.html",{'categorias':categorias})

def productos(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk) # Busca la categoría con la primary key (pk)
    productos = Producto.objects.filter(categoria=categoria) # Filtra los productos por esta categoría
    return render(request, "productos/productos.html", {'categoria': categoria, 'productos': productos})

def productoRev(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    opiniones = Opinion.objects.filter(producto=producto)

    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            nueva_opinion = form.save(commit=False)
            nueva_opinion.producto = producto
            nueva_opinion.save()
            return redirect('productoRev', pk=pk)
    else:
        form = OpinionForm()

    return render(request, 'productos/productoRev.html', {'productos': producto, 'opiniones': opiniones, 'form': form})