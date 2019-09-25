# Create your tests here.

import pytest
import json

import requests
from requests.auth import HTTPBasicAuth


@pytest.mark.django_db
def testCreateColaborador():
    """
    """
    payload = {'name': 'Colaborador10', 'registration': '0010'}
    headers = {'content-type': 'application/json'}
    auth = HTTPBasicAuth('admin', 'admin')
    url = 'http://localhost:8000/colaborador/'
    r = requests.post(
        url, headers=headers, auth=auth, data=json.dumps(payload))

    assert r.status_code == 201
    assert r.json().get('name') == 'Colaborador10'
    assert r.json().get('registration') == '0010'

@pytest.mark.django_db
def testCreatePonto():
    """
    """
    payload = {'name': 'Colaborador11', 'registration': '0011'}
    headers = {'content-type': 'application/json'}
    auth = HTTPBasicAuth('admin', 'admin')
    url = 'http://localhost:8000/colaborador/'
    r = requests.post(
        url, headers=headers, auth=auth, data=json.dumps(payload))

    assert r.status_code == 201
    assert r.json().get('name') == 'Colaborador11'
    assert r.json().get('registration') == '0011'
    assert r.json().get('id', False) != False

    colaborador_id = r.json().get('id')

    payload = {
        'horario':'2019-02-01 12:00:00',
        'colaborador_id':colaborador_id,
        'tipo':'entrada',
    }
    headers = {'content-type': 'application/json'}
    auth = HTTPBasicAuth('admin', 'admin')
    url = 'http://localhost:8000/ponto/'
    r = requests.post(
        url, headers=headers, auth=auth, data=json.dumps(payload))

    assert r.status_code == 201
    assert r.json().get('colaborador_id') == colaborador_id
