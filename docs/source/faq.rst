.. toctree::
           :maxdepth: 1



How to ask a question
=====================

I can't ``ssh`` into a VM
=========================

How to check VM accessibility
=============================

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
