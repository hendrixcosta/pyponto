FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /pyponto
WORKDIR /pyponto

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y libsqlite3-dev

RUN pip install -U pip setuptools psycopg2

COPY requirements.txt /pyponto/

RUN pip install -r /pyponto/requirements.txt

ADD . /pyponto/

RUN chmod +x /pyponto/run.sh

# Django service
EXPOSE 8000
