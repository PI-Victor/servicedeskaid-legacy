####Suse deployment environment for Service Desk Aid

[Docker image for cloning and automated build](https://registry.hub.docker.com/u/codeflavour/docker-suse/dockerfile/)


#####Removing test builds from docker
docker rm $(docker ps -a -q) 

#####Removing untagged images
docker rmi $(docker images | grep "^<none>" | awk "{print $3}") 


#serve a local mongodb container without binding it to servicedeskaid to start it
sd run -d --name=servicedesk -p 8008:5000 -e "MONGODB_PORT_27017_TCP_ADDR=172.17.42.1" -e "MONGODB_PORT_27017_TCP_PORT=27017" codeflavour/servicedeskaid:api