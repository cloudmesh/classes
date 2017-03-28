.. _cm_install_:

Cloudmesh Client on Ubuntu 16.04
================================

In this class, we will be accessing for several projects multiple
clouds. This could pose a significant development issue for some in
the class. to simplify access we introduce you to one method that we
recommend for this class. We will be using a project called
cloudmesh_client that allows users to easily access multiple clouds
from the command line. Switching between clouds can be achieved with
one variable. The advantages include:

* access to another cloud in case of failure
* relocation of experiments to see if they are robust
* performance benchmarking to compare clouds.
  
Installation
------------

First, let us install cloudmesh client using pip and make sure you
install the latest updates. Install cloudmesh client using pip ::

  $ pip install -U cloudmesh_client

In order to make sure cloudmesh is running properly, enter cm in your
command line.  It will show a terminal in the following way::

  $ cm

If the installation was successful, this will start the cloudmesh
shell. To exit the shell, you can issue the ``quit`` command::
  
  +=======================================================+
  .   ____ _                 _                     _      .
  .  / ___| | ___  _   _  __| |_ __ ___   ___  ___| |__   .
  . | |   | |/ _ \| | | |/ _` | '_ ` _ \ / _ \/ __| '_ \  .
  . | |___| | (_) | |_| | (_| | | | | | |  __/\__ \ | | | .
  .  \____|_|\___/ \__,_|\__,_|_| |_| |_|\___||___/_| |_| .
  +=======================================================+
                       Cloudmesh Shell
  cm> quit
  $ 
  
Cloudmesh Client Upgrade
------------------------

.. note:: Please skip this section if this is your first time
	  installing cloudmesh client.
	  
From time to time we will release new versions of cloudmesh
client. The safest way to install it is to make sure that you shut
down all VMs in all clouds. Then you reset the db with::

  cm reset

Next, you uninstall all previous versions of cloudmesh with::

  pip uninstall cloudmesh_client

You need to repeat the uninstall step as long as you find older
versions of cloudmesh client. Once there aren't any old versions, you
simply install the new version of cloudmesh client with::

  pip install -U cloudmesh_client
  
As the reset has deleted the db, you need to add your key and set
refresh to on with::
  
  cm refresh on
  cm key add —ssh

Test it out to do things such as listing images or booting vms::

  cm vm list
  cm vm boot

Naturally you must have done the setup step previously.
  
Setting Up
----------

Now cloudmesh is installed locally. In order to run a virtual machine
in chameleon cloud, there are a few configurations steps that have to
be completed. We show this below, and if you want to get more detailed
information on configuring the cloudmesh client, you can access it at
http://cloudmesh.github.io/client/configuration.html.

Open the cloudmesh client configuration file,
``~/.cloudmesh/cloudmesh.yaml``, in your preferred text editor. The
first section in the file you need to update is ``profile:``, which by
default will look as follows::
  
  profile:
  firstname: TBD
  lastname: TBD
  email: TBD
  user: TBD

Change it with your personal information. For example::

   profile:
        firstname: Vibhatha
        lastname: Abeykoon
        email: vibhatha@gmail.com
        user: vibhatha

The ``user`` field doesn't refer to any specific username (e.g. for
cloudmesh, IU, etc.). However, it is good to set it to something that
you are fairly sure will be unique. Your IU username is a good choice.

Setting Up Chameleon Cloud
--------------------------

In ``cloudmesh.yaml``, set chameleon cloud as the active cloud like
this::

   active:
    - chameleon
   clouds:
   ...

.. tip::
   For full details on how to set up Chameleon Cloud with
   cloudmesh client, go here:
   http://cloudmesh.github.io/client/configuration.html#chameleon-cloud

Next, you need to fill in the details about your chameleon cloud
account. The relevant section will look like this::
  
   OS_PASSWORD: TBD
   OS_TENANT_NAME: TBD
   OS_TENANT_ID: TBD
   OS_PROJECT_NAME: TBD
   OS_USERNAME: TBD

Fill in the username, password and project details from your chameleon
cloud account::
  
    OS_PASSWORD: <enter your chameleon cloud password here>
    OS_TENANT_NAME: CH-818664
    OS_TENANT_ID: CH-818664
    OS_PROJECT_NAME: CH-818664
    OS_USERNAME: vibhatha

.. tip::
     
   If you don't want to put your cloud password in the yaml file, you
   can put ``read`` instead of the password in ``OS_PASSWORD``
   field. In this way, every time you need to access the cloud, you
   will type in the password.

Make sure the ``TENANT_NAME`` has the value ``CH-818664``. This
identifies the class allocation, which you should have been added to,
and should be able to see on your dashboard at
https://www.chameleoncloud.org/user/dashboard/. If this is not the
case, please contact us immediately on the class Piazza.

.. note:: Replace all TBD values with correct values (only in profile
          section and chameleon cloud section).

Preparing for Chameleon Access
-------------------------------

We need to make sure that any VMs we start will be created on
chameleon cloud and the correct user profile information will be
used. To do this, we need to set the following options::
  
   $ cm default cloud=chameleon
   $ cm register profile 
   $ cm default user=YOURUSERNAME 

Information about the configuration of cloudmesh can be retrieved by
the following command::

   $ cm info

Next, we need to add the ssh key to the cloudmesh database. Make sure
you have already generated an ssh key with ``ssh-keygen``. Then, the
following command will add the ``id_rsa.pub`` key from your ``~/.ssh``
directory to the local cloudmesh client database::
  
   $ cm key add --ssh

The key is now in our local cloudmesh database, but we need to upload
it to all active clouds. As we have just one active cloud it will
upload the key to the chamelon cloud once you execute the command::

   $ cm key upload

We must be able to communicate with the virtual machines, and to
facilitate this, we need to set the ``secgroup`` command as follows::

   $ cm secgroup upload

To see the details of the secgroup configuration, you can execute::
   
   $ cm secgroup list
   
Booting VMs
-----------

To boot a virtual machine using your configuration, run this command::

   $ cm vm boot

To see all currently running VMs, use the command::

   $ cm vm list

Logging In To A VM
-----------------

To login to the vm you need to assign a publicly available IP
address. You can do this with::

   $ cm vm ip assign

Finally, to access your newly created VM, you enter::

   $ cm vm ssh

You will see a prompt like this::

   cc@hostname$ 

To exit the VM, do::

  cc@hostname$ exit
  
.. warning:: Many errors could occur that are unrelated to cloudmesh
	     client. Such errors could include network interruptions,
	     resource starvation on chameleon cloud during which
	     either no VMs can be started, or an IP address can not be
	     assigned, or chameleon cloud is offline for
	     maintenance. Please, check for these and other similar
	     errors before you assume there is something wrong with
	     cloudmesh client.

Removing VMs
------------

To delete a virtual machine, run the following command (exit the VM
first if necessary)::

   $ cm vm delete <name_of_vm>

For example::

   $ cm vm delete vibhatha-001

To delete multiple virtual machines, run the following command::
  
   $ cm vm delete <name_of_vm>* 

or with ``--all`` option::

   $ cm vm delete --all

It is important that you delete or terminate your VMs after you are done
as chameleon cloud has a limited set of resources. We recommend that
you do not keep a VM up for more than 6 hours. Please be aware when
you delete a VM everything on that VM is deleted. hence we recommend
that you make appropriate backups of the content in the VM and have
Ansible scripts to recreate your software stack.
	  
Exercise
--------

cloudmesh.1: Follow the instructions in this lesson to install
cloudmesh, create a VM and delete it.
