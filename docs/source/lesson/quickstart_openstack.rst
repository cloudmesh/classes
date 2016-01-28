QuickStart Guide for OpenStack on FutureSystems
===============================================================================

This lesson provides a short guide to start using OpenStack on FutureSystems.
More lessons e.g. components of OpenStack including storage, network and image
will be follwoing in the course. This material is prepared for the
first time users only.

Prerequisite
-------------------------------------------------------------------------------

* Portal Account
* SSH Key Registration at portal.futuresystems.org
* FutureSystems Project Membership

Overview
-------------------------------------------------------------------------------

The following contents are discussed in this quickstart guide.

* SSH Access to india.futuresystems.org
* ``nova`` command
* OpenStack Credential
* Required Options
   - flavor
   - image
   - key
   - network ID
* Launch/Terminate Instance

Login to India Login Node
-------------------------------------------------------------------------------

First step, you need to be in india.futuresystems.org. Use one of SSH Client
tools, for example:

* Putty, Cygwin or OpenSSH on Windows
* Terminal on Mac OS or Linux

SSH into india, for example::

  ssh PORTALUSERNAME@india.futuresystems.org

.. note:: Replace PORTALUSERNAME with your actual portal account ID

.. tips:: If you see 'Permission Denied' SSH error, it's probably because of
  either wrong public/private keys or delays in account creation. '-vvv'
  verbose option to `ssh` command is helpful which generates debugging
  messages in case you want to find out issues.

Connection is granted with the Welcome message like:

::

  Welcome to india.futuresystems.org

  =======================================================================

  ANNOUNCEMENT
  ------------
  * Planed Outage: 12/01/15 8:00-23:59 EDT: All systems will be offline 
    for monthly maintenance. Please plan accordingly.

  * SSH keys must be registered in the portal. Local authorized_keys
    are disabled.

  * Do not run jobs on the login node. Any long-running jobs on the 
    login node will be terminated without warning.

  SUPPORT
  -------
  If you have a problem, please submit a ticket.
   --> https://portal.futuresystems.org/help

Nova Command Tool
-------------------------------------------------------------------------------

OpenStack Compute ``nova`` command is enabled on India by ``module`` command
like::

  module load openstack

This command can be added to ``.bash_profile`` to enable OpenStack Client
commands when you login. This way you don't need to run the module command
every time when you open a new SSH terminal for India. For example::

  echo "module load openstack" >> ~/.bash_profile

See the ``.bash_profile`` file by::

  cat ~/.bash_profile

If you successfully added the command, the file content looks like::

  # .bash_profile

  # Get the aliases and functions
  if [ -f ~/bashrc ]; then
        . ~/.bashrc
  fi

  module load openstack

See the last line of the file. ``module`` command is added. ``.bash_profile`` or
``.bashrc`` exists in your home directory to initialze a shell when you login.
Any commands or environmental variables e.g. PATH in these files is going to be
executed. Find more information online, if you are interested in. `Bash Startup
Files from GNU
<https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html>`_

Now, we can use ``nova`` command, try and see help messages::

  $ nova
  usage: nova [--version] [--debug] [--os-cache] [--timings]
              [--os-auth-token OS_AUTH_TOKEN]
              [--os-tenant-name <auth-tenant-name>]
              [--os-tenant-id <auth-tenant-id>] [--os-region-name <region-name>]
              [--os-auth-system <auth-system>] [--service-type <service-type>]
              [--service-name <service-name>]
              [--volume-service-name <volume-service-name>]
              [--os-endpoint-type <endpoint-type>]
              [--os-compute-api-version <compute-api-ver>]
              [--bypass-url <bypass-url>] [--insecure]
              [--os-cacert <ca-certificate>] [--os-cert <certificate>]
              [--os-key <key>] [--timeout <seconds>] [--os-auth-url OS_AUTH_URL]
              [--os-domain-id OS_DOMAIN_ID] [--os-domain-name OS_DOMAIN_NAME]
              [--os-project-id OS_PROJECT_ID]
              [--os-project-name OS_PROJECT_NAME]
              [--os-project-domain-id OS_PROJECT_DOMAIN_ID]
              [--os-project-domain-name OS_PROJECT_DOMAIN_NAME]
              [--os-trust-id OS_TRUST_ID] [--os-user-id OS_USER_ID]
              [--os-user-name OS_USERNAME]
              [--os-user-domain-id OS_USER_DOMAIN_ID]
              [--os-user-domain-name OS_USER_DOMAIN_NAME]
              [--os-password OS_PASSWORD]
              <subcommand> ...

              Command-line interface to the OpenStack Nova API.

   ...

