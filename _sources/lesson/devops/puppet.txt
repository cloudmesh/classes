
.. _ref-class-lesson-devops-puppet:

Puppet
======================================================================

Overview
----------------------------------------------------------------------

This lesson will introduce you to a very important topic to Puppet, an open
source configuration management tool.

.. tip:: Duration: 1 hour

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have knowledge of

* `OpenStack for Beginners <../iaas/openstack.html>`_

Description
----------------------------------------------------------------------

Puppet is an open source configuration management software to configure systems
declaratively. If you describe system resources and configurations using
Puppet's declarative language (combination of JSON and Ruby) or Ruby DSL
(Domain Specific Language), Puppet discovers servers (nodes) and applies the
instructions that you described to the target machines. Puppet manages
configurations and installations with a client-server model like Chef.  You
need to use command line tools or web interfaces to communicate with a Puppet
server. There are many similar features and functionalities between Chef and
Puppet. Try to compare these two tools when you use their commands tools or
write the scripts. Chef calls the script as a ``Recipe``, and Puppet calls it
as a ``manifest``.

Open Source Puppet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Puppet Labs supports Puppet software in two different versions. This lesson
uses an open source Puppet instead of Puppet Enterprise which is a commercial
version of Puppet. A few features are only available in the Enterprise version
but the core parts of Puppet are identical in both.

Installation Puppet
-------------------------------------------------------------------------------

This lesson is based on FutureSystems which means you create a VM instance on
India OpenStack and install Puppet on top of it. If you prefer to use other
virtual environments, we recommend to use Vagrant and VirtualBox.

We assume you use a OpenStack instance on FutureSystems.

.. note:: If don't know how to launch a new instance? `See here
    <../iaas/openstack.html#launching-a-new-instance>`_

Guideline on India FutureSystems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You *DON'T* install Puppet on India. If you see the cursor like:

::

  [albert@i136 ~]$

You *should NOT* install any program.

You have to log into *your VM instance* to install Puppet. ``i136`` is a India
login node which is like a gateway.  You are supposed not to perform any tasks
on India, especially if you require ``root`` privileges. Please create a VM
instance on India OpenStack and SSH into your VM to run and install your
software. You will have a full access of your virtual machine instance.

Quick instructions
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

* Launch a VM instance is::

    nova boot --flavor m1.small --image futuresystems/ubuntu-14.04 --key_name $USER-key $USER-puppet

* Once your VM instance is ready, try to login using SSH::

    ssh ubuntu@[IP ADDRESS]

Puppet on Ubuntu 14.04 (Standalone Mode)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use a VM instance with a Ubuntu 14.04 image. The installation commands are::

        wget https://apt.puppetlabs.com/puppetlabs-release-trusty.deb
        sudo dpkg -i puppetlabs-release-trusty.deb
        sudo apt-get update
        sudo apt-get install puppet

.. info:: This is a client installation only. If you'd like to install Puppet
          Server, please read the instructions here:
          http://docs.puppetlabs.com/guides/install_puppet/install_debian_ubuntu.html

Check your installation::

  puppet --version

You expect to see 3.7.5 or higher version, otherwise your installation is incomplete.

``root`` Access
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We will install Puppet and other software using ``root`` account. Using ``root``
account means that you have a permission to use entire system resources without
any restriction. Since this lesson includes a couple of examples using Puppet, we
strongly recommend to use OpenStack VM instance on FutureSystems. DON'T try to
install Puppet on your local machine or on the ``india.futuresystems.org`` host.
Use a benefit of VM instance which you can easily delete and re-create a new
one.

On a VM instance, simply run a switch user command::

  ubuntu@puppet:~$ sudo su -

If you see ``root`` label, you are in ``root`` account on your machine::

  root@puppet:~#


Update Hostname
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you see ``sudo: unable to resolve host``, try to add hostname with the
following command::

  echo -e "\n127.0.1.1 $HOSTNAME" >> /etc/hosts


A Puppet Template - manifest (.pp)
-------------------------------------------------------------------------------

You define system resources that you use in a puppet template, a manifest. It
uses Puppet Domain Specific Language (DSL) which is a combination of JSON and
Ruby. you describes resources such as file, package, or service to apply your
instructions to target systems (nodes).

