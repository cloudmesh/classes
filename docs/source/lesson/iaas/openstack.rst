.. _ref-openstack-beginners:

OpenStack for Beginners
======================================================================

.. sidebar:: Page Contents

   .. contents::
      :local:

Overview
----------------------------------------------------------------------

This lesson will introduce you to a very important topic to OpenStack core
components.

.. tip:: Duration: 1 hour

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have knowledge of

* `Overview OpenStack <overview_openstack.html>`_
* Create an ssh key by following :ref:`s-ssh-generate`
* Make sure to set the ``PORTALNAME`` appropriatly (``albert`` is just an example)::

    $ export PORTALNAME=albert

Description
----------------------------------------------------------------------

OpenStack is an open source cloud IaaS platform which provides compute,
storage, and networking resources with service components.  We explore these
components with a few examples in this lesson to have a taste of OpenStack
cloud on FutureSystems.

OpenStack consists of the following set of core components:

Table 1. Core components of OpenStack

=============   ==============  ======================= ======================
Component       Project Name    Main task               Sample Command
=============   ==============  ======================= ======================
Compute         Nova            vm management           nova boot 
Storage         Swift           Data warehouse          swift post
Network         Neutron         Network management      neutron net-create
Account         Keystone        Identity/Authentication keystone tenant-create
Web Interface   Horizon         Web User Interface      
=============   ==============  ======================= ======================

There are many other important components in OpenStack, for example, OpenStack
Heat provides automated deployment service with AWS CloudFormation template,
and OpenStack Telemetry (previously Ceilometer) offers a billing service based
on the measured data. Block Storage service named Cinter and virtual machine
image service named Glance are also major components in OpenStack.

Nova Compute
------------------------------------------------------------------------------

Nova Compute engine manages computing resources on OpenStack. It starts a
virtual machine instance with a choice of a machine (i.e. small, medium, large,
or cpu-intensive) and an image (i.e. Ubuntu, CentOS, etc.), and updates or
terminates the instance.

To have your own virtual machine (vm) instance on OpenStack cloud, you need to
submit your request of a vm instance via a command line tool (Nova client) or
on a dashboard Horizon.

.. note:: `Using Horizon on OpenStack <openstack_horizon.html>`_

Let's explore a few examples to allocate vm instances. In FutureSystems, you
need to be on the India login node.  (India is a hostname for OpenStack on
FutureSystems)

::

  $ ssh india.futuresystems.org

You should now load the ``openstack`` module to gain access to the
necessary commands.::

  $ module load openstack

Next, you need to set up your environment correctly to use some
OpenStack commands. This has been configured for you so you just need
to source the appropriate file::

  $ source ~/.cloudmesh/clouds/india/juno/openrc.sh


Adding your SSH key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Access to the machines we will start is authenticated using SSH.
First, we need to tell openstack about our ssh key.
This only needs to be done once for each public key you wish to register::

  $ nova keypair-add --pub-key ~/.ssh/id_rsa.pub $PORTALNAME-key

.. note::

   In order for this to work you **must** have an ssh key.  Please see
   the section :ref:`Generate an SSH Key <s-ssh-generate>` to do so.


For instance, in order to log into an openstack virtual machine from india, make sure you created an SSH keypair **on** india first, then add it to nova.
You can now see that your key is visible to OpenStack::

  $ nova keypair-list

  +-----------------+-------------------------------------------------+
  | Name            | Fingerprint                                     |
  +-----------------+-------------------------------------------------+
  | $PORTALNAME-key | 35:74:ee:be:14:4b:43:dd:ed:d8:cf:8e:de:13:ea:ce |
  +---------------+---------------------------------------------------+


.. note::

   You can check that the key registered with OpenStack (as shown by
   ``nova keypair-list``) is valid by comparing the fingerprint with
   that of your public key. Run the following to get your public key's
   fingerprint::

     $ ssh-keygen -lf ~/.ssh/id_rsa.pub

   The fingerprint is displayed as the colon-seperated two-digit
   hexadecimal values. Compare this with the fingerprint shown by::

     $ nova keypair-list




