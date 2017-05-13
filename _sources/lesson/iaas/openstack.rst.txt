.. _s-openstack:

OpenStack on FutureSystems
======================================================================

.. highlight:: bash

.. role:: pink

.. note:: Many of us use cloudmesh directly to access the various
	  clouds. The interface cloudmesh provides is in regards to
	  starting multiple virtual machines more convenient. Please
	  try out the nova commands so you can appreciate what
	  cloudmesh offers. For more information about cloudmesh see
	  the Section :ref:`s_cloudmesh`.


.. note:: FutureSystems Portalname and Project ID
          For this example, we assume you have set the shell variable
	  :pink:PORTALNAME to your FutureSystems portal username. This can
	  be done as follows. Let us assume your portal name is
	  `albert`. Then you can set it with::

              $ export PORTALNAME=albert

	 If you execute the steps in this manual on india your india
	 login name is the portalname, thus you can do::

              $ export PORTALNAME=$USER

         We also assume that you have a project id that you set to::

              $ export PROJECTID=fg101
 
         if it is the number 101.


Login
-------

Currently, FutureSystems has OpenStack Kilo installed on India. To use
it you need to first log into india and prepare your OpenStack
credentials::

       $ ssh $PORTALNAME@india.futuresystems.org

Setup OpenStack Environment
---------------------------

In case you like to use the shell command line tools you can load them
with ::

    $ module load openstack

Creating the openrc.sh file
----------------------------------------------------------------------

An initial openrc file is currently created for you automatically and
can be activated with ::

    $ source ~/.cloudmesh/clouds/india/kilo/openrc.sh


In future, this file will be created with the help of cloudmesh
simplifying access to multiple heterogeneous clouds on FutureSystems.

List flavors
------------

To list the flavors, please execute the following command ::

    $ nova flavor-list

Everything is fine if you see an output similar to ::

       +----+-----------+-----------+------+-----------+------+-------+-------------+-----------+-------------+
       | ID | Name      | Memory_MB | Disk | Ephemeral | Swap | VCPUs | RXTX_Factor | Is_Public | extra_specs |
       +----+-----------+-----------+------+-----------+------+-------+-------------+-----------+-------------+
       | 1  | m1.tiny   | 512       | 0    | 0         |      | 1     | 1.0         | True      | {}          |
       | 2  | m1.small  | 2048      | 20   | 0         |      | 1     | 1.0         | True      | {}          |
       | 3  | m1.medium | 4096      | 40   | 0         |      | 2     | 1.0         | True      | {}          |
       | 4  | m1.large  | 8192      | 80   | 0         |      | 4     | 1.0         | True      | {}          |
       | 5  | m1.xlarge | 16384     | 160  | 0         |      | 8     | 1.0         | True      | {}          |
       +----+-----------+-----------+------+-----------+------+-------+-------------+-----------+-------------+

If not your environment may not be set up correctly. Make sure that
you follow the steps in this section and the account management
section carefully.

List images
-----------

After you got the flavor list, you can list the current set of
uploaded images with the nova image-list command::

       $ nova image-list

You will see an output similar to::

  +--------------------------------------+----------------------------+--------+--------+
  | ID                                   | Name                       | Status | Server |
  +--------------------------------------+----------------------------+--------+--------+
  | 05a7e78f-d105-4c32-84c8-75562f61cfff | futuresystems/centos-7     | ACTIVE |        |
  | b1bab925-6eaa-4928-bced-47d7607103c8 | futuresystems/fedora-21    | ACTIVE |        |
  | c2a9788a-89f5-463d-96e5-61e144e05ba6 | futuresystems/ubuntu-12.04 | ACTIVE |        |
  | 04a6d3aa-026b-4679-bd6b-7fef8a98e4be | futuresystems/ubuntu-14.04 | ACTIVE |        |
  +--------------------------------------+----------------------------+--------+--------+
  

