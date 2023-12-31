install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

build:
	poetry build

publish:
	poetry publish --dry-run

start:
	python manage.py runserver

migration:
	python manage.py makemigrations