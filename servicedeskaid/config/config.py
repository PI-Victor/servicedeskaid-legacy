import os


__all__ = ['Production', 'Development', 'Testing', 'Staging', 'Docker']


class Config(object):
    WORKDIR =  os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    TMPDIR = os.path.join(os.path.sep, WORKDIR, 'tmp')
    LOGDIR = os.path.join(os.path.sep, WORKDIR, 'log')
    DB_DIALECT = 'postgres'
    DATABASE = 'deskdb'
    SQLALCHEMY_DATABASE_URI = 'postgresql://127.0.0.1:5432'
    DATABASE_USER = 'postgres'
    DATABASE_PASSWORD = 'password'
    DEBUG = False
    RELOAD = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'aPAcheHel!c0ptEr'
    HOST = '0.0.0.0'
    

class Production(Config):
    try:
        HOST = os.environ['BINDHOSTIP']
    except KeyError as e:
        pass


class Staging(Config):
    DEVELOPMENT = True
    DEBUG = True


class Development(Config):
    DEVELOPMENT = True
    DEBUG = True
    RELOAD = True
    DB_DIALECT = 'potgres'
    DATABASE = 'deskdb'
    DATABASE_URI = 'postgresql://127.0.0.1:5432'
    DATABASE_USER = 'deskuser'
    DATABASE_PASSWORD = '123123'


class Testing(Config):
    TESTING = True


class Docker(Config):
    """Docker container configuration"""
    DATABASE_URI = 'postgresql://deskuser:123123@127.0.0.1:5432'
    DATABASE_PASSWORD = '123123'
    DB_DIALECT = 'postgres'
