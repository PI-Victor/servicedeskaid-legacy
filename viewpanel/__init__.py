import mongoengine
import flask
from collection import graphing as gr, formvalid
home = True

app = flask.Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    form = formvalid.LoginForm(flask.request.form)
    if flask.request.method == 'POST' and form.validate():
        return flask.render_template('viewpanel.html')
    else:
        return flask.render_template('login.html')

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/viewpanel')
def viewpanel():
    return flask.render_template('viewpanel.html')

@app.route('/graphs')
def graphing():
    gr.generate_graph()
    return flask.render_template('graphs.html')

@app.route('/timezones')
def timezones():
    return flask.render_template('flipclock.html')
