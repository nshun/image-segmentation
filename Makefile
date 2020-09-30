NAME=my-prometheus

restart: stop start

start:
		docker-compose up --build -d
stop:
		docker-compose down
