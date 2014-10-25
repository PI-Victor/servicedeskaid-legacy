import flask
from viewpanel import app

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if flask.request.method == 'POST':
        print "This is a post"
        return flask.render_template('login.html', error=False)
    elif flask.request.method == 'GET':
        print "This is a get"
        return flask.render_template('login.html', error=True)
    else:
        print "You screwed up"

@app.route('/')
def index():
    return flask.render_template('wall.html')


@app.route('/viewpanel')
def viewpanel():
    return flask.render_template('viewpanel.html')


@app.route('/timezones')
def timezones():
    return flask.render_template('timezones.html')


@app.route('/users')
def show_users():
    from viewpanel.collection.models import Users  # <---- wtf, might wanna move the import out of here
    return flask.render_template('users.html', Users=Users)


@app.route('/statistic')
def statistic():
    return flask.render_template('statistic.html')
