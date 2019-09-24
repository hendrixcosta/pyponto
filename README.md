
<h1 align="center">
  PyPonto
  <br>
</h1>

<h4 align="center">Plataforma para Registrar Pontos de Funcionários</h4>

<p align="center">

  <a href="https://travis-ci.org/hendrixcosta/pyponto">
    <img src="https://travis-ci.org/hendrixcosta/pyponto.svg?branch=master&style=flat-square" alt="Version">
  </a>
  
  <a href='https://coveralls.io/github/hendrixcosta/pyponto?branch=master'>
    <img src='https://coveralls.io/repos/github/hendrixcosta/pyponto/badge.svg?branch=master' alt='Coverage Status' />
  </a>

  <a href='https://pyponto.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/pyponto/badge/?version=latest' alt='Documentation Status' />
  </a>
  
  
<p align="center">
  <a href="#recursos">Recursos</a> |
  <a href="#instalação">Instalação</a> |
  <a href="#como-usar">Como Usar</a> |
  <a href="#créditos">Créditos</a>
</p>


## Recursos

-   Registrar novos Funcionários
-   Registrar Pontos (horários) de funcionários
-   Calcular horas trabalhadas no mês do funcionário


## Instalação

O PyPonto pode ser facilmente inicializado com o comando a seguir:

```shell
docker-compose up
```

Ou então:

```shell

git clone git@github.com:hendrixcosta/pyponto.git

cd pyponto/

virtualenv .  --python=python3

source bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

```


Setar Usuário para painel administrativo do Django

```shell
python manage.py createsuperuser
```


Executar
```shell
python manage.py runserver
```


## Como usar


Para adicionar Novo Colaborador:

```shell
curl -X POST -H 'Content-Type: application/json' -u admin:admin "http://127.0.0.1:8000/colaborador/" -d '{"name":"Colaborador1","registration":"0001"}'
```

Para visualizar todos colaboradores:

```shell
curl -H 'Content-Type: application/json' -u admin:admin "http://127.0.0.1:8000/colaborador/"
```



## Créditos

Copyright (C) 2019 por Hendrix Costa
