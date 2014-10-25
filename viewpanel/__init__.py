import flask
import os
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from mongoengine import ConnectionError
import collection


app = flask.Flask(__name__)

app.config['WORK_DIR'] = collection.WORKDIR
app.config['TMP_DIR'] = collection.TMPDIR
app.config['LOG_DIR'] = collection.LOGDIR
app.config['SECRET_KEY'] = collection.SECRETKEY
app.config['MONGODB_SETTINGS'] = {
    'db': collection.DESKDB,
    'host': collection.DEFAULTHOST,
    'port': 27017
}

try:
    db = MongoEngine(app)
except ConnectionError as e:
    exit(["Error, couldn't connect to the MongoDB instance. ",e])

loginman = LoginManager()
loginman.init_app(app)
opid = OpenID(app, app.config['LOG_DIR'])
