import flask

app = flask.Flask(__name__)

"""
Main view panel
"""
home = False

if home:
    ipaddress = '192.168.15.106'
else:
    ipaddress = '10.0.2.15'


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/timezones')
def timezones():
    return flask.render_template('flipclock.html')



if __name__ == '__main__':
    app.run(host=ipaddress, debug=True)

