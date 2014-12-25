'''Test application and database settings
'''

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from viewpanel import db
from viewpanel import app


def test_app():
    assert isinstance(app, Flask)


def test_db():
    assert db is not None
    assert isinstance(db, MongoEngine)
