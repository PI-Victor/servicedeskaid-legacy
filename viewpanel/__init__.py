import flask
import os
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from mongoengine import ConnectionError

app = flask.Flask(__name__)

app.config['WORK_DIR'] = os.path.join(os.path.sep, os.path.dirname(os.path.realpath(__file__)))
app.config['TMP_DIR'] = '/home/vectra/projects/servicedeskaid/tmp'  #   Leave this hardcoded until config is in place
app.config['LOG_DIR'] = '/home/vectra/projects/servicedeskaid/log'
app.config['SECRET_KEY'] = 't3st Patience'
app.config['MONGODB_SETTINGS'] = {
    'db': 'deskdb',
    'host': '127.0.0.1',
    'port': 27017
}

try:
    db = MongoEngine(app)
except ConnectionError as e:
    exit("Error, couldn't connect to the MongoDB instance. "+ str(e))

loginman = LoginManager()
loginman.init_app(app)
opid = OpenID(app, app.config['LOG_DIR'])
