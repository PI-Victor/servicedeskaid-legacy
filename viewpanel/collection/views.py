import flask
import jinja2
from flask.views import MethodView
from viewpanel.collection.schema import Users


login_page = flask.Blueprint('login_page', __name__, template_folder='templates')


#@login_page.route('/login', defaults={'page': 'login'})
@login_page.route('/<page>')
def show(page):
    try:
        return flask.render_template('pages/%s.html' % page)
    except jinja2.TemplateNotFound:
        flask.abort(404)


# @app.route('/login', methods=['GET', 'POST'])
# def user_login():
#     form = formvalid.LoginForm(flask.request.form)
#     if flask.request.method == 'POST':
#         if form.validate():
#             if user_validate(flask.request.form['loginname'], flask.request.form['loginpass']):
#                 return flask.render_template('viewpanel.html')
#         else:
#             flask.flash("Invalid chars in the login")
#     else:
#         return flask.render_template('login.html')
#
# @app.route('/')
# def index():
#     return flask.render_template('index.html')
#
# @app.route('/viewpanel')
# def viewpanel():
#     return flask.render_template('viewpanel.html')
#
# @app.route('/graphs')
# def graphing():
#     gr.generate_graph()
#     return flask.render_template('graphs.html')
#
# @app.route('/timezones')
# def timezones():
#     return flask.render_template('flipclock.html')
#
#
# #leave this messy mess here for now, just need basic login no computer science
# def user_validate(user,password):
#     print "i got here"
#     if Users.objects(userid=user):
#         print Users.userid
