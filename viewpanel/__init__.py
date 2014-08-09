import flask
#from collection.schema import Users
from collection import graphing as gr
from collection import formvalid
from flask.ext.mongoengine import MongoEngine

home = True

app = flask.Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'db': 'deskdb',  'host': '192.168.15.101'}
db = MongoEngine(app)


def register_blueprints(app):
    from viewpanel.collection.views import login
    app.register_blueprint(login)

register_blueprints(app)

if __name__ == '__main__':
    app.run()


