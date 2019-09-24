# Create your tests here.

import pytest
import pytz
from django.utils.timezone import now

from ponto.models import Colaborador, Ponto

from django.utils import timezone




from datetime import timedelta

@pytest.mark.django_db
def testModelColaborador():
    colaborador1 = Colaborador.objects.create(
        name="Colaborador1", registration="0001", qtd_horas_diarias=8)
    colaborador2 = Colaborador.objects.create(
        name="Colaborador2", registration="0002", qtd_horas_diarias=8)

    assert colaborador1.__str__() == 'Colaborador1'
    assert colaborador2.__str__() == 'Colaborador2'

@pytest.mark.django_db
def testModelPonto():

    colaborador1 = Colaborador.objects.create(
        name="Colaborador1", registration="0001", qtd_horas_diarias=8)

    ponto1 = Ponto.objects.create(
        horario=now(),
        colaborador_id=colaborador1,
    )
    assert ponto1.__str__() == 'Colaborador1 - Ponto em: {}'.format(
        str(now().date()))
