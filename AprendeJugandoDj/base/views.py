from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request, 'base/inicio.html')

def categorias(request):
    return render(request, 'base/categorias.html')

def productos(request):
    return render(request, 'base/productos.html')

def nosotros(request):
    return render(request, 'base/nosotros.html')

def cuenta(request):
    return render(request, 'base/cuenta.html')

def registro(request):
    return render(request, 'base/registro.html')

def logeado(request):
    return render(request, 'base/logeado.html')

class vistaLogin(LoginView):
    template_name = 'base/cuenta.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('admin:index')  #Redirección

    def form_invalid(self, form):
        messages.error(self.request, '*Nombre de usuario o contraseña incorrectos intente otra vez')
        return super().form_invalid(form)

    def get_success_url(self):
        return self.success_url
