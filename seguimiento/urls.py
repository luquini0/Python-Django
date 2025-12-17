<<<<<<< HEAD
from django.contrib import admin
from django.urls import include, path
from inicio.views import inicio, otra, comprar_perro, listar_perros, ver_perro, ActualizarPerro, EliminarPerro
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('usuarios/', include('usuarios.urls')),

    # path('admin/', admin.site.urls),
    # path('', inicio, name='inicio'),
    # path('otra/', otra),
    # path('ver_perro/<int:perro_id>/', ver_perro, name='ver'),
    # path('actualizar_perro/<pk>/', ActualizarPerro.as_view(), name='actualizar'),
    # path('eliminar_perro/<pk>/', EliminarPerro.as_view(), name='eliminar'),
    # path('comprar-perro/', comprar_perro, name='comprar'),
    # path('listar-perros/', listar_perros, name='listar'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
"""
URL configuration for seguimiento project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from inicio.views import inicio, otra, comprar_perro, listar_perros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('otra/', otra),
    # path('comprar-perro/', comprar_perro),
    path('comprar-perro/<raza>/<tamaño>', comprar_perro),
    path('listar-perros/', listar_perros),
]
>>>>>>> dd686a4e1f4202362c07ebce170f5dcb86ca1bbc
