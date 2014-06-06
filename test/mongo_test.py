from viewpanel.collection.schema import Users, Metrics
import datetime as dt


def test_user_insert():

    otherinfo = Users.OtherInfo(email_address='ip545k@intl.att.com',
                                password='123123')
    # TODO : somehow the test fails if not all the fields are added - timestamp is a default field
    users_doc = Users(userid='vectra',
                      other_info=otherinfo,
                      timestamp=dt.datetime.utcnow())
    users_doc.save()
    db_user = Users.query.filter(Users.userid == 'vectra').first()
    assert db_user.userid == users_doc.userid
    users_doc.remove()


def test_metrics_insert():

    usermetrics = Metrics.UserDataSeries(timestamp=dt.datetime.utcnow(),
                                         worked_issues=30,
                                         opened_issues=20,
                                         closed_issues=50,)
    osmetrics = Metrics.OsDataSeries(timestamp=dt.datetime.utcnow(),
                                     cpu_usage=30.2,
                                     virtual_mem=50,
                                     swap_memory=30,)

    metrics_doc = Metrics(user_dataseries=usermetrics, os_dataseries=osmetrics)
    metrics_doc.save()
    result_set = Metrics.query.filter(Metrics.UserDataSeries.timestamp == usermetrics.timestamp).first()
    assert result_set == usermetrics
