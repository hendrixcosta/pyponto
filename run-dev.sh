#!/usr/bin/env bash

python manage.py migrate --settings=settings-dev
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" --settings=settings-dev
python manage.py runserver 0.0.0.0:8000 --settings=settings-dev
