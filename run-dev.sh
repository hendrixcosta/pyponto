#!/usr/bin/env bash

virtualenv . --python=python3

source bin/activate

pip install -r requirements.txt
pip install -r requirements-dev.txt

python manage.py makemigrations --settings=settings-dev

python manage.py migrate --settings=settings-dev

python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" --settings=settings-dev

python manage.py runserver 0.0.0.0:8000 --settings=settings-dev
