import flask
from mongoengine import register_connection
from viewpanel.collection.schema import Users

app = flask.Flask(__name__)
db = register_connection('deskdb', app)


users = Users(userid='testest')
users.save()



if __name__ == '__main__':
    app.run()
