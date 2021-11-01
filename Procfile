web: gunicorn advisor_api.wsgi
release: python3 manage.py makemigrations --noinput
release: python3 manage.py collectstatic --noinput
release: python3 manage.p migrate --noinput
