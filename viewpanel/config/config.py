import os


class Config(object):
    WORKDIR =  os.path.join(os.path.sep, os.path.dirname(os.path.realpath(__file__)))
    TMPDIR = os.path.join(os.path.sep, WORKDIR, 'tmp')
    LOGDIR = os.path.join(os.path.sep, WORKDIR, 'log')
    DATABASE = 'deskdb'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'aPAcheHel!c0ptEr'

    
class ProductionConfig(Config):
    DEBUG = False

    
class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
