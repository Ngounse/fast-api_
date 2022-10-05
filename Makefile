## help	:	Print commands help.
help : Makefile
	@sed -n 's/^##//p' $<

## build	:	Build python image.
build:
	@docker-compose build $(filter-out $@,$(MAKECMDGOALS))

## up	:	Start up containers.
up:
	@docker-compose up $(filter-out $@,$(MAKECMDGOALS))

## down	:	Stop containers.
down:
	@docker-compose down $(filter-out $@,$(MAKECMDGOALS))

logs:
	docker-compose logs -f


# https://stackoverflow.com/a/6273809/1826109
%:
	@: