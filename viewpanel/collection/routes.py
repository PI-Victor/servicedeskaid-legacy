from . import app
from viewpanel.collection import schema as sc
from flask.ext.login import LoginManager
import flask
#from viewpanel.templates import * 


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if flask.request.method == 'GET':
        return flask.render_template('login.html')
    user_name = flask.request.form['login-username']
    user_pass = flask.request.form['login-password']
    user_remember = flask.request.formp['login-remember']
#    results = sc.Users.query.filter()
    print results



@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/timezones')
def timezones():
    return flask.render_template('flipclock.html')

