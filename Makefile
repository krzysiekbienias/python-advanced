VENV := .venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
JUPYTER := $(VENV)/bin/jupyter

.DEFAULT_GOAL := help

.PHONY: help venv install install-dev test run lab clean

help: ## Pokaz dostepne komendy
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

venv: ## Stworz virtualenv w .venv (jesli nie istnieje)
	test -d $(VENV) || python3 -m venv $(VENV)

install: venv ## Zainstaluj zaleznosci produkcyjne
	$(PIP) install -r requirements.txt

install-dev: venv ## Zainstaluj zaleznosci deweloperskie (pytest itd.)
	$(PIP) install -r requirements-dev.txt

test: ## Uruchom testy (pytest)
	$(PY) -m pytest

run: ## Uruchom plik: make run FILE=sciezka/do/pliku.py
	@test -n "$(FILE)" || { echo "Uzycie: make run FILE=sciezka/do/pliku.py"; exit 1; }
	$(PY) $(FILE)

lab: ## Uruchom JupyterLab
	$(JUPYTER) lab --allow-root

clean: ## Usun cache Pythona i pytest
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache
