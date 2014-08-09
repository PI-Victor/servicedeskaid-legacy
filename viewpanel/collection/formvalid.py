import wtforms


class LoginForm(wtforms.Form):
    loginname = wtforms.StringField('loginname', [wtforms.validators.Length(min=4, max=25),
                                  wtforms.validators.DataRequired()])
    loginpass = wtforms.PasswordField('loginpass', [wtforms.validators.DataRequired()])
