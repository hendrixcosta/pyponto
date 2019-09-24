=====
Usage
=====


Para adicionar Novo Colaborador

.. code-block:: bash

    curl -X POST -H 'Content-Type: application/json' -u admin:admin "http://127.0.0.1:8000/colaborador/" -d '{"name":"Colaborador1","registration":"0001"}'


Para visualizar todos colaboradores

.. code-block:: bash

    curl -H 'Content-Type: application/json' -u admin:admin "http://127.0.0.1:8000/colaborador/"


Para adicionar registro de ponto

.. code-block:: bash

    curl -X POST -H 'Content-Type: application/json' -u admin:admin "http://127.0.0.1:8000/ponto/" -d '{"colaborador_id":"1","tipo":"entrada", "horario":"2019-01-01 12:00:00"}'

    curl -X POST -H 'Content-Type: application/json' -u admin:admin "http://127.0.0.1:8000/ponto/" -d '{"colaborador_id":"1","tipo":"saida", "horario":"2019-01-01 17:00:00"}'


Para visualizar todos registros de Pontos

.. code-block:: bash

    curl -H 'Content-Type: application/json' -u admin:admin "http://127.0.0.1:8000/ponto/"


Para visualizar detalhes de registro de ponto do mês

    Paramêtros: id do funcionario e mes para detalhes

.. code-block:: bash

    curl -H 'Content-Type: application/json' -u admin:admin "http://127.0.0.1:8000/pontomes/?id=1&mes=1"

