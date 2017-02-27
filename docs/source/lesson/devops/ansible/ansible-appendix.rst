Ansible: Write a Playbooks for MongoDB
======================================

Ansible Playbooks are automated scripts written in YAML data format.  Instead
of using manual commands to setup multiple remote machines, you can utilize
Ansible Playbooks to configure your entire systems. YAML syntax is easy to read
and express the data structure of certain Ansible functions. You simply write
some tasks, for example, installing software, configuring default settings, and
starting the software, in a Ansible Playbook.  With a few examples in this
tutorial, you will understand how it works and how to write your own Playbooks.

.. note:: There are also several examples of using Ansible `Playbooks
         <http://docs.ansible.com/playbooks.html>`_ from the official site. It covers
         from basic usage of Ansible Playbooks to advanced usage such as applying
         patches and updates with different roles and groups.

Tutorial: Writing Ansible Playbook
----------------------------------

In this tutorial, we are going to write a basic playbook of Ansible software.
Keep in mind that ``Ansible`` is a main program and ``playbook`` is a template
that you would like to use. You may have several playbooks in your Ansible.

First playbook for MongoDB Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As a first example, we are going to write a playbook which installs MongoDB
server.  It includes the following tasks:

* Import the public key used by the package management system
* Create a list file for MongoDB
* Reload local package database
* Install the MongoDB packages
* Start MongoDB

