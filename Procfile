web: gunicorn advisor_api.wsgi
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noinput
release: python manage.p migrate --noinput
