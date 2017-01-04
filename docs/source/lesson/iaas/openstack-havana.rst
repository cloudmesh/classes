.. _s-openstack-havana:

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
          For this example we assume you have set the shell variable
	  :pink:PORTALNAME to your FutureSystems portal username. This can
	  be done as follwows. Let us assume your portal name is
	  `albert`. Than you can set it with::

              $ export PORTALNAME=albert

	 If you execute the steps in this manual on india your india
	 login name is the portalname, thus you can do::

              $ export PORTALNAME=$USER

         We also assume that you have a project id that you set to::

              $ export PROJECTID=fg101
 
         if it is the number 101.


Login
-------

Currently FutureSystems OpenStack Havana installed on India.  To use
it you need to first log into india and prepare your Openstack
credentials::

       $ ssh $PORTALNAME@india.futuresystems.org

Setup OpenStack Environment
---------------------------

In case you like to use the shell command line tools you can load them
with ::

    $ module load novaclient

Creating the novarc file
----------------------------------------------------------------------

An initial novarc file is currently created for you automatically and
can be activated wih ::

    $ source ~/.futuregrid/openstack_havana/novarc


In future this file will be created with the help of cloudmesh
simplifying access to multiple heterogeneous clouds on FutureSystems.

List flavors
------------

To list the flavors, please execute the following command ::

    $ nova flavor-list

Everything is fine, if you see an output similar to ::

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

       +--------------------------------------+-------------------------+--------+--------+
       | ID                                   | Name                    | Status | Server |
       +--------------------------------------+-------------------------+--------+--------+
       | 18c437e5-d65e-418f-a739-9604cef8ab33 | futuregrid/fedora-18    | ACTIVE |        |
       | 1a5fd55e-79b9-4dd5-ae9b-ea10ef3156e9 | futuregrid/ubuntu-14.04 | ACTIVE |        |
       +--------------------------------------+-------------------------+--------+--------+   


Key management
--------------
.. note:: Make sure to check if you have not already created a key with
	  the name  at::

	    ~/.ssh/$PORTALNAME-key

	  if so, please use another name. However, if you want to
	  reuse the key, you certainly can do that. Also make sure the
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
your `~/.ssh` directory that you may want to use. For example if you use
rsa, your key will be located at `~/.ssh/id_rsa.pub`. 

Managing security groups
----------------------------------------------------------------------

In the next step we need to make sure that the security groups allow
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

To boot an instance you simply can now use the command::

       $ nova boot --flavor m1.small \
                   --image "futuregrid/ubuntu-14.04" \
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
       | image                       | futuregrid/ubuntu-14.04              |
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

       +-------------+----------------+--------+---------------------+
       | ID          | Name           | Status | Networks            |
       +-------------+----------------+--------+---------------------+
       | e15 ... 3b7 | $PORTALNAME-001| ACTIVE | private=10.35.23.18 |
       +-------------+----------------+--------+---------------------+

Once it has changed from for example BUILD to ACTIVE, you can log
in. Pleas use the IP address provided under networks. Note that the
first address is private and can not be reached from outside india::

       $ ssh -l ubuntu -i ~/.ssh/$PORTALNAME-key 10.35.23.18

If you see a warning similar to::

       Add correct host key in ~/.ssh/known_hosts to get rid of this message.
       Offending key in ~/.ssh/known_hosts:3

you need to delete the offending host key from ~/.ssh/known_hosts.

Use block storage
----------------------------------------------------------------------

You can create a block storage with the volume-create command. A
volume is useful as you can store data in it and associate that
particular volumen to a VM. Hence, if you delete the VM, your volume
and the data on it is still there to be reused. To create one 1G volume
you can do ::

       $ nova volume-create 1 --display-name $PORTALNAME-vol-001

To more conveniently identify the image we also specified a
displayname. Please chose a uinque name so you can identify the volume
more easily.

