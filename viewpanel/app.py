import flask
from collection.schema import SessionHandler as Sh


home = True

app = flask.Flask(__name__)

#TODO have to move the below to a config file later on
app.config['MONGOALCHEMY_DATABASE'] = 'deskdb'
app.config['DEBUG'] = False
app.config['SECRET_KEY'] = '!b@n@n@s are very ch3ap!'
ipaddress = ['10.0.2.15', '192.168.15.107'][home]


session_handler = Sh().bind_to_app(app)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/timezones')
def timezones():
    return flask.render_template('flipclock.html')


if __name__ == '__main__':
    app.run(host=ipaddress)
    print dir(app)

