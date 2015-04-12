import os
import sys

#import SQLAlchemy
import click

from viewpanel.config import config
from viewpanel.app import app_factory


config_options = {
    'production': config.Production,
    'staging' : config.Staging,
    'development': config.Development,
    'testing': config.Testing,
}

@click.command()
@click.option('--config', help='Configuration load options')
def runserver(config):
    if config in config_options.keys():
        application = app_factory(config_options.get(config))
#        db = SQLAlchemy(application)
    else:
        print('Config not found! Available: ', [i for i in config_options.keys()])
        sys.exit(1)
        
    application.run(
        use_debugger = application.config['DEBUG'],
        use_reloader = application.config['RELOAD'],
        host = application.config['HOST']
    )

if __name__ == '__main__':
    runserver()
