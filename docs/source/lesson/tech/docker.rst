:orphan:

.. _ref-class-lesson-docker:

Docker Basics on FutureSystems
===============================================================================

Docker is an image-based resource isolation software by using
operating system level virtualization.  Docker host runs software
containers which deploy applications with its environments. You can
easily share your application using Docker container across different
platforms or operating systems.  This section, we introduce basic
commands of ``docker`` to explore Docker software on FutureSystems.
In the next section, we will the explore advanced use of ``docker``
with Cloudmesh on FutureSystems.

Overview
-------------------------------------------------------------------------------

.. tip:: approximate time 1 hour

In this tutorial, we are going to learn basic commands of Docker.
Keep in mind that ``docker`` is a main program and ``container`` is an image
that you would like to use. You may have several containers in your docker.

The commands will be covered:

* Start a container (run)
* List containers (ps)
* Logs (logs)
* Search containers (search)
* Stop and delete a container (stop, rm)

Docker Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use Ubuntu package tool `apt-get` to download and install Docker.

::

  sudo apt-get update
  sudo apt-get install docker.io

.. tip:: To get the latest version, try this:
    curl -sSL https://get.docker.com/ubuntu/ | sudo sh

..  sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
    sudo sh -c "echo deb https://get.docker.com/ubuntu docker main\
    > /etc/apt/sources.list.d/docker.list"
    sudo apt-get update
    sudo apt-get install lxc-docker

Example I: "Hello, World"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run a simple command "Hello, World".

::

  sudo docker run -it ubuntu echo "Hello, World"

Shell Prompt in Docker Container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Docker command has a sub-command ``run`` to execute containers with a few
parameters.  In this example, we use Ubuntu 14.04 image to get bash shell
prompt.

::

  sudo docker run -i -t ubuntu:14.04 /bin/bash


You expect to see results like so: 

::
  
  root@8110bb395822:/#

Type ``exit`` to quit the shell and return to Docker host.

Example II: Apache Tomcat Server on Docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's easy to deploy Apache Tomcat using Docker. Please run the following
command: (sudo is suppressed)

:: 

  docker run -d -p 80:8080 tomcat:8.0

It downloads tomcat image from Docker Hub and connects 80 port to 8080 port.
So, if you open a web browser ``http://localhost`` or ``http://ip address of
host`` your connection forwards to the container 8080 port. ``-d`` option
daemonizes the container.

.. tip:: Did you see ``Unable to find image 'tomcat:8.0' locally``?
         Your Docker will find ``tomcat`` from Docker Hub and download it to
         your local.


Listing Containers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use ``ps`` sub command to list available containers.

::

  docker ps

You expect to see results like so::

  CONTAINER ID        IMAGE                        COMMAND             CREATED             STATUS              PORTS                    NAMES
  4690a7973fef        tomcat:8.0                   "catalina.sh run"   8 seconds ago       Up 5 seconds        0.0.0.0:8888->8080/tcp   adoring_lalande

Logs of Container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can find out details of your container by looking at log messages. Use
``NAMES`` from the previous command.  This example we use ``adoring_lalande`` for
your tomcat:8.0 container.

::

   docker logs -f adoring_lalande

Logs look like so::

  13-Feb-2015 03:02:57.524 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log Server version:        Apache Tomcat/8.0.18
  13-Feb-2015 03:02:57.526 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log Server built:          Jan 23 2015 11:56:07 UTC
  13-Feb-2015 03:02:57.526 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log Server number:         8.0.18.0
  13-Feb-2015 03:02:57.526 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log OS Name:               Linux
  13-Feb-2015 03:02:57.526 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log OS Version:            3.13.0-44-generic
  ...

Search Containers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are looking for other containers, ``search`` command is useful to find.

For example, try to find ``ipython`` containers.

::

  docker search ipython
  
You expect to see results like so:: 

        NAME                                DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
        ipython/scipyserver                 IPython notebook server with the full SciP...   36                   [OK]
        ipython/notebook                    The most recent version of IPython, config...   35                   [OK]
        ipython/scipystack                                                                  10                   [OK]
        ...

.. tip:: ``STARS`` indicates popular containers.

Stop and Delete Container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Like stopping and terminating a virtual instance, docker stops and deletes its
container with two commands: ``stop`` and ``rm`` We use ``NAMES`` from ``docker
ps`` command. This example we use ``adoring_lalande`` for your tomcat:8.0
container.

::
  
  docker stop adoring_lalande

After stopping the container, you can delete it.

::

  docker rm adoring_lalande

Review Docker Commands
-------------------------------------------------------------------------------

We have learned some Docker commands. These are basic commands for Docker
software.

* ``docker run``: runs a container. ``-it`` option allows you an interactive
  mode. ``-d`` option daemonizes your container.
* ``docker logs``: displays log messages.
* ``docker ps``: shows available containers.
* ``docker search``: searches containers from Docker Hub.
* ``docker stop``: stops your container.
* ``docker rm``: deletes your container image.

Reference
-------------------------------------------------------------------------------

The main tutorial from Docker is here:
https://docs.docker.com/installation/ubuntulinux/


..
  COMMENT

  Next Step
  -------------------------------------------------------------------------------

  In the next lesson, we learn how to deploy Cloudmesh using Docker.

  :ref:`Next Tutorial- Deploying Cloudmesh using Docker <ref-class-lesson-docker-with-cloudmesh>`


OTHER DOCKER SECTION

Docker
======

Installing Docker Community Edition
-----------------------------------

To install docker on your computer, please visit the page:

-  `Docker Community
   Edition <https://www.docker.com/community-edition>`__

Here you will find a variety of packages, one of which will hopefully
suitable for your OS. The supported operating systems currently include:

-  OSX, Windows, Centos, Debian, Fedora, Ubuntu, AWS, Azure

Please chose the one most suitable for you.

Instalation for OSX
~~~~~~~~~~~~~~~~~~~

The docker community edition for OSX can be found at the following link

-  `Information for
   OSX <https://store.docker.com/editions/community/docker-ce-desktop-mac?tab=description>`__

We recommend that at this time you get the

-  [Docker CE for MAC (stable)]
   (https://download.docker.com/mac/stable/Docker.dmg)

This will download a dmg file to your machine, that you than will need
to install by double clicking and allowing access to the dmg file. Upon
instalation a ``whale`` in the top status bar shows that Docker is
running, and you can acess it via a terminal.

.. figure:: https://d1q6f0aelx0por.cloudfront.net/icons/whale-in-menu-bar.png
   :alt: image: menu bar

   image: menu bar

Testing if the install works
----------------------------

To test if it works execute the following commands in a terminal:

::

    $ docker version

You should see an output similar to

::

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

::

    $ docker run hello-world

Once executed you should see an outout similar to

::

    Unable to find image 'hello-world:latest' locally
    latest: Pulling from library/hello-world
    78445dd45222: Pull complete 
    Digest: sha256:c5515758d4c5e1e838e9cd307f6c6a .....
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
