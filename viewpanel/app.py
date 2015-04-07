import logging
import os

import flask

from .config import config
from .views import pages


def app_factory():
    app = flask.Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.register_blueprint(pages)
    return app
