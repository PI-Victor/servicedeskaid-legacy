import mongoengine
import flask
import pymongo
home = True

app = flask.Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if flask.request.method == 'GET':
        return flask.render_template('login.html')
    user_name = flask.request.form['login-username']
    user_pass = flask.request.form['login-password']
    user_remember = flask.request.formp['login-remember']

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/graphs')
def graphing():
    return flask.render_template('graphs.html')

@app.route('/timezones')
def timezones():
    return flask.render_template('flipclock.html')

