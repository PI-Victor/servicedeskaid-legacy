from viewpanel.collection.models import Users, Issues, Metrics
import datetime as dt
import random

from viewpanel import db_factory

"""Test insertion into the DB, save document, assert it's the document
inserted upon select and then delete the entry to avoid unwanted entries
"""

def test_db():
    db = db_factory()
    assert db is not None


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
    user_rand = 'testuser_{}'.format(str(random.random()))
    users = Users(userid=user_rand,
                  email='victor@scifi.thecodeflavour.org',
                  fullname='Administrator',
                  password='123123',
                  role = 'admin',
                  full_name = 'test1',
              )
    users.save()
    db_user = Users.objects(userid=user_rand).get()
    assert db_user.get_id() == users.get_id()
    users.delete()


def test_metrics_insert():
    metrics = Metrics(worked_issues=155055,
                      open_issues=3,
                      closed_issues=4)
    metrics.save()
    resultset = Metrics.objects(worked_issues=155055).first()
    assert resultset.get_dataseries() == metrics.get_dataseries()
    metrics.delete()


def test_issues_insert():
    comments = Issues.Comments(comment=long_comment)
    issues = Issues(comments=comments)
    issues.save()
    resultset = Issues.objects(comments=comments).first()
    assert issues.comments.comment == resultset.comments.comment
    issues.delete()
