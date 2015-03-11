#servicedesk aid git cloning

FROM centos:latest

MAINTAINER Victor@http://github.com/pi-victor

RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm

RUN yum update -y

RUN yum install git gcc make gcc-c++ \
    kernel-devel python-virtualenv \
    python-devel -y

#RUN zypper --non-interactive in gcc libopenssl0_9_8 python-devel python-virtualenv git

#change dir to clone to opt
WORKDIR /opt

RUN git clone -b develop https://github.com/pi-victor/servicedeskaid.git

WORKDIR /opt/servicedeskaid

RUN virtualenv .venv

RUN .venv/bin/pip install -r requirements.txt

ENTRYPOINT [".venv/bin/python", "server.py", "runserver"]

EXPOSE 5000
