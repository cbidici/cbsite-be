release: python manage.py migrate
release: python manage.py createsuperuser --noinput
release: python manage.py collectstatic
web: gunicorn cbsite.wsgi --log-file -
