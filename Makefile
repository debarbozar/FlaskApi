APP = restapi

test:
	@flake . --exclude .venv

compose:
	@docker-compose build
	@docker-compose up