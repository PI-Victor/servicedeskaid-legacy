import os
import logging


__all__ = ['Production', 'Development', 'Testing', 'Staging', 'Docker']


class Config(object):
    """Default class for config object.
    Here all the default values can be overwritten by classes the inherit this one
    and they can also be overwritten once more by the config file in the instance
    folder.
    """

    WORKDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    TMPDIR = os.path.join(os.path.sep, WORKDIR, 'tmp')
    LOGDIR = os.path.join(os.path.sep, WORKDIR, 'log')
    DATABASE_DIALECT = 'postgres'
    DATABASE = 'deskdb'
    DATABASE_USER = 'deskuser'
    DATABASE_PASSWORD = '123123'
    DATABASE_IP = '0.0.0.0'
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}/{}'.format(
        DATABASE_DIALECT,
        DATABASE_USER,
        DATABASE_PASSWORD,
        DATABASE_IP,
        DATABASE
    )
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    DEBUG = False
    RELOAD = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'aPAcheHel!c0ptEr'
    HOST = '0.0.0.0'
    SILENT_IMPORT = True
    BINDHOSTIP = '0.0.0.0'


class Production(Config):
    """These are the production configuration defaults.
    This will log a warning each time they are imported
    because of python namespaces.
    """

    try:
        HOST = os.environ['BINDHOSTIP']
    except KeyError as e:
        HOST = '127.0.0.1'
        logging.warning("No BINDHOSTIP specified: Production config will run on 127.0.0.1")


class Staging(Config):
    """No use scenario yet"""

    DEVELOPMENT = True
    DEBUG = True


class Development(Config):
    """Development configuration defaults"""

    DEVELOPMENT = True
    DEBUG = True
    RELOAD = True
    DB_DIALECT = 'postgres'
    DATABASE = 'deskdb'
    DATABASE_URI = 'postgresql://127.0.0.1:5432'
    DATABASE_USER = 'deskuser'
    DATABASE_PASSWORD = '123123'
    SILENT_IMPORT = False


class Testing(Config):
    """Testing configuration defaults"""

    TESTING = True


class Docker(Config):
    """Docker container configuration. The default values here are
     overwritten by the container injection when they get linked.
     Or they can be specified at container runtime.
    """

    DATABASE_URI = 'postgresql://deskuser:123123@127.0.0.1:5432'
    DATABASE_PASSWORD = '123123'
    DB_DIALECT = 'postgres'
