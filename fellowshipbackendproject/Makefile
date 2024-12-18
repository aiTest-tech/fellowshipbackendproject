startdev:
	python3 manage.py runserver 10.10.2.179:8000

startdevguni:
	DJANGO_ENV=dev gunicorn -w 5 -b 10.10.2.179:8082 fellowshipbackendproject.wsgi:application -t 600

startstagguni:
	DJANGO_ENV=staging gunicorn -w 5 -b 0.0.0.0:8083 fellowshipbackendproject.wsgi:application -t 600

startprodguni:
	DJANGO_ENV=production gunicorn -w 5 -b 10.10.2.179:8084 fellowshipbackendproject.wsgi:application -t 600

black:
	python3 -m black .

mig:
	python3 manage.py makemigrations

migandmigrate: mig migrate ;

migstag:
	DJANGO_ENV=staging python3 manage.py makemigrations

migratestag:
	DJANGO_ENV=staging python3 manage.py migrate


migandmigratestag: migstag  migratestag;


migprod:
	DJANGO_ENV=production python3 manage.py makemigrations

migrateprod:
	DJANGO_ENV=production python3 manage.py migrate

migandmigrateprod: migprod  migrateprod;

collectstatic:
	python3 manage.py collectstatic

createsuperuserdev:
	python3 manage.py createsuperuser

createsuperuserstag:
	DJANGO_ENV=staging python3 manage.py createsuperuser

createsuperuserprod:
	DJANGO_ENV=production python3 manage.py createsuperuser

