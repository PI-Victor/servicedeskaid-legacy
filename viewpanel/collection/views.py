import flask
from viewpanel import app


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if
        return flask.render_template('login.html')

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/viewpanel')
def viewpanel():
    return flask.render_template('viewpanel.html')

@app.route('/timezones')
def timezones():
    return flask.render_template('flipclock.html')
