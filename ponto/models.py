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

    def __str__(self):
        return self.name

    def getPontoDiaColaborador(self, dia=False):
        """
        Retornar todos registros de ponto do dia ou todos pontos do colaborador
        :param dia: datetime Dia referencia
        :return: Ponto
        """

        # Se um dia estiver no parametro, retornar os pontos daquele dia
        if dia:
            return Ponto.objects.filter(
            colaborador_id__exact=self.id, horario__date=dia)

        # Caso contrario retornar todos pontos daquele colaborador
        return Ponto.objects.filter(colaborador_id__exact=self.id)

    def getHoraspordia(self, dia):
        """
        Retorna a quantidade total de horas trabalhadas do colaborador em
        determinado dia
        :param dia: datetima
        :return: float quantidade de horas
        """

        # Pontos registrados naquele dia
        ponto_ids = self.getPontoDiaColaborador(dia)

        # Identificar o ponto de entrada e o de saida
        entrada = [x for x in ponto_ids if x.tipo == 'entrada']
        saida = [x for x in ponto_ids if x.tipo == 'saida']

        # Se nao encontrar um registro de entrada e um de saida, retornar zero
        # TODO: Disparar erro quando nao tiver corretamente registrado?
        if not entrada or not saida:
            return 0

        # Retornar a diferença da entrada e da saida
        # Utilizando o primeiro registro encontrado para evitar duplicidade
        # TODO: Tratar intervalos
        # TODO: Tratar erros de duplicidade de forma ótima
        return saida[0].horario - entrada[0].horario

    def getPontoMesColaborador(self, mes):
        """
        Retornar todos registros de ponto do mês
        :param mes: int Mes de referência
        :return: Dict Todos os pontos do mes e somatório
                       de horas trabalhadas no mes
        """
        detail_ponto_mes = {}
        total_mes = relativedelta()

        import calendar
        # Determinar quantidade de dias do mes
        _, num_days = calendar.monthrange(2019, int(mes))
        first_day = datetime(2019, int(mes), 1)
        last_day = datetime(2019, int(mes), num_days)
        reference = first_day

        # Iterar todos os dias do mes
        while reference <= last_day:

            # buscar qtd de horas trabalhadas naquele dia
            horas_trabalhadas = self.getHoraspordia(reference.date())

            # Guardar informações de cada dia em dict
            detail_ponto_mes[str(reference.date())] = str(horas_trabalhadas)
            reference += relativedelta(days=1)

            # Somatorio de horas trabalhadas no mes em delta
            total_mes += \
                horas_trabalhadas if horas_trabalhadas else relativedelta()

        # Formatar relativedelta
        qtdTotalHorasMes = (total_mes.days * 24) + total_mes.hours
        qtdTotalHorasMes = '{:02}:{:02}:{:02}'.format(
            qtdTotalHorasMes, total_mes.minutes, total_mes.seconds)

        return {
            'pontoMes': detail_ponto_mes,
            'qtdTotalHorasMes': qtdTotalHorasMes,
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
