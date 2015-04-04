import os
import sys
import flask
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID


pages = flask.Blueprint('pages', __name__)

ckbindip = os.getenv("BINDIP") 
#environment paths
WORKDIR = os.path.join(os.path.sep, os.path.dirname(os.path.realpath(__file__)))
TMPDIR = 
LOGDIR = os.path.join(os.path.sep, WORKDIR, 'log')
DBNAME = 'deskdb'
SECRETKEY = 't3st Patience'

DEFAULTHOST = ckbindip


def app_factory(config=None):
    app = flask.Flask(__name__)
    app.config = {
        'WORK_DIR': WORKDIR,
        'TMP_DIR': TMPDIR,
        'LOGDIR': os.path.join(os.path.sep, WORKDIR, 'tmp')
    }

    app.register_blueprint(pages)
    return app 

app = app_factory()
db = db_factory()
loginman = LoginManager()
loginman.init_app(app)
opid = OpenID(app, app.config['LOG_DIR'])
