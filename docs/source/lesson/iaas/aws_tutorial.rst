Amazon Web Services (AWS)
======================================================================

Overview
----------------------------------------------------------------------

This lesson will introduce you to a very important topic to Amazon Web Services
(AWS). Amazon Elastic Compute Cloud (EC2) provides Infrastructure as a Service
(IaaS) and other services e.g. Simple Storage Service (S3) supports storing
objects (files) on cloud environments, are working together to offer dominant
cloud services compared to other competitors, e.g. Microsoft Azure, or Google
Compute Engine. In this lesson, we focus on a simple tutorial of starting a
Apache HTTP Server using Amazon EC2 virtual machine instances. We expect that
readers gain basic knowledge of using Amazon Cloud and have some experience of
building services on the cloud.


.. tip:: Duration: 30 minutes

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have:

* Amazon Account
* SSH Client tool (e.g. putty, cygwin or terminal)

Description
----------------------------------------------------------------------

We will create a EC2 instance on Amazon cloud, and start a Apache Web Server on
the Ubuntu 14.04 machine image. Our conditions are:

* Ubuntu 14.04 LTS Server 64 bit (VM Image)
* t2.small Instance Type (1 vcpu + 2 gb memories)
* HTTP, HTTPS (80, 443) port opening using security groups
* SSH key pair authentication
* Use of package manager (i.e. apt-get) with switching to admin privileges
* Use Amazon Management Console (Web interface)
   - We may have other lessons for using a ec2 command line tool.

Getting Started
-------------------------------------------------------------------------------

Amazon provides web management tool, AWS Management console to use AWS cloud
services. We will use this web interface to create a VM instance.

AWS Management Console
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Sign in Amazon Web Services (AWS)
   - http://aws.amazon.com

* Sign up, if you don't have an account
   - Free trial is available for using t2.micro instances (1 vCPU + 1 GB
     Memories)
 
* Find EC2 in AWS Management Console
   - EC2 is Amazon Compute Engine. We create a VM instance in the EC2 page.

Preparing VM Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Select VM base image
   * Find Ubuntu 14.04 LTS Server 64Bit from Quick Start.
   * There are about 40,000 VM images available in Community AMIs.

* Choose an Instance Type
   - select t2.small or other preferred size of VM instance
   - OpenStack Flavor and Azure Size have similar format for the size of VM
     instances.

* Skip to 6. Configure Security Group
   - Add a rule for HTTP and HTTPs
   - SSH (22) port is default

* Click 'Review and Launch'
   - This is a last step before we choose SSH key pair.
   - Confirm your VM image, size and rules in the security group.

SSH Key Pair
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Amazon EC2 uses SSH key pair to get access of your VM instance.

You have a few options. You can create a new key for your new VM instance or
use a existing key.

If you create a new key, carefully store your private key file.

Launch a Instance and IP Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you successfully launched your instance, it will be available in a few
seconds.

* Find a IP Adddress or hostname
   - We need destination address to ssh into the server. You can find IP address
     or hostname in the Instances page.

SSH into VM Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use your ssh client tool to login to the virtual server.

* ``ubuntu`` as a user name 
   - We used Ubuntu 14.04 VM image which has a default username ``ubuntu``.
     Once we logged into the VM instance, we can switch to other users e.g.
     ``root`` or create a new user.

* SSH private key
   - Make sure you are SSH'ing to the VM instance with your SSH key pair.
     Otherwise, your login won't be accepted from the virtual server.

Install and Run Apache Web Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We assume that you know how to use some basic linux commands.
We will use the following commands 1) sudo, 2) su, 3) apt-get, and 4) service,
to install and run Apache HTTP server.

* ``sudo apt-get update``
   - This command updates a list of Linux package repositories.

* ``sudo apt-get install apache2``
   - We install Apache HTTP version 2 using package manager ``apt-get``.

* ``sudo service restart`` (optional)
   - If you made a change on HTTP server, you may need to restart.

* ``sudo su -`` (optional)
   - If you switch a user to ``root`` with this command, you won't need to issue
     ``sudo`` command every time when you need admin privileges.

Check ``It Works!`` Page on the Web
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Open a web browser and type the IP address or hostname of your VM instance.
   - If you see ``It Works!`` page, you have now working Apache Web Server on
     Amazon EC2.

Terminate your Instance *IMPORTANT*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you completed your jobs on Amazon cloud, you need to shutdown your instances
and return the lease.  There is ``terminate instance`` command or menu. Amazon
has hour-basis charging system, if you do not terminate your system, you will
receive a charge of using cloud services e.g. EC2, S3, or CloudWatch.

Exercises
-------------------------------------------------------------------------------

* Start a web server using CherryPy or other Python software using ec2
  command-line client tool. 
   - tip1: you may need to install python packages, e.g. pip or virtualenv.
   - tip2: you may need to install and configure ec2 client tool.

* Save your data on S3 or Block Storage
   - You expect to understand how to use S3 or block storage service.

Next Step
-----------

In the next page, starting a Flask web server on Microsoft Azure will be
addressed.

`Microsoft Azure  <azure_tutorial.html>`_

