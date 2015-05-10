from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


# TODO :Remember to change column data types accordingly


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    fullname = Column(String)
    email = Column(String)
    role = Column(String)
    avatar = Column(String)

    def __init__(self, username, fullname):
        self.username = username
        self.fullname = fullname

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def is_authenticated(self):
        return True

    def is_activete(self):
        return True

    def is_anonymous(self):
        return False


class Issues(Base):
    __tablename__ = 'issues'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer)
    opened = Column(String)
    closed = Column(String)


class Updates(Base):
    __tablename__ = 'updates'
    """This should be a json object under issues, that has
    just multiple entries for each time a user updates an issue.
    """

    id = Column(Integer, primary_key=True)
    id_issue = Column(Integer)
    comment = Column(String)

# keep old mongodb structure for reference.
"""
class Users(db.Document):
    ''' User information document'''
    user_roles = (
        ('admin',1),
        ('user',2),
        ('reader',3),
    )
    email= db.EmailField(required=True)
    password = db.StringField(required=True)  
    role = db.StringField(
        choices=user_roles,
        required=True, 
        default=user_roles[2],
    )
    fullname = db.StringField(required=True)
    avatar = db.ImageField(size=(200, 200, True))
    created = db.DateTimeField(
        required=True, 
        default=dt.datetime.utcnow()
    )
    userid = db.StringField(
        required=True,
        unique=True,
    )
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.userid
    
    meta = {
        'ordering': ['+userid'],
        'indexes': ['userid'],
    }


class Metrics(db.Document):
    '''User and system performance metrics'''
    timestamp = db.DateTimeField(
        required=True, 
        default=dt.datetime.utcnow(),
    )
    open_issues = db.IntField(
        min_value=0,
        required=True,
    )
    closed_issues = db.IntField(
        min_value=0,
        required=True,
    )
    worked_issues = db.IntField(
        min_value=0,
        required=True,
    )

    def get_dataseries(self):
        return {
            self.closed_issues,
            self.open_issues,
            self.worked_issues,
        }

    meta = {
        'ordering': ['+timestamp'],
        'indexes': ['timestamp'],
    }


class Issues(db.Document):
    '''Issue information collection'''
    created = db.DateTimeField(
        required=True, 
        default=dt.datetime.utcnow(),
    )
    owner = db.StringField(required=True)
    status = db.StringField(
        required=True,
        default='Open',
    )
    severity = db.StringField(
        required=True,
        default='Low',
    )
    last_updated = db.ListField(
        db.DateTimeField(dt.datetime.utcnow())
    )
    closed = db.DateTimeField()
    
    class Comments(db.EmbeddedDocument):
        '''Comments embedded doc'''
        posted = db.DateTimeField(
            required=True, 
            default=dt.datetime.utcnow(),
        )
        userid = db.StringField(required=True)
        fullname = db.StringField(required=True)
        content = db.StringField(required=True)
        
    comments = db.ListField(db.EmbeddedDocumentField(Comments))
    
    meta = {
        'ordering': ['+created'],
        'indexes': ['created'],
    }


class Customers(db.Document):
    '''Holds the client data'''
    customerid = db.StringField(required=True)
    name = db.StringField(required=True)
    #could use tel for identifying a customer
    telephone = db.StringField(required=True)
    email= db.EmailField(required=True)
    address = db.StringField(required=True)
    contractno = db.StringField(required=True)
    other_info = db.StringField(required=True)
    
    meta = {
        'ordering': ['+customerid'],
        'indexes': ['customerid'],
    }
"""
