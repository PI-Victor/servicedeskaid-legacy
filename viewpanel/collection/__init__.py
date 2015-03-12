import os
from . import *
import socket

#check to see if we are running a linked container mongodb 
ckdbport = os.getenv("MONGODB_PORT_27017_TCP_PORT")
ckdbhost = os.getenv("MONGODB_PORT_27017_TCP_ADDR")
ckbindip = os.getenv("BINDIP") 
#environment paths
WORKDIR = os.path.join(os.path.sep,
                      os.path.dirname(os.path.realpath(__file__)))
TMPDIR = os.path.join(os.path.sep, WORKDIR, 'tmp')
LOGDIR = os.path.join(os.path.sep, WORKDIR, 'log')
#mongodb settings
DBNAME = 'deskdb'
SECRETKEY = 't3st Patience'   #this should easy to configure 

#use a temporary workaround for docker container binding
if ckbindip is None:
    try:
        DEFAULTHOST = ([(s.connect(('8.8.8.8', 80)), s.getsockname()[0],
                         s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
    except socket.error as e:
        DEFAULTHOST = '127.0.0.1'
else:
    DEFAULTHOST = ckbindip

if ckdbhost is None:
    DBHOST = '127.0.0.1'
    DBPORT = 27017
else:
    DBHOST = ckdbhost
    DBPORT = int(ckdbport)

