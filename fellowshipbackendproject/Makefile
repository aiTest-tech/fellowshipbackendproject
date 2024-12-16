startdev:
	python3 manage.py runserver

startprod:
	gunicorn -w 5 -b 0.0.0.0:8082 fellowshipbackendproject.wsgi:application -t 600

black:
	python3 -m black .

mig:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

migandmigrate: mig migrate ;

