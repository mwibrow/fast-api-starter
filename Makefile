# Initialise development enviromment
init:
	pip install pipenv --upgrade
	export PIPENV_VENV_IN_PROJECT=1 && pipenv install --dev
	pipenv run pre-commit
