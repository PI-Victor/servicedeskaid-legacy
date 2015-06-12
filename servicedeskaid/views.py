import flask
from flask.ext.login import current_user

from .forms import LoginForm

pages = flask.Blueprint('pages', __name__)


#@pages.before_request
#def before_request():
#    flask.g.user = current_user

@pages.route('/')
def index():
	return flask.render_template('viewpanel.html')	


@pages.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	flask.flash('Submitted')
    	return redirect('viewpanel.html')
    return flask.render_template('login.html', form=form)


@pages.route('/signup')
def sign_up():
    return flask.render_template('signup.html')
