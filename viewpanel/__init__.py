import mongoengine
import flask
from collection import graphing as gr
home = True

app = flask.Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if flask.request.method == 'POST':
        user_name = flask.request.form['loginname']
        user_pass = flask.request.form['loginpass']
        user_remember = flask.request.form['loginremember']
        return flask.render_template('index.html')
    else:
        return flask.render_template('login.html')


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

