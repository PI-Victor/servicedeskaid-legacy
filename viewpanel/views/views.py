from flask import g, request, render_template, flash, abort, redirect, url_for
from flask.ext.login import login_user, curent_user
from forms import LoginForm
from viewpanel import pages
from viewpanel.collection.models import Users 
from viewpanel import loginman, opid


@lm.user_loader
def load_user(id):
    try:
        user = Users.objects(userid=user, password=password).get()
    except Users.DoesNotExist as err:
        user = False
        
    return user

@app.before_request
def before_request():
    g.user= current_user
