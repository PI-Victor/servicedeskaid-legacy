from flask.ext.script import Manager
from flask.ext.script import Server
from viewpanel import app, db
from viewpanel.collection import views

manager = Manager(app)
manager.add_command('runserver',
                    Server(
                        use_debugger=True,
                        use_reloader=True,
                        host='127.0.0.1',)
                    )

if __name__ == '__main__':
    manager.run()
