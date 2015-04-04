

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
