# flask-api-server

The simple template project for api server based on flask


### Run
FLASK_ENV=development nohup python run.py >> stdout.log &
curl -o /dev/null --silent --head --write-out '%{http_code}\n' 127.0.0.1:5000/monitor/alive