Puppet Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You Puppet is ready to use on you VM instance. Let's create a Puppet
configuration file.  The installation process have created a Puppet directory
under ``/etc/``. (If it hasn't, create it with ``mkdir /etc/puppet``).

::

  cd /etc/puppet/;
  ls

You see files and directories like so::

  environments  manifests  modules  puppet.conf  templates

We're going to use ``manifests`` directory to create a Puppet configuration file.

.. note:: If you don't have one, run: ``mkdir /etc/puppet/manifests``

Warning: Setting templatedir is deprecated.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you encounter this warning message, you need to update your Puppet
configuration file. Please update the following file using your editor, vi or
nano:

::

  /etc/puppet/puppet.conf

The file contains::

  [main]
  logdir=/var/log/puppet
  vardir=/var/lib/puppet
  ssldir=/var/lib/puppet/ssl
  rundir=/var/run/puppet
  factpath=$vardir/lib/facter
  templatedir=$confdir/templates

  ..

You need to **REMOVE** the ``templatedir=`` line, then you won't see the
warning message again.

References of this issue are here:
https://tickets.puppetlabs.com/browse/PUP-2566,
https://docs.puppetlabs.com/puppet/3.7/reference/deprecated_settings.html#templatedir

First ``manifest`` - "Creating a file"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We are going to write a first Puppet manifest to create a single text file.

Move to ``manifests`` directory. We will create a new file in the directory.

:: 

  cd /etc/puppet/manifests/

Open a new file ``first-manifest.pp`` with your editori, vi or nano.

::

  file { "HelloWorld":
      path => "/tmp/HelloWorld.txt",
      ensure => "file",
      owner  => "root",
      group  => "root",
      mode   => "700",
      content => "Hello World!
      The new file has been created by Puppet!",}


Check you have created the first Puppet ``manifest`` file.

::

   cat /etc/puppet/manifests/first-manifest.pp

If you see same contents that you wrote, you are ready to apply your code to
Puppet. We provided an instruction to create a particular file named
"/tmp/HelloWorld.txt". ``ensure => "file"`` means that Puppet need to confirm
that there is a file with the path, owner, group and mode.

This Puppet manifest does not only create a file but also check the options
that we specified.  If there is changes in the file, Puppet inspects and get it
right. For example, if the file name is changed, Puppet rename it to the
original one ``HelloWorld.txt``. If it does not exist, Puppet will create the
file.  Puppet will correct the changes based on the instructions in the manifest
file. You can run Puppet again and again to ensure that your instructions in the
manifest file is valid.  Puppet will check and compare the state.

``puppet apply`` Command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command simply executes your instructions in a ``manifest (.pp)`` file.

::

  puppet apply /etc/puppet/manifests/first-manifest.pp

You may see:

::

  Notice: Compiled catalog for puppet.openstacklocal in environment production in 0.06 seconds
  Notice: /Stage[main]/Main/File[first-manifest]/ensure: defined content as '{md5}1a81759353d36dbd31059fc261af0aa2'
  Notice: Finished catalog run in 0.06 seconds

It's quite simple, isn't it? Let's check out whether the file is created.

::

  ls -al /tmp/HelloWorld.txt

You see similar like so::

  -rwx------ 1 root root 16 Apr  5 04:19 /tmp/HelloWorld.txt

``-rwx------`` satisfies ``mode => "700"`` and ``root root`` is identical with
``owner => "root"`` and ``group => "root"``.

Let's check the content::

  cat /tmp/HelloWorld.txt

You see::

  Hello World!
  The new file has been created by Puppet!

Congraturations! 
You have installed and tested Puppet with your first
``manifest`` to create and manage a file.  In this tutorial, we used ``file``
Puppet type, there are many types are available including ``package`` and
``service`` Please find more information here:
https://docs.puppetlabs.com/references/latest/type.html

.. _ref-class-lesson-devops-puppet-exercises:

Exercises
----------------------------------------------------------------------

Exercise I
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Start to record outputs in your shell by ``script <USER>-puppet-ex1.txt``
  command.  Replace ``<USER>`` with your real username e.g. ``albert``.

* Run the following commands::
  cat /etc/puppet/manifests/first-manifest.pp
  puppet apply /etc/puppet/manifests/first-manifest.pp
  ls -al /tmp/HelloWorld.txt
  cat /tmp/HelloWorld.txt

* Exit the recording with ``exit`` command or ``^D``.
  (^D is Control-D)

* Submit your ``<USER>-puppet-ex1.txt`` file.

Exercise II
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Explain the following manifest:: 

          package { 'apache':
            ensure => present,
            name   => $::operatingsystem ? {
              /(?i:Ubuntu|Debian|Mint)/ => 'apache2',
              default                   => 'httpd',
            }
          }
          service { 'apache2':
            ensure => running,
            enable => true,
          }

* Q1. If we run this on Ubuntu 14.04, we will see ``apache2`` process. If you
  run this on CentOS, what name of the process do you expect?

* Q2. There are two Puppet types used in this manifest. Describe what
  ``package`` and ``service`` do.

* Submit your answer with ``<USER>-puppet-ex2.txt`` file.

Next Step
-----------

In the next page, Chef will be introduced.

:ref:`Chef <ref-class-lesson-devops-chef>`

