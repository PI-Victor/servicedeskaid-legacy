Service Desk Aid
==============
Master Branch Build : [![Build Status](https://travis-ci.org/thecodeflavour/servicedeskaid.svg?branch=master)](https://travis-ci.org/PI-Victor/servicedeskaid)  
Develop Branch Build: [![Build Status](https://travis-ci.org/thecodeflavour/servicedeskaid.svg?branch=develop)](https://travis-ci.org/PI-Victor/servicedeskaid)


#### Updates:
The app is going through a major re-writing to implement at least basic functionality of a backend in python with a frontend more oriented to js.
Changed to python3


An outdated demo version of the latest build from the develop branch can be found [here](http://servicedeskaid.thecodeflavour.org)


Service desk aid is a service desk delivery tool in active development for call centers and ops alike.  
It incorporates a fast way to communicate, implements tools that allow you to template and document properly work done, tickets, and much more.
You can share snippets, screen shots and other useful data.

#### Demo version

For a stable demo version use the master branch
You can get a demo version of this simply by cloning the project and:
`virtualenv -p python3 .venv`  
`ln -s .venv/bin/activate`
`source activate`
`pip3 install .`
`python server.py runserver`
make sure you use virtualenv for this.

The demo version will be available on http://localhost:5000 or http://127.0.0.1:5000

Functionality so far is limited.
