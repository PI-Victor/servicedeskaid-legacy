from viewpanel import app_factory
from flask import Flask


def test_app():
    app = app_factory()
    assert isinstance(app, Flask)




