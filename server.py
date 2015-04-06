import logging

from flask.ext.script import Manager
from flask.ext.script import Server

from viewpanel.app import app_factory


application = app_factory()
manager = Manager(application)


#implement config based on what is passed as param

@manager.command
def runserver(environment):
    print(environment)
    Server(use_debugger = application.config['DEBUG'],
           use_reloader = application.config['RELOAD'],
           host = application.config['HOST'],
    )

if __name__ == '__main__':
    manager.run()
