__author__ = 'vectra'
from flask import Flask

"""
Main viewpanel
"""

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


if __name__ == '__main__':
    app.run(host='10.0.2.15', debug=True)