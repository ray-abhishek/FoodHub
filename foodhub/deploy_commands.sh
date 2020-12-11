docker-compose down && docker-compose up -d
docker ps
docker exec -it foodhub_server_1 python3 manage.py migrate
