#servicedesk aid git cloning

FROM centos:latest

MAINTAINER Victor@http://github.com/pi-victor

RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm

RUN yum update -y

RUN yum install git gcc make gcc-c++ \
    postgresql-devel \
    kernel-devel python-virtualenv \
    python-devel npm -y

#change dir to clone to opt
WORKDIR /opt

RUN git clone -b develop https://github.com/pi-victor/servicedeskaid.git

WORKDIR /opt/servicedeskaid

RUN virtualenv -p python3 .venv

RUN .venv/bin/pip3 install -r requirements.txt

RUN npm install -g bower

RUN bower install --allow-root

ENTRYPOINT [".venv/bin/python", "server.py" ]

EXPOSE 5000