Key management
--------------
.. note:: Make sure to check if you have not already created a key with
	  the name  at::

	    ~/.ssh/$PORTALNAME-key

	  if so, please use another name. However, if you want to
	  reuse the key, you certainly can do that. Also, make sure the
	  key is not already uploaded.  This can be easily done in the
	  following way::

	    $ nova keypait-list

To start a virtual machine you must first upload a key to the
cloud::

       $ nova keypair-add $PORTALNAME-key > ~/.ssh/$PORTALNAME-key
       $ chmod 600 ~/.ssh/$PORTALNAME-key
       $ nova keypair-list
       +-----------------+-------------------------------------------------+
       | Name            | Fingerprint                                     |
       +-----------------+-------------------------------------------------+
       | $PORTALNAME-key | ab:a6:63:82:dd:08:d3:bc:c0:21:56:4c:e2:bb:22:ac |
       +-----------------+-------------------------------------------------+

Make sure you are not already having the key with that name in order
to avoid overwriting it in the cloud. Thus be extra careful to execute
this step twice. Often it is the case that you already have a key in
your `~/.ssh` directory that you may want to use. For example, if you use
rsa, your key will be located at `~/.ssh/id_rsa.pub`. 

Managing security groups
----------------------------------------------------------------------

In the next step, we need to make sure that the security groups allow
us to log into the VMs. To do so we create the following policies as
part of our default security policies. Not that when you are in a
group project this may already have been done for you by another group
member. We will add ICMP and port 22 on default group::

       $ nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0
       $ nova secgroup-add-rule default tcp 22 22 0.0.0.0/0
       $ nova secgroup-list-rules default

.. note:: Most likely you will get some errors at this time as the
	  definitions may already uploaded by default. simply ignore
	  the errors and move on.

You will see the following output if everything went correctly::

       +-------------+-----------+---------+-----------+--------------+
       | IP Protocol | From Port | To Port | IP Range  | Source Group |
       +-------------+-----------+---------+-----------+--------------+
       | icmp        | -1        | -1      | 0.0.0.0/0 |              |
       | tcp         | 22        | 22      | 0.0.0.0/0 |              |
       +-------------+-----------+---------+-----------+--------------+

Booting an image
----------------------------------------------------------------------
To boot an instance you will need first to identify the `$NET_ID`::

    $ NET_ID=$(nova net-list| awk '/ $OS_TENANT_NAME-net / {print $2}')

Now you can use the command::

  $ nova boot --flavor m1.small \
            --image "ubuntu-14.04-64" \
            --nic net-id=$NET_ID \
            --key_name $PORTALNAME-key $PORTALNAME-001

	    
Please note that the last parameter is a "label" for the VM and we
recommend thst you use a unique label. If everything went correctly,
you will see an output similar to::

       +-----------------------------+--------------------------------------+
       | Property                    | Value                                |
       +-----------------------------+--------------------------------------+
       | status                      | BUILD                                |
       | updated                     | 2013-05-15T20:32:03Z                 |
       | OS-EXT-STS:task_state       | scheduling                           |
       | key_name                    | $PORTALNAME-key                      |
       | image                       | ubuntu-14.04-64                      |
       | hostId                      |                                      |
       | OS-EXT-STS:vm_state         | building                             |
       | flavor                      | m1.small                             |
       | id                          | e15ad5b6-c3f0-4c07-996c-3bbe709a63b7 |
       | security_groups             | [{u'name': u'default'}]              |
       | user_id                     | 3bd2d773911c4502982e5c2cd81437f7     |
       | name                        | vm001                                |
       | adminPass                   | KgiKjek99dgk                         |
       | tenant_id                   | b7ea98db7b3449b184b58d28e80c7541     |
       | created                     | 2013-05-15T20:32:03Z                 |
       | OS-DCF:diskConfig           | MANUAL                               |
       | metadata                    | {}                                   |
       | accessIPv4                  |                                      |
       | accessIPv6                  |                                      |
       | progress                    | 0                                    |
       | OS-EXT-STS:power_state      | 0                                    |
       | OS-EXT-AZ:availability_zone | None                                 |
       | config_drive                |                                      |
       +-----------------------------+--------------------------------------+


