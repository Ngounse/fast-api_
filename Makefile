build_:
	docker build -t fastapi-hello:0.1 .

up_:
	docker run -p 8000:8000 --name my-api fastapi-hello:0.1

stop_:
	docker stop my-api

kill_:
	docker kill my-api