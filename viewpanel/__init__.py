import flask
import os
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from mongoengine import ConnectionError

app = flask.Flask(__name__)

app.config['WORKING_DIRECTORY'] = os.path.join(os.path.sep, os.path.dirname(os.path.realpath(__file__)))
#app.config['TMP_DIRECTORY'] = 
#app.config[]
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
opid = OpenID(app, )
