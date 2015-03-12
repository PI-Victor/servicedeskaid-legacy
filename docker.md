####Suse deployment environment for Service Desk Aid

[Docker image for cloning and automated build](https://registry.hub.docker.com/u/codeflavour/docker-suse/dockerfile/)


#####Removing test builds from docker
docker rm $(docker ps -a -q) 

#####Removing untagged images
docker rmi $(docker images | grep "^<none>" | awk "{print $3}") 
