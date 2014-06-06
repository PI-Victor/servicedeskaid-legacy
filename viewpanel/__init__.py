from flask.ext.mongoalchemy import MongoAlchemy
import flask
import pymongo
home = True

app = flask.Flask(__name__)
#app.jinja_loader = jinja2.FileSystemLoader('viewpanel/templates')

#TODO have to move the below to a config file later on
app.config['MONGOALCHEMY_DATABASE'] = 'deskdb'
app.config['SECRET_KEY'] = '!b@n@n@s are very ch3ap!'
app.config['DEBUG'] = True
app.config['IPADRESS'] = ['10.0.2.15', '192.168.15.106'][home]
try:
    session_handler = MongoAlchemy(app)
except:
    raise


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if flask.request.method == 'GET':
        return flask.render_template('login.html')
    user_name = flask.request.form['login-username']
    user_pass = flask.request.form['login-password']
    user_remember = flask.request.formp['login-remember']
#    results = sc.Users.query.filter()
    #print results


@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/graphs')
def graphing():
    return flask.render_template('graphs.html')

@app.route('/timezones')
def timezones():
    return flask.render_template('flipclock.html')