Launching a New Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting a new instance is simple. The following command starts a new
instance named *$PORTALNAME-tutorial1* with a Ubuntu 14.04 base image.  The size
of the machine will be **small**.


Boot the instance using the following command:

::

  $ nova boot --flavor m1.small --image futuresystems/ubuntu-14.04 --key_name $PORTALNAME-key $PORTALNAME-tutorial1


Here are some explanations for the arguments.

* ``boot`` is a sub command to start a new server.
* ``--flavor`` is a name for your machine size. ``m1.small`` typically
  has 1 vCPU and 2GB memories.
* ``--image`` is a name for your base image. ``nova image-list``
  displays all registered image.
* ``--key_name`` is a key name to use for SSH connection. This key
  should be registered on Nova Compute. Try ``nova keypair-list`` to
  see registered keys.
* ``$PORTALNAME-tutorial1`` is a name for your vm instance.


Some useful ``nova`` subcommands are:

* ``list``: list active servers
* ``flavor-list``: list of available flavors
* ``host-list``: available hosts
* ``keypair-list``: keypairs for a user

You can get more information by executing the ``nova -h`` command.

Floating IP Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If we want our machine to be accessible from outside the private
network, we need to create a "floating IP address" and associate it
with an instance.  Since floating ips come from some pool of available
addresses, we can list the pools using the ``floating-ip-pool-list``
subcommand::

  $ nova floating-ip-pool-list
  +---------+
  | name    |
  +---------+
  | ext-net |
  +---------+

We then create an ip for our instance::

  $ nova floating-ip-create ext-net
  +-----------------+-----------+----------+---------+
  | Ip              | Server Id | Fixed Ip | Pool    |
  +-----------------+-----------+----------+---------+
  | 149.165.158.107 | -         | -        | ext-net |
  +-----------------+-----------+----------+---------+

Now that the ip has been created, associate it with our instance::

  $ nova floating-ip-associate
  usage: nova floating-ip-associate [--fixed-address <fixed_address>]
                                    <server> <address>

  $ nova floating-ip-associate $PORTALNAME-tutorial1 149.165.158.107


Access to VM Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* We login to the VM instance we just created using SSH.::

    $ ssh ubuntu@[IP ADDRESS]

* To find out the ``[IP ADDRESS]``, use ``nova list`` command::

          $ nova list
          +--------------------------------------+-----------------------+--------+------------+-------------+--------------------------------------+
          | ID                                   | Name                  | Status | Task State | Power State | Networks                             |
          +--------------------------------------+-----------------------+--------+------------+-------------+--------------------------------------+
          | 7ea44f58-ddd8-49b1-b655-4aa00b819d0c | $PORTALNAME-tutorial1 | ACTIVE | -          | Running     | int-net=10.23.2.182, 149.165.158.107 |
          ...

* Use the internal IP address followed by ``int-net=`` in your VM instance. In
  this example we have ``10.23.2.182``. You **have to use your IP address** to
  gain access. So now, we run::
    
    $ ssh ubuntu@10.23.2.182

**REPLACE** the IP address ``10.23.2.182`` with one you have.

You expect to see welcome message of your Ubuntu 14.04 VM instance.

::


  Welcome to Ubuntu 14.04.2 LTS (GNU/Linux 3.13.0-46-generic x86_64)

  * Documentation:  https://help.ubuntu.com/

  System information as of Mon Apr  6 17:42:15 UTC 2015

  System load:  0.0               Processes:           69
  Usage of /:   5.2% of 19.65GB   Users logged in:     0
  Memory usage: 5%                IP address for eth0: 10.23.2.182
  Swap usage:   0%

  Graph this data and manage this system at:
  https://landscape.canonical.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
  http://www.ubuntu.com/business/services/cloud

  0 packages can be updated.
  0 updates are security updates.

  Last login: Mon Apr  6 17:42:15 2015 from 149.165.159.252
  ubuntu@$PORTALNAME-tutorial1:~$ 

Now you are on the VM instance.

Deleting VM Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can delete your instance with:

::

  $ nova delete $PORTALNAME-tutorial1

