HW5: Ansible Exercise
===============================================================================

.. note:: Replace ``mongodb.yml`` to ``site.yml`` in *hw5.sh*, if you failed
   running hw5.sh with the incorrect filename. If you recently pulled hw5
   branch in your private repository, you don't need this fix.

Guidelines
-------------------------------------------------------------------------------

* Assignments must be completed individually.
* Discussion is allowed (e.g. via Slack) but the submission should be made by
  yourself. Acknowledge your helpers/collaborators name in the submission if
  you discussed or got help from anyone.
* Use an individual github repository. A repository in FutureSystems will be
  given later.

Use ``hw5`` branch
-------------------------------------------------------------------------------

* Login https://github.iu.edu with your IU Username and Password
  (It is a same IU Credential that you use on other IU sites e.g. one.iu.edu)

* Checkout hw5 branch

MongoDB Ansible Role
-------------------------------------------------------------------------------

Writing Mongodb playbook is taught in the Ansible lessons. You write
MongoDB Ansible role in this assignment. Submit inventory, main playbook,
command script and your role including sub-directories.

Requirements
-------------------------------------------------------------------------------

The following files should be included in your submission

* ``inventory`` file
* ``site.yml`` the main playbook file
* ``mongodb`` directory (which is ansible role for mongodb)
* ``hw5-cmd.script`` file

Preparation
-------------------------------------------------------------------------------

* Login to india.futuresystems.org
* Use the same ``bdossp-sp16`` virtualenv used in hw3
* Install ``ansible`` via python package manager
* Change a directory to your IU GitHub repository where you work on hw5
* Create a new branch ``hw5`` by::

   git checkout -b hw5
* Pull hw5 template files by::

   git pull git@github.iu.edu:bdossp-sp16/assignments.git hw5
* Sync to remote by::

    git push origin hw5
* Start working on hw5

HW5 Tasks
-------------------------------------------------------------------------------

You need to write an Ansible role to install mongodb on your vm instance
``hw3-$USER``.  Ansible Playbook for MongoDB installation is given in the
Ansible lessons. You may start from there but you need to install MongoDB on
Ubuntu 15.10 at this time. Systemd is a main init system in Ubuntu 15.10 and
you need to locate a service file using Ansible modules. Certain conditions
should be met in your submission, see the requirements below:

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
   - mongodb_repository_list (to store deb http://...)
   - (more vars can be defined)

* Two handlers
   - one for starting mongodb
   - one for reloading mongodb

* Locate a service file where:
   - destination is ``/lib/systemd/system/mongodb.service``
   - owner/group of the destination file is ``root``
   - mode of the file is ``0644``
   - reload mongodb after adding this file to remote
   - You can find *mongodb.service.j2* template file in your hw5 branch

* Write a main playbook:
   - to include your new role
   - in ``site.yml`` file

* Run ``hw5.sh`` to record your outputs in ``hw5-cmd.script`` file

Grading Guidelines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Existence of required files/directories (15%)
   - inventory 
   - site.yml
   - (role) directory including subdirectories
   - hw5-cmd.script
* Proper use of Ansible Variables (15%)
* Proper use of Ansible Tasks (15%)
* Proper use of Ansible Templates (15%)
* Proper use of Ansible Handlers (15%)
* General understanding of Ansible Roles (20%)
* Successful Execution (5%)

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

2. Create a ``hw5`` branch 

::

   git branch hw5
   git checkout hw5

3. Run ``pull`` command to fetch and merge with the template repository::

   git pull git@github.iu.edu:bdossp-sp16/assignments.git hw5

4. Sync with remote::

   git push -u origin hw5

5. Add files and directories to your repository::

   git add inventory
   git add mongodb
   git add site.yml
   git add hw5-cmd.script

6. commit

   ::

     git commit -am "submission hw5"

7. Sync your changes::

   git push -u origin hw5

Challenging Tasks (Optional)
-------------------------------------------------------------------------------

The following tasks are optional but strongly recommended to try. These are
to write mongodb roles for RedHat-based operating system as well using Ansible
conditionals and different modules, if necessary.

MongoDB Roles for RedHat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You have completed writing mongodb roles for Ubuntu 15.10 which is Debian-based
operating system only.  In this challenge task, you are required to extend your
mongodb roles for RedHat-based operating system as well.  Ansible conditionals
is recommended to select correct tasks/files in different operating systems.

Find ``mongodb-redhat`` directory in challange sub-directory. Add your extended
mongodb role in the directory.

Possible Project idea (Running Ansible on Windows)
-------------------------------------------------------------------------------

Develop Ansible Playbooks and Roles for Windows machines using PowerShell and
winrm Python package instead of SSH. You may find multiple ways like:

- develop a PowereShell script that starts a VirtualBox and runs the Debian
  ansible in it, have a local key be used see the instalation instructions of
  Cloudmesh that let you set up ssh on a windows machine also.

- develop a Docker based ansible container. However this is not as straight
  forward as the key management need to be done right.

You can find more information here `Windows Support
<http://docs.ansible.com/ansible/intro_windows.html>`_

Useful links
-------------------------------------------------------------------------------

* Ansible Basic: http://bdossp-spring2016.readthedocs.org/en/latest/lesson/ansible.html
* Ansible Playbook: http://bdossp-spring2016.readthedocs.org/en/latest/lesson/ansible_playbook.html
* Ansible Role: http://bdossp-spring2016.readthedocs.org/en/latest/lesson/ansible_roles.html
* Ansible Best Practices: https://docs.ansible.com/ansible/playbooks_best_practices.html
* Ansible official documentation: http://docs.ansible.com/ansible/index.html