List running images
----------------------------------------------------------------------

To check if your instance is active you can repeatedly issue the list
command and monitor the Status field in the table::

       $ nova list

       +-------------+-----------------+--------+------------+-------------+--------------------+
       | ID          | Name            | Status | Task State | Power State | Networks           |
       +-------------+-----------------+--------+------------+-------------+--------------------+
       | c66 ... c73 | $PORTALNAME-001 | ACTIVE | -          | Running     | int-net=10.23.0.87 |
       +-------------+-----------------+--------+------------+-------------+--------------------+

Once it has changed from for example BUILD to ACTIVE, you can log
in. Please use the IP address provided under networks. Note that the
first address is private and may only be reached from india ::

       $ ssh -l ubuntu -i ~/.ssh/$PORTALNAME-key 10.23.0.87

If you see a warning similar to::

       Add correct host key in ~/.ssh/known_hosts to get rid of this message.
       Offending key in ~/.ssh/known_hosts:3

you need to delete the offending host key from ~/.ssh/known_hosts.

Add floating IP address
----------------------------------------------------------------------

The internal IP address is not reachable from external nework. If you 
want to make your instance reachable from outside, you can use a 
floating IP address.

First, create a floating IP address::

       $ nova floating-ip-create ext-net
       +-----------------+-----------+----------+---------+
       | Ip              | Server Id | Fixed Ip | Pool    |
       +-----------------+-----------+----------+---------+
       | 149.165.158.149 | -         | -        | ext-net |
       +-----------------+-----------+----------+---------+

Check your floating ip list::

       $ nova floating-ip-list
       +-----------------+-----------+----------+---------+
       | Ip              | Server Id | Fixed Ip | Pool    |
       +-----------------+-----------+----------+---------+
       | 149.165.158.149 | -         | -        | ext-net |
       +-----------------+-----------+----------+---------+

And then, add the IP address to your instance::

       $ nova floating-ip-associate $PORTALNAME-001 149.165.158.149

.. note:: nova add-floating-ip is deprecated.

Check your floating ip list again to see if the ip address is added to your 
instance::

       # nova floating-ip-list
       +-----------------+--------------------------------------+-------------+---------+
       | Ip              | Server Id                            | Fixed Ip    | Pool    |
       +-----------------+--------------------------------------+-------------+---------+
       | 149.165.158.149 | xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx | 10.23.0.87  | ext-net |
       +-----------------+--------------------------------------+-------------+---------+

Now, you should be able to login to your instance via ssh command like this::

       $ ssh -l ubuntu -i ~/.ssh/$PORTALNAME-key 149.165.158.149

If you see a warning similar to::

       Add correct host key in ~/.ssh/known_hosts to get rid of this message.
       Offending key in ~/.ssh/known_hosts:3

you need to delete the offending host key from ~/.ssh/known_hosts.

Please do not forget to also delete your 001 vm if you no longer need
it.

Releasing Floating IP Address
-------------------------------------------------------------------------------

If you are removing the association with a floating IP address and a VM instance::

  nova  floating-ip-disassociate <server> <address>

It looks like so::

  $ nova floating-ip-disassociate $PORTALNAME-001 149.165.158.149

There is one more step to fully return the lease of IP address. *THIS IS
IMPORTANT SINCE IP ADDRESSES ARE NOT SUFFICIENT*.

Check your floating ip list::

       $ nova floating-ip-list
       +-----------------+-----------+----------+---------+
       | Ip              | Server Id | Fixed Ip | Pool    |
       +-----------------+-----------+----------+---------+
       | 149.165.158.149 | -         | -        | ext-net |
       +-----------------+-----------+----------+---------+


The floating IP address is not associated with your VM instance but it is still
in your pool which means it is reserved for you and others can't use the IP
address.

