import datetime as dt


'''
Uses flask-mongokit
must have mongodb installed:

Installing MongoDb on OpenSuse 13.1
    zypper addrepo http://download.opensuse.org/repositories/server:database/openSUSE_13.1/server:database.repo
    zypper refresh
    zypper install mongodb

Document Structure:
'''

class Users(db.Document):
    __


class UserData(mk.Document):
    __database__ = 'deskdb'
    __collection__ = 'userdata'

    structure = {
        '_id': basestring,
        'timestamp': dt.datetime,
        'userid': basestring,
        'detailed': {'email_address': basestring,
                     'password': basestring,
                     'admin': bool, }
    }

    required_fields = ['_id',
                       'detailed.email_address',
                       'detailed.password'
                       'userid', ]

    indexes = [{'fields': '_id'},
               {'fields': 'timestamp'}]

    default_values = {'timestamp': dt.datetime.utcnow, 'detailed.admin': 'False'}
