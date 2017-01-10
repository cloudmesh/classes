Microsoft Azure Virtual Machine
======================================================================

Overview
----------------------------------------------------------------------

This lesson will introduce you to a very important topic to Microsoft Azure
cloud services . Azure Virtual Machine offers IaaS with linux operating
systems. The use of key pairs or creating virtual instances is slightly
different compared to other clouds e.g. Amazon EC2 or OpenStack Nova.  In this
lesson, we focus on a simple tutorial of running a Python Flask Web Framework
on Azure Virtual Machine. We expect that readers gain basic knowledge of using
Azure cloud services and have some experience of building services on the
cloud.

.. tip:: Duration: 50 minutes

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have:

* Azure Account
* Subscription for billing and payment
* SSH Client tool (e.g. putty, cygwin or terminal)
* openssl is not required (we replaced it with one-time password login and ssh
  key pair access)

Description
----------------------------------------------------------------------

We will create a VM instance on Azure cloud, and start a Flask Web Framework on
the Ubuntu 14.04 machine image. Our conditions are:

* Ubuntu 14.04 LTS Server 64 bit (VM Image)
* A1 Size (1 vcpu + 1.75 gb memory)
* HTTP, HTTPS (80, 443) port opening using security groups
* Password authentication for the first login
* SSH key pair authentication after password authentication is disabled
* Use of package manager (i.e. apt-get) with switching to admin privileges
* Use of Python packages
* Editors e.g. vi, nano, emacs
* Use Azure Management Portal (Web interface)
   - We might have other lessons for using an azure command line tool.

Getting Started
-------------------------------------------------------------------------------

Microsoft Azure provides web management tool, Azure Management Portal to
control Azure cloud services. We will use this web interface to create, list or
delete a VM instance.

Azure Management Portal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Sign in Azure Management Portal 
  http://manage.windowsazure.com

* Sign up, if you don't have an account

* Register a new subscription
   - 1-month Free trial is available
   - Pay-as-you-go is available

* go to Azure Management Portal
   - Find the Virtual Machines page. We create a VM instance in the page.

Preparing VM Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Select a VM base image from Gallery
   * Gallery is a repositofy for VM images
   * Choose ``Ubuntu`` tab.
   * There are a few VMs available. Select Ubuntu 14.04 LTS.
   * Community VMs are also available.

* Provide a name for your VM instance
   - Your VM instance need a name. This name is also used for dns name.
     For example, if you created a VM instance with ``tutorial-azure``,
     you may have dns name, ``tutorial-azure.cloudapp.net``.
   - Azure provides a unique dns address using the name in this format ``[unique
     vm name].cloudapp.net``.  Unque name means that there is no duplication
     across entire Azure cloud services.

* Choose a size of your VM instance
   - select A1 (1core, 1.75 memory) or other preferred size of VM instance
   - OpenStack Flavor and Amazon Instance types have similar format for the size
     of VM instances.

* Choose a region
   - It is a physical location of your VM instance.
   - Geological different data centers provide better network access if you're
     close to them. Choose a location based on the location for your service.

* Add a rule
   - SSH (22) port is default
   - HTTP (80) and HTTPs (443)

* Choose ``provide password`` and disable ``ssh key pair authentication``
   - We use ``azureuser`` as a user name.
   - We provide a password instead of key authentication file e.g. pem.

* Click 'Complete'
   - Confirm your VM image, size and rules.

Launch a Instance and IP Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you successfully launched your instance, it will be available in a few
moments.

* Find a IP Adddress or hostname
   - We need destination address to ssh into the server. You can find IP address
     or hostname in the Instances page.
   - Typically you have a dns name like ``[your vm name].cloudapps.net``.

SSH into VM Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use your ssh client tool to login to the virtual server.

* ``azureuser`` as a user name 
   - We specified this name as login name when we deploy a VM instance.
     Once we logged into the VM instance, we can switch to other users e.g.
     ``root`` or create a new user.

* Password Authentication
   - We login to the VM instance using the passowrd that we provided in the
     process of vm creation.

Switch Password Authentication to SSH Key Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since we used password authentication, we need to switch it to SSH key pair
authentication.  This requires a few steps with ``root``.

