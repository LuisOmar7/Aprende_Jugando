from django.shortcuts import render
from .models import Categoria

def categorias(request):
    categorias = Categoria.objects.all()

    return render(request, "productos/categorias.html",{'categorias':categorias})
# Create your views here.
