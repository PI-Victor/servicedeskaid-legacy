''' ODM for Mongo, this is the sketch structure of the collections docs
'''
import datetime as dt
from viewpanel import db


class Users(db.Document):
    ''' User information document'''
    user_roles = (
        ('admin',1),
        ('user',2),
        ('reader',3),
    )
    email= db.EmailField(required=True)
    password = db.StringField(required=True)  
    role = db.StringField(
        choices=user_roles,
        required=True, 
        default=user_roles[2],
    )
    fullname = db.StringField(required=True)
    avatar = db.ImageField(size=(200, 200, True))
    created = db.DateTimeField(
        required=True, 
        default=dt.datetime.utcnow()
    )
    userid = db.StringField(
        required=True,
        unique=True,
    )
    
    def get_id(self):
        return self.userid
    
    meta = {
        'ordering': ['+userid'],
        'indexes': ['userid'],
    }


class Metrics(db.Document):
    '''User and system performance metrics'''
    timestamp = db.DateTimeField(
        required=True, 
        default=dt.datetime.utcnow(),
    )
    open_issues = db.IntField(
        min_value=0,
        required=True,
    )
    closed_issues = db.IntField(
        min_value=0,
        required=True,
    )
    worked_issues = db.IntField(
        min_value=0,
        required=True,
    )


    def get_dataseries(self):
        return {
            self.closed_issues,
            self.open_issues,
            self.worked_issues,
        }

    meta = {
        'ordering': ['+timestamp'],
        'indexes': ['timestamp']
    }


class Issues(db.Document):
    '''Issue information collection'''
    created = db.DateTimeField(
        required=True, 
        default=dt.datetime.utcnow(),
    )
    owner = db.StringField(required=True)
    status = db.StringField(
        required=True,
        default='Open',
    )
    severity = db.StringField(
        required=True,
        default='Low',
    )
    last_updated = db.ListField(
        db.DateTimeField(dt.datetime.utcnow())
    )
    closed = db.DateTimeField()

    class Comments(db.EmbeddedDocument):
        '''Comments embedded doc'''
        posted = db.DateTimeField(
            required=True, 
            default=dt.datetime.utcnow(),
        )
        userid = db.StringField(required=True)
        user_name = db.StringField(required=True)
        content = db.StringField(required=True)
        
    comments = db.ListField(db.EmbeddedDocumentField(Comments))
    
    meta = {
        'ordering': ['+created'],
    }
