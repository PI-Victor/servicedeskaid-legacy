from flask import Flask
from schema import SessionHandler as Sh


home = True

app = Flask(__name__)

#TODO have to move the below to a config file later on
app.config['MONGOALCHEMY_DATABASE'] = 'deskdb'
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '!b@n@n@s are very ch3ap!'
app.config['IPADRESS'] = ['10.0.2.15', '192.168.15.106'][home]


session_handler = Sh().bind_to_app(app)

