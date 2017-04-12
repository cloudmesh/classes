.. _single_public_ip_:

Use only one public IP address on Chameleon cloud
=================================================

Chameleon cloud has relatively limited public IP addresses. In order
to avoid consuming all, we require you to use only one ``head``
virtual machine, which will have a public IP associated with. All
other nodes needed for your project will be non-floating IP nodes,
meaning that that don't have a public accessible IP address. You can
only access these nodes from your ``head`` node.

Essentially, you just need to migrate the VirtualBox vm that you have
used on your laptop to Chameleon cloud. Instead of have
cloudmesh_client up and running on your VirtualBox vm, you re-setup
everything on a public accessible (and the only) Chameleon node. From
here, you execute all your script to configure your cluster. Because
this ``head`` node is inside Chameleon cloud, those local IP addresses
e.g. 192.168.x.x can be used to communicate.

Step 0: local machine
---------------------

Make sure your terminate all your previously allocated resources. To remove
all your cluster virtual machines from Chameleon, run::

    $ cm cluster delete <cluster name>

Step 1: local machine
---------------------

Create a single vm on Chameleon cloud::

    $ cm vm boot

Step 2: local machine
---------------------

Assign a public IP address to this virtual machine::

    $ cm vm ip assign

Step 3: head node
-----------------

First, login this vm through ssh::

    $ cm vm ssh

Next, you need to reproduce your laptop virtual environment. Here we assume the
head node is Ubuntu 14.04 fresh installed. If you use a different Linux distro,
please adjust the package installation accordingly. On the head node:::

    $ sudo apt-get update
    $ sudo apt-get install pip, git, virtualenv

The image I used at this moment needs a few more packages to let cm to run::

    $ sudo apt-get install python-dev, libffi-dev, libssl-dev
    
Finally, activate virtualenv::

    $ virtualenv <provide a venv folder name>

Again, your situation may vary depending on the cloud and image you choose.

Step 4. head node
-----------------

:doc:`Install cloudmesh_client <./cloudmesh-installation>`

On this newly installed vm, remember to:

    * upload your keys to home folder
    * update cloudmesh.yaml accordingly to set cloud, key and user


Step 5: head node
-----------------

It is time to bring up your cluster in a private IP environment. Consult to
:doc:`earlier chapters <../devops/hadoop>` to set your cluster up. The outline
is::

    $ cm cluster define --count 3 --no-floating-ip
    $ cm cluster allocate
    $ cm cluster nodes <your cluster name>
    $ cm vm ssh <node-name>

So now you can refer your nodes with their names, not the public IP addresses.