To list the volumes you can use::

       $ nova volume-list
       +--------------+-----------+---------------------+------+-------------+-------------+
       | ID           | Status    | Display Name        | Size | Volume Type | Attached to |
       +--------------+-----------+---------------------+------+-------------+-------------+
       | 6d0d ... abc | available | $PORTALNAME-vol-001 |  1   | None        |             |
       +--------------+-----------+---------------------+------+-------------+-------------+

To attach the volume to your instance you can use the volume-attach
subcommand. Let us assume we like to attache it as "/dev/vdb", than
you can use the command:::

       $ nova volume-attach $PORTALNAME-001 6d0d8285-xxxx-xxxx-xxxx-xxxxxxxxxabc "/dev/vdb"

.. hint:: Hint

   $PORTALNAME-001 refers to the name of the VM that we have
   created earlier with the boot command.

Next, let us login to your instance, make filesystem and mount it.
Here's an example, mounting on /mnt::

       $ ssh -l ubuntu -i ~/.ssh/$PORTALNAME-key 10.35.23.18
       ubuntu@$PORTALNAME-001:~$ sudo su -
       root@$PORTALNAME-001:~# mkfs.ext4 /dev/vdb
       root@$PORTALNAME-001:~# mount /dev/vdb /mnt
       root@$PORTALNAME-001:~# df -h
       Filesystem      Size  Used Avail Use% Mounted on
       /dev/vda1        20G  2.1G   17G  11% /
       none            4.0K     0  4.0K   0% /sys/fs/cgroup
       udev            998M  8.0K  998M   1% /dev
       tmpfs           201M  236K  201M   1% /run
       none            5.0M     0  5.0M   0% /run/lock
       none           1002M     0 1002M   0% /run/shm
       none            100M     0  100M   0% /run/user
       /dev/vdb        4.8G   23M  0.8G   1% /mnt

When you want to detach it, unmount /mnt first, go back to indias's
login node and execute volume-detach::

       root@$PORTALNAME-001:~# umount /mnt
       root@$PORTALNAME-001:~# exit
       ubuntu@$PORTALNAME-001:~$ exit
       
       $ nova volume-detach $PORTALNAME-001 6d0d8285-xxxx-xxxx-xxxx-xxxxxxxxxxxx

Set up external access to your instance
---------------------------------------

So far we only used the internal IP address, but you can also assign
an external address, so that you can log in from other machines than
india. Firts, Create an external ip address with::

       $ nova floating-ip-create

       +-----------------+-------------+----------+------+
       | Ip              | Instance Id | Fixed Ip | Pool |
       +-----------------+-------------+----------+------+
       | 198.202.120.193 | None        | None     | nova |
       +-----------------+-------------+----------+------+

Next, put it on your instance with::

       $ nova add-floating-ip $PORTALNAME-001 198.202.120.193
       $ nova floating-ip-list

       +-----------------+--------------------------------------+-------------+------+
       | Ip              | Instance Id                          | Fixed Ip    | Pool |
       +-----------------+--------------------------------------+-------------+------+
       | 198.202.120.193 | c0bd849a-221a-4e53-bf7b-7097541a9bcc | 10.35.23.20 | nova |
       +-----------------+--------------------------------------+-------------+------+

Now you should be able to ping and ssh from external and can use the
given ip address.

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
key. Than you can issue on india the following command::

       $ nova image-create $PORTALNAME-001 fg101/$PORTALNAME/my-ubuntu-01
       $ nova image-list
       +--------------+--------------------------------+--------+--------------+
       | ID           | Name                           | Status | Server       |
       +--------------+--------------------------------+--------+--------------+
       | 18c43 ... 33 | futuregrid/fedora-18           | ACTIVE |              |
       | 1a5fd ... e9 | futuregrid/ubuntu-14.04        | ACTIVE |              |
       | f4337 ... 44 | fg101/$PORTALNAME/my-ubuntu-01 | ACTIVE | c0bd ... bcc |
       +--------------+--------------------------------+--------+--------------+

If you want to download your customized image, you can do it with this::

       $ glance image-download --file "my-ubuntu-01.img" "fg101/$PORTALNAME/custom-ubuntu-01"

.. warning:: Please note that images not following this convention may
   be deleted without warning. Also ifyou do no longer need an image,
   please remove it.

