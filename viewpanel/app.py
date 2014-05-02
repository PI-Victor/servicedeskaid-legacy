import flask
from collection.schema import SessionHandler as Sh


home = True

app = flask.Flask(__name__)

app.config['MONGOALCHEMY_DATABASE'] = 'deskdb'
app.config['DEBUG'] = True
app.config['HOST'] = '192.168.15.107' if home else '10.0.2.15'


session_handler = Sh(app)


#
#
# if home:
#     ipaddress = '192.168.15.107'
# else:
#     ipaddress = '10.0.2.15'


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/timezones')
def timezones():
    return flask.render_template('flipclock.html')



if __name__ == '__main__':
    app.run()

