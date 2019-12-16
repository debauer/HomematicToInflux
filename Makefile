init:
	pip install -r requirements.txt
run:
	python hmtoinflux/core.py
test:
	python -m unittest discover -v
build:
	python setup.py sdist