Automate some initial configuration
-----------------------------------

You may want to install some packages into the image, enable root, and
add ssh authorized_keys. With the OpenStack cloud-init such steps can
be simplified.

Create a file(mycloudinit.txt) containing these lines::

       #cloud-config

       # Enable root login.
       disable_root: false

       # Install packages.
       packages:
       - apt-show-versions
       - wget
       - build-essential

       # Add some more ssh public keys.
       ssh_authorized_keys:
       - ssh-rsa AAAfkdfeiekf....fES7060rb myuser@s1
       - ssh-rsa AAAAAAkgeig78...skdfjeigi myuser@myhost

Now boot your instance with --user-data mycloudinit.txt like this::

       $ nova boot --flavor m1.small \
                   --image "futuregrid/ubuntu-14.04" \
                   --key_name $PORTALNAME-key \
                   --user-data mycloudinit.txt $PORTALNAME-002

You should be able to login to $PORTALNAME-002 as root, and the added packages are installed.

Get the latest version of Ubuntu Cloud Image and upload it to the OpenStack
---------------------------------------------------------------------------

.. note:: We will try to provide the latest images. E.g., currently in india openstack 
the ubuntu 14.04 image is officially available under name: futuregrid/ubuntu-14.04. So 
usually you can skip this section to simply use the one provided officially.

Several versions of Ubuntu cloud images are available at
`http://cloud-images.ubuntu.com/
<http://cloud-images.ubuntu.com/>`__. Choose the version you want and
download the file name with \*\*\*\*\*\*-cloudimg-amd64-disk1.img. For
example, downloading Ubuntu-14.04 is done like this::

       $ wget https://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-disk1.img

If you need a different version, please adapt the link accordingly.
You can upload the image with the glance client like this::

       $ glance image-create \
              --name fg101/$PORTALNAME/myimages/ubuntu-14.04 \
              --disk-format qcow2 \
              --container-format bare \
              --file trusty-server-cloudimg-amd64-disk1.img

Now your new image is listed on ``nova image-list`` and will be
available when the status become "ACTIVE".

Delete your instance
--------------------

You can delete your instance with::

       $ nova delete $PORTALNAME-002

Please do not forget to also delete your 001 vm if you no longer need
it.

   

How to change your password
---------------------------

#. Sometimes, users accidentally send password to a collaborator/support
   for debugging, and then regret. When you put yourself in the
   situation by mistake, don't worry. Just use keystone client and reset
   your password with::

       $ keystone password-update

Remember, you will also need to change it in your novarc. This can be
achieved by either editing your novarc file directly, or by editing
the file ~/.futuregrid/cloudmesh.yaml and recreating your novarc file.

Things to do when you need Euca2ools or EC2 interfaces
------------------------------------------------------

Even though the nova client and protocols will provide you with more
advanced features, some users still want to access OpenStack with EC2
compatible tools. We recommend against this and recommend instead that
you use `nova`. One such tool using eucarc files is euca2tools. We
explain briefly how you can access them.

#. Create a directory for putting eucarc, and create pk.pem, cert.pem
   and cacert.pem::

       cd ~/.futuregrid/openstack_havana
       nova x509-create-cert
       nova x509-get-root-cert
       ls -la

#. Create EC2_ACCESS_KEY and EC2_SECRET_KEY::

       keystone ec2-credentials-create

