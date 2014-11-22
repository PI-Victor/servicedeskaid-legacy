from flask.ext.script import Manager
from flask.ext.script import Server
from viewpanel import app_factory
from viewpanel.collection import views, DEFAULTHOST



app, application = app_factory()
manager = Manager(app)


manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host=DEFAULTHOST,
))

if __name__ == '__main__':
    manager.run()

