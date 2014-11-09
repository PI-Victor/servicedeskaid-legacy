Service Desk Aid
==============
Master Branch Build : [![Build Status](https://travis-ci.org/PI-Victor/servicedeskaid.svg?branch=master)](https://travis-ci.org/PI-Victor/servicedeskaid)  
Develop Branch Build: [![Build Status](https://travis-ci.org/PI-Victor/servicedeskaid.svg?branch=develop)](https://travis-ci.org/PI-Victor/servicedeskaid)    


[A live demo version of the latest build from the develop branch can be found live here](http://servicedeskaid.thecodeflavour.org)


Service desk aid is a service desk delivery tool in active development for call centers and ops alike. It incorporates a fast way to communicate, implements tools that allow you to template and document properly work done, tickets, and much more. You can share snippets, screen shots and other useful data.

####Credit to:
[Flip Clock JS by @objectivehtml](http://flipclockjs.com/)  
[Login form from Bootsnip.com calvinko](http://bootsnipp.com/calvinko)  
  

####Demo version

For a stable demo version use the master branch  
You can get a demo version of this simply by cloning the project and running `pip setup install .` and then `python server.py runserver` make sure you use virtualenv for this.
The demo version will be available on http://localhost:5000 or http://127.0.0.1:5000

Functionality so far is limited to just displaying the web interface and navigating trough a few pages.
Coming soon:
User sign up and login functionality
  
####How to install Mongo on Opensuse 13.1

Installing MongoDb on OpenSuse 13.1
*    zypper addrepo http://download.opensuse.org/repositories/server:database/openSUSE_13.1/server:database.repo
*    zypper refresh
*    zypper install mongodb


Showcase:

Animated version:

![servicedeskaid animated](https://github.com/codeflavour/servicedeskaid/blob/develop/showcase/servicedeskaid.gif?raw=true "gif")


The Front, (in construction - will show a summary of open issues and users logged in)  

![servicedeskaid front](https://github.com/codeflavour/servicedeskaid/blob/develop/showcase/front.png?raw=true "Front")

The issue page (in construction)  

![servicedeskaid issues] (https://github.com/codeflavour/servicedeskaid/blob/develop/showcase/issues.png?raw=true "Issues")

The login/sign up form  

![servicedeskaid login form] (https://github.com/codeflavour/servicedeskaid/blob/develop/showcase/login.png?raw=true "Login form")

![servicedeskaid signup form] (https://github.com/codeflavour/servicedeskaid/blob/develop/showcase/signup.png?raw=true "Sign up form")
