from flask import g, request, render_template, flash, abort, redirect, url_for
from flask.ext.login import login_user
from forms import LoginForm
from viewpanel import pages
from viewpanel.collection.models import Users 
from viewpanel import loginman, opid


@loginman.user_loader
def get_user(user, password):
    try:
        user = Users.objects(userid=user, password=password).get()
    except Users.DoesNotExist as err:
        user = False
    return user


@pages.route('/login', methods=['GET', 'POST'])
@opid.loginhandler
def user_login():
    form = LoginForm(request.form)
    user = get_user(form.loginname.data, form.loginpass.data)
    if request.method == 'POST' and form.validate() and user is not None:
        login_user(user)
        print dir(loginman)
        return url_for('viewpanel')
    elif request.method == 'GET':
        return render_template('login.html', error='')
    else:
        error = "Invalid username or password"
        return render_template('login.html', error=error)


@pages.route('/signup', methods=['POST'])
def signup():
    return redirect('login')
    

@pages.route('/')
def index():
    return render_template('wall.html')


@pages.route('/viewpanel')
def viewpanel():
    return render_template('viewpanel.html')


@pages.route('/timezones')
def timezones():
    return render_template('timezones.html')


@pages.route('/users')
def show_users():

    return render_template('users.html', Users=Users)


@pages.route('/statistic')
def statistic():
    return render_template('statistic.html')
