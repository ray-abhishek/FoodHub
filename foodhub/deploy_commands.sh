echo $0
echo $1
CONTAINS_MIGRATION='true'
docker-compose build server
docker-compose down && docker-compose up -d
if $CONTAINS_MIGRATION
then 
    docker-compose run --rm --entrypoint "python3 manage.py migrate" server
fi