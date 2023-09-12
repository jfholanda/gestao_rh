from django.db import models
from funcionarios.models import Funcionario


class Documento(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    percente = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'Documento: {self.nome}'