from viewpanel.collection.schema import Users
import datetime as dt


def test_user_insert():

    otherinfo = Users.OtherInfo(email_address='ip545k@intl.att.com',
                                password='123123')

    users_doc = Users(userid='vectra',
                      other_info=otherinfo,
                      timestamp=dt.datetime.utcnow())
    users_doc.save()
    db_user = Users.query.filter(Users.userid == 'vectra').first()
    assert db_user.userid == users_doc.userid
    users_doc.remove()