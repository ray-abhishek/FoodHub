cd foodhub
git pull origin ${BRANCH}
source /opt/foodhub/bin/activate
sudo docker-compose build server
sudo docker-compose down && sudo docker-compose up