Returning Floating IP Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your instance is deleted, your floating ip address will become available,
and nova floating-ip-list should show the output like this::

        $ nova floating-ip-list
        +-----------------+-----------+----------+---------+
        | Ip              | Server Id | Fixed Ip | Pool    |
        +-----------------+-----------+----------+---------+
        | 149.165.158.107 | -         | -        | ext-net |
        +-----------------+-----------+----------+---------+

To de-allocate the floating IP address::

   $  nova floating-ip-delete 149.165.158.107

.. _lab-openstack-1:

Lab - OpenStack - Launch an Instance
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

* Launch a new medium instance with a CentOS image using a different
  key (call it ``openstack-ex1-key``). Name the CentOS instance
  ``$PORTALNAME-tutorial1-ex1`` and make sure both instances are running using the
  ``nova list`` command.
* Allocate a floating ip address to the instance that you just launched.

Glance Image Management
------------------------------------------------------------------------------

OpenStack Glance is a virtual machine (VM) image management tool which
registers, manages, shares or deletes machine images. The registered VM image
can be used to launch a compute instance from users if it is open to public.
Typically various operating systems are provided as basic VM images and users
can add a variation to the images for saving their work on a VM instance.
The following sub commands tell what you can do:

* image-create: Create a new image
* image-delete: Delete specified image(s)
* image-download: Download a specific image
* image-list: List images you can access
* image-show: Describe a specific image
* image-update: Update a specific image
* member-create: Share a specific image with a tenant
* member-delete: Remove a shared image from a tenant
* member-list: Describe sharing permissions by image or tenant
* bash-completion: Prints all of the commands and options to stdout

These commands are available in glance version 0.15.0.

Creating a New Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following command will register Ubuntu 14.04 image to OpenStack cloud. You
can download cloud images from Ubuntu Cloud.

::

  $ glance image-create \
  --name $PROJECT/$PORTALNAME/myimages/ubuntu-14.04 \
  --disk-format qcow2 \
  --container-format bare \
  --file trusty-server-cloudimg-amd64-disk1.img

If your image registered successfully, you will see ACTIVE status in the image-list command.

::

  $ glance image-list
  
Keystone Account and Authenticaion
-------------------------------------------------------------------------------

OpenStack Keystone manages user accounts and provides authentication service
using tokens. If you need to add a new user or a group, you may use keystone
client tool to register. As a developer, you use Keystone for user
authentication with tokens when you send a service request via OpenStack API.
The token is a convinient method to deal with authenticaion instead of a pair
of username and password. Let's explore a few basic commands of OpenStack
Keystone.

.. Note:: Keystone commands are only available to administrator

Project Creation (Tenant)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OpenStack manages user accounts with a group. OpenStack represents a group as a
*project* or a *tenant* interchangeably. Each user should participate in at
least a single project, they can join multiple projects though. With a group of
users, it is convenient to manage different settings across multiple groups.
For example, you can set limits of 10 instances to project1 but project2 may
have higher or smaller size of vm instances.

::

  $ keystone tenant-create --name=project1 --description="futuresystems project 1"

User Creation 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a new user, you need a tenant (project) id, if you provide a
group-based cloud service.

::

  $ keystone user-create --name=albert \
    --pass=*** \
    --tenant_id=*** \
    --email=albert@futuresystems.org

List of Users or Projects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Try ``user-list`` or ``tenant-list`` sub command to see a list of users or
projects.

::

  $ keystone user-list

  or

  $ keystone tenant-list

.. tip:: Try ``keystone`` command itself. The help message shows that available
        sub commands including tenant-create, user-create, user-list and
        tenant-list.

Role management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Project members need to have different privileges to control allocated
resources to the project.  For example, *albert* needs an admin permission to
terminate or update other user's vm instances in a same project.  OpenStack
Keystone has a role management with a pair of a user and a project.

The following commands are useful to manage roles in a project:

* role-create: Create new role
* role-delete: Delete role
* role-get: Display role details
* user-role-add: Add role to user
* user-role-list: List roles granted to a user
* user-role-remove: Remove role from user

