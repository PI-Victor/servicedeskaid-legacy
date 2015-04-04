from flask.ext.script import Manager
from flask.ext.script import Server
from viewpanel import app_factory
from viewpanel.collection import DEFAULTHOST


application = app_factory()
manager = Manager(application)

manager.add_command('runserver', Server(
    use_debugger = True,
    use_reloader = True,
    host = DEFAULTHOST,
))

if __name__ == '__main__':
    manager.run()
