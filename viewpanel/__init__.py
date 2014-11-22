import flask
import os
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from mongoengine import ConnectionError
import collection

pages = flask.Blueprint('pages', __name__)

def app_factory(config=None):
    app = flask.Flask(__name__)
    app.config['WORK_DIR'] = collection.WORKDIR
    app.config['TMP_DIR'] = collection.TMPDIR
    app.config['LOG_DIR'] = collection.LOGDIR
    app.config['SECRET_KEY'] = collection.SECRETKEY
    app.config['MONGODB_SETTINGS'] = {
        'db': collection.DBNAME,
        'host': collection.DBHOST,
        'port': collection.DBPORT
    }
    app.register_blueprint(pages)
    return app 

def db_factory():
    try:
        db = MongoEngine(app)
    except ConnectionError as e:
        db = None
        exit(["Error, couldn't connect to the MongoDB instance. ",e])

    return db

app = app_factory()
db = db_factory()

loginman = LoginManager()
loginman.init_app(app)
opid = OpenID(app, app.config['LOG_DIR'])
