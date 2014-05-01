from lib import app
import flask
"""
Main view panel
"""
home = True

if home:
    ipaddress = '192.168.15.106'
else:
    ipaddress = '10.0.2.15'


@app.route('/')
def index():
    return flask.render_template('/templates/index.html')


@app.route('/timezones')
def timezones():
    return flask.render_template('/templates/flipclock.html')



if __name__ == '__main__':
    app.run(host=ipaddress, debug=True)
