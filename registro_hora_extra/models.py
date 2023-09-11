from django.db import models


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.motivo}'
