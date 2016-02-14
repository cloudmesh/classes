.. _ref-class-lesson-devops-ansible:

Ansible
======================================================================

.. sidebar:: Page Contents

   .. contents::
      :local:


Overview
----------------------------------------------------------------------

This lesson will introduce you to using the Ansible 

.. tip:: Duration: 1 hour 30  minutes

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have knowledge of

* Using the shell
* Editing files
* Accessing FutureSystems


.. tip::

   Ansible uses ssh to access many machines.
   To simplify your life, start an ssh agent and add your credentials::

     $ eval $(ssh-agent -s)
     $ ssh-add ~/.ssh/id_rsa

   Make sure that the fingerprint matches with the key you boot the OpenStack instance with::

     $ nova keypair-list
     $ ssh-keygen -lf ~/.ssh/id_rsa.pub


.. include:: ../ansible.rst

.. include:: ../ansible_playbook.rst

  
.. _ref-class-lesson-devops-ansible-lab:

Lab Session
----------------------------------------------------------------------

Write an Ansible Playbook to start the Apache webserver on your
instances.

On each instance:

- install the ``apache2`` package
- start the apache

.. important::

   You can check that apache is listening on port 80 using the ``nc`` command.
   For example::

     $ nc -zv 10.23.2.101 80
     Connection to 10.23.2.101 80 port [tcp/http] succeeded!

   Additionaly, use ``curl`` to print the header::

     $ curl --head 10.23.2.101
     HTTP/1.1 200 OK
     Date: Thu, 02 Apr 2015 19:01:47 GMT
     Server: Apache/2.4.7 (Ubuntu)
     Last-Modified: Thu, 02 Apr 2015 18:54:59 GMT
     ETag: "2cf6-512c25e61433f"
     Accept-Ranges: bytes
     Content-Length: 11510
     Vary: Accept-Encoding
     Content-Type: text/html

