.. _cm_install_:

Cloudmesh Client on Ubuntu 16.04
================================

In this class we will be accessing for several projects multiple
clouds. This could pose a significant development issue for some in
the class. to simplify access we introduce you to one method that we
recommend for this class. We will be using a project called
cloudmesh_client that allows users to easily access multiple clouds
from the commandline. Switching between clouds can be achieved with one
variable. The advantages include:

* access to another cloud in case of failure
* relocation of experiments to see if they are robust
* performance benchmarking to compare clouds.
  

Installation
------------

First, let us install cloudmesh client using pip and make sure you
install the latest updates. Install cloudmesh client using pip ::

  $ pip install -U cloudmesh_client

In order to make sure cloudmesh is running properly, enter cm in your command line.
It will show a terminal in the following way.

::

  $ cm


, 2017, at 11:21 AM, Gregor von Laszewski <laszewski@gmail.com> wrote:


On Mar 10, 2017, at 11:13 AM, Gregor von Laszewski <laszewski@gmail.com> wrote:

All:

I released a new cm version 4.6.0.

Please test vm boot, cluster, and hadoop 

do 

pip uninstall cloudmesh_client
…. till you get an error that no older versions are there
pip uninstall cloudmesh_client

pip install cloudmesh_client
cm reset
cm refresh on
cm key add —ssh

cm vm boot

Cloudmesh Client Upgrade
------------------------

From time to time we will release new versions of cloudmesh client. The
safest way to install it is to make sure that you shut down all VMs in
all clouds. Than you reset the db with::

  cm reset

Next you uninstall all previous versions of cloudmesh with::

  pip uninstall cloudmesh_client

YOu repeat the uninstall step ass long as you will find older versions
of cloudmesh client. Once there is no more old version, you simply
install the new version of cloudmesh client with::

  pip install cloudmesh_client -U
  
As the reset has deleted the db, you need to add your key and set
refresh to on with::
  
  cm refresh on
  cm key add —ssh

Test it out to do things such as listing images or booting vms::

  cm vm list
  cm vm boot

Naturally you must have done the setup stap eiather previously.
  
Setting Up
----------

Now cloudmesh is installed locally. In order to run a virtual machine
in chameleon cloud, there are few configurations that have to be
done. You can find the configuration information in the following
location.

http://cloudmesh.github.io/client/configuration.html

After setting up cloudmesh client locally, the yaml file
can be opened by running the following command. You can use
vim or vi instead of emacs to run this. ::

  $ emacs ~/.cloudmesh/cloudmesh.yaml

examples::
  
   $ vim ~/.cloudmesh/cloudmesh.yaml
   $ vi ~/.cloudmesh/cloudmesh.yaml
   $ gedit ~/.cloudmesh/cloudmesh.yaml

First the profile section must be updated as follows::

  profile:
  firstname: TBD
  lastname: TBD
  email: TBD
  user: TBD


example configuration::

   profile:
        firstname: Vibhatha
        lastname: Abeykoon
        email: vibhatha@gmail.com
        user: vibhatha

This must be filled when working on Cloudmesh set up.
And this can be found in the configuration file in cm- yaml file.


Setting Up Chameleon Cloud
--------------------------

In the cloudmesh.yaml file, set chameleon cloud as the active cloud
as shown below. Locate the attribute value in the::

   active:
    - chameleon

Go to the following link and you can find the information regarding,
the chameleon cloud setup.

http://cloudmesh.github.io/client/configuration.html#chameleon-cloud

The following parameters has to be replaced with corresponding values::

   OS_PASSWORD: TBD
   OS_TENANT_NAME: TBD
   OS_TENANT_ID: TBD
   OS_PROJECT_NAME: TBD
   OS_USERNAME: TBD

Make sure you are following the above url.
And after replacing all the TBD values, the configuration should look like
as follows.

example configuration::
  
    OS_PASSWORD: NOTMYPASSWORD
    OS_TENANT_NAME: CH-818664
    OS_TENANT_ID: CH-818664
    OS_PROJECT_NAME: CH-818664
    OS_USERNAME: vibhatha

.. tip::
     
   If you don't want to put your cloud password in the yaml file, you can
   put ``read`` instead of the password in ``OS_PASSWORD`` field. In this
   way, every time you need to access the cloud, you will type in password.


Make sure the TENANT_NAME: CH-818664.  You must be a member of the
project in the Chameleon cloud, in order to gain access to the virtual
machines.

.. note:: Replace all TBD values with correct values (only in profile section and chameleon cloud section).


http://cloudmesh.github.io/client/configuration.html#chameleon-cloud


Preaparing for Chameleon Access
-------------------------------

To create a virtual machine we need first to make sure we start it on
chamelon cloud. This we need to set the default cloud to be chameleon
with the following command::

   $ cm default cloud=chameleon
   $ cm register profile 
   $ cm default user=YOURUSERNAME 

Information about the configuration of cloudmesh can be retrieved by
the following command::

   $ cm info

Next we need to add the ssh key to the cloudmesh database by running
the following command.  Make sure you have already generated a
ssh key with ssh-keygen. The command will add the default id_rsa.pub
key to a local database:: 

   $ cm key add --ssh

Not that the key is in our local cloudmesh database, we need to upload
it to all active clouds. As we have just one active cloud it will
uploade the key to the chamelon cloud once you execute the command::

   $ cm key upload

Furthermore, we must be able to communicate with the
virtualmachines. To communicate which ports we use we execute the
secgroup command. To just use the defaults we execute the command::

   $ cm secgroup upload

To see the details of the secgropus please use the command::

   
   $ cm secgroup list
   
   
Boot Virtual Machine
--------------------

Run the following command to boot the virtual machine::

   $ cm vm boot

To see all vms just use the command::

   $ cm vm list


Login to the vm
---------------

To login to the vm you need to have a publicly available (floating) ip. This
can be achieved with the command::

   $ cm vm ip assign

You can after this command has succeed login to the vm with the command::

   $ cm vm ssh

After a successful launch it will show a similar console as shown below::

   cc@hostname$-

.. warning:: Many errors could occur that are unrelated to cloudmesh
	     client. Such errors could include network interruptions,
	     resource starvation of cloudmesh, while either no vms
	     can be started, they are out of ip addresses, ir they
	     have a maintenance day. Please do not blame cloudmesh for
	     such issues and explore first if they originate through
	     such issues.

   
Step 7 : Remove Virtual Machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To delete a virtual machine, run the following command (exit the vm first if necessary)::

   $ cm vm delete <name_of_vm>

Example::

   $ cm vm delete vibhatha-001

To delete multiple virtual machines, run the following command::
  
   $ cm vm delete <name_of_vm>* 

or with ``--all`` option::

   $ cm vm delete --all


It is important that you delete or terminate the vm after you are done
as chameleon cloud has a limited set of resources. we recommend that
you do not keep a vm up for more than 6 hours. Please be aware when
you delete a vm everything on that vm is deleted. hence we recommend
you to make appropriate backups of the content in the vm and have
scripts via ansible to recreate your softwarstack. 
	  
Exercise
--------

cloudmesh.1: install cloudmesh, create a vm and delete it
