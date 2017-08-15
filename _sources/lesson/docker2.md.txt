# Docker 
## Installing Docker Community Edition


To install docker on your computer, please visit the page:

* [Docker Community Edition](https://www.docker.com/community-edition)

Here you will find a variety of packages, one of which will hopefully suitable for your OS. The supported operating systems currently include:

* OSX, Windows, Centos, Debian, Fedora, Ubuntu, AWS, Azure

Please chose the one most suitable for you.


### Instalation for OSX

The docker community edition for OSX can be found at the following link

* [Information for OSX](https://store.docker.com/editions/community/docker-ce-desktop-mac?tab=description)

We recommend that at this time you get the 

* [Docker CE for MAC (stable)] (https://download.docker.com/mac/stable/Docker.dmg)

This will download a dmg file to your machine, that you than will need to install by double clicking and allowing access to the dmg file. Upon instalation a  `whale` in the top status bar shows that Docker is running, and you can acess it via a terminal.

![image: menu bar](https://d1q6f0aelx0por.cloudfront.net/icons/whale-in-menu-bar.png)


## Testing if the install works

To test if it works execute the following commands in a terminal:

	$ docker version
	
You should see an output similar to 

	docker version
	Client:
 	  Version:      17.03.1-ce
 	  API version:  1.27
 	  Go version:   go1.7.5
 	  Git commit:   c6d412e
 	  Built:        Tue Mar 28 00:40:02 2017
 	  OS/Arch:      darwin/amd64

	Server:
 	  Version:      17.03.1-ce
 	  API version:  1.27 (minimum version 1.12)
 	  Go version:   go1.7.5
 	  Git commit:   c6d412e
 	  Built:        Fri Mar 24 00:00:50 2017
 	  OS/Arch:      linux/amd64
 	  Experimental: true
 
 To see if you can run a container use
 
	$ docker run hello-world
	
Once executed you should see an outout similar to 

	Unable to find image 'hello-world:latest' locally
	latest: Pulling from library/hello-world
	78445dd45222: Pull complete 
	Digest:	sha256:c5515758d4c5e1e838e9cd307f6c6a .....
	Status: Downloaded newer image for hello-world:latest

	Hello from Docker!
	This message shows that your installation appears to 
	be working correctly.

	To generate this message, Docker took the following steps:
 	1. The Docker client contacted the Docker daemon.
 	2. The Docker daemon pulled the "hello-world" image 
 	   from the Docker Hub.
	3. The Docker daemon created a new container from that 
	   image which runs the executable that produces the 
	   output you are currently reading.
 	4. The Docker daemon streamed that output to the Docker 
 	   client, which sent it to your terminal.

	To try something more ambitious, you can run an Ubuntu container 
	with:
 	
 	$ docker run -it ubuntu bash

	Share images, automate workflows, and more with a free Docker ID:
 	https://cloud.docker.com/

	For more examples and ideas, visit:
 	https://docs.docker.com/engine/userguide/



