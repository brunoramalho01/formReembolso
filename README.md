# Formulario automatizado de Reembolso

- Visão Geral:

- Objetivo:


## Como Instalar:
Modo Dev:
clonar o repositorio 

pip install -r requirements.txt

python -m runserver

Modo Prod:
clonar o repositorio 

python3 -m venv .venv

. . venv/bin/activate

pip install -r requirements.txt

executar via terminal linux:
gunicorn -w 4 -b 0.0.0.0:8000 app:app
para rodar em segundo plano:
gunicorn -w 4 -b 0.0.0.0:8000 app:app &


## Configurações:


## Tecnologias Empregadas

Python v3.10

HTML 5

BootStrap 5 CSS Framework