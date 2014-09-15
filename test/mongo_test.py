from viewpanel.collection.models import Users, Issues, Metrics

import datetime as dt
import random

long_comment = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem " \
               "accusantium doloremque laudantium, totam rem aperiam, eaque ipsa " \
               "quae ab illo inventore veritatis et quasi architecto beatae vitae " \
               "dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit " \
               "aspernatur aut odit aut fugit, sed quia consequuntur magni dolores " \
               "eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, " \
               "qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, " \
               "sed quia non numquam eius modi tempora incidunt ut labore et dolore " \
               "magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis " \
               "nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut " \
               "aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit " \
               "qui in ea voluptate velit esse quam nihil molestiae consequatur, " \
               "vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"


def test_user_insert():
    """ """
    otherinfo = Users.OtherInfo(email_address='victor@scifi.thecodeflavour.org',
                                password='123123')
    user_rand = 'testuser_{}'.format(str(random.random()))
    users_doc = Users(userid=user_rand,
                      other_info=otherinfo,
                      timestamp=dt.datetime.utcnow())
    users_doc.save()
    db_user = Users.objects(userid=user_rand).first()
    assert db_user.get_id() == users_doc.get_id()
#    users_doc.remove()


def test_metrics_insert():
    usermetrics = Metrics.UserDataSeries(timestamp=dt.datetime.utcnow(),
                                         worked_issues=1,
                                         open_issues=3,
                                         closed_issues=4)
    metrics_doc = Metrics(user_dataseries=usermetrics)
    metrics_doc.save()
    user_resultset = Metrics.objects(user_dataseries=usermetrics).first()
    assert user_resultset.get_dataseries() == metrics_doc.get_dataseries()


def test_issues_insert():
    test_comments = Issues.Comments(created=dt.datetime.utcnow(),
                                    comment=long_comment)
    issues_test = Issues(comments=test_comments)
    issues_test.save()
    issues_resultset = Issues(comments=test_comments)
    assert issues_test
