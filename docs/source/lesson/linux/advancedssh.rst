.. _ref-advanced-ssh:

Advanced SSH
======================================================================

Overview
----------------------------------------------------------------------

This lesson will introduce you to advanced SSH configuration and
tunneling. You can have a shortcut to your SSH connection with a
``ssh`` configuration file or you can create a secure connection
between local and remote machines using SSH tunneling. You will find
out as how to define ssh options in the ``ssh`` config and what
commands you need to establish SSH tunneling with a few examples.

.. .. tip:: Duration: 30 mins

Topics:

* SSH config
* SSH tunneling

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have knowledge of basics of SSH.

If you missed the lesson of basic SSH, go to 
`here <../system/futuresystemsuse.html#ssh>`_

SSH Configuration File
----------------------------------------------------------------------

If you frequently log into a large number of remote machines with different
keys and user names, you probably want to avoid typing a path of your key, a
user name and a server name all the time. Fortunately, ``ssh`` has a feature to
pick up pre-defined configurations for ssh connection.

``~/.ssh/config`` file is a configuration file for a user which contains
settings for the SSH connection per host. Account name, port number, identify
file (private key), or port forwarding can be defined in the file. For
instance, if you have a machine named ``india`` to log in, you can have a
configuration like this: 

::

  Host india
  User albert
  Hostname india.futuresystems.org
  IdentityFile ~/.ssh/id_rsa_india

Once you have this configuration, you can simply run ``ssh india`` to get
access ``india.futuresystems.org``.  Let's see what these keywords are in the
configuration.

* Host: is a label for your host. SSH recognizes your settings with this label.
* User: is a user name to log in. If you have a different user name on
  different machines, this option is useful.
* Hostname: is a real name to log into.
* IdentityFile: is an authentication identity for RSA or DSA. This typically
  specifies the path of your private key.

If you have other hosts to configure, simply add a new block in the
configuation file. If you would like know more about other keywords, please see
``ssh_config`` man page.

.. note:: If you don't have a file like ``~/.ssh/id_rsa`` in your home
          directory?  Please learn about creating a new ssh key 
          `here <../system/futuresystemsuse.html#ssh>`_

SSH Tunneling (Port Forwarding)
----------------------------------------------------------------------

If you need to ensure a secure and encrypted connection between a local machine
and a remote machine, SSH tunneling rather than VPN is simple and useful to
protect against sniffing and eavesdropping of network traffic.

.. figure:: /images/lesson_ssh_tunnel.png

   Figure 1. Example of SSH tunneling - Local 10010 ports is mirrored to remote 80 ports.

You can transfer inbound traffic to outbound ports using SSH tunnel. SSH tunnel
listens on a particular port and redirects incoming packets to the destination.
This is useful to bypass certain restrictions, e.g. blocked ports or protocols,
especially if you are behind a firewall or on a private network. 

Exercises
----------------------------------------------------------------------

Exercise I
^^^^^^^^^^^^^^^^^^

* Configure your FutureSystems account in SSH configuration file.

Exercise II
^^^^^^^^^^^^^^^^^^

* Assume that we have ``ssh -L 10010:remote:80
  albert@exercise.futuresystems.org``. Define your SSH configuration to simply
  use ``ssh tunnel_exercise`` in the shell.

.. tip:: See the man page of ssh_config for ssh tunneling. ``LocalForward``
   keyword will be required.  
   
Next Step
-----------

In the next page, ...

`Modules Environment Tools <modules.html>`_
