from viewpanel import db #why is this a circular dependency in the example???
import datetime as dt


''' ODM for Mongo, this is the sketch structure of the collections docs
'''

class Users(db.Document):
    """ User information document"""

    class OtherInfo(db.EmbeddedDocument):
        email_address = db.StringField(required=True)
        password = db.StringField(required=True)  
        admin = db.BooleanField(default=False)

    created = db.DateTimeField(required=True, default=dt.datetime.utcnow())
    userid = db.StringField(required=True)
    other_info = db.EmbeddedDocumentField(OtherInfo)


class Metrics(db.Document):
    """User and system performance metrics """
    class UserDataSeries(db.EmbeddedDocument):
        timestamp = db.DateTimeField(required=True, default=dt.datetime.utcnow())
        open_issues = db.IntField(min_value=0,required=True)
        closed_issues = db.IntField(min_value=0, required=True)
        worked_issues = db.IntField(min_value=0,required=True)

    user_dataseries = db.EmbeddedDocumentField(UserDataSeries)

    meta = {
        'ordering' : ['-user_dataseries.timestamp']
    }


class Issues(db.Document):
    """main issue collection"""

    class Comments(db.EmbeddedDocument):
        created = db.DateTimeField(required=True, default=dt.datetime.utcnow())
        comment = db.StringField(required=True)
        updated = db.DateTimeField(default=dt.datetime.utcnow())

    created = db.DateTimeField(required=True, default=dt.datetime.utcnow())
    closed = db.DateTimeField()
    comments = db.EmbeddedDocumentField(Comments)
    
    meta = {
        'ordering' : ['-created']
}
