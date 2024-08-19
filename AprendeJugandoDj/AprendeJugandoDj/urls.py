"""
URL configuration for AprendeJugandoDj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base import views
from productos import views as views_productos
from django.conf import settings
from base.views import vistaLogin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='Inicio'),
    path('categorias/', views_productos.categorias, name='Categorias'),
    path('productos/<int:pk>/', views_productos.productos, name='Productos'),
    path('producto/<int:pk>/', views_productos.productoRev, name='productoRev'),
    path('nosotros/', views.nosotros, name='Nosotros'),
    path('cuenta/', vistaLogin.as_view(), name='Cuenta'),
    path('registro/', views.registro, name = "Registro"),
    path('logeado/', views.logeado, name = "Logeado"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
