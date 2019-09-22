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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    start = models.DateTimeField()

    end = models.DateTimeField()

    colaborador_id = models.ForeignKey(Colaborador,on_delete=models.CASCADE)

    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - Ponto em: {}'.format(self.colaborador_id, str(self.start)[:10])
