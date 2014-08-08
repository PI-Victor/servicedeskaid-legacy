import mongoengine
import datetime as dt


class Users(db.Document):

    class OtherInfo(mongoengine.EmbeddedDocument):
        email_address = mongoengine.StringField(required=True)
        password = mongoengine.StringField(required=True)  
        admin = mongoengine.BooleanField(default=False)

    created = mongoengine.DateTimeField(required=False, default=dt.datetime.utcnow())
    userid = mongoengine.StringField(required=True)
    other_info = mongoengine.EmbeddedDocumentField(OtherInfo)


class Metrics(db.Document):

    class UserDataSeries(mongoengine.EmbeddedDocument):
        timestamp = mongoengine.DateTimeField(required=True, default=dt.datetime.utcnow())
        open_issues = mongoengine.IntField(min_value=0,required=True)
        closed_issues = mongoengine.IntField(min_value=0, required=True)
        worked_issues = mongoengine.IntField(min_value=0,required=True)

    user_dataseries = mongoengine.EmbeddedDocumentField(UserDataSeries)

    meta = {
        'ordering' : ['-user_dataseries.timestamp']
    }
