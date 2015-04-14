#Test application and database settings

from flask import Flask
from servicedeskaid.app import app_factory

def test_app():
    app = app_factory()
    assert isinstance(app, Flask)
