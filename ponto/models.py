from django.db import models


class Colaborador(models.Model):

    name = models.CharField(
        max_length=120,
        help_text='Nome'
    )

    registration = models.TextField(
        help_text="Matricula"
    )

    def __str__(self):
        return self.name
