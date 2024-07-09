from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'base/inicio.html')

def categorias(request):
    return render(request, 'base/categorias.html')

def productos(request):
    return render(request, 'base/productos.html')

def nosotros(request):
    return render(request, 'base/nosotros.html')

def registro(request):
    return render(request, 'base/registro.html')
def cuenta(request):
    return render(request, 'base/cuenta.html')
