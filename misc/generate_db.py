
'''generated bogus data and inserts into mongodb 
for testing
'''


import sys
import random
import os
import mongoengine
from viewpanel.collection.models import Users, Metrics, Issues

if len(sys.argv) < 2:
    print "You can send the number of records to be generated as parameter \n /
    Generating 10 records by default, you can run the script again and specify /
    the number of records then."
else:
    print "Generating {} of records"

try:
    records = int(sys.argv[1])
except Exception as e:
    print "Can not convert to int reverting to 10 records", e
    

def drop_db():
    dbdrop = raw_input("Do you want to drop the database? [y/n]")
    return [False, True][dbdrop == 'y']


def get_workdir():
    return os.path.dirname(os.path.realpath(__file__))


def insert_users():
    
    users = {
        'John': 'john@testcase.com' ,
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
    
    print "Generating users... "
    
    for person, email in users.items():
        genid = person+ str(random.randrange(9999))
        users = Users(
            userid=genid,
            email=email,
            password='testcase',
            role='user',
            fullname=person,
        )
        users.save()

def users_provider():
    user_list = []
    for user in Users.objects:
        user_list.append(user.userid)
        
    return user_list[random.randint(0, 9)]
        
        
def comments_provider():
    entry = 3
    lines = ''
    comments_file = os.path.join(
        os.path.sep,
        get_workdir(),
        'comments_data.txt'
    )
    
    user_comments = []
    try:
        comments = open(comments_file, 'r') 
        with comments :
            for line in comments:
                if entry == 0:
                    user_comments.append(
                        Issues.Comments(
                            userid = users_provider(),
                            user_name = 'testcase',
                            content = lines,
                            )
                    )
                    entry = 3
                    lines = ''
                else:
                    lines = "{} {}".format(lines, line)
                    entry -= 1
    except IOError as e:
        print "There was a problem opening the comments file! - {}".format(e)

    return user_comments
        
def insert_tickets():
    records = 10
    
    print "Generating {} ticket entries... ".format(records)
    
    issue_status = [
        'Open',
        'Pending',
        'Closed',
    ]
    issue_severity = [
        'Critical',
        'Medium',
        'Low',
    ]

    for i in xrange(records):
        generated_com = comments_provider()
        issues = Issues(
            owner = users_provider(),
            status = issue_status[random.randint(0, 2)],
            severity = issue_severity[random.randint(0, 2)],
            comments = generated_com
        )
        issues.save()

    print "[DONE] \n {} Records generated".format(records)

    
if __name__ == '__main__':
    if drop_db():
        print "Dropping the database"
        con = mongoengine.connect('deskdb')
        #using it because it's good to know
        db = mongoengine.connection._get_db()  
        db.connection.drop_database(db)
    else:
        print "Continuing as normal"
        
    insert_users()
    insert_tickets()
