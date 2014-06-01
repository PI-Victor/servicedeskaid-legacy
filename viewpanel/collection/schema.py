from viewpanel import session_handler as db
from flask.ext.mongoalchemy import BaseQuery
import datetime as dt


class UsersQuery(BaseQuery):

    def user_auth(self, login_username, user_password):
        return self.filter(self.type.userid == login_username, self.type.password == user_password)


class Users(db.Document):
    config_collection_name = 'Users'
    query_class = UsersQuery

    class OtherInfo(db.Document):
        email_address = db.fields.StringField(required=True)
        password = db.fields.StringField()  # TODO : have to see if there's a different type of field to use for encr
        admin = db.fields.BoolField(default=False)
        put = db.fields.StringField(default='entry')

    timestamp = db.fields.DateTimeField(required=False, default=dt.datetime.utcnow())
    userid = db.fields.StringField(required=True)
    other_info = db.DocumentField(OtherInfo)
