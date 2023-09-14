from django.urls import path
from .views import DepartamentoList, DepartamentoCreate, DepartamentoUpdate, DepartamentoDelete

urlpatterns = [
    path('', DepartamentoList.as_view(), name='list_departamentos'),
    path('novo/', DepartamentoCreate.as_view(), name='create_departamento'),
    path('editar/<int:pk>', DepartamentoUpdate.as_view(), name='update_departamento'),
    path('excluir/<int:pk>', DepartamentoDelete.as_view(), name='delete_departamento')
]