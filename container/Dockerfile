#Opensuse deployment environment for Service Desk Aid

#checkout the official opensuse image for now
#has to be replaced by a build with basic packages for suse

#docker repository file @  https://registry.hub.docker.com/u/codeflavour/docker-suse/dockerfile/

FROM opensuse

MAINTAINER Victor@htttp://github.com/p-victor

#add mongod and install dep for virtualenv & co
RUN zypper ar http://download.opensuse.org/repositories/server:database/openSUSE_13.1/server:database.repo
RUN zypper --no-gpg-check ref
RUN zypper --non-interactive --no-gpg-checks up -y
RUN zypper --non-interactive in gcc python-devel python-virtualenv python-pip uwsgi nginx mongodb
#create & make the data dir writable for mongodb user
RUN mkdir -p /data/db
RUN chown mongodb /data/db

#open port for connections
EXPOSE 27017


#CMD['/']
