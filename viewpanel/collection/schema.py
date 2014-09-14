import datetime as dt
from mongoengine import *

''' ODM for Mongo, this is the sketch structure of the collections docs
'''

class Users(Document):
    """ User information document"""

    class OtherInfo(EmbeddedDocument):
        roles = (('admin', 1),
                 ('user', 2),
                 ('reader', 3))
        email_address = EmailField(required=True)
        password = StringField(required=True)  
        role = IntField(choices=roles)
        avatar = ImageField(size=(200, 200, True))

    created = DateTimeField(required=True, default=dt.datetime.utcnow())
    userid = StringField(required=True, unique=True)
    other_info = EmbeddedDocumentField(OtherInfo)
    
    def is_active(self):
        return True
    
    def get_id(self):
        return self.userid

    def __repr__(self):
        return self.userid
    
    meta = {'ordering': ['+userid'],
            'indexes': ['userid']
    }


class Metrics(Document):
    """User and system performance metrics """

    class UserDataSeries(EmbeddedDocument):
        timestamp = DateTimeField(required=True, default=dt.datetime.utcnow())
        open_issues = IntField(min_value=0, required=True)
        closed_issues = IntField(min_value=0, required=True)
        worked_issues = IntField(min_value=0, required=True)

    user_dataseries = EmbeddedDocumentField(UserDataSeries)

    meta = {'ordering': ['+user_dataseries.timestamp']}


class Issues(Document):
    """Issue information collection"""

    class Comments(EmbeddedDocument):
        created = DateTimeField(required=True, default=dt.datetime.utcnow())
        comment = StringField(required=True)
        updated = DateTimeField(default=dt.datetime.utcnow())
        closed = DateTimeField(default=dt.datetime.utcnow())

    created = DateTimeField(required=True, default=dt.datetime.utcnow())
    comments = EmbeddedDocumentField(Comments)
    
    meta = {
        'ordering': ['+created']
    }
