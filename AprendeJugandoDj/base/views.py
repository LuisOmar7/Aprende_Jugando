from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'base/inicio.html')

def categorias(request):
    return render(request, 'base/categorias.html')

def productos(request):
    return render(request, 'base/productos.html')