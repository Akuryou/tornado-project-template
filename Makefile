ENV = env
PIP = $(ENV)/bin/pip
PYTHON = $(ENV)/bin/python

all:
	@echo 'Please use "make development" or "make production"'

environment:
	test -d "$(ENV)" || virtualenv $(ENV)

requirements-base: environment
	$(PIP) install -r requirements/base.txt --upgrade

requirements-development: requirements-base
	$(PIP) install -r requirements/development.txt --upgrade

requirements-production: requirements-base
	$(PIP) install -r requirements/production.txt --upgrade

server-development:
	$(PYTHON) run.py --target=development

server-production:
	$(PYTHON) run.py --target=production

development: requirements-development server-development

production: requirements-production server-production

clean:
	rm -rf $(ENV)
