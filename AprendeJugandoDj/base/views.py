from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ComentarioContactoForm

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


def comentarioForm(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():  # Si los datos recibidos son correctos
            form.save()  # Guarda el formulario en la base de datos
            return redirect('Inicio')  # Redirige a la página de inicio o a otra página de tu elección
    form = ComentarioContactoForm()  # Inicializa un formulario vacío si no es una solicitud POST
    # Si algo sale mal o si es GET, se reenvían al formulario los datos ingresados
    return render(request, 'base/base.html', {'form': form})