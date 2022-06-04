install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

selfcheck:
	poetry check

build:
	poetry build

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest
