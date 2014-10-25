from flask.ext.script import Manager
from flask.ext.script import Server
from viewpanel import app, db
from viewpanel.collection import views, DEFAULTHOST



manager = Manager(app)
application = app

manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host=DEFAULTHOST,
))

if __name__ == '__main__':
    manager.run()

