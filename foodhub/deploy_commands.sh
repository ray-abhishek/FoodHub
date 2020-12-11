docker-compose down && docker-compose up -d
docker ps
docker exec foodhub_server_1 python3 manage.py runserver 0.0.0.0:8000
