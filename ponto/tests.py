# Create your tests here.

from datetime import timedelta

import pytest
from django.utils.timezone import now

from ponto.models import Colaborador, Ponto


@pytest.mark.django_db
def testModelColaborador():
    colaborador1 = Colaborador.objects.create(
        name="Colaborador1", registration="0001")
    colaborador2 = Colaborador.objects.create(
        name="Colaborador2", registration="0002")

    assert colaborador1.__str__() == 'Colaborador1'
    assert colaborador2.__str__() == 'Colaborador2'

@pytest.mark.django_db
def testModelPonto():

    colaborador1 = Colaborador.objects.create(
        name="Colaborador1", registration="0001")

    ponto1 = Ponto.objects.create(
        start=now(), end=now() + timedelta(hours=8),
        colaborador_id=colaborador1
    )
    assert ponto1.__str__() == 'Colaborador1 - Ponto em: {}'.format(
        str(now().date()))
