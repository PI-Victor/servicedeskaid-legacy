import flask
import os
from flask.ext.mongoengine import MongoEngine

app = flask.Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'deskdb',
    'host': '127.0.0.1',
    'port': 27017
}
#app.config['WORKING_DIRECTORY'] = os.path.join(os.path.sep, os.path.dirname(os.path.realpath(__file__)))
db = MongoEngine(app)