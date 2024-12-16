# Airline Project

Este é um projeto Django de exemplo para gerenciar um sistema de voos e passageiros. O projeto inclui funcionalidades de registro de aeroportos, voos e passageiros, com a capacidade de associar passageiros a voos.

## Funcionalidades

- Cadastro de **Aeroportos** (com código e cidade).
- Cadastro de **Voos** (com origem, destino e duração).
- Cadastro de **Passageiros**, com a possibilidade de associá-los a múltiplos voos.
- Interface administrativa (admin) do Django com filtros horizontais para gerenciar passageiros e voos.

## Tecnologias Usadas

- **Django** (Framework Web Python)
- **Python** (Linguagem de Programação)
- **SQLite** (Banco de Dados, padrão do Django)
- **HTML/CSS** (para interfaces básicas do Django Admin)

## Como Rodar o Projeto

### Requisitos

- Python 3.6 ou superior
- Django (instalado no ambiente virtual)

### Passos para rodar

1. Clone o repositório:
   ```bash
   git clone :

python3 -m venv myvenv
source myvenv/bin/activate  # Para sistemas Unix/macOS
myvenv\Scripts\activate     # Para sistemas Windows
pip install -r requirements.txt
python manage.py 
python manage.py createsuperuser
python manage.py runserver