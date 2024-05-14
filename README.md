# Formulario automatizado de Reembolso

- Visão Geral:

- Objetivo:


## Como Instalar:
Modo Dev(Windows/Ubuntu):
Clonar o repositorio:
git clone https://github.com/brunoramalho01/formReembolso.git

Instalar depêndencias:
pip install -r requirements.txt

Rodar o Servidor:
python -m runserver

Modo Prod(Linux):

Clonar o repositorio:
git clone https://github.com/brunoramalho01/formReembolso.git

Criar um ambiente virtual:
python3 -m venv .venv

Ativar o ambiente no terminal:
. . venv/bin/activate

Instalar as dependencias no ambiente virtual:
pip install -r requirements.txt

Executar via terminal linux:
gunicorn -w 4 -b 0.0.0.0:8000 app:app

Para rodar em segundo plano:
gunicorn -w 4 -b 0.0.0.0:8000 app:app &

## Configurações:


## Tecnologias Empregadas

Python v3.10

BootStrap 5 CSS Framework - via CDN

HTML 5

Javascript