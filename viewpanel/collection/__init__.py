from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy
home = True

app = Flask(__name__)

#TODO have to move the below to a config file later on
app.config['MONGOALCHEMY_DATABASE'] = 'deskdb'
app.config['SECRET_KEY'] = '!b@n@n@s are very ch3ap!'
app.config['DEBUG'] = True

#app.config['IPADRESS'] = ['10.0.2.15', '192.168.15.106'][home]

session_handler = MongoAlchemy(app)

import routes