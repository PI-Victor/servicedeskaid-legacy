import os
import sys

from flask.ext.script import Manager
from flask.ext.script import Server

from viewpanel.config import config
from viewpanel.app import app_factory


application = app_factory()
manager = Manager(application)

config_options = {
    'production': config.ProductionConfig,
    'staging' : config.StagingConfig,
    'development': config.DevelopmentConfig,
    'testing': config.TestingConfig ,
}

@manager.command
def runserver(environment):
    if environment in config_options.keys():
        application.config.from_object(config_options.get(environment))
    else:
        print('Config not found! Available: ', [i for i in config_options.keys()])
        sys.exit(1)
        
    application.run(
        use_debugger = application.config['DEBUG'],
        use_reloader = application.config['RELOAD'],
        host = application.config['HOST']
    )

if __name__ == '__main__':
    manager.run()
