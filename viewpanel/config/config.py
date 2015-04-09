import os
import logging


logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s',
                    level=logging.DEBUG)

class Config(object):
    WORKDIR =  os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    TMPDIR = os.path.join(os.path.sep, WORKDIR, 'tmp')
    LOGDIR = os.path.join(os.path.sep, WORKDIR, 'log')
    DB_DIALECT = 'postgres'
    DATABASE = 'deskdb'
    DATABASE_URI = 'postgresql://'
    DEBUG = False
    RELOAD = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'aPAcheHel!c0ptEr'
    HOST = '0.0.0.0'


class Production(Config):
    try:
        HOST = os.environ['BINDHOSTIP']
    except:
        pass


class Staging(Config):
    DEVELOPMENT = True
    DEBUG = True


class Development(Config):
    DEVELOPMENT = True
    DEBUG = True
    RELOAD = True


class Testing(Config):
    TESTING = True


class Docker(Config):
    '''Docker container configuration'''
    DATABASE_URI = ''
    
