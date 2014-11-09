import flask
from viewpanel import pages
from viewpanel.collection.models import Users 


@pages.route('/login', methods=['GET', 'POST'])
def user_login():
    if flask.request.method == 'POST':
        return flask.render_template('login.html', error=False)
    elif flask.request.method == 'GET':
        return flask.render_template('login.html', error=True)
    else:
        print "You screwed up"

@pages.route('/')
def index():
    return flask.render_template('wall.html')


@pages.route('/viewpanel')
def viewpanel():
    return flask.render_template('viewpanel.html')


@pages.route('/timezones')
def timezones():
    return flask.render_template('timezones.html')


@pages.route('/users')
def show_users():

    return flask.render_template('users.html', Users=Users)


@pages.route('/statistic')
def statistic():
    return flask.render_template('statistic.html')
