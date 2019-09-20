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


class Ponto(models.Model):

    start = models.DateTimeField()

    end = models.DateTimeField()

    colaborador_id = models.ForeignKey(Colaborador,on_delete=models.CASCADE)

    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {} '.format(self.start, self.end)
