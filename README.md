
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

Navegue até:

```shell
http://localhost:8000/

http://localhost:8000/admin
```

## Como usar

irei Dizer


## Créditos

Copyright (C) 2019 por Hendrix Costa
