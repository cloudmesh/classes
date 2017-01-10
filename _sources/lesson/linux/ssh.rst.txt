.. _s-using-ssh:

Using SSH Keys
======================================

If you do not know what ssh is we recommend that you
`read up on it <http://openssh.com/manual.html>`__ .
However, the simple material presented here will help you
etting started quickly. It can however not replace the more
comprehensive documentation.


To access remote resources this is often achieved via SSH. You need to
provide a public ssh key to FutureSystem. We explain how to generate a
ssh key, upload it to the FutureSystem portal and log onto the
resources. This manual covers UNIX, Mac OS X. 

.. _s-using-ssh-windows:

Using SSH from Windows
----------------------------------------------------------------------

.. hint:: For Linux users, please skip to the section :ref:`s-ssh-generate`
.. hint:: For Mac users, please skip to the section :ref:`s-ssh-osx`

.. warning:: For this class we recommend that you use a virtual
	     machine via virtual box and use the Linux ssh
	     instructions. The information here is just provided for
	     completness and no support will be offered for native
	     windows support.	  
	
Windows users need to have some special software to be able to use the
SSH commands. If you have one that you are comfortable with and know
how to setup key pairs and access the contents of your public key,
please feel free to use it.

The most popular software making ssh clients available to Windows
users include 

* `cygwin <http://cygwin.com/install.html>`__
* `putty <http://the.earth.li/~sgtatham/putty/0.62/htmldoc/>`__
* or installing a `virtualiztion software
  <http://cygwin.com/install.html>`__ and running Linux virtual
  machine on your Windows OS.
* using chocolatey
* using bash ubuntu under WIndows 10 (we need a contribution on this)  
  
We will be discussing here how to use it in Powershell with the help
of chopolatey. Other options may be better suited for you and we leave
it up to you to make this decission. In general we recommend that you
use an ubuntu OS either on bare hardware or a virtual
machine. Naturally your computer must support this. It will be up to
you to find such a computer.

However if you want a unix like environments with ssh you can use
Chocolatey.

Chocolatey is a software management tool that mimics the install
experience that you have on Linux and OSX. It has a repository with
many packages. Before using and installing a package be aware of the
consequences when installing software on your computer. Please be
aware that there could be malicious code offered in the chocolatey
repository although the distributors try to remove them.

The installation is sufficently explained at

* https://chocolatey.org/install

Once installed you have a command choco and you should make sure you
have the newest version with ::

  choco upgrade chocolatey

Now you can browse packages at

* https://chocolatey.org/packages

Search for openssh and see the results. You may find different
versions. Select the one that most suits you and satisfies your
security requirements as well as your architecture. Lets assume you
chose the Microsoft port, than you can install it with::

  choco install win32-openssh

.. warning:: If you have a different version such as a 64 bit version
	     please find teh appropriate commands  

Other packages of interest include

* LaTeX:: `choco install miktex`
* jabref: `choco install jabref`
* pycharm: `choco install pycharm-community`
* python 2.7.11: `choco install python2`
* pip: `choco install pip`
* virtual box: `choco install virtualbox`
* emacs: `choco install emacs`
* lyx: `choco install lyx`
* vagrant: `choco install vagrant`

Before installing any of them evaluate if you need them.
  
.. _s-ssh-osx:

Using SSH on Mac OS X
----------------------------------------------------------------------

Mac OS X comes with an ssh client. In order to use it you need to open
the ``Terminal.app`` application. Go to ``Finder``, then click ``Go``
in the menu bar at the top of the screen. Now click ``Utilities`` and
then open the ``Terminal`` application.


.. _s-ssh-generate:

Generate a SSH key
-----------------------

.. sidebar:: |info-image| Hint

   In case you do not want to type in your password everytime,
   please learn about ssh-agent and ssh-add.

First we must generate a ssh key with the tool `ssh-keygen
<http://linux.die.net/man/1/ssh-keygen>`__. This program is commonly
available on most UNIX systems (this includes Cygwin if you installed
the ssh module or use our pre-generated cygwin executable). It will
ask you for the location and name of the new key. It will also ask you
for a passphrase, which you **MUST** provide. Some teachers and teaching 
assistants advice you to not use passphrases. This is **WRONG** as it 
allows someone that gains access to your computer to also gain access to 
all resources that have the public key. Also, please use a strong passphrase 
to protect it appropriately. 

In case you already have a ssh key in your machine, you can reuse it
and skip this whole section.

To generate the key, please type::

Example::

    ssh-keygen -t rsa -C localname@indiana.edu

This command requires the interaction of the user. The first question is::

    Enter file in which to save the key (/home/localname/.ssh/id_rsa): 

We recommend using the default location ~/.ssh/ and the default name id\_rsa. 
To do so, just press the enter key.

.. note:: Your *localname* is the username on
   your computer. 


The second and third question is to protect your ssh key with a
passphrase. This passphrase will protect your key because you need to
type it when you want to use it. Thus, you can either type a
passphrase or press enter to leave it without passphrase. To avoid
security problems, you **MUST** chose a passphrase. Make sure to not
just type return for an empty passphrase::

    Enter passphrase (empty for no passphrase):

and::

    Enter same passphrase again:


If executed correctly, you will see some output similar to::

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


Once, you have generated your key, you should have them in the .ssh
directory. You can check it by ::

    $ cat ~/.ssh/id_rsa.pub

If everything is normal, you will see something like::

    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCXJH2iG2FMHqC6T/U7uB8kt
    6KlRh4kUOjgw9sc4Uu+Uwe/EwD0wk6CBQMB+HKb9upvCRW/851UyRUagtlhgy
    thkoamyi0VvhTVZhj61pTdhyl1t8hlkoL19JVnVBPP5kIN3wVyNAJjYBrAUNW
    4dXKXtmfkXp98T3OW4mxAtTH434MaT+QcPTcxims/hwsUeDAVKZY7UgZhEbiE
    xxkejtnRBHTipi0W03W05TOUGRW7EuKf/4ftNVPilCO4DpfY44NFG1xPwHeim
    Uk+t9h48pBQj16FrUCp0rS02Pj+4/9dNeS1kmNJu5ZYS8HVRhvuoTXuAY/UVc
    ynEPUegkp+qYnR user@myemail.edu

Add or Replace Passphrase for an Already Generated Key
----------------------------------------------------------------------

In case you need to change your change passphrase, you can simply run
“ssh-keygen -p” command. Then specify the location of your current key,
and input (old and) new passphrases. There is no need to re-generate
keys::

    ssh-keygen -p

You will see the following output once you have completed that step::

    Enter file in which the key is (/home/localname/.ssh/id_rsa):
    Enter old passphrase:
    Key has comment '/home/localname/.ssh/id_rsa'
    Enter new passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved with the new passphrase.  

Upload the key to gitlab
------------------------

Follow the instructions provided here:

* http://docs.gitlab.com/ce/ssh/README.html

  
Exercise
--------

SSH.1:
  create an SSH key pair

SSH.2:
  upload the key to github and/or gitlab. Create a fork in git and use
  your ssh key to clone and commit to it

SSH.3:
  Get an account on futuresystems.org (if you are authorized to do
  so). Upload your key to futuresystems.org. Login to
  india.futuresystems.org
  Note. that this could take some time as administrators need to
  approve you. Be patient.

  
