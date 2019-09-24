# Create your tests here.

from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta
import pytest
from django.utils.timezone import get_current_timezone

from ponto.models import Colaborador, Ponto


def createColaboradorcomPonto(tipo='entrada', dia=False, qtd_registros=1):
    """
    Utilitario para criar registro de ponto e retornar o colaborador com
    registros criados
    """
    colaborador1 = Colaborador.objects.create(
        name="Colaborador1", registration="0001", qtd_horas_diarias=8)

    if not dia:
        dia = datetime(
            year=2019, month=1, day=1, hour=12, tzinfo=get_current_timezone())

    while qtd_registros:

        Ponto.objects.create(
            horario=dia,
            colaborador_id=colaborador1,
            tipo=tipo,
        )
        qtd_registros -= 1
        tipo = 'entrada' if tipo == 'saida' else 'saida'

        if dia.hour == 20:
            dia = dia + relativedelta(days=1)
            dia = dia.replace(hour=12)
        else:
            dia += relativedelta(hours=8)

    return colaborador1

@pytest.mark.django_db
def testgetPontoDiaColaborador():
    """
    Cadastrar 2 registros de ponto no dia e a função deverá encontra-los
    """

    colaborador_id = createColaboradorcomPonto()
    ponto_ids = colaborador_id.getPontoDiaColaborador()

    assert len(ponto_ids) == 1
    assert ponto_ids[0].colaborador_id == colaborador_id
    assert ponto_ids[0].tipo == 'entrada'

    colaborador_id = createColaboradorcomPonto(qtd_registros=2)
    ponto_ids = colaborador_id.getPontoDiaColaborador()
    assert len(ponto_ids) == 2

    colaborador_id = createColaboradorcomPonto(qtd_registros=10)
    ponto_ids = colaborador_id.getPontoDiaColaborador()
    assert len(ponto_ids) == 10

@pytest.mark.django_db
def testgetHoraspordia():
    """
    Cadastrar 2 registros de ponto no dia e a função deverá encontrar a
    quantidade total de horas trabalhadas naquele dia
    """
    one_day = datetime(
        year=2019, month=1, day=1, tzinfo=get_current_timezone())

    colaborador_id = createColaboradorcomPonto(dia=one_day, qtd_registros=2)

    ponto_ids = colaborador_id.getPontoDiaColaborador(one_day)
    assert len(ponto_ids) == 2

    tempo = colaborador_id.getHoraspordia(one_day)
    assert tempo.seconds / 3600 == 8.0

@pytest.mark.django_db
def testgetPontoMesColaborador():
    """
    Cadastrar 10 registros de ponto no mes e encontra
        - quantidade total de horas trabalhadas no mes
        - quantidade de horas trabalhadas por dia
    """
    colaborador_id = createColaboradorcomPonto(qtd_registros=10)

    ponto_ids = colaborador_id.getPontoDiaColaborador()
    assert len(ponto_ids) == 10

    result = colaborador_id.getPontoMesColaborador(1)

    horas = result.get('qtdTotalHorasMes')
    assert result.get('pontoMes').get('2019-01-01') == '8:00:00'
    assert result.get('pontoMes').get('2019-01-02') == '8:00:00'
    assert result.get('pontoMes').get('2019-01-03') == '8:00:00'
    assert result.get('pontoMes').get('2019-01-04') == '8:00:00'
    assert result.get('pontoMes').get('2019-01-05') == '8:00:00'
    assert result.get('qtdTotalHorasMes') == '40:00:00'
