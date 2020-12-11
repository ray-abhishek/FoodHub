docker-compose down && docker-compose up -d
docker-compose exec -it foodhub_server_1 python3 manage.py migrate
