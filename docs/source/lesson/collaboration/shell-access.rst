Shell Access
======================================================================

.. sidebar:: Page Contents

   .. contents::
      :local:

.. warning:: This section is for advanced access of the staff to your
	     machine. We recommend that you do not do this section if
	     you do not understand its implication and engage with the
	     staff of the class **before** you do it. In many cases
	     this will not be needed.
	 
This lesson describes how to provide access to your account on
FutureSystems to a Teaching Assistant.


Prerequisites
----------------------------------------------------------------------

You will need:

* an account on FutureSystems (see `Creating FutureSystems Accounts and Projects`_)
* upload an SSH key (see `Using SSH Keys`_)

These prerequisites are satisfied if

* your FutureSystems status is all green in your "Portal Account" tab on https://portal.futuresystems.org/
* log into ``india.futuresystems.org`` using SSH.

You may wish to view a `Detailed discussion about SSH`_.

.. _Creating FutureSystems Accounts and Projects: http://cloudmesh.github.io/introduction_to_cloud_computing/accounts/accounts.html
.. _Using SSH Keys: http://cloudmesh.github.io/introduction_to_cloud_computing/accounts/accounts.html
.. _Detailed discussion about SSH: http://cloudmesh.github.io/introduction_to_cloud_computing/class/lesson/linux/advancedssh.html


.. note:: Futuresystems Portalname and Project ID

          In case you use OSX or Linux terminals to access
	  FutureSystems, we recommend that you define a portalname and project ID.
          This can be done as follwows. Let us assume your portal name is
	  `albert`. Than you can set it with::

              export PORTALNAME=albert

         We also assume that you have a project id that you set to::

              export PROJECTID=fg101
 
         if it is the number 101.


Providing Access
----------------------------------------------------------------------

First log into ``india.futuresystems.org`` with::

  ssh $PORTALNAME@india.futuresystems.org

You will need to have the public key of the person you are giving access to.
Here is an example public key. Please do not copy this key into this
file or do this if you do not understand what this is for::

 ssh-rsa
 AAAAB3NzaC1yc2EAAAADAQABAAABAQDKTtes2ngM+L0og8zKugcxXwYWMkzUiPofW1qyZ
 tSsO73a6ZEJR0opRRti24ooPP/+h7Scnbt8ATQP5Iz++FIUCyf5v9wo7Lvglq39FuGqaul
 Iq5PI1Y5jr0zFLzfmjGCr+M5Cz0C9wO0r6C0vsabHqC28xltV+o683EqR1Yz+PpPcS4GNx
 PCEXpTP1ZiF5/sNNrBMemO9rk22JybEoDSTWnbQizzptMx0BOgmhoiIQwwS7r7g07PBjdU
 oBUK7XuccglMYF4HjE/1jR0MKosZBRfb29decjPef+1ndstMOrVTf89BHcmv3TVedfPlGe
 o9CCQJfpaEC22B/2ZY0XGCt
 user@example.com


You need to modify the ``~/.ssh/authorized_keys`` file and add the public key::

 $ cd .ssh
 $ nano authorized_keys
 # now past the public key to the bottom of the file

Now the Teaching Assistant can log into your account.


.. caution::
   Be aware that this procedure allows someone to log into your account as you.
   Once this session is over, you should remove their public key from your ``~/.ssh/authorized_keys`` file.


Exercise
----------------------------------------------------------------------

Communicate with a support staff members and ask them for their public
key. Add this public key to your authorized keys file on
``india``. Ask the staff member to log into your account. You naturally
need to give the staff member your portalname.
Verify if he can browse to the project you have an issue with.
