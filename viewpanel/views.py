import flask


pages = flask.Blueprint('pages', __name__)


@pages.route('/')
def index():
    return flask.render_template('wall.html')
