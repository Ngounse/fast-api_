build:
	@docker-compose build $(filter-out $@,$(MAKECMDGOALS))

up:
	@docker-compose up $(filter-out $@,$(MAKECMDGOALS))

down:
	@docker-compose down $(filter-out $@,$(MAKECMDGOALS))

logs:
	docker-compose logs -f