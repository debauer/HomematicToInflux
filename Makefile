init:
	pip install -r requirements.txt
run:
	python -m hmtoinflux
test:
	python -m unittest discover -v
build:
	python setup.py sdist

init-docker:
	sudo mkdir -p /srv/docker/grafana/data
	sudo chown 472:472 /srv/docker/grafana/data
	sudo mkdir -p /srv/docker/influxdb/data
	sudo docker pull grafana/grafana
	sudo docker pull influxdb
run-docker:
	sudo docker-compose up -d
stop-docker:
	sudo docker-compose stop
cleanup-docker:
	sudo docker-compose rm

cleanup-influx:
	curl -i -XPOST http://localhost:8086/query --data-urlencode "q=DROP database homematicToInflux"
	curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE database homematicToInflux"