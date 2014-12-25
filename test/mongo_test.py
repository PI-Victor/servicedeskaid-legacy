'''Test insertion into the DB, save document, assert it's the document
inserted upon select and then delete the entry to avoid unwanted entries
'''


import random
import datetime as dt
from viewpanel.collection.models import Users, Issues, Metrics



def test_user_insert():
    user_rand = 'testuser_{}'.format(random.random())
    users = Users(
        userid=user_rand,
        email='victor@scifi.thecodeflavour.org',
        fullname='Administrator',
        password='123123',
        role = 'admin',
        full_name = 'Pi-Victor',
    )
    users.save()
    db_user = Users.objects(userid=user_rand).get()
    assert db_user.get_id() == users.get_id()
    users.delete()


def test_metrics_insert():
    metrics = Metrics(
        worked_issues=155055,
        open_issues=3,
        closed_issues=4,
    )
    metrics.save()
    resultset = Metrics.objects(worked_issues=155055).first()
    assert resultset.get_dataseries() == metrics.get_dataseries()
    metrics.delete()


def test_issues_insert():
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
    
    comment1 = Issues.Comments(
        userid = 'Victor123',
        fullname = 'Victor P',
        content = long_comment,
    )

    comment2 = Issues.Comments(
        userid = 'Victor12222',
        fullname = 'Victor P',
        content = long_comment,
    )
    
    issue = Issues(
        owner = 'Victor123',
        status = 'Open',
        severity = 'Critical',
        comments =  [comment1, comment2]
    )
    
    issue.save()
    resultset = Issues.objects(owner='Victor123').first()
    assert resultset.owner == issue.owner
    assert isinstance(resultset.comments, list)
    issue.delete()
