import flask
from collection.schema import SessionHandler as Sh
from flask.ext.login import LoginManager
from collection.schema import Users

home = True

app = flask.Flask(__name__)

#TODO have to move the below to a config file later on
app.config['MONGOALCHEMY_DATABASE'] = 'deskdb'
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '!b@n@n@s are very ch3ap!'
app.config['IPADRESS'] = ['10.0.2.15', '192.168.15.106'][home]


session_handler = Sh().bind_to_app(app)


login_manager = LoginManager()

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if flask.request.method == 'GET':
        return flask.render_template('login.html')
    user_name = flask.request.form['login-username']
    user_pass = flask.request.form['login-password']
    user_remember = flask.request.formp['login-remember']
    results = session_handler.query(Users)
    print results



@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/timezones')
def timezones():
    return flask.render_template('flipclock.html')


if __name__ == '__main__':
    app.run(host=app.config['IPADRESS'], debug=app.config['DEBUG'])

