#servicedesk aid git cloning

FROM python:3.4.3

MAINTAINER Victor@http://github.com/pi-victor

#change dir to clone to opt
WORKDIR /opt

RUN git clone -b develop https://github.com/pi-victor/servicedeskaid.git

WORKDIR /opt/servicedeskaid

RUN easy_install pip

RUN pip3 install -r requirements.txt

RUN curl -sL https://deb.nodesource.com/setup_0.12 | bash - && \
    apt-get install -y nodejs 

RUN curl https://www.npmjs.com/install.sh | sh

RUN npm install -g bower

RUN bower install --allow-root

RUN apt-get autoremove -y

ENTRYPOINT ["python3", "server.py" ]

EXPOSE 5000
