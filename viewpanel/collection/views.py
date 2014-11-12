from flask import g, request, render_template, flash, abort, redirect
from viewpanel import pages
from viewpanel.collection.models import Users 
from forms import LoginForm


@pages.before_request
def get_user():
    g.user = 'test'

@pages.route('/login', methods=['GET', 'POST'])
def user_login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Users.objects(userid=form.loginname.data, 
                             password=form.loginpass.data).get()
        if user is not None:
            g.user = user
            return redirect('viewpanel')
    elif request.method == 'GET':
        return render_template('login.html', error='')
    else:
        error = "Invalid username or password"
        return render_template('login.html', error=error)

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
