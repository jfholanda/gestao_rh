from django.db import models


class Documento(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'Documento: {self.nome}'