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