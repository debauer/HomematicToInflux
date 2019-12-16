init:
	pip install -r requirements.txt
init-docker:
	sudo mkdir -p /srv/docker/grafana/data
	sudo chown 472:472 /srv/docker/grafana/data
	sudo mkdir -p /srv/docker/influxdb/data
	docker pull grafana/grafana
	docker pull influxdb
run-docker:
	docker-compose up
run:
	python -m hmtoinflux
test:
	python -m unittest discover -v
build:
	python setup.py sdist
