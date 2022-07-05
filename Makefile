install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/hexlet_code-0.1.1-py3-none-any.whl

selfcheck:
	poetry check

build:
	poetry build

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff

test-coverage-xml:
	poetry run pytest --cov=gendiff --cov-report xml
