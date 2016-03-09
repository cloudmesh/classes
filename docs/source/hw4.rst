HW4: Ansible Exercise
===============================================================================

Guidelines
-------------------------------------------------------------------------------

* Assignments must be completed individually.
* Discussion is allowed (e.g. via Slack) but the submission should be made by
  yourself. Acknowledge your helpers/collaborators name in the submission if
  you discussed or got help from anyone.
* Use an individual github repository. A repository in FutureSystems will be
  given later.

Use ``hw4`` branch
-------------------------------------------------------------------------------

* Login https://github.iu.edu with your IU Username and Password
  (It is a same IU Credential that you use on other IU sites e.g. one.iu.edu)

* Checkout hw4 branch

MongoDB Ansible Role
-------------------------------------------------------------------------------

Writing Mongodb playbook is taught in the Ansible lessons. You write
MongoDB Ansible role in this assignment. Submit inventory, main playbook,
command script and your role including sub-directories.

Submission
-------------------------------------------------------------------------------

The following files should be included in your submission

* ``inventory`` file
* ``site.yml`` the main playbook file
* ``mongodb`` directory (which is ansible role for mongodb)
* ``hw4-cmd.script`` file

Preparation
-------------------------------------------------------------------------------

* Login to india.futuresystems.org
* Use the same ``bdossp-sp16`` virtualenv used in hw3
* Install ``ansible`` via python package manager

HW4 Tasks
-------------------------------------------------------------------------------

You need to write an Ansible role to install mongodb on your vm instance
``hw3-$USER``.  Ansible Playbook for MongoDB installation is given in Ansible
lessons. You may start from there but you need to install MongoDB on Ubuntu
15.10 at this time. Systemd is a main init system in Ubuntu 15.10 and you need
to place a service file using an Ansible module. Certain conditions should be
met in your submission, see the requirements below:

* create a new Ansible role where
   - ``mongodb`` is a role name

* Describe tasks in *tasks* directory
   - Add the MongoDB public GPG key from:
       - ``hkp://keyserver.ubuntu.com:80``
       - Use ``EA312927`` as MongoDB public GPG Key ID when Ubuntu package
         management imports a key (apt-key)
   - Install ``mongodb-org`` with 3.2 Community Edition for Ubuntu Trusty 14.04
     LTS by adding a MongoDB repository from:
       - ``deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse``

* Define those as Ansible variables in *defaults* directory, at least the three
  variable names below should be used:

   - mongodb_keyserver (to store hkp://...)
   - mongodb_gpgkey_id (to store EA312...)
   - mongodb_repository_list (to store deb http://...)a
   - (more vars can be defined)

* Two handlers
   - one for starting mongodb
   - one for reloading mongodb

* Place a service file where:
   - destination is ``/lib/systemd/system/mongodb.service``
   - owner/group of the destination file is ``root``
   - mode of the file is ``0644``
   - reload mongodb after adding this file to remote
   - *You can find mongodb.service* template file in your hw4 branch

* Write a main playbook:
   - to include your new role
   - in ``site.yml`` file

* Run ``hw4.sh`` to record your outputs in ``hw4-cmd.script`` file

FAQ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Q. How do I avoid typing SSH passphrase while current session is alive?

A. Use ssh-agent like this::

    eval `ssh-agent`
    ssh-add

Q. Where should I run Ansible Playbooks or Roles?

A. It is on india.futuresystems.org, not on your VM instance.

Submission via IU GitHub (github.iu.edu)
-------------------------------------------------------------------------------

Use IU GitHub to submit assignments on a private repository. :ref:`IU GitHub
Guidelines <ref-iu-github-for-assignments>`

1. Clone your private repository from the course organization.
   You IU Username is the name of your repository.

2. Create a ``hw4`` branch 

::

   git branch hw4
   git checkout hw4

3. Run ``pull`` command to fetch and merge with the template repository::

   git pull git@github.iu.edu:bdossp-sp16/assignments.git hw4

4. Sync with remote::

   git push -u origin hw4

5. Add files and directories to your repository::

   git add inventory
   git add mongodb
   git add site.yml
   git add hw4-cmd.script

6. commit

   ::

     git commit -am "submission hw4"

7. Sync your changes::

   git push -u origin hw4

Useful links
-------------------------------------------------------------------------------


