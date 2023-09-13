from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from empresas.models import Empresa
from departamentos.models import Departamento


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return f'Funcionario: {self.nome}'
    
    def get_absolute_url(self):
        return reverse('list_funcionarios')
