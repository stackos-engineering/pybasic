# Basics

For more information about how to customize your python image
go to : https://hub.docker.com/_/python?tab=description

# StackOS

Note StackOS currently only supports docker hub images.  You must create
a free Docker Hub account to host your image, then deploy that image to 
StackOS.  If your image has private data, you may use your username and 
password to protect your image.  StackOS can use your username and password
to access your private image during deploy.

For more information about how to use this image on StackOS visit
the docs.  The most common questions are answered here:

https://docs.stackos.io/stackos-docs/faqs/introductory-faqs

# How to build

Note: APPNAME includes a name + tag.  You must change/increment the tag and 
deploy the new tag for StackOS to recognize the change

The docker image source files are located in the folder "example_with_requirements"

In that directory, build the image using these commands
```
DOCKERHUB_USERNAME=johndoe
APPNAME=pybasic:v1
docker build -t  $DOCKERHUB_USERNAME/$APPNAME .
docker push $DOCKERHUB_USERNAME/$APPNAME 
```

To test the image locally you can run then terminate with Control+C

```
DOCKERHUB_USERNAME=johndoe
APPNAME=pybasic:v1
docker run --rm -ti $DOCKERHUB_USERNAME/$APPNAME 
```


# How to deploy on StackOS

Fund your account: https://docs.stackos.io/stackos-docs/operations/account-funding-general

Launch your pod: https://docs.stackos.io/stackos-docs/operations/pod-launch-general

View pod logs: https://docs.stackos.io/stackos-docs/operations/webtty-logs-shell-access

Reference other pods like mysql or redis:

You can internally address other pods in the same  StackOS account by the standard hostname scheme:
PODNAME-0xYourEthAddress

Where you can replace PODNAME with the actual name of your pod such as redis or mysql resulting in hostname such as:
redis-0xYourEthAddress
mysql-0xYourEthAddress

