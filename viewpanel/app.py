import logging
import os
import logging

import flask
from flask.ext.sqlalchemy import SQLAlchemy

from .config import config
from .views import pages

logger = logging.getLogger(__name__)


def app_factory(config, envfile=''):
    app = flask.Flask(__name__)
    app.config.from_object(config)
    logging.debug(envfile)
    #load aditional configuration if specified
    if envfile:
        try:
            app.config.from_pyfile(envfile)
        except Exception as e:
            logging.info('Unable to load config file. Using defaults!', e)
            pass
        
    db = SQLAlchemy(app)
    app.register_blueprint(pages)
    return app
