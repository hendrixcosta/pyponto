=====
Usage
=====

Colaborador
===========

Para adicionar Novo Colaborador

::

    curl -X POST -H 'Content-Type: application/json' -u admin:admin "http://127.0.0.1:8000/colaborador/" -d '{"name":"Colaborador1","registration":"0001"}'


Para visualizar todos colaboradores

::

    curl -H 'Content-Type: application/json' -u admin:admin "http://127.0.0.1:8000/colaborador/"

Registro de Ponto
=================

Para adicionar registro de ponto

::

    curl -X POST -H 'Content-Type: application/json' -u admin:admin "http://127.0.0.1:8000/ponto/" -d '{"colaborador_id":"1","tipo":"entrada", "horario":"2019-01-01 12:00:00"}'

    curl -X POST -H 'Content-Type: application/json' -u admin:admin "http://127.0.0.1:8000/ponto/" -d '{"colaborador_id":"1","tipo":"saida", "horario":"2019-01-01 17:00:00"}'


Para visualizar todos registros de Pontos

::

    curl -H 'Content-Type: application/json' -u admin:admin "http://127.0.0.1:8000/ponto/"


Ponto Detalhado do mês
======================

Para visualizar detalhes de registro de ponto do mês

    Paramêtros: id do funcionario e mês para detalhes

GET
---

::

    curl -H 'Content-Type: application/json' -u admin:admin "http://127.0.0.1:8000/pontomes/?id=1&mes=1"

POST
----

::

    curl -X POST -H 'Content-Type: application/json' -u admin:admin "http://127.0.0.1:8000/pontomes/" -d '{"colaborador_id":"1","mes":"1"}'

.. note:: Utilizar usuário  ```admin``` com a senha padrão: ```admin```.

