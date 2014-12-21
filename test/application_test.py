'''Test application and database settings
'''

from flask import Flask
from viewpanel import db_factory
from viewpanel import app_factory

def test_app():
    app = app_factory()
    assert isinstance(app, Flask)


def test_db():
    db = db_factory()
    assert db is not None




