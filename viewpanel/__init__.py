import mongoengine
import flask
from collection import graphing as gr
home = True

app = flask.Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if flask.request.method == 'GET':
        print "something"
        return flask.render_template('login.html')
    if flask.request.method == 'POST':
        user_name = flask.request.form['login-username']
        user_pass = flask.request.form['login-password']
        user_remember = flask.request.form['login-remember']
    print user_name, user_pass, user_remember

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/graphs')
def graphing():
    gr.generate_graph()
    return flask.render_template('graphs.html')

@app.route('/timezones')
def timezones():
    return flask.render_template('flipclock.html')

