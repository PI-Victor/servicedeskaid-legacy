import logging

from flask.ext.script import Manager
from flask.ext.script import Server

from viewpanel.app import app_factory

application = app_factory()
manager = Manager(application)
manager.add_command('runserver', Server(
    use_debugger = True,
    use_reloader = True,
    host = application.config['HOST']
))

if __name__ == '__main__':
    manager.run()
