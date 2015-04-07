import logging
import os

from flask.ext.script import Manager
from flask.ext.script import Server

from viewpanel.app import app_factory


application = app_factory()
#the manager requires a single argument, either a flask instance or
#a factory pattern that returns a flask instance, however uwsgi
#needs an instance called application
manager = Manager(application)

config_options = {
    'production': 'config.ProductionConfig',
    'staging' : 'config.StagingConfig',
    'devlopment': 'config.DevelopmentConfig',
    'testing': 'config.TestingConfig'
}

@manager.command
def runserver(environment):
    if environment in config_options.keys():
#        os.environ['APP_SETTINGS'] = config_options.get(environment)
#        application.config.from_object(os.environ['APP_SETTINGS'])
    else:
        print([i for i in config_options.keys()])
        
    Server(use_debugger = application.config['DEBUG'],
           use_reloader = application.config['RELOAD'],
           host = application.config['HOST'],
    )

if __name__ == '__main__':
    manager.run()
