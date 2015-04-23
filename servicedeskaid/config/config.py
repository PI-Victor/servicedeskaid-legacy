import os


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
    SQLALCHEMY_DATABASE_URI = 'postgres://deskuser:123123@127.0.0.1:5432/deskdb'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    DEBUG = False
    RELOAD = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'aPAcheHel!c0ptEr'
    SILENT_IMPORT = True
    HOST = '0.0.0.0'


class Production(Config):
    """These are the production configuration defaults.
    This will log a warning each time they are imported
    because of python namespaces.
    """

    HOST = '127.0.0.1'


class Staging(Config):
    """No use case scenario yet"""

    DEVELOPMENT = True
    DEBUG = True


class Development(Config):
    """Development configuration defaults"""

    DEVELOPMENT = True
    DEBUG = True
    RELOAD = True
    SQLALCHEMY_DATABASE_URI = 'postgres://deskuser:123123@0.0.0.0:5432/deskdb'
    SILENT_IMPORT = False


class Testing(Config):
    """Testing configuration defaults"""

    TESTING = True


class Docker(Config):
    """Docker container configuration. The default values here are
     overwritten by the container injection when they get linked.
     Or they can be specified at container runtime.
    """

    SQLALCHEMY_DATABASE_URI = 'postgres://deskuser:123123@0.0.0.0:5432/deskdb'
