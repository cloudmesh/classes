:orphan:

==================================
 Setting Up Ubuntu 16.04 for i524
==================================


Prerequisites
=============

This assumes:

#. You have a recent installation of Ubuntu 16.04 running, either
   installed natively or through VirtualBox. See the
   :doc:`../lesson/linux/ubuntu` lesson for details on how to
   accomplish this.

   Check by running the following command:

   ::

      $ lsb_release -a
      No LSB modules are available.
      Distributor ID: Ubuntu
      Description:    Ubuntu 16.04.1 LTS
      Release:        16.04
      Codename:       xenial

#. You have administrative privileges on this machine.

   Check by running the following command:

   ::

      $ sudo whoami
      root

Setting Up
==========

Updating the cache
------------------

Once the requirements are satisfied, you must ensure the package
manager has an up-to-date cache of the available packageds.
Do so by running the ``apt-get`` command:

  ::

     $ sudo apt-get update
     Get:1 http://security.ubuntu.com/ubuntu xenial-security InRelease [102 kB]
     Hit:2 http://archive.ubuntu.com/ubuntu xenial InRelease                              
     Get:3 http://security.ubuntu.com/ubuntu xenial-security/main Sources [55.8 kB]
     Get:4 http://archive.ubuntu.com/ubuntu xenial-updates InRelease [102 kB]
     # ....etc
     Fetched 11.1 MB in 23s (474 kB/s)
     Reading package lists... Done


.. _r-i524-ubuntu-setup-devtools:

Installing Development Tools
----------------------------

Editors
~~~~~~~

You should ensure that an editor such as emacs, vim, or nano is installed:

::

   $ sudo apt-get install -y emacs vim nano

Version Control (Git)
~~~~~~~~~~~~~~~~~~~~~

Install Git using:

::

   $ sudo apt-get install -y git

Development Tools
~~~~~~~~~~~~~~~~~

Install Python and other necessary programs and tools:

::

   $ sudo apt-get install -y python-dev python-virtualenv python-pip graphviz make


LaTeX
~~~~~


You should also install the full TexLive package. This will result in
several gigabytes of download and install, so make take a while:

::

   $ sudo apt-get install -y texlive-full

