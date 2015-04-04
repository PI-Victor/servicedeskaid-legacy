import os
import sys
import flask
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID


pages = flask.Blueprint('pages', __name__)

def app_factory(config=None):
    app = flask.Flask(__name__)
    app.bootstrap_config(app)
    app.config['WORK_DIR'] = collection.WORKDIR
    app.config['TMP_DIR'] = collection.TMPDIR
    app.config['LOG_DIR'] = collection.LOGDIR
    app.config['SECRET_KEY'] = collection.SECRETKEY
    app.register_blueprint(pages)
    return app 



app = app_factory()
db = db_factory()
loginman = LoginManager()
loginman.init_app(app)
opid = OpenID(app, app.config['LOG_DIR'])
