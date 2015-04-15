import click

from servicedeskaid.config import logger
from servicedeskaid import config
from servicedeskaid import app_factory


log = logger.getlogger(__name__)

config_options = {
    'production': config.Production,
    'staging': config.Staging,
    'development': config.Development,
    'testing': config.Testing,
}


@click.command()
@click.option('--conf', help='Configuration load options. Default: development.',
              default='development',
              type=click.Choice([i for i in config_options.keys()]))
@click.option('--envfile', help='Additional configuration file.')
def runserver(conf, envfile):
    """Start the application with the configuration specified
    as a parameter. If no configuration parameter was specified on start
    it uses the development configuration as default.
    """
    application = app_factory(config_options.get(conf), envfile)
    log.info('Loaded %s configuration.' % conf)
    application.run(
        use_debugger=application.debug,
        use_reloader=application.config['RELOAD'],
        host=application.config['HOST'],
    )

if __name__ == '__main__':
    runserver()
