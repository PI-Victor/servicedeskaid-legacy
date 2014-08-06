import wtforms


class LoginForm(wtforms.Form):
    loginname = wtforms.TextField('loginname', [wtforms.validators.Length(min=4, max=25),
                                  wtforms.validators.Required()])
    loginpass = wtforms.PasswordField('loginpass', [wtforms.validators.Required()])