We must release the IP address so that others can use it.:: 

  nova floating-ip-delete <address> 

It looks like this::

  $ nova floating-ip-delete 149.165.158.149

Delete your instance
--------------------

You can delete your instance with::

       $ nova delete $PORTALNAME-001

If your instance is deleted, your floating ip address will become available,
and `nova floating-ip-list` should show the output like this::

       $ nova floating-ip-list
       +-----------------+-----------+----------+---------+
       | Ip              | Server Id | Fixed Ip | Pool    |
       +-----------------+-----------+----------+---------+
       | 149.165.158.149 | -         | -        | ext-net |
       +-----------------+-----------+----------+---------+

Make a snapshot of an instance
------------------------------

To allow snapshots, you must use the following convention: 

* use your project number fg### in the prefix of your snapshot name followed
  by a /

* If needed you can also add your username as a prefix in addition to
  the project number. Replace the $PORTALNAME with the username of your
  FutureSystems account.

Let us assume your project is fg101 and you want to save the image
with by reminding you it was a my-ubuntu-01 image you want to
key. Then you can issue on india the following command::

       $ nova image-create $PORTALNAME-001 fg101/$PORTALNAME/my-ubuntu-01
       $ nova image-list
       +--------------+--------------------------------+--------+--------------+
       | ID           | Name                           | Status | Server       |
       +--------------+--------------------------------+--------+--------------+
       | 18c43 ... 33 | futuresystems/fedora-20        | ACTIVE |              |
       | 1a5fd ... e9 | futuresystems/ubuntu-14.04     | ACTIVE |              |
       | f4337 ... 44 | fg101/$PORTALNAME/my-ubuntu-01 | ACTIVE | c0bd ... bcc |
       +--------------+--------------------------------+--------+--------------+

If you want to download your customized image, you can do it with this::

       $ glance image-download --file "my-ubuntu-01.img" "fg101/$PORTALNAME/custom-ubuntu-01"

.. warning:: Please note that images not following this convention may
   be deleted without warning. Also, if you do no longer need an image,
   please remove it.

What to do if you forgot your password
----------------------------------------------------------------------

In order to reset your password or you need to recreate your openrc.sh
without knowing your current password you need to send e-mail with the
following information to help@futuresystems.org and copy it to the
e-mail that you used in the portal. Below is a template for you to use
where you replace <username> with your portal name::

  Subject: lost openstack password <username>

  Name: Firstname, Lastname
  username: <username>
  e-mail registered in the portal: <portale-mail you used>

  Please reset my openrc file for the Kilo cloud. By mistake I have modified it and can not remember the password.
 
  Thanks

  yourname here
  your email here

Change of rc file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to make a change in your rc file (openrc.sh), follow the
instructions below.

* Open a ``~/.cloudmesh/clouds/india/kilo/openrc.sh`` file
* Replace your old password to a new password in a ``OS_PASSWORD`` key.
* Load your rc file ``source ~/.cloudmesh/clouds/india/kilo/openrc.sh``
* Try nova command line e.g. ``nova list``
* If you see a message like the below, your change is made incorrectly::

  ERROR (Unauthorized): The request you have made requires authentication. (HTTP 401)

.. _s-openstack-horizon:

Horizon GUI
---------------------------

Horizon is a graphical user interface/dashbooard for OpenStack. For
starting up VMs and stopping them by hand horizon may be a good
mechanism to manage your Virtual machines. The Kilo Horizon url is: https://openstack.futuresystems.org/horizon

The passphrase for horizion is on purpose not the same as the portal
password to introduce an additional layer of security.

You can locate the passphrase while looking at the openrc file for the
appropriate machine on india. Thus first log into india, and than load
the openstack module with::

     $ module load openstack

Look at 

     $ cat ~/.cloudmesh/clouds/india/kilo/openrc.sh

and use the password included here. If you reset your password in Horizon you may
have to update it in this file after you changed it.
