from wtforms import Form, BooleanField, TextField, PasswordField, validators
from models import Users


class LoginForm(Form):
    loginname = TextField('Username', [validators.Length(min=4, max=25)])
    loginpass = PasswordField('New Password', [validators.Required()])
    remember = BooleanField('Remember me') 
    
class RegisterForm(Form):
    username = TextField('Username'), [validators.Length(min=4, max=25)]
    password = TextField('Password'), [validators.Length(min=6, max=25)]
    email = TextField('Email Address'), [validators.Length(min=6, max=35)]
