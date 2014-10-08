from viewpanel.collection.models import Users, Metrics, Issues
import sys
import random
import mongoengine

'''generated bogus data and inserts into monbodb 
to make testing easier
'''

records = 1000 #default number of records to be inserted

if len(sys.argv) == 2 and type(sys.argv[1]):
    try:
        records = int(sys.argv[1])
    except:
        print "Not an integer switching to default no of entries: " + str(records)

print "Inserting {}  of records into the database".format(str(records))


def insert_users():

    users = { 'John': 'john@testcase.com' ,
          'Anna': 'anna@testcase.com',
          'Julya': 'july@testcase.com',
          'Andrew': 'andrew@testcase.com', 
          'Jack': 'jack@testcase.com',
          'Mona': 'mona@testcase.com',
          'Maria': 'maria@testcase.com',
          'Derp': 'derp@testcase.com',
          'Liam': 'liam@testcase.com',
          'Jordan': 'jordan@testcase.com',
      }

    for person, email in users.items():
        genid = person+ str(random.randrange(9999))
        info = Users.OtherInfo(email_address=email,
                               password='testcase',
                               role='user',
                               full_name=person
        )
        users = Users(userid=genid, other_info=info)
        users.save()
    
#    for issue in range(records):

def drop_db():
    dbdrop = raw_input("Do you want to drop the database? [y/n]")
    return [False, True][dbdrop == 'y']

if drop_db():
    print "Dropping the database"
    con = mongoengine.connect('deskdb')
    db = mongoengine.connection._get_db()  #using it because it's good to know
    db.connection.drop_database(db)
else:
    print "Continuing as normal"

insert_users()