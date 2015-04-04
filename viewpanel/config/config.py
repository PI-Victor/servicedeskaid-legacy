#-*- coding: utf-8 -*-
import os
import logging


logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s',
                    level=logging.DEBUG)

class Config(object):
    DIALECT = 'postgres'
    WORKDIR =  os.path.join(os.path.sep, os.path.dirname(os.path.realpath(__file__)))
    TMPDIR = os.path.join(os.path.sep, WORKDIR, 'tmp')
    LOGDIR = os.path.join(os.path.sep, WORKDIR, 'log')
    DATABASE = 'deskdb'
    DATABASE_URI = 'postgresql://'
    DEBUG = False
    RELOAD = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'aPAcheHel!c0ptEr'
    HOST = ''


class ProductionConfig(Config):
    HOST = '0.0.0.0'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    RELOAD = True
    HOST = '0.0.0.0'


class TestingConfig(Config):
    TESTING = True


class DockerConfig(Config):
    '''Docker container configuration'''
    #REMEMBERTO: bind the host to the right env variables
