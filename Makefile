ENV = env
PIP = $(ENV)/bin/pip

environment:
	test -d "$(ENV)" || virtualenv $(ENV)

requirements: environment
	$(PIP) install -r requirements/base.txt

requirements-dev: requirements
	$(PIP) install -r requirements/development.txt
