from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Colaborador(models.Model):

    name = models.CharField(
        max_length=120,
        help_text='Nome',
    )

    registration = models.CharField(
        help_text="Matricula",
        max_length = 120,
    )

    qtd_horas_diarias = models.FloatField(
        help_text="Horas Diárias",
    )

    def __str__(self):
        return self.name

    def getPontoDiaColaborador(self, dia):
        """
        Retornar todos registros de ponto do dia
        :param dia: str <aaaa-mm-dd>
        :return: Ponto
        """
        ponto_ids = Ponto.objects.filter(
            colaborador_id__exact=self.id, horario__date=dia)
        return ponto_ids

    def getHoraspordia(self, dia):

        ponto_ids = self.getPontoDiaColaborador(dia)

        entrada = [x for x in ponto_ids if x.tipo == 'entrada']
        saida = [x for x in ponto_ids if x.tipo == 'saida']

        if not entrada or not saida:
            return 0

        return saida[0].horario - entrada[0].horario

    def getPontoMesColaborador(self, mes):
        """
        Retornar todos registros de ponto do mês
        :param mes: int
        :return: Ponto
        """
        detail_ponto_mes = {}
        total_mes = relativedelta()

        import calendar
        _, num_days = calendar.monthrange(2019, int(mes))
        first_day = datetime(2019, int(mes), 1)
        last_day = datetime(2019, int(mes), num_days)

        reference = first_day

        while reference <= last_day:
            horas_trabalhadas = self.getHoraspordia(reference.date())
            detail_ponto_mes[str(reference.date())] = str(horas_trabalhadas)
            reference += relativedelta(days=1)
            total_mes += horas_trabalhadas if horas_trabalhadas else relativedelta()

        return {
            'pontoMes': detail_ponto_mes,
            'qtdTotalHorasMes' :
                '{} Horas e {} Minutos!'.format(
                    total_mes.hours, total_mes.minutes),
        }


class Ponto(models.Model):

    tipo = models.CharField(
        max_length=10,
        choices=[
            ('entrada','Entrada'),
            ('saida','Saída'),
            ('pausa_in','Intervalo'),
            ('pausa_out','Retorno do Intervalo'),
        ],
        default='entrada',
    )

    horario = models.DateTimeField(default=datetime.now)

    colaborador_id = models.ForeignKey(Colaborador,on_delete=models.CASCADE)

    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - Ponto em: {}'.format(
            self.colaborador_id, str(self.horario)[:10])

    def getPontoMes(self, mes, id_colaborador):
        """
        Buscar Registro de ponto do mês e do colaborador
        :param mes: int Mês a ser consultado
        :param id_colaborador: int id do colaborador
        :return: Ponto Registros de Ponto do mês
        """
        colaborador_id = Colaborador.objects.get(pk=id_colaborador)

        return colaborador_id.getPontoMesColaborador(mes)
