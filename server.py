import os
import sys
import logging

import click

from viewpanel.config import config
from viewpanel.app import app_factory


logger = logging.getLogger(__name__)

config_options = {
    'production': config.Production,
    'staging' : config.Staging,
    'development': config.Development,
    'testing': config.Testing,
}

@click.command()
@click.option('--config',
              help='Configuration load options. If unspecified, defaults to: development',
              default='development',
              type=click.Choice([i for i in config_options.keys()]))
@click.option('--envfile', help='Aditional configuration file.')
def runserver(config, envfile):
    '''Start the application with the configuration sepcified
    as a parameter. 
    '''
    if config in config_options.keys():
        application = app_factory(config_options.get(config), envfile)
        logger.info('Loaded application with %s configuration.' %config)
    else:
        print('Config not found! Use --help')
        sys.exit(1)
        
    application.run(
        use_debugger = application.debug,
        use_reloader = application.config['RELOAD'],
        host = application.config['HOST'],
    )

if __name__ == '__main__':
    runserver()
