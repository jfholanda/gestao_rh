from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('funcionarios/', include('funcionarios.urls')),
    path('empresa/', include('empresas.urls')),
    path('departamentos/', include('departamentos.urls')),
    path('documentos/', include('documentos.urls')),
    path('horas-extras/', include('registro_hora_extra.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
