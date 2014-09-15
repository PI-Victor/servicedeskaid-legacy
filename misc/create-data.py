from viewpanel.collection.models import Users, Metrics, Issues
import sys
import random

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
          'Julya': 'july@testcase',
          'Andrew': 'andrew@testcase.com', 
          'Jack': 'jack@testcase.com',
          'Mona': 'mona@testcase.com',
          'Maria': 'maria@testcase.com',
          'Derp': 'derp@testcase.com',
          'Liam': 'liam@testcase.com',
          'Jordan': 'jordan@testcase.com',
      }

    for person, email in users.items():
        genid = ''.join([person,'_',str(random.random())])
        info = Users.OtherInfo(email_address=email,
                               password='xAasfsdAsdfX12',)
        users = Users(userid=genid, other_infor=info)
        users.save()

insert_users()
