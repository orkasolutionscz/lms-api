#!/bin/sh

# Tohle na vzcisti tabulky VSECHNY ktere jsou management!!!!!
#python manage.py flush --no-input

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic  --no-input --clear

exec "$@"
