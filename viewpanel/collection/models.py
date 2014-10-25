import datetime as dt
from viewpanel import db


''' ODM for Mongo, this is the sketch structure of the collections docs
'''


class Users(db.Document):
    """ User information document"""

    class OtherInfo(db.EmbeddedDocument):
        roles = (('admin',1), ('user',2), ('reader',3))
        email_address = db.EmailField(required=True)
        password = db.StringField(required=True)  
        role = db.StringField(choices=roles, required=True, 
                              default=roles[2])
        full_name = db.StringField(required=True)
        avatar = db.ImageField(size=(200, 200, True))

    created = db.DateTimeField(required=True, 
                               default=dt.datetime.utcnow())
    userid = db.StringField(required=True, unique=True)
    other_info = db.EmbeddedDocumentField(OtherInfo)
    
    def is_active(self):
        return True
    
    def get_id(self):
        return self.userid

    def __repr__(self):
        return self.userid
    
    meta = {
        'ordering': ['+userid'],
        'indexes': ['userid'],
    }


class Metrics(db.Document):
    """User and system performance metrics """

    class UserDataSeries(db.EmbeddedDocument):
        timestamp = db.DateTimeField(required=True, 
                                     default=dt.datetime.utcnow())
        open_issues = db.IntField(min_value=0, required=True)
        closed_issues = db.IntField(min_value=0, required=True)
        worked_issues = db.IntField(min_value=0, required=True)

    user_dataseries = db.EmbeddedDocumentField(UserDataSeries)

    def get_dataseries(self):
        return {self.UserDataSeries.timestamp,
                self.UserDataSeries.closed_issues,
                self.UserDataSeries.open_issues,
                self.UserDataSeries.worked_issues, }

    meta = {
        'ordering': ['+user_dataseries.timestamp'],
        'indexes': ['user_dataseries.timestamp']
    }


class Issues(db.Document):
    """Issue information collection"""
    
    created_by = db.StringField(required=False) #required=True)
    status = db.StringField(required=True, default='Open')
    severity = db.StringField(required=True, default='Low')

    class Comments(db.EmbeddedDocument):
        created = db.DateTimeField(required=True, 
                                   default=dt.datetime.utcnow())
        comment = db.StringField(required=True)
        last_updated = db.ListField(db.DateTimeField())
        closed = db.DateTimeField()
    
    created = db.DateTimeField(required=True, 
                               default=dt.datetime.utcnow())
    comments = db.EmbeddedDocumentField(Comments)
    
    meta = {
        'ordering': ['+created'],
    }
