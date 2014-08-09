import os
import sys
from flask.ext.script import Manager
from flask.ext.script import Server
from viewpanel import app

manager = Manager(app)

manager.add_command('start', Server(
    use_debugger = True,
    use_reloader = True,
    host = '192.168.15.101')
)

if __name__ == '__main__':
    manager.run()
