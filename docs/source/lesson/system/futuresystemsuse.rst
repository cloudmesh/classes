Use of FutureSystems
----------------------------------------------------------------------

.. sidebar:: Page Contents

   .. contents::
      :local:


Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section describes using SSH on and with FutureSystems.

There are two ways SSH is used:

- providing access to FutureSystems resources
- once logged into FutureSystems, get access to OpenStack images and
  running instances.

Since all assignments and lessons will be done on FutureSystems, it is
important that you can log on. Whether you are starting from Windows,
Mac OS X, or Linux, only a few steps are needed.

Once you can log into ``india.futuresystems.org``, SSH keys are used
to manage access to OpenStack. At this point your computer is just a
client to access FutureSystems resources. All commands are executed on
FutureSystems.

The steps, describes below, are:

- get and account with FutureSystems (portal)
- join a project (portal)
- upload SSH public key (computer -> portal)
- log into FutureSystems (computer -> ``india``)
- manage keys for OpenStack (``india`` -> VM)


Getting an Account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to use FutureSystems you will need to get an account.

.. important::

   Make sure you have cookies enabled or you will not be able to log
   in to your account.


#. Navigate to `FutureSystems.org <https://portal.futuresystems.org/>`_.
#. Click on ``Register`` at the top near the search bar
#. Fill out the information. Asterisk-denoted (``*``) fields are required.
#. Please be patient after clicking the ``Create new account` button.
   It may take one or two business day for the account to be approved.
#. Once your account is approved you will receive an email.

.. important:: At this point you will not be able to use any
   FutureSystems resources.  You will need to join a project and
   enable remote login to do so.  Only when the status is all green in
   the ``My FutureGrid HPC account status`` of your `portal account`_
   information will you have access to resources.

.. tip:: Please see Section :ref:`s-screencast-accounts` for
   additional details.

.. _portal account: https://portal.futuresystems.org/my/fg-account


Join a Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that you have a FutureSystems account you will need to join a
project.

#. Navigate to `FutureSystems.org
   <https://portal.futuresystems.org/>`_ and log into your account.
#. Click on the appropriate project name
#. Click on the ``Join the project`` link on the right hand side.
#. Upon approval you will receive an email.

.. tip::
   Please see :ref:`s-account-join-project` for further details.


Remote Login
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. important::

   All coursework will be done on your FutureSystems account on
   ``india``. You will to use PuTTY to access ``india`` and then you
   can follow along with the other instructions.


In order to login into your account on FutureSystems you will need:

- an account on FutureSystems (see above)
- an SSH client


Linux and OSX
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

We assume that Linux users are familiar on how to start a terminal. On
Mac OS X open a terminal via `Applications --> Utilities --> Terminal`. Alternatively you can search for the term "terminal" in the
spotlight search and locate the terminal application and click on it.

To proceed you will need to know your FutureSystems Portalname and
Project ID.

For this example we assume you have set the shell variable PORTALNAME
to your FutureSystems portal username. This can be done as
follwows. Let us assume your portal name is `albert`. Than you can set
it with::

            export PORTALNAME=albert

We also assume that you have a project id that you set to::

              export PROJECTID=fg101
 
if it is the number 101. Once you have set up your portal name you can
log in via::

  $ ssh $PORTALNAME@india.futuresystems.org

Naturally, you could also directly place your portal name into the
command. Thus if your portalname would be albert, you could do
alternatively to the above command::

  $ ssh $PORTALNAME@india.futuresystems.org


.. tip:: Please see Section :ref:`s-using-ssh` for details on
   configuring and using an SSH client.


Windows
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

In order to SSH into your FutureSystems account using Windows, you
will need to install PuTTY and PuTTYgen from the `PuTTY project page`_

Generate an key using PuTTYgen:

#. open the application ``puttygen.exe``
#. press "Generate"
#. enter a desired passphrase (make sure they match!)
#. save the private and public keys
#. copy the displayed public key

You can now upload your public key to the FutureSystems portal.

To connect, open ``putty.exe`` and go to `Connection ---> SSH --->
Auth` on the left and browse to add the private key.  Then go to the
`Session` category and enter ``india.futuresystems.org`` for the Host
Name and click "Open".  This will launch a terminal and allow you to
connect using the passphrase specified in ``puttygen.exe``.

.. _PuTTY project page: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html
.. _PuTTY: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html



