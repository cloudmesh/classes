.. _openstack_kilo:

FutureSystems OpenStack Kilo - Quickstart Guide
==============================

OpenStack Kilo is the current cloud offerring from FutureSystems. Here are the quickstart guide on using the kilo cloud.

Nova Client on India
---------------------
Load the nova client by:

.. code::

    module load openstack

Then load your account information for Kilo. The Kilo account information is enabled by:

.. code::

   source ~/.cloudmesh/clouds/india/kilo/openrc.sh

You will see instances or images on Kilo now by nova client tools, e.g. nova list.

Start a New Instance
---------------------

Starting a new instance is not difficult but requres a few steps like keypair registration and floating ip association. The simple instructions will be provided in this page.

SSH Key Pair Registraion
""""""""""""""""""""""""""""

If this is a first time to run a instance, the keypair registration is required. We assume you have a key registered on India Juno which is a previous release of OpenStack. Let's register your key on OpenStack Kilo. Juno and Kilo are separated clouds so we need to register your key on both side.

.. note:: If you don't have one, don't worry. It is easy to create a new one. Please follow the instructions here. 

.. code::

    nova keypair-add --pub-key $HOME/ssh/id_rsa.pub $USER-india-key

Once you register your key, you can confirm the registration by::

    nova keypair-list

Let's continue to start a VM in the next section.

.. tip:: The following commands will create a new SSH key pair. Provide passphrase when prompts appear.
 
    ssh-keygen -t rsa -C $USER-india-key

Start a VM Instance
""""""""""""""""""""""""

The ``nova boot`` simple command will start a VM instance. Note that ``NETID`` is required on OpenStack Kilo which is different from OpenStack Juno.
   
.. code::

    NETID=`nova network-list | grep $OS_TENANT_NAME-net | awk {'print $2'}`
    nova boot --image Ubuntu-14.04-64 --key-name $USER-india-key --flavor m1.small $USER-first-instance --nic net-id=$NETID

.. note:: replace $USER-india-key if you have a different name for your registered key. Replace other options e.g. image or flavor as you wish.

Floating IP Address
""""""""""""""""""""""""""

Now your VM instance is up and running but can't be accessible because it only has an internal IP address. We will associate a floating IP address here to get SSH access to a VM instance.

.. code::

    nova floating-ip-create ext-net
    +--------------------------------------+-----------------+-----------+----------+---------+
    | Id                                   | IP              | Server Id | Fixed IP | Pool    |
    +--------------------------------------+-----------------+-----------+----------+---------+
    | 030bf69d-88a4-41b6-90c5-9c6e7d5be442 | 149.165.159.112 | -         | -        | ext-net |
    +--------------------------------------+-----------------+-----------+----------+---------+

Now we have a IP address to assign to a VM instance. In this example, we will associate ``149.165.159.112`` to our ``$USER-first-instance`` VM instance by.

.. code::

    nova floating-ip-associate $USER-first-instance 149.165.159.112 

Once you completed this step, you are now able to SSH into your VM instance.

.. code::

    ssh ubuntu@149.165.159.112

.. note:: ``ubuntu`` is login name your your VM if you start a VM with Ubuntu image. Try other names if you used other distributions like CentOS or CoreOS. For example, ``centos`` is for ``CentOS`` and ``core`` is for ``CoreOS`` image.

Horizon Web Interface
--------------------------

Openstack provides a web interface to manage cloud resources easily. Usage reports, current quota or Heat stacks are visible on the web.

* Use your OS_USERNAME and OS_PASSWORD to login.  ``~/.cloudmesh/clouds/india/kilo/openrc.sh`` contains your ``OS_`` variables.
* https://openstack.futuresystems.org/horizon/

Termination of VM Instance
-----------------------------

If you completed your work on your VM instance, you may terminate your VM and release a floating IP address associated with. For example, we terminate our first instance and the IP address by:

.. code::

    nova delete $USER-first-intance
    nova floating-ip-delete 149.165.159.112
    



FAQ
------

Q. My ssh connection was denied with the message like below. What should I do?

.. code::

      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

A. SSH checks ssh server's fingerprint to verify the identity of the machine that you connect to. You will see the message above if the fingerprint doesn't match with one saved on your local machine (~/.ssh/known_hosts) when you ssh into the machine first time. In the cloud computing, however, you may encounter this message very often wihtout a real vulnerability. It is because that you use a same ip address with a newly deployed virtual machine which has a new fingerprint. We can ignore the host key checking or remove the fingerprint saved on a local machine by:

* Add the following options to ``ssh`` command

.. code::

     -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no

OR

* Remove the fingerprint in your ``~/.ssh/known_hosts`` file

.. code::

     ssh-keygen -f $HOME/.ssh/known_hosts -R HOSTNAME_OR_IPADDRESS
     
.. note::

     Replace HOSTNAME_OR_IPADDRESS with your destination

Q. I am seeing the following error when I run ``nova`` command:

.. code::

    You must provide a username or user id via --os-username, --os-user-id, env[OS_USERNAME] or env[OS_USER_ID]

A. You see the error because the nova client does not recognize you. Import your credential on india by:

    source ~/.cloudmesh/clouds/india/kilo/openrc.sh

This file contains your os-username, etc. regarding your account and the ``source`` command imports and keeps these information while your ssh session alive.
