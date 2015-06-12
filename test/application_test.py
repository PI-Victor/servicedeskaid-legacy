from flask import Flask

from servicedeskaid import app_factory
from servicedeskaid.config import Testing


def test_app():
    app = app_factory(Testing)
    assert isinstance(app, Flask)
    assert app.import_name is 'servicedeskaid'
