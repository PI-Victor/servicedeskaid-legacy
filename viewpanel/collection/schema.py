import mongoengine
import datetime as dt


class Users(mongoengine.Document):

    class OtherInfo(mongoengine.EmbeddedDocument):
        email_address = mongoengine.StringField(required=True)
        password = mongoengine.StringField(required=True)  
        admin = mongoengines.BoolField(default=False)

    created = mongoengine.DateTimeField(required=False, default=dt.datetime.utcnow())
    userid = mongoengine.StringField(required=True)
    other_info = mongoengine.EmbeddedDocumentField(OtherInfo)


class Metrics(mongoengine.Document):

    class UserDataSeries(mongoengine.EmbeddedDocument):
        timestamp = db.fields.DateTimeField(required=True, default=dt.datetime.utcnow())
        open_issues = db.fields.IntField(min_value=0,required=True)
        closed_issues = db.fields.IntField(min_value=0, required=True)
        worked_issues = db.fields.IntField(min_value=0,required=True)

    user_dataseries = mongoengine.EmbeddedDocumentField(UserDataSeries)
