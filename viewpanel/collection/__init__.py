import os



#environment paths
WORKDIR = os.path.join(os.path.sep, 
                       os.path.dirname(os.path.realpath(__file__)))
TMPDIR = os.path.join(os.path.sep, WORKDIR, 'tmp')
LOGDIR = os.path.join(os.path.sep, WORKDIR, 'log')


#mongodb settings
DESKDB = 'deskdb'
SECRETKEY = 't3st Patience'   #this should easy to configure 
DEFAULTHOST = '127.0.0.1'
