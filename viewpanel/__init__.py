import flask
import random
from flask.ext.mongoengine import MongoEngine


app = flask.Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'deskdb',
    'host': '127.0.0.1',
    'port': 27017
}

db = MongoEngine(app)

print dir(db)

@app.route('/')
def user_get():
    pass    

#users = Users(userid='testest {}'.format(random.randrange(111000)))
#users.save()



if __name__ == '__main__':
    app.run()
