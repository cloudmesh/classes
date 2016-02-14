Ansible
-------------------------------------------------------------------------------

Ansible is an IT automation tool which deploys software and configures systems
on multiple servers using SSH protocol. Python based Ansible stores information
about deployment and configuration in a yaml format file, named Ansible
Playbook. Tasks defined in the playbook allows you to have identical
configurations and software across multiple machines in your infrastructure.
This section, we introduce basic commands of ``ansible`` to introduce Ansible
software on FutureSystems.  In the next section, we will explore advanced use
of ``ansible`` on FutureSystems.

Tutorial: Ansible Basic commands
-------------------------------------------------------------------------------

.. tip:: approximate time 45 minutes

In this tutorial, we are going to learn basic commands of Ansible software.
Keep in mind that ``ansible`` is a main program and ``playbook`` is a template
that you would like to use. You may have several playbooks in your Ansible.

Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to continue, ensure you have loaded the appropriate modules
and registered a key with openstack.
The modules needed are:

- python
- openstack

Additionally, you can manage virtual machines using the `openstack web portal`_.
The login credentials are:

- username: your FutureSystems portal id
- password: the value of ``OS_PASSWORD`` in ``~/.cloudmesh/clouds/india/kilo/openrc.sh``

.. _openstack web portal: https://openstack.futuresystems.org/horizon/project/


Ansible has two types of servers: a control machine and a managed node.
Typically, a single control machine executes tasks over the one or more nodes.

Control machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You will use your personal VM as our control machine.
Let's install Ansible from via PyPI, if you haven't installed.

You will create a seperate virtualenv for this::

  $ virtualenv $HOME/bdossp-sp16
  $ source $HOME/bdossp-sp16/bin/activate

Now install Ansible::

  $ pip install --trusted-host pypi.python.org ansible

Managed machines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We need to launch some virtual machines.  Go to the `openstack web
portal`_. Make sure that the correct projectid is selected in the top
left (just to the right of the "openstack" logo"). For example,
``fg491`` or ``fg465``.  Go to ``Compute ---> Instances ---> Launch
Instance`` to start the procedure for launching an instance. Make sure
to provide an instance name and specify a keypair.

Launch several instances, say three.  Once they launch, note down the
IP addresses. We will need these later.


.. tip::

   As a sanity check, make sure you can ssh into these nodes from ``india``::

     $ ssh ubuntu@$IP

   where ``$IP`` is the IP address of the instance you noted down.


Explanation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ansible works by executing **modules** on an **inventory** of
machines.  Since many machines can be managed, this inventory is
written to a file.  Within the inventory file, groups of machines can
be named arbitrarily.  These names should have some meaning however:
for example "production", "development", and "testing" may be
appropriate names.

The modules executed update the state of the machine. For instance,
the ``apt`` module allows software to be installed. While the
``shell`` module exists and is a convenient way to execute shell
commands on the managed nodes it is run every time. Other modules,
like ``apt``, allow ansible to be intelligent about changing state:
only necessary modifications are done. For instance, of an application
is already installed, there is not reason to reinstall.

Since ansible requires ssh access from controller to managed nodes, it
can be run as an unpriviledged user, rather than requiring
administrative access on the controller.

The ``ansible.cfg`` file can be used to override certain ansible
configuration settings.

Please see the `ansible documentation
<http://docs.ansible.com/index.html>`_ for further details.


Using Ansible
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that we have some nodes we wish to manage, let us use ansible to
control them.

Inventory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, we need our inventory of managed machines.
Create an ``inventory.txt`` file with contents similar to the following::

  [ansible-test]
  10.39.1.1
  10.38.1.2

.. important::

   Do not copy-and-paste this. Use the IP addresses of the machines
   you started earlier.


Ansible SSH Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We need to override some of ansible default ssh settings.
Create a ``ansible.cfg`` file with the following contents::

  [ssh_connection]
  ssh_args = -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null

These options modify the behavior of ssh when connecting to the
managed nodes. Disabling the ``StrictHostKeyChecking`` option prevents
ssh from requiring that the node be present in you
``~/.ssh/known_hosts`` file. SSH will still update the file and so we
override ``UserKnownHostsFile``.

.. tip::

   If you are using a different ssh key for authentication, such as
   one generated by OpenStack's ``nova keypair-add`` command, you can
   specify the path to the private key in the ``ansible.cfg`` file by
   adding::

     -o IdentityFile=~/.ssh/$PORTALID-india-key

Shell module: Hello World
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's try to run 'echo Hello World' over the nodes.

::

  ansible all -i inventory.txt -u ubuntu -a "echo Hello World"

An explanation of the flags:

- ``-i`` specifies the inventory file
- ``-u`` specifies the user on the managed machines
- ``-c`` use ssh rather than paramiko so that our overrides in
  ``ansible.cfg`` take effect.
- ``-a`` specifies the module arguments to run.

You expect to see::

        10.39.1.1 | success | rc=0 >>
        Hello World

        10.39.1.2 | success | rc=0 >>
        Hello World

Ping module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run a simple command "ping".

::

  ansible all -i inventory.txt -u ubuntu -c ssh -m ping

You expect to see::

        10.39.1.1 | success >> {
            "changed": false,
            "ping": "pong"
        }

        10.39.1.2 | success >> {
            "changed": false,
            "ping": "pong"
        }



More examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can find more examples from here: https://github.com/ansible/ansible-examples

Reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The main tutorial from Ansible is here: https://docs.ansible.com/installation/ubuntulinux/