.. note::

   This tutorial is based on the manual installation of MongoDB from
   the official site:
   http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/*

   We also assume that we install MongoDB on Ubuntu 15.10.

Enabling Root SSH Access
^^^^^^^^^^^^^^^^^^^^^^^^

Some setups of managed nodes may not allow you to log in as root. As
this may be problematic later, let us create a playbook to resolve
this. Create a ``enable-root-access.yaml`` file with the following
contents::

  ---
  - hosts: ansible-test
    remote_user: ubuntu
    tasks:
      - name: Enable root login
        shell: sudo cp ~/.ssh/authorized_keys /root/.ssh/


Explanation:

- ``hosts`` specifies the name of a group of machines in the inventory
- ``remote_user`` specifies the username on the managed nodes to log in as
- ``tasks`` is a list of tasks to accomplish having a ``name`` (a
  description) and modules to execute. In this case we use the
  ``shell`` module.

We can run this playbook like so::

  $ ansible-playbook -i inventory.txt -c ssh enable-root-access.yaml
  
  PLAY [ansible-test] *********************************************************** 
  
  GATHERING FACTS *************************************************************** 
  ok: [10.23.2.105]
  ok: [10.23.2.104]
  
  TASK: [Enable root login] ***************************************************** 
  changed: [10.23.2.104]
  changed: [10.23.2.105]
  
  PLAY RECAP ******************************************************************** 
  10.23.2.104                : ok=2    changed=1    unreachable=0    failed=0   
  10.23.2.105                : ok=2    changed=1    unreachable=0    failed=0



Hosts and Users
^^^^^^^^^^^^^^^

First step is choosing hosts to install MongoDB and a user account to run
commands (tasks).  We start with the following lines in the example filename of
``mongodb.yaml``::

  ---
  - hosts: ansible-test
    remote_user: root

In a previous tutorial, we setup two machines with ``ansible-test`` group name.
This tutorial uses that two machines for MongoDB installation.  Also, we use
``root`` account to complete Ansible tasks.

.. important:: Indentation is important in YAML format. Do not ignore spaces start
          with in each line.

Tasks
^^^^^

A list of tasks contains commands or configurations to be executed on remote
machines in a sequential order.  Each task comes with a ``name`` and a
``module`` to run your command or configuration.  You provide a description of
your task in ``name`` section and choose a ``module`` for your task.  There are
several modules that you can use, for example, ``shell`` module simply executes
a command without considering a return value.  You may use ``apt`` or ``yum``
module which is one of the packaging modules to install software. You can find
an entire list of modules here:
http://docs.ansible.com/list_of_all_modules.html

Module ``apt_key``: add repository keys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We need to import the MongoDB public GPG Key. This is going to be a first task
in our playbook.::

  tasks:
    - name: Import the public key used by the package management system
      apt_key: keyserver=hkp://keyserver.ubuntu.com:80 id=7F0CEB10 state=present


Module ``apt_repository``: add repositories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next add the MongoDB repository to apt::

   - name: Add MongoDB repository
     apt_repository: repo='deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' state=present


Module ``apt``: install packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use ``apt`` module to install ``mongodb-org`` package.
``notify`` action is added to start ``mongod`` after the completion of this task.
Use the ``update_cache=yes`` option to reload the local package database.::

  - name: install mongodb
    apt: pkg=mongodb-org state=latest update_cache=yes
    notify:
    - start mongodb

Module ``service``: manage services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use ``handlers`` here to start or restart services. It is similar to
``tasks`` but will run only once.::

   handlers:
     - name: start mongodb
       service: name=mongod state=started

The Full Playbook
^^^^^^^^^^^^^^^^^

Our first playbook looks like this::

  ---
  - hosts: ansible-test
    remote_user: root
    tasks:
    - name: Import the public key used by the package management system
      apt_key: keyserver=hkp://keyserver.ubuntu.com:80 id=7F0CEB10 state=present
    - name: Add MongoDB repository
      apt_repository: repo='deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' state=present
    - name: install mongodb
      apt: pkg=mongodb-org state=latest update_cache=yes
      notify:
      - start mongodb
    handlers:
      - name: start mongodb
        service: name=mongod state=started

Running a Playbook
^^^^^^^^^^^^^^^^^^

We use ``ansible-playbook`` command to run our playbook::

  $ ansible-playbook -i inventory.txt -c ssh mongodb.yaml
  
  PLAY [ansible-test] *********************************************************** 
  
  GATHERING FACTS *************************************************************** 
  ok: [10.23.2.104]
  ok: [10.23.2.105]
  
  TASK: [Import the public key used by the package management system] *********** 
  changed: [10.23.2.104]
  changed: [10.23.2.105]
  
  TASK: [Add MongoDB repository] ************************************************ 
  changed: [10.23.2.104]
  changed: [10.23.2.105]
  
  TASK: [install mongodb] ******************************************************* 
  changed: [10.23.2.104]
  changed: [10.23.2.105]
  
  NOTIFIED: [start mongodb] ***************************************************** 
  ok: [10.23.2.105]
  ok: [10.23.2.104]
  
  PLAY RECAP ******************************************************************** 
  10.23.2.104                : ok=5    changed=3    unreachable=0    failed=0   
  10.23.2.105                : ok=5    changed=3    unreachable=0    failed=0


.. note::

   If you rerun the playbook, you should see that nothing changed::

     $ ansible-playbook -i inventory.txt -c ssh mongodb.yaml 
     
     PLAY [ansible-test] *********************************************************** 
     
     GATHERING FACTS *************************************************************** 
     ok: [10.23.2.105]
     ok: [10.23.2.104]
     
     TASK: [Import the public key used by the package management system] *********** 
     ok: [10.23.2.104]
     ok: [10.23.2.105]
     
     TASK: [Add MongoDB repository] ************************************************ 
     ok: [10.23.2.104]
     ok: [10.23.2.105]
     
     TASK: [install mongodb] ******************************************************* 
     ok: [10.23.2.105]
     ok: [10.23.2.104]
     
     PLAY RECAP ******************************************************************** 
     10.23.2.104                : ok=4    changed=0    unreachable=0    failed=0   
     10.23.2.105                : ok=4    changed=0    unreachable=0    failed=0

Sanity Check: Test MongoDB
^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's try to run 'mongo' to enter mongodb shell.::

   $ ssh ubuntu@$IP
   $ mongo
   MongoDB shell version: 2.6.9
   connecting to: test
   Welcome to the MongoDB shell.
   For interactive help, type "help".
   For more comprehensive documentation, see
           http://docs.mongodb.org/
   Questions? Try the support group
           http://groups.google.com/group/mongodb-user
   > 

Terms
^^^^^

* Module: Ansible library to run or manage services, packages, files or
  commands.
* Handler: A task for notifier.
* Task: Ansible job to run a command, check files, or update configurations.
* Playbook: a list of tasks for Ansible nodes. YAML format used.
* YAML: Human readable generic data serialization.

Reference
^^^^^^^^^

The main tutorial from Ansible is here:
http://docs.ansible.com/playbooks_intro.html

You can also find an index of the ansible modules here:
http://docs.ansible.com/modules_by_category.html