Useful SSH commands
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The following is a short list of useful SSH commands.

Change the password
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

You can change the password for the key by using the  the ``-p`` flag.
For example::

  $ ssh-keygen -p

Change the comment
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

You can change the comment of an key by modifying the public key file.
For example, Ada Lovelace wishes to replace an uninformative comment
with her email address.
She would execute the following::

  $ cat ~/.ssh/id_rsa.pub
  ssh-rsa  AAAAB3N.... this is not informative
  $ nano ~/.ssh/id_rsa.pub
  $ cat ~/.ssh/id_rsa.pub
  ssh-rsa  AAAAB3N.... lovelace@gmail.com


Show fingerprint
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The fingerprint of a key can be used to authenticate the validity of
the key.  For example, if Ada were to share his public key with Albert
Einstein, she would transmit the key.  Albert could then compute the
fingerprint and ensure that it matches.  To do so, Albert would save
the key to ``~/.ssh/$PORTALNAME-key`` and execute::

  $ ssh-keygen -l -f ~/.ssh/$PORTALNAME-key.pub
  2048 6c:52:54:20:b9:85:04:d4:30:46:48:c7:c4:bc:fe:c7  lovelace@gmail.com (RSA)

FutureSystems, for instance, uses fingerprints to identify keys once
they have been uploaded.  You may see this fingerprint on the
`FutureSystems portal
<https://portal.futuresystems.org/my/ssh-keys>`_.


Delete a known host
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Whenever you log into a new machine via SSH, the host key of the
destination machine is added to ``~/.ssh/known_hosts``.
The next time you try to log in this key will be checked.
If it has changed you will need to remove the entry before attempting
to log back in.

.. note::
   The host key may change if the machine undergoes a major upgrade or
   change.
   Another reason may be that a third party is performing a
   `man-in-the-middle attack`_.


To remove a key for ``india.futuresystems.org`` from ``~/.ssh/known_hosts``::

  $ ssh-keygen -R india.futuresystems.org


.. _man-in-the-middle attack: http://en.wikipedia.org/wiki/Man-in-the-middle_attack



SSH
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Secure Shell, or SSH, is a protocol for securely connecting to a Shell
on a remote computer.

.. tip::

   See Section :ref:`s-shell-lesson` for more details on what a shell
   is and how to use it.

This security is accomplished by encrypting the data that is sent
between the two endpoints.  In order for this communication to be
considered "safe", the machines need to identify each other.  The
identity is usually accomplished through the use of a **key** file,
which usually comes in pairs: a **public** key and a **private** key.
This is usually called a **key pair**.  On Mac OS X and Linux a key
pair can be created using the ``ssh-keygen`` command. You can test this out by opening a terminal and entering the following:

.. code:: bash

   $ ssh-keygen -f ~/test_identity

What this does is actually create two file:

- ``~/test_identity``
- ``~/test_identity.pub``

The second file, ending in ``.pub``, is the public key and needs to be
shared with the machines you wish to access.  In the case of
FutureSystems, you add the public key to your `SSH Keys
<https://portal.futuresystems.org/my/ssh-keys>`_.  In the case of
GitHub (see Section :ref:`s-lesson-git`) you add it to your account.

.. caution::

   **Never** share the private key with anyone.  This is used to
   identify you and can be used to completely regenerate the public
   key. Try it for yourself with:

   .. code:: bash

      $ ssh-keygen -y -f ~/test_identity

   and compare the output with ``~/test_identity.pub``

.. tip::

   A good practice for managing SSH keys is to create a key pair on
   each machine you use and to add a comment indicating your contact
   information and the machine this key belongs to.::

     $ ssh-keygen -C 'host:relativity contact:albert@gmail.com'

   In the above the comment is specified with the ``-C`` flag and the
   body of the comment is within the single quotes.

   The contact information is useful when sharing the key with others
   as it helps them understand who you are.

   The host information is useful for you if you have multiple
   machines.


.. _lab-futuresystems-access:

Lab - Account Applications
----------------------------------------------------------------------

For this exercise, you need to log into your FutureSystems account.
On Windows, use the PuTTY program.
On Mac OS X use the Terminal application.

Execute the following commands:

- ``whoami``
- ``uname -a``
- ``pwd``

Post the result (copy and paste the ASCII text of what you see in the
screen to the homework system.
