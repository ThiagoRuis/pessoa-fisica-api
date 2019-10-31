# API de cadastro de pessoas fisicas


1. criar virtualenvironment (virtualenv --python=python3 venv)
1. inicializar o virtualenvironment (. venv/bin/activate)
1. rodar o comando 'pip install -r requirements.txt'
1. iniciar o docker para o banco de dados (docker-compose up -d)
1. rodar as migrations 'python manage.py migrate'
1. iniciar o serviço 'python manage.py runserver'
