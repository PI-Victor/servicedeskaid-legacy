import flask
from collection import graphing as gr
from collection import formvalid
from flask.ext.mongoengine import MongoEngine

app = flask.Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'db': 'deskdb'}  # have to create config for the application
db = MongoEngine(app)


def register_blueprints(app):
    from viewpanel.collection.views import login
    app.register_blueprint(login)

register_blueprints(app)

if __name__ == '__main__':
    app.run()