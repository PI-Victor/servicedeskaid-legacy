import datetime as dt
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


class Users(Document):
    __database__ = 'deskdb'
    __collection__ = 'userdata'

    timestamp = ma.DateTimeField()
    admin = ma.BoolField()
    userid = ma.StringField()
    email_address = ma.StringField()
    password = ma.StringField() #TODO : have to see if there's a different type of field to use for encr



# class UserData(mk.Document):
#     __database__ = 'deskdb'
#     __collection__ = 'userdata'
l
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