OpenStack provides lots of CLI tools but we focus on Compute API ``nova`` to
learn how VM instances can be started or stopped. Here are some useful
resources.

* `OpenStack command-line clients <http://docs.openstack.org/user-guide/cli.html>`_
* `Launch an instance from an image
  <http://docs.openstack.org/user-guide/cli_nova_launch_instance_from_image.html>`_

OpenStack Credential 
-------------------------------------------------------------------------------

``nova`` command is ready but we still need a OpenStack credential because we
use OpenStack under a project membership and OpenStack verifies our identity by
looking at OpenStack credentials. It is simply done by:

::

  source ~/.cloudmeh/clouds/india/kilo/openrc.sh

and select project by::

  source ~/.cloudmeh/clouds/india/kilo/fg491

Choose a different file if you are in the other project. We chose 'fg491' in
this example.


Let's try one of ``nova`` sub command, for example, see a list of VM images by::

  nova image-list

You may see some images available on your project like::

        +--------------------------------------+------------------+--------+--------------------------------------+
        | ID                                   | Name             | Status | Server                               |
        +--------------------------------------+------------------+--------+--------------------------------------+
        | 0245beac-f731-427c-8eb0-4e434af51cf6 | CoreOS-Alpha     | ACTIVE |                                      |
        | 9eb8416d-1313-4748-a832-5fe0ecbbdffc | Ubuntu-14.04-64  | ACTIVE |                                      |
        | f51bd217-f809-46a1-9cdb-604d977ad4e9 | Ubuntu-15.10-64  | ACTIVE |                                      |
        | 1a80ac5b-4e57-479d-bed6-42e1448e6785 | cirros           | ACTIVE |                                      |
        | 41b2320f-8c3b-4bd9-8701-a96bdf59100d | fedora23         | ACTIVE |                                      |
        +--------------------------------------+------------------+--------+--------------------------------------+

If the loading credential is failed, you see the errors likes::

        ERROR (CommandError): You must provide a username or user id via
        --os-username, --os-user-id, env[OS_USERNAME] or env[OS_USER_ID]

This is because either you do not have ``openrc.sh`` or a project file i.e.
``fg491`` or a credential file is broken. Check your file and report your issue
to the course email or the ticket system on FutureSystems.

Required Options
-------------------------------------------------------------------------------

There are a few options required to start a new VM instance on OpenStack. Let's
talk about SSH Key first.


SSH Key on OpenStack
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We will create a VM instance and use it like a normal server which means that
we need to use SSH Key to get access to the instance. Typing password is not
allowed. This is **a different SSH Key** which is not the key that you
registered on either the portal.futuresystems.org or github.com.

:: 

  nova keypair-add quickstart-key > ~/.ssh/quickstart-key

This command does two things: one is registering a new public key to Openstack
and the other one is saving a new private key to your .ssh directory. 

Let's check your new keypair by::

   nova keypair-list

You expect to see *quickstart-key* in your list of keys::

   +----------------+-------------------------------------------------+
   | Name           | Fingerprint                                     |
   +----------------+-------------------------------------------------+
   | quickstart-key | 68:22:1f:e7:d0:92:7a:68:d8:f5:3d:d2:ca:cd:cd:b9 |
   +----------------+-------------------------------------------------+

And your private key is::

   ls -al ~/.ssh/quickstart-key

The file should exist::

   -rw-r--r-- 1 abc users 1751 Jan 25 00:10 /N/u/abc/.ssh/quickstart-key

The permission is too open, change the file permission with the owners only
read-write permission by::

   chmod 600 ~/.ssh/quickstart-key

And run ``ls`` command again to confirm the file permission. ``-rw-------`` is
expected.

Passphrase on Private Key
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

It is important that we have passphrase-enabled SSH key. Let's add a
passphrase::

        ssh-keygen -p -f ~/.ssh/quickstart-key

