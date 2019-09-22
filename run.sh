#!/usr/bin/env bash

cd /pyponto/
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
