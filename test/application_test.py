#Test application and database settings

from flask import Flask

from servicedeskaid.app import app_factory
from servicedeskaid.config import config


def test_app():
    app = app_factory(config.Testing)
    assert isinstance(app, Flask)