Provide your passphrase, your private key will be updated::

   Enter new passphrase (empty for no passphrase): 
   Enter same passphrase again: 
   Your identification has been saved with the new passphrase.

VM Images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We will launch a new VM instance with a VM image, let's see the list of images
by::

  nova image-list

We use ``Ubuntu-15.10-64`` the latest Ubuntu distribution with 64 bit::

        +--------------------------------------+------------------+--------+--------------------------------------+
        | ID                                   | Name             | Status | Server                               |
        +--------------------------------------+------------------+--------+--------------------------------------+
        | 0245beac-f731-427c-8eb0-4e434af51cf6 | CoreOS-Alpha     | ACTIVE |                                      |
        | 9eb8416d-1313-4748-a832-5fe0ecbbdffc | Ubuntu-14.04-64  | ACTIVE |                                      |
        | f51bd217-f809-46a1-9cdb-604d977ad4e9 | Ubuntu-15.10-64  | ACTIVE |                                      |
        | 1a80ac5b-4e57-479d-bed6-42e1448e6785 | cirros           | ACTIVE |                                      |
        | 41b2320f-8c3b-4bd9-8701-a96bdf59100d | fedora23         | ACTIVE |                                      |
        +--------------------------------------+------------------+--------+--------------------------------------+

Server Sizes (Flavors)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We can choose a size of a new VM instance, the flavor.

Try ``nova`` command like::

   nova flavor-list
                              
We use ``m1.small`` but available flavors are::

        +----+-----------+-----------+------+-----------+------+-------+-------------+-----------+
        | ID | Name      | Memory_MB | Disk | Ephemeral | Swap | VCPUs | RXTX_Factor | Is_Public |
        +----+-----------+-----------+------+-----------+------+-------+-------------+-----------+
        | 1  | m1.tiny   | 512       | 1    | 0         |      | 1     | 1.0         | True      |
        | 2  | m1.small  | 2048      | 20   | 0         |      | 1     | 1.0         | True      |
        | 3  | m1.medium | 4096      | 40   | 0         |      | 2     | 1.0         | True      |
        | 4  | m1.large  | 8192      | 80   | 0         |      | 4     | 1.0         | True      |
        | 5  | m1.xlarge | 16384     | 160  | 0         |      | 8     | 1.0         | True      |
        +----+-----------+-----------+------+-----------+------+-------+-------------+-----------+

Network ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use a private network assigned to our project in OpenStack Kilo.

Try ``nova`` command like::

    nova network-list

We use ``fg491-net`` the private network for fg491 project from::

        +--------------------------------------+-----------+------+
        | ID                                   | Label     | Cidr |
        +--------------------------------------+-----------+------+
        | a9815176-daa7-45ef-98ca-60dff58e7baf | ext-net   | -    |
        | e5228c15-38af-4f91-a6de-1590d399427e | fg491-net | -    |
        +--------------------------------------+-----------+------+

Launch a New VM Instance
-------------------------------------------------------------------------------

We are now ready to start a new VM instance with the options that we chose earlier.

* Image: Ubuntu-15.10-64
* Flavor: m1.small
* Key: quickstart-key
* Network ID: e5228c15-38af-4f91-a6de-1590d399427e
* VM Name: quickstart-$USER

Launch a VM instance by::

  nova boot --image Ubuntu-15.10-64 --flavor m1.small --key-name quickstart-key
  --nic net-id=e5228c15-38af-4f91-a6de-1590d399427e quickstart-$USER

