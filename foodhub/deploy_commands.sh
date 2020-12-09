cd foodhub
git pull
source /opt/foodhub/bin/activate
pip install -r requirements.txt
./manage.py migrate
exit