#!/bin/sh
echo "------ Create database tables ------"
python manage.py syncdb --noinput

echo "------ starting gunicorn  ------"
gunicorn mapstory.wsgi --log-level=debug --logger-class=simple -b 0.0.0.0:$PORT
