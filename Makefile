init:
	pip install -r requirements.txt

test:
	py.test tests

freeze:
	pip freeze > requirements.txt

build:
	docker build -t aberegov/mockrtb:latest .

run:
	docker run -p 8080:9000 -d aberegov/mockrtb

shell:
	docker run -ti aberegov/mockrtb /bin/bash

.PHONY: init test freeze build run shell
