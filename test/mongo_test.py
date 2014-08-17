from viewpanel.collection.schema import Users, Metrics
from mongoengine import connect
import datetime as dt
import random

connection = connect('deskdb')


def test_user_insert():
    """ """
    otherinfo = Users.OtherInfo(email_address='victor@scifi.thecodeflavour.org',
                                password='123123')
    user_rand = ''.join(['vectra_', str(random.random())])
    users_doc = Users(userid=user_rand,
                      other_info=otherinfo,
                      timestamp=dt.datetime.utcnow())
    users_doc.save()
    db_user = Users.objects(userid=user_rand).first()
    assert db_user == users_doc
#    users_doc.remove()


def test_metrics_insert():
    usermetrics = Metrics.UserDataSeries(timestamp=dt.datetime.utcnow(),
                                         worked_issues=1,
                                         open_issues=3,
                                         closed_issues=4)
    metrics_doc = Metrics(user_dataseries=usermetrics)
    metrics_doc.save()

    user_resultset = Metrics.objects().first()
    assert user_resultset.user_dataseries.worked_issues == usermetrics.worked_issues

