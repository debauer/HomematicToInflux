init:
	pip install -r requirements.txt
test:
	python -m unittest discover -v
build:
	python setup.py sdist