Your new VM instance named *quickstart-$USER* will be created shortly. Your
launching request is accepted with the messages like::

        +--------------------------------------+--------------------------------------------------------+
        | Property                             | Value                                                  |
        +--------------------------------------+--------------------------------------------------------+
        | OS-DCF:diskConfig                    | MANUAL                                                 |
        | OS-EXT-AZ:availability_zone          | nova                                                   |
        | OS-EXT-STS:power_state               | 0                                                      |
        | OS-EXT-STS:task_state                | scheduling                                             |
        | OS-EXT-STS:vm_state                  | building                                               |
        | OS-SRV-USG:launched_at               | -                                                      |
        | OS-SRV-USG:terminated_at             | -                                                      |
        | accessIPv4                           |                                                        |
        | accessIPv6                           |                                                        |
        | adminPass                            | juXmTsv66                                              |
        | config_drive                         |                                                        |
        | created                              | 2016-01-26T19:42:32Z                                   |
        | flavor                               | m1.small (2)                                           |
        | hostId                               |                                                        |
        | id                                   | a700fad0-ad69-4036-b184-cdca18d516a4                   |
        | image                                | Ubuntu-15.10-64 (f51bd217-f809-46a1-9cdb-604d977ad4e9) |
        | key_name                             | quickstart-key                                         |
        | metadata                             | {}                                                     |
        | name                                 | quickstart-abc                                         |
        | os-extended-volumes:volumes_attached | []                                                     |
        | progress                             | 0                                                      |
        | security_groups                      | default                                                |
        | status                               | BUILD                                                  |
        | tenant_id                            | 0193f2237d3d342f106fbf04bdd2f                          |
        | updated                              | 2016-01-26T19:42:33Z                                   |
        | user_id                              | 4186710ab90a642455889d3a8b51a                          |
        +--------------------------------------+--------------------------------------------------------+

Access to VM
-------------------------------------------------------------------------------

Booting up a VM instance takes a few minutes. Let's check its status by::

  nova list

If you see it is active and running like ::  

        +--------------------------------------+------------------+--------+------------+-------------+--------------------+
        | ID                                   | Name             | Status | Task State | Power State | Networks           |
        +--------------------------------------+------------------+--------+------------+-------------+--------------------+
        | a700fad0-ad69-4036-b184-cdca18d516a4 | quickstart-abc   | ACTIVE | -          | Running     | fg491-net=10.0.6.4 |
        +--------------------------------------+------------------+--------+------------+-------------+--------------------+

We may try SSH into the *quickstart-$USER* VM. Note that you see your portal ID
in *abc*. SSH into the private IP addres and like you SSHed to India but with a
different SSH key like::

        ssh -i ~/.ssh/quickstart-key 10.0.6.4 -l ubuntu

``-l ubuntu`` parameter is added to specify a default user name of the base
image *Ubuntu-15.10-64*.

You provide your SSH passphrase to get access and you will see a welcome
message on your new Ubuntu 15.10 virtual server::

        Enter passphrase for key '/N/u/hrlee/.ssh/quickstart-key': 
        Welcome to Ubuntu 15.10 (GNU/Linux 4.2.0-16-generic x86_64)

         * Documentation:  https://help.ubuntu.com/

           Get cloud support with Ubuntu Advantage Cloud Guest:
               http://www.ubuntu.com/business/services/cloud

         0 packages can be updated.         
         0 updates are security updates.


         The programs included with the Ubuntu system are free software;
         the exact distribution terms for each program are described in the
         individual files in /usr/share/doc/*/copyright.

         Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
         applicable law.

         To run a command as administrator (user "root"), use "sudo <command>".
         See "man sudo_root" for details.

         ubuntu@quickstart-abc:~$ 

You are the owner of your new VM instance. You can install any software and
manage services as a root with sudo command, if you like.

Terminate VM
-------------------------------------------------------------------------------

Now, we need to learn how to terminate a VM instance once our work on a vm is
completed. Running idle VM instances is not allowed in the course because we
share compute resources with other students.

Use ``nova`` command to terminate::

  nova delete a700fad0-ad69-4036-b184-cdca18d516a4

or::
  
  nova delete quickstart-$USER

You will see the message like::
        
        Request to delete server a700fad0-ad69-4036-b184-cdca18d516a4 has been accepted.

ID is unique but Name of your VM is not. Try to use ID when you terminate VM
instance.

FAQ
-------

Q. ``nova`` command doesn't work with the error::

   ERROR (Unauthorized): The request you have made requires authentication. (HTTP 401) (Request-ID: req-82f94837-78e7-4abd-a413-ff7645c45a7f)

A. Your OpenStack credential (i.e. openrc.sh) is not valid. Check your file and project ID. If a problem is consistent, report to the course team.

Any Questions?
-------------------------------------------------------------------------------

Please use Slack or the course email, if you have issues or questions regarding
this tutorial.

