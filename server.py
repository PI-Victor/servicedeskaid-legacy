import logging

from flask.ext.script import Manager
from flask.ext.script import Server

from viewpanel.app import app_factory

application = app_factory()
manager = Manager(application)
manager.add_command('runserver', Server(
    use_debugger = application.config['DEBUG'],
    use_reloader = application.config['RELOAD'],
    host = application.config['HOST']
))

if __name__ == '__main__':
    manager.run()
