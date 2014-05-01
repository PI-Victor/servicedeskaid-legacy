import flask
from flask.ext.mongoalchemy import MongoAlchemy


app = flask.Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'deskdb'
app.config['SECRET_KEY'] = '!b@n@nas for Sal3!'
app.config['DEBUG'] = True

db_sda = MongoAlchemy(app)

