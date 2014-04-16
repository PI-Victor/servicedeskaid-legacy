import flask

"""
Main view panel
"""
home = True

if home:
    ipaddress = '10.0.2.15'
else:
    ipaddress = '192.168.15.106'

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/timezones')
def timezones():
    return flask.render_template('flipclock.html')


if __name__ == '__main__':
    app.run(host=ipaddress, debug=True)
