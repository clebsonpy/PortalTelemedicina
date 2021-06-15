# PortalTelemedicina

API Rest list products. 

## Desenvolvimento

### Cria as imagens do projeto
    
    docker-compose build --no-cache

Com o `make` instalado:

    make build

### Setup do banco de dados
Para iniciar o banco de dados é necessário rodar o migrate

    docker-compose run --rm backend python manage.py migrate

Com o `make` instalado:

    make migrate

### Super usuário

    docker-compose run --rm backend python manage.py createsuperuser

Com o `make` instalado:

    make createsuperuser

### Subir ambiente de desenvolvimento

    docker-compose up

Com o `make` instalado:

    make runserver
