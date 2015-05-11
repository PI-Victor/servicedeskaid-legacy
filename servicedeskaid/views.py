import flask
from flask.ext.login import current_user

from .forms import LoginForm

pages = flask.Blueprint('pages', __name__)


#@pages.before_request
#def before_request():
#    flask.g.user = current_user

@pages.route('/')
def index():
 #   if not flask.g.user.is_authenticated:
        return flask.render_template('login.html')
    
 #   return flask.render_template('wall.html')
    
@pages.route('/login')
def login():
    pass


@pages.route('/signup')
def sign_up():
    return flask.render_template('signup.html')
