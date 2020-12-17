echo $0
CONTAINS_MIGRATION=$1
echo $CONTAINS_MIGRATION
git clone git@github.com:ray-abhishek/FoodHub.git
git pull origin master

docker-compose build server
docker-compose down && docker-compose up -d
if [ $CONTAINS_MIGRATION == "true" ]
then 
    docker-compose run --rm --entrypoint "python3 manage.py migrate" server
fi