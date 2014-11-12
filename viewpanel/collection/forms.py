from wtforms import Form, BooleanField, TextField, validators
from models import Users


class LoginForm(Form):
    username = TextField('Username'), [validators.Length(min=4, max=25)]
    password = TextField('Password'), [validators.Length(min=6, max=25)]
    email = TextField('Email Address'), [validators.Length(min=6, max=35)]
    remember = BooleanField('Remember me'), [validators.Required()]
    
    
