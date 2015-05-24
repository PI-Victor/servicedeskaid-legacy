from flask.ext.wtf import Form
from wtforms import BooleanField, StringField
from wtforms import PasswordField, validators, TextField
from .models import Users


class LoginForm(Form):
    openid = StringField('openid', validators=[validators.DataRequired()])
    remember = BooleanField('remember', default=False)

class RegisterForm(Form):
    username = TextField('Username',
                         [validators.Length(min=4, max=25)])
    password = TextField('Password',
                         [validators.Length(min=6, max=25)])
    email = TextField('Email Address',
                      [validators.Length(min=6, max=35)])

    
class AddIssue(Form):
    description = TextField('issue',
                      [validators.Length(min=10, max=25)])
    
