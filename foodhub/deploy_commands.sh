docker-compose down && docker-compose up -d
docker-compose run --rm --entrypoint "python3 manage.py migrate --noinput" server > /dev/null
