echo $0
echo $1
contains_migration = $1
docker-compose build server
docker-compose down && docker-compose up -d
if contains_migration
then 
    sh 'ls'
    docker-compose run --rm --entrypoint "python3 manage.py migrate" server
