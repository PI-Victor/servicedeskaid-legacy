import os
from . import *


#check to see if we are running a linked container mongodb 
ckdbhost = os.getenv("MONGODB_PORT_27017_TCP")

#environment paths
WORKDIR = os.path.join(os.path.sep,
                      os.path.dirname(os.path.realpath(__file__)))
TMPDIR = os.path.join(os.path.sep, WORKDIR, 'tmp')
LOGDIR = os.path.join(os.path.sep, WORKDIR, 'log')
#mongodb settings
DBNAME = 'deskdb'
SECRETKEY = 't3st Patience'   #this should easy to configure 
DEFAULTHOST = '127.0.0.1'

if ckdbhost is None:
    DBHOST = '127.0.0.1'
else:
    DBHOST = ckdbhost

DBPORT = 27017
