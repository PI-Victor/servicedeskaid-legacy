import flask.ext.mongoalchemy as ma

'''
Uses flask-mongokit
must have mongodb installed:

Installing MongoDb on OpenSuse 13.1
    zypper addrepo http://download.opensuse.org/repositories/server:database/openSUSE_13.1/server:database.repo
    zypper refresh
    zypper install mongodb

Document Structure:
'''


class SessionHandler(object):
    """
    CRUD Session base
    """
    def bind_to_app(self, app_obj):
        return ma.MongoAlchemy(app_obj)


class UsersQuery(ma.BaseQuery):

    def with_id(self, userid):
        pass


class Users(ma.Document):
    query_class = UsersQuery

    class OtherInfo(ma.Document):
        email_address = ma.fields.StringField()
        password = ma.fields.StringField() #TODO : have to see if there's a different type of field to use for encr
        admin = ma.fields.BoolField(default=False)

    timestamp = ma.fields.DateTimeField()
    userid = ma.fields.StringField()
    other_info = ma.fields.DocumentField(OtherInfo)


# class UserData(mk.Document):
#     __database__ = 'deskdb'
#     __collection__ = 'userdata'
#     structure = {
#         '_id': basestring,
#         'timestamp': dt.datetime,
#         'userid': basestring,
#         'detailed': {'email_address': basestring,
#                      'password': basestring,
#                      'admin': bool, }
#     }

#     required_fields = ['_id',
#                        'detailed.email_address',
#                        'detailed.password'
#                        'userid', ]

#     indexes = [{'fields': '_id'},
#                {'fields': 'timestamp'}]

#     default_values = {'timestamp': dt.datetime.utcnow, 'detailed.admin': 'False'}
