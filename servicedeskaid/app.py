import os
import logging

import flask
from flask.ext.sqlalchemy import SQLAlchemy

from .views import pages

logger = logging.getLogger(__name__)

db =  SQLAlchemy()

def app_factory(config, envfile=''):
    app = flask.Flask('servicedeskaid')
    app.config.from_object(config)
    logging.debug(envfile)
    # load the additional configuration file if specified
    if envfile:
        envfile = os.path.join(os.path.sep, app.config['WORKDIR'], envfile)
        try:
            app.config.from_pyfile(envfile)
        except Exception as e:
            logging.info('Unable to load config file. Using defaults!', e)
            pass
    db.init_app(app)
    app.register_blueprint(pages)
    logging.info(db)
    return app


