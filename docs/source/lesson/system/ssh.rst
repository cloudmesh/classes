.. _s-using-ssh:

Using SSH Keys
======================================

.. sidebar:: Page Contents

   .. contents::
      :local:

   .. hint:: |info-image|

      If you do not know what ssh is we recommend that you `read up on
      it <http://openssh.com/manual.html>`__ .  However, the simple
      material presented here will help you getting started quickly on
      FutureSystem. Some screencasts about this topic are available in
      section :ref:`s-screencast-accounts`.


To access the various FutureSystem resources, you need to provide a public
ssh key to FutureSystem.  We explain how to generate a ssh
key, upload it to the FutureSystem portal and log onto the resources. This
manual covers UNIX, Mac OS X, and Windows Users.

.. _s-using-ssh-windows:

Using SSH from Windows
----------------------------------------------------------------------

.. hint:: |info-image| For Linux users, please skip to the section :ref:`s-ssh-generate`
.. hint:: |info-image| For Mac users, please skip to the section :ref:`s-ssh-osx`


Windows users need to have some special software to be able to use the
SSH commands. If you have one that you are comfortable with and know
how to setup key pairs and access the contents of your public key,
please feel free to use it.
The most popular software making ssh clients available to Windows
users include 

* `putty <http://the.earth.li/~sgtatham/putty/0.62/htmldoc/>`__
* `cygwin <http://cygwin.com/install.html>`__
* or installing a `virtualiztion software
  <http://www.vagrantup.com/downloads>`__ and running Linux virtual
  machine on your Windows OS.

Putty is a single file to run. It does not require installation. You simply
download a file and run it to open a SSH session. Cygwin provides
Linux-like environment for Windows and both Putty or Cygwin will ease your
experience with FutureSystems.

.. comment:: If you have cygwin already installed, please use it, but make sure you have ssh
        installed. If not, we have made it even easier for you as we prepared a special
        Cygwin version that is ready to use. Once you have installed it, you can follow
        the same instructions as given in the rest of the sections presented to access
        FutureSystems from SSH. You can install cygwin with the following steps.


        .. list-table:: 
           :widths: 10 60 30
           :header-rows: 1

           * - Step
             - Description
             - Supporting Screenshot
           * - Step 1
             - Download Cygwin from our Portal \ :portal:`sites/default/files/cygwin.zip`.
             - 
           * - Step 2
             - Uncompress the file.
             - |image21|
           * - Step 3
             - Execute the file the 'Windows Batch File' called Cygwin.bat
             - 
           * - Step 4
             - You may get a warning. Click on the Run button
             - |image22|
           * - Step 5
             - You get a Linux-like terminal that will allow you to continue
               with this manual. Hint: When showing examples of commands, the $ symbol precedes the
               actual command. So, the other lines are the output obtained after
               executing the command.
             - |image23|
             


.. _s-ssh-osx:

Using SSH on Mac OS X
----------------------------------------------------------------------

Mac OS X comes with an ssh client.
In order to use it you need to open the ``Terminal.app`` application.
Go to ``Finder``, then click ``Go`` in the menu bar at the top of the
screen.
Now click ``Utilities`` and then open the ``Terminal`` application.


.. _s-ssh-generate:

Generate a SSH key
-------------------------------------------------------------------------------

.. sidebar:: |info-image| Hint

   In case you do not want to type in your password everytime,
   please learn about ssh-agent and ssh-add.

First we must generate a ssh key with the tool `ssh-keygen
<http://linux.die.net/man/1/ssh-keygen>`__. This program is commonly available
on most UNIX systems. It will ask you for the location and name of the new key.
It will also ask you for a passphrase, which you **MUST** provide. Also, please
use a strong passphrase to protect it appropriately. 

If you already have a ssh key in your machine, you can reuse it and skip
this section.

To generate the key, please type::

Example::

    ssh-keygen -t rsa -C localname@indiana.edu

This command requires a user input like::

    Enter file in which to save the key (/home/localname/.ssh/id_rsa): 

We recommend using the default location ~/.ssh/ and the default name id\_rsa. 
To do so, just press the enter key.

.. sidebar:: |info-image| Hint 

   Please note that your *localname* is the username on
   your computer and may be different from your *portalusername*.


The second and third questions are to protect your ssh key with a passphrase.
This passphrase will protect your key because you need to type it when your key
is used. You can skip these if you want not to have passphrase. To avoid
security problems, however, you **MUST** choose a passphrase. Make sure not to
just type return for an empty passphrase::

    Enter passphrase (empty for no passphrase):

and::

    Enter same passphrase again:


If you executed correctly, some output messages will be displayed similar to::

    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/localname/.ssh/id_rsa): 
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/localname/.ssh/id_rsa.
    Your public key has been saved in /home/localname/.ssh/id_rsa.pub.
    The key fingerprint is:
    34:87:67:ea:c2:49:ee:c2:81:d2:10:84:b1:3e:05:59 localname@indiana.edu
    The key's random art image is::

    +--[ RSA 2048]----+
    |.+...Eo= .       |
    | ..=.o + o +o    |
    |O.  o o +.o      |
    | = .   . .       |
    +-----------------+


