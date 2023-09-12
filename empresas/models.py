from django.db import models
from django.urls import reverse


class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome da Empresa")

    def __str__(self) -> str:
        return f'Empresa: {self.nome}'
    
    def get_absolute_url(self):
        return reverse('home')