* Create a new SSH key pair
   - If you use Windows OS, try ``puttygen.exe``
   - Store your private key in a safe place.
   - Copy your public key string. We need to provide this to SSH on the VM instance.

* Move to $HOME/.ssh directory
   - There is a ``authorized_keys`` file which holds a list of public key strings.
     If you register your public key in this file, you will be able to login to
     this machine using a pair, your private key.

* Run ``echo [your public key string] >> $HOME/.ssh/authorized_keys``
   - This way, you register your public key to your virtual server.

* Open ``/etc/ssh/sshd_config`` with your editor e.g. nano, emacs, or vi.
   - e.g. ``sudo vi /etc/ssh/sshd_config``

* Change ``PasswordAuthentication yes`` to ``PasswordAuthentication no``
  and save the file.

* Run ``sudo service ssh restart``
   - This command restarts a SSH server on your virtual server.

* Your password login is disabled.
   - After the command above, you won't allow to use password to login.
   - SSH key login is only allowed.

Install and Run Flask Python Web Framework
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's time to install and run Flask Web Framework. It is a minimal software to
run a web server using Python. We will try to use a sample code ``hello.py``
from the Flask official site.

We assume that you know how to use some basic Linux commands, editors and
Python. We will use the following commands 1) sudo, 2) su, 3) apt-get, and 4)
service, 5) python to install and run Flask.

* ``sudo apt-get update``
   - This command updates a list of Linux package repositories.

* ``sudo apt-get install python-pip``
   - We install Python package manager ``pip``.

* ``sudo apt-get install virtualenv``
   - We install Python virtualenv software ``virtualenv``.

* Create a new virtualenv
   - ``virtualenv $HOME/FLASK``

* Enable ``FLASK`` environment for Python
   - ``source $HOME/FLASK/bin/activate``
   - If you see **(FLASK)** label in front of your prompt, you are now in the
     ``FLASK`` environment. 

* Write a python script in ``hello.py``

  ::

        from flask import Flask
        app = Flask(__name__)

        @app.route("/")
        def hello():
            return "Hello World!"

        if __name__ == "__main__":
            app.run()

* Test your python program
   - ``python hello.py``
   - If you see  ``* Running on http://localhost:5000/``,
     you successfully run your Flask on the localhost with 5000 port number.

Make a Public Web Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We will make a small change to provide Flask in public.
This way, anyone on the internet can see your ``Hello World!`` message.

* Switch to ``root`` account to use system port 80.
   - ``sudo su -``
   - *80 or 443 port is reserved port range to system administrator i.e. ``root``*
   - Now you are in ``root`` account. Try ``pwd`` command to confirm that you
    are in ``/root``
 
* Move to ``azureuser`` home directory and enable virtualenv
   - ``cd /home/azureuser``
   - ``source /home/azureuser/FLASK/bin/activate``
   - If you see **(FLASK)** label in front of your prompt, you are now in the
     ``FLASK`` environment. 

* Change ``app.run()`` function to ``app.run(host='0.0.0.0', port=80)``
   - ``0.0.0.0`` is a way to specify *any IPv4-host at all*. You Flask will
     provide web service through your internal/external network of your virtual
     server.
   - ``port=80`` is a way to tell Flask that you are using HTTP default port.

Check ``Hello World!`` Page on the Web
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Open a web browser and type the IP address or hostname of your VM instance.
   - If you see ``Hello World!`` page, you have now working Flask Web Framework
     on Azure.

Terminate your Cloud Resources *IMPORTANT*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you completed your jobs on Azure cloud, you need to shutdown all of your
cloud resources and return the lease.  There is ``delete Cloud Service``
command or menu. If you do not terminate your resources, you will receive a
charge of using cloud services e.g. Virtual Machine, Cloud Service, or Storage.

Exercise1
-------------------------------------------------------------------------------

* Try to start a virtual server with Windows Server 2008 R2 SP1. Use Remote
  Desktop to log in. 

Exercise2
-------------------------------------------------------------------------------

**Additional (Optional) Study Material**

* Start a one of community VM images. It needs some preparation before starting
  a virtual machine. Get some experience with using VM Depot which is a open
  repository for Azure VM images.

