from viewpanel.collection.schema import Users, Metrics
import datetime as dt


def test_user_insert():

    otherinfo = Users.OtherInfo(email_address='victor@scifi.thecodeflavour.org',
                                password='123123')
    # TODO : somehow the test fails if not all the fields are added - timestamp is a default field
    users_doc = Users(userid='vectra',
                      other_info=otherinfo,
                      timestamp=dt.datetime.utcnow())
    users_doc.save()
    db_user = Users.query.filter(Users.userid == 'vectra').first()
    assert db_user.userid == users_doc.userid
#    users_doc.remove()


def test_metrics_insert():
    usermetrics = Metrics.UserDataSeries(timestamp=dt.datetime.utcnow(),
                                         worked_issues=0,
                                         open_issues=0,
                                         closed_issues=0)

#    osmetrics = Metrics.OsDataSeries(timestamp=dt.datetime.utcnow(),
#                                     cpu_usage=0,
#                                     virtual_mem=0,
#                                     swap_memory=0)
    
    metrics_doc = Metrics(user_dataseries=usermetrics)
    metrics_doc.save()
    user_resultset = Metrics.query.filter(Metrics.UserDataSeries.timestamp == usermetrics.timestamp).limit(1)
#    os_resultset = Metrics.query.filter(Metrics.OsDataSeries.timestamp == osmetrics.timestamp).first()
    assert user_resultset.timestamp == usermetrics.timestamp
#    assert os_resultset == osmetrics
