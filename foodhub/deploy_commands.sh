echo $0
echo $1
CONTAINS_MIGRATION = $1
docker-compose build server
docker-compose down && docker-compose up -d
if CONTAINS_MIGRATION
then 
    sh 'ls'
    docker-compose run --rm --entrypoint "python3 manage.py migrate" server
fi