#. Create the file calle `~/.futuregrid/openstack_havana/eucarc` and put your EC2_ACCESS_KEY and
   EC2_SECRET_KEY that you obtained from the previous command into
   this file::

       export NOVA_KEY_DIR=$(cd $(dirname ${BASH_SOURCE[0]}) && pwd)
       export EC2_ACCESS_KEY="Your EC2_ACCESS_KEY"
       export EC2_SECRET_KEY="Your EC2_SECRET_KEY"
       export EC2_URL="http://i57r.idp.iu.futuregrid.org:8773/services/Cloud"
       export S3_URL="http://i57r.idp.iu.futuregrid.org:3333"
       export EC2_USER_ID=11
       export EC2_PRIVATE_KEY=${NOVA_KEY_DIR}/pk.pem
       export EC2_CERT=${NOVA_KEY_DIR}/cert.pem
       export NOVA_CERT=${NOVA_KEY_DIR}/cacert.pem
       export EUCALYPTUS_CERT=${NOVA_CERT}
       alias ec2-bundle-image="ec2-bundle-image --cert ${EC2_CERT} --privatekey ${EC2_PRIVATE_KEY} --user 42 --ec2cert ${NOVA_CERT}"
       alias ec2-upload-bundle="ec2-upload-bundle -a ${EC2_ACCESS_KEY} -s ${EC2_SECRET_KEY} --url ${S3_URL} --ec2cert ${NOVA_CERT}"

#. Confirm if euca2ools works::

       module load euca2ools/3.1.0
       source ~/.futuregrid/openstack_havana/eucarc
       euca-describe-images
       euca-describe-instances

.. note::

   Here's our known issues on using euca2ools or ec2 interface.

   - euca-upload-bundle with Boto 2.25.0 fails with "S3ResponseError: 404 Not Found".
   - tagging function such as euca-create-tags, euca-describe-tags fail with "InvalidRequest: The request is invalid."

.. _s-openstack-horizon:

Horizon GUI
---------------------------

Horizon is a graphical user interface/dashbooard for OpenStack. For
starting up VMs and stoping them by hand horizon may be a good
mechanism to manage your Virtual machines.  We have currently the
following horizon deployments available. However, please note that on
Alamo an older version of Openstack is run.
 
.. list-table:: Horizon endpoints
   :header-rows: 1
   :widths: 10,10,10,10,70

   * - Image
     - Version
     - Machine
     - Protocol
     - Description
   * - |image-horizon| 
     - Havana 
     - `India <https://openstack-h.india.futuregrid.org/horizon>`_
     - Native OpenStack
     - India offers a Graphical user interface to access
       OpenStack. For those interested in only managing a few images
       this may be a good way to start. The link to the GUI is 
       https://openstack-h.india.futuregrid.org/horizon The password
       can be found by following the method discussed above.


.. |image-horizon| image:: /images/fg-horizon.png 
   :width: 100px 


Screencasts
----------------------------------------------------------------------

This series of screencasts will walk you through the various ways on
how you can use OpenStack on FutureSystems. This includes the following:

* using openstack client command line tools to 

  * start, stop, assign ips, and query virtual machines
  * list images and flavors
  * to create security groups for login 
  * to log in to your virtual machine while using a key

* using the openstack horizon interface

.. list-table::
   :widths: 15 5 15 65
   :header-rows: 1

   * - Video
     - Length
     - Titles of the Lessons
     - Description of the Lessons
   * - |video-openstack| 
     - 11:55 min
     - Using OpenStack command line tools
     - This lesson explains you how to use the OpenStack Commandline
       tools on the FutureSystems cluster called sierra.futuregrid.org. 
       For written material, see section :ref:`s-openstack`.

       .. warning:: please replace sierra with india.

   * - |video-horizon| 
     - 8:30 min
     - Using OpenStack horizon GUI
     - This lesson explains you how to use the OpenStack Horizon to
       access the FutureSystems OpenStack IaaS framework on sierra.futuregrid.org. 
       For written material, see section :ref:`s-openstack-horizon`.

       .. warning:: please replace sierra with india.

.. |video-image| image:: /images/glyphicons_402_youtube.png 

.. |video-openstack| replace:: |video-image| :youtube:`xRVJfOaR23w`
.. |video-horizon| replace:: |video-image| :youtube:`JkNlWAUlxF0`
.. |video-eucalyptus| replace:: |video-image| :youtube:`D1v_twqWIxg`

Excersises
----------------------------------------------------------------------

#. Create a VM on india and login
#. Create a volume and attach it to the vm
#. Read up on the openstack web page what vilumes are for.
#. Log into horizon and explore the interface. Start up a VM, create a
   volume and attach it to the VM. Assign a public ip and log in.
