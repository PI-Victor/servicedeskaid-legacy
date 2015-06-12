import os
import logging

import flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData

from .views import pages

logger = logging.getLogger(__name__)


def app_factory(config, envfile=''):
    app = flask.Flask('servicedeskaid', instance_relative_config=True)
    app.config.from_object(config)
    logging.debug(envfile)
    # load the additional configuration file if specified
    if envfile:
        envfile = os.path.join(app.instance_path, envfile)
        try:
            app.config.from_pyfile(envfile, silent=app.config['SILENT_IMPORT'])
        except Exception as e:
            logging.warning('Unable to load config file. Using defaults!', e)
    db, engine = engine_factory(app)
    engine.connect()
    db.init_app(app)
    app.register_blueprint(pages)
    logging.info(db)
    return app


def engine_factory(app):
    db = SQLAlchemy(app)
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    meta = MetaData(bind=engine, reflect=True)
    meta.bind = engine
    meta.create_all()
    return db, engine
