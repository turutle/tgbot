import os
import psycopg2
import requests
import flask

DB_URI = 'postgres://fmbdpcejbpsbxp:02538aa5feb439f7b50b9ab5df71bf8be38153d66ffcd457e50f8ea73c7661b7@ec2-99-81-16-126.eu-west-1.compute.amazonaws.com:5432/d54rrsefseb7hf'
APP_URL = 'https://tgbot-12795.herokuapp.com/'
TIME_URL = 'http://worldtimeapi.org/api/timezone/Europe/Moscow'

db_connection = psycopg2.connect(DB_URI, sslmode="require")
db_object = db_connection.cursor()
server = flask.Flask(__name__)
nowTime = requests.get(TIME_URL).json()['datetime']

@server.route('/')
def index():
    return nowTime

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))