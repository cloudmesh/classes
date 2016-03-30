.. toctree::
           :maxdepth: 1



How to ask a question
=====================

Why can't I ``ssh`` into my VM?
===============================

#. Make sure that the machine have fnished boot by checking that ssh daemon is listening on port 22. If the private IP does not work, assign a floating ip as use that:

   ::

      $ nc -zv $IP 22
      Connection to 149.165.158.1 22 port [tcp/ssh] succeeded!

#. Check that you have a registered with openstack using ``nova keypair-list`` and make note of the fingerprint:

   ::

      $ nova keypair list
      +----------------+-------------------------------------------------+
      | Name           | Fingerprint                                     |
      +----------------+-------------------------------------------------+
      | india          | 41:29:20:a2:51:25:5d:66:71:02:15:b6:cd:e2:36:06 |
      +----------------+-------------------------------------------------+

#. Check that the correct key name was passed to ``nova boot`` when starting the VM by using ``nova show``:

   ::

      $ nova show $USER-myvmname
      +--------------------------------------+----------------------+
      | Property                             | Value                |
      +--------------------------------------+----------------------+
      # ...
      | key_name                             | india                |
      # ...
      +--------------------------------------+----------------------+

#. Ensure that the fingerprint matches:

   ::

      $ ssh-keygen -lf ~/.ssh/id_rsa.pub
      2048 41:29:20:a2:51:25:5d:66:71:02:15:b6:cd:e2:36:06 ~/.ssh/id_rsa.pub

#. Make sure that the key was injected into the VM during the startup by grabbing the console log and searching for your fingerprint. Make sure to wait for a few minutes after ``nova boot`` to allow the node start up:

  ::

     $ nova console-log $USER-myvmname \
       | grep -A 2 -B 4 '41:29:20:a2:51:25:5d:66:71:02:15:b6:cd:e2:36:06'
     ci-info: ++++++Authorized keys from /home/centos/.ssh/authorized_keys for user centos+++++++
     ci-info: +---------+-------------------------------------------------+---------+-----------+
     ci-info: | Keytype |                Fingerprint (md5)                | Options |  Comment  |
     ci-info: +---------+-------------------------------------------------+---------+-----------+
     ci-info: | ssh-rsa | 41:29:20:a2:51:25:5d:66:71:02:15:b6:cd:e2:36:06 |    -    |           |
     ci-info: +---------+-------------------------------------------------+---------+-----------+




If, after going through these steps, you are still unable to access the VM, delete the VM and try again two or three times, waiting a few minutes between each attempt.
OpenStack is a collection of many distributed systems, and the nature of distributed systems is that they can be prone to random failure.

If you are still unable to log in, please contact us and indicate that you have gone through these steps, and show the output of the above commands.

Why I can't modify my ``~/.ssh/authorized_keys`` file?
======================================================

You can not manually manage your ``authorized_keys`` file on ``india`` for security reasons.
If you need to change your ssh key, do so via the ``SSH keys`` tab on your `Web Portal Account <https://portal.futuresystems.org/user>`_.

Why does my MongoDB deployment fail?
====================================

In this case: mongodb is installed successfully, but the service cannot be started.
Solving this is the goal of the assignment, which is demonstrating an important aspect of many development processes: namely the affects of changing infrastructure.

To put this in context: Ubuntu for many years (through the 14.04 LTS release) used the `Upstart`_ init daemon.
As of 15.04, this is switched to `systemd`_.
However, the mongodb installation expects to use Upstart to run the service, which therefore fails.

There are many solutions to this type of problem:

#. add the system service file by hand

#. rollback the OS from Ubuntu 15.04 to 14.04

#. use a different repository which includes the systemd service file

For the purposes of this homework, the first option is taken, and the service file is provided in the repository.
As the `hw instructions say <https://github.iu.edu/bdossp-sp16/assignments/tree/hw5#hw5-tasks>`_ place the provided service file in the appropriate location.


.. _Upstart: http://upstart.ubuntu.com/
.. _systemd: https://freedesktop.org/wiki/Software/systemd/
