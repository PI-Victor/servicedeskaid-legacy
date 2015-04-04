import os
import sys
import flask
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import ProductionConfig
pages = flask.Blueprint('pages', __name__)


def app_factory(config=None):
    app = flask.Flask(__name__)
    app.config.from_object(ProductionConfig)
    app.register_blueprint(pages)
    return app 
