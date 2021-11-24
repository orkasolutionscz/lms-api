#!/bin/sh

# Tohle na vzcisti tabulky VSECHNY ktere jsou management!!!!!
#python manage.py flush --no-input

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic  --no-input
# python manage.py runserver 0.0.0.0:8000

# gunicorn core.wsgi:application --bind 0.0.0.0:8000

exec "$@"
