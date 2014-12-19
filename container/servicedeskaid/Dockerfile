#servicedesk aid git cloning


FROM opensuse

MAINTAINER Victor@http://github.com/pi-victor

RUN zypper ar http://download.opensuse.org/repositories/server:database/openSUSE_13.1/server:database.repo

RUN zypper --no-gpg-check ref
RUN zypper --non-interactive --no-gpg-check up -y
RUN zypper --non-interactive in gcc libopenssl0_9_8 python-devel python-virtualenv git

#change dir to clone to opt
WORKDIR /opt

RUN git clone -b develop https://github.com/pi-victor/servicedeskaid.git

WORKDIR /opt/servicedeskaid

RUN virtualenv .venv

RUN source .venv/bin/activate && pip install -r requirements.txt

ENTRYPOINT [".venv/bin/python", "server.py", "runserver"]

EXPOSE 5000
