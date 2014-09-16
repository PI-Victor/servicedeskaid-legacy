import flask
from viewpanel import app

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if flask.request.method == 'POST':
        pass
    else:
        return flask.render_template('login.html', error=True)

@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/viewpanel')
def viewpanel():
    return flask.render_template('viewpanel.html')


@app.route('/timezones')
def timezones():
    return flask.render_template('flipclock.html')


@app.route('/users')
def show_users():
    from viewpanel.collection.models import Users
    return flask.render_template('users.html', Users=Users)
