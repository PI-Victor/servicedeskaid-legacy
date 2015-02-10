#Opensuse deployment environment for Service Desk Aid

#checkout the official opensuse image for now
#has to be replaced by a build with basic packages for suse

FROM opensuse

MAINTAINER Victor@http://github.com/pi-victor

#add mongod and install dep for virtualenv & co
RUN zypper ar http://download.opensuse.org/repositories/server:database/openSUSE_13.1/server:database.repo
RUN zypper --no-gpg-check ref
RUN zypper --non-interactive --no-gpg-checks up -y
RUN zypper --non-interactive in gcc libopenssl0_9_8 libsnmp30 net-snmp snmp-mibs cyrus-sasl \
    	   		     cyrus-sasl-gssapi python-devel python-virtualenv python-pip mongodb

#create & make the data dir writable for mongodb user
RUN mkdir -p /data/db
RUN chown mongodb /data/db

#you can mount a host dir as a volume inside docker with this
#VOLUME [""]

#defines the working directory
WORKDIR /data

EXPOSE 27017

# Define default command.
CMD ["mongod", "--noprealloc"]
