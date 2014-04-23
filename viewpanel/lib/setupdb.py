import mongokit as mk

'''
Uses flask-mongokit
must have mongodb installed:

Installing MongoDb on OpenSuse 13.1
    zypper addrepo http://download.opensuse.org/repositories/server:database/openSUSE_13.1/server:database.repo
    zypper refresh
    zypper install mongodb

Document Structure:
'''


class UserData(mk.Document):
    __database__ = 'servdeskdb'
    __collection__ = 'userdata'

    structure = {
        '_id': basestring,
        'userid': basestring,
        'detailed': {
                        'email_adress' : basestring,
                        'password': basestring,
                        'admin' : bool,
        }
    }