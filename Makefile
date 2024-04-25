.PHONY: install migrate createsuperuser runserver


install:
	pip install -r requirements.txt
 
migrate:
	python manage.py makemigrations app_basket
	python manage.py makemigrations app_category
	python manage.py makemigrations app_favorite
	python manage.py makemigrations app_product
	python manage.py makemigrations app_user
	python manage.py makemigrations app_account
	python manage.py makemigrations app_collection
	python manage.py makemigrations app_banner
	python manage.py migrate
 
createsuperuser:
	python manage.py createsuperuser
 
runserver:
	python manage.py runserver