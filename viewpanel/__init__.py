import flask
from collection.schema import Users
from collection import graphing as gr
from collection import formvalid
from flask.ext.mongoengine import MongoEngine

home = True

app = flask.Flask(__name__)

DB_NAME='deskdb'
HOST='192.168.15.101'

app.config['MONGODB_DB'] = DB_NAME

db = MongoEngine(app)

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    form = formvalid.LoginForm(flask.request.form)
    if flask.request.method == 'POST' and form.validate():
        if user_validate(flask.request.form['loginname'], flask.request.form['loginpass']):
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


#leave this messy mess here for now, just need basic login no computer science
def user_validate(user,password):
    if Users.objects(userid=user):
        print Users.userid