Once, you have generated a new key, you should have them in the .ssh
directory. You can check it by ::

    $ ls -al $HOME/.ssh/

To confirm a public key with a default name id_rsa.pub, run::

    $ cat $HOME/.ssh/id_rsa.pub


If everything is normal, you will see something like::

    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCXJH2iG2FMHqC6T/U7uB8kt6KlRh4kUOjgw9sc4Uu+Uwe/EwD0wk6CBQMB+HKb9upvCRW/851UyRUagtlhgythkoamyi0VvhTVZhj61pTdhyl1t8hlkoL19JVnVBPP5kIN3wVyNAJjYBrAUNW4dXKXtmfkXp98T3OW4mxAtTH434MaT+QcPTcxims/hwsUeDAVKZY7UgZhEbiExxkejtnRBHTipi0W03W05TOUGRW7EuKf/4ftNVPilCO4DpfY44NFG1xPwHeimUk+t9h48pBQj16FrUCp0rS02Pj+4/9dNeS1kmNJu5ZYS8HVRhvuoTXuAY/UVcynEPUegkp+qYnR user@myemail.edu

Add or Replace Passphrase for an existing Key
-------------------------------------------------------------------------------

In case you need to change your change passphrase, you can simply run
“ssh-keygen -p” command. Then specify the location of your current key,
and input (old and) new passphrases. There is no need to re-generate
a key::

    ssh-keygen -p

You will see the following output once you have completed ::

    Enter file in which the key is (/home/localname/.ssh/id_rsa):
    Enter old passphrase:
    Key has comment '/home/localname/.ssh/id_rsa'
    Enter new passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved with the new passphrase.  


Upload Publick Key to FutureSystems (portal.futuresystems.org)
-------------------------------------------------------------------------------

Next you need to upload the key to the portal. You must sign in the portal to
do so.


.. list-table:: 
   :widths: 10 60 30
   :header-rows: 1

   * - Step
     - Description
     - Supporting Screenshot
   * - Step 1 
     - Log into the portal
     - |image25|
   * - Step 2
     - Click in the "ssh key" button. or go directly to https://portal.futuresystems.org/my/ssh-keys
     - |image26|
   * - Step 3
     - Click in the "add a public key" link.
     - |image27|
   * - Step 4
     - Paste your ssh key into the box marked Key. Use a text editor
       to open the “id_rsa.pub”. Copy the entire contents of this file
       into the ssh key field as part of your profile
       information. Many errors are introduced by users in this step
       as they do not paste and copy correctly.
     - |image28|
   * - Step 5
     - Click the submit button. **IMPORTANT**: Leave the Title field blank.
       Make sure that when you paste your key, it does not contain
       newlines or carriage returns that may have been introduced by
       incorrect pasting and copying. If so, please remove them.
     - 
     
At this point you have uploaded your key. However you may wait till the key is
activated. You will receive notification emails once there are progress. You
can also check the status at the portal and see if the boxes in your account
status information are all greens. Contact course team or issue a ticket at
FutureSystems if you think there is an error. 

Login FutureSystems with New SSH Key
-------------------------------------------------------------------------------

If you are a first time user on FutureSystems, you may wait one-two business
days until your account is activated. Otherwise, using your new key is almost
instantaneous on india.futuresystems.org.  For other clusters e.g. juliet it
can take upto 30 minutes to apply your new ssh keys.

To log into india simply type the usual ssh command such as:: 

    $ ssh portalname@india.futuresystems.org

The first time you ssh into a machine you will see a message like this::

    The authenticity of host 'india.futuresystems.org (192.165.148.5)' can't be established.
    RSA key fingerprint is 11:96:de:b7:21:eb:64:92:ab:de:e0:79:f3:fb:86:dd.
    Are you sure you want to continue connecting (yes/no)?

You have to type ``yes`` to confirm host key verification. Then you will be
logging into india. Other FutureSystem machines can be reached in a same
fashion. Just replace the name ``india``, with the appropriate
FutureSystems resource name e.g. ``juliet``.


.. |image21| image:: ../images/cygwim1.png
   :width: 200px
.. |image22| image:: ../images/cygwin2.png
   :width: 200px
.. |image23| image:: ../images/cygwinfirst.png
   :width: 200px
.. |image24| image:: ../images/register-sshkey.png
   :target: https://portal.futuresystems.org/my/ssh-keys
.. |image25| image:: ../images/portalLogin_0.png
   :width: 200px
.. |image26| image:: ../images/portalsshkey.png
   :width: 200px
.. |image27| image:: ../images/portalclikaddkey_0.png
   :width: 200px
.. |image28| image:: ../images/portalkeypaste_0.png
   :width: 200px


.. |info-image| image:: ../images/glyphicons_195_circle_info.png 