Swift Storage 
------------------------------------------------------------------------------

Swift is an object storage service on OpenStack like Amazon Simple Storage
Service (S3). If you are looking for a block storage, OpenStack Cinder is one
for you.

The following sub commands tell what you can do:

* delete: Delete a container or objects within a container
* download: Download objects from containers
* list: Lists the containers for the account or the objects for a container
* post: Updates meta information for the account, container, or object; creates
  containers if not present 
* stat: Displays information for the account,
  container, or object
* upload: Uploads files or directories to the given container
* capabilities: List cluster capabilities
* tempurl: Create a temporary URL

.. note:: Swift Storage is not available on FutureSystems.

.. tip:: Not to decide Swift or Cinder? If you need a large disk space mounted
        on your VM instance, Cinder is useful.  If you need to get access of a
        file across multiple servers using API? Swift is the answer.

Neutron Network
------------------------------------------------------------------------------

Neutron is a OpenStack Networking service to manage NAT, firewall, etc. This
type of tasks is for OpenStack cloud administrator. We briefly explore a few
commands available on Neutron to understand basic services on OpenStack
Networking.

* neutron net-list: List Current Neutron Networks
* neutron subnet-list: List Current Neutron Subnets
* neutron security-group-create <SEC-GROUP-NAME>: Create Neutron Security Group
* neutron security-group-rule-create --direction <ingress OR egress>
  --ethertype <IPv4 or IPv6> --protocol <PROTOCOL> --port-range-min
  <PORT-NUMBER> --port-range-max <PORT-NUMBER> <SEC-GROUP-NAME>: Add Rules to
  Neutron Security Group
* neutron floatingip-create <NET-NAME>: Create a Neutron Floating IP Pool
  - If you need N number of floating IP addresses, run this command N number of times:
* neutron port-create <NET-NAME> --fixed-ip ip_address=<IP-ADDRESS>: Create a
  Neutron Port with a Fixed IP Address

Example 1. add a rule to the default Neutron Security Group to allow SSH access
to instances::

        neutron security-group-rule-create --direction ingress \
        --ethertype IPv4 --protocol tcp \
        --port-range-min 22 --port-range-max 22 default

Example 2. add a rule to the default Neutron Security Group to allow ICMP
communication to instances::

        neutron security-group-rule-create --direction ingress \
        --ethertype IPv4 --protocol icmp default

 
Exercises
----------------------------------------------------------------------

1. Try to run Python CherryPy or Apache Web Server in your virtual server.
   It requires:

- VM instance creation
- CherryPY or HTTP Server installation using package manager (pip or apt-get)
- HTTP, HTTPs ports open using security groups
- Floating IP allocation 

.. note::

   Make sure to open ports 80 and 8080 in the openstack security group::

     $ nova secgroup-list-rules default
     +-------------+-----------+---------+-----------+--------------+
     | IP Protocol | From Port | To Port | IP Range  | Source Group |
     +-------------+-----------+---------+-----------+--------------+
     | tcp         | 8888      | 8888    | 0.0.0.0/0 |              |
     | tcp         | 22        | 22      | 0.0.0.0/0 |              |
     | icmp        | -1        | -1      | 0.0.0.0/0 |              |
     |             |           |         |           | default      |
     | tcp         | 8080      | 8080    | 0.0.0.0/0 |              |
     | tcp         | 80        | 80      | 0.0.0.0/0 |              |
     |             |           |         |           | default      |
     | tcp         | 5000      | 5000    | 0.0.0.0/0 |              |
     +-------------+-----------+---------+-----------+--------------+

   If you do not see ports 80 and 8080 present, add them like so::

     $ nova secgroup-add-rule default tcp 80 80 0.0.0.0/0
     $ nova secgroup-add-rule default tcp 8080 8080 0.0.0.0/0
   


.. note:: Return your leased resources after your practice is completed. 1)
        Terminate your instance, 2) Deallocate IP address



Next Step
-----------

In the next page, we will learn how to start a virtual server using OpenStack
Horizon.

`OpenStack horizon <openstack_horizon.html>`_

