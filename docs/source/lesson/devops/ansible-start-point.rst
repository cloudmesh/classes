

Ansible
======================================================================

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson:

* You can install Ubuntu 16.04 virtual machine on VirtualBox
* You can install software packages via 'apt-get' tool in Ubuntu virtual host
* You already reserved a virtual cluster (with at least 1 virtual machine in it) on some cloud. OR you can use VMs installed in VirtualBox instead.
* You set up SSH credentials and can login to your virtual machines.

What can you do with Ansible?
----------------------------------------------------------------------

Humans do maintenance and configurations on computers. Essentially, we specify a list of operations and a list of target machines where the operations apply to. After defining these two critical lists, the creative works are done, and the rest labour can be automated. And this is what Ansible is used for.

Let us develop a sample from scratch, based on this paradigm.

A sample use case
----------------------------------------------------------------------

In this example, we are going to use Ansible to install Apache server on our VMs.

- install Ansible tool on your machine first

.. code-block:: bash

   $ sudo apt-get update
   $ sudo apt-get install ansible

- prepare a working environment for your Ansible

.. code-block:: bash

   $ mkdir ansible-apache
   $ cd ansible-apache

- next, we are going to create a local configuration file for Ansible.
   
When you execute Ansible within this folder, this local configuration file is always going to overwrite a system level Ansible configuration. It is in general beneficial to keep custom configurations locally unless you absolutely believe it should be applied system wide. Create a file 'ansible.cfg' in this folder, and fill::

   [defaults]
   hostfile = hosts
   
This local configuration file simple tells that the target machines' names are given in a file named 'hosts'

- specify hosts in the file

You should have accesses to all VMs listed in this file as part of our prerequisites. Create and edit file 'hosts'::

   [apache]
   <server_ip> ansible_ssh_user=<server_username>
   
The name 'apache' in the brackets defines the server group name. We will use this name to refer to all server items in this group next. Fill in IP addresses of the virtual machines you launched in your VirtualBox and fire up these VMs in you VirtualBox.

- compose a playbook

A playbook tells Ansible what to do. it uses YAML Markup syntax. Create and edit a file with a proper name e.g. apache.yml as follow::

   ---
   - hosts: apache #comment: apache is the group name we just defined
     become: yes #comment: this operation needs privilege access
     tasks:
       - name: install apache2 # text description
         apt: name=apache2 update_cache=yes state=latest

This block defines the target VMs and operations(tasks) need to apply. you may wonder what 'apt' means. here comes the concept of Ansible modules in next paragraph.

The concept of modules
----------------------------------------------------------------------

'apt' is the module used in our sample playbook. it installs packages on Ubuntu for us.

Ansible relies on various kinds of modules to fulfil tasks on the remote servers. These modules are developed for particular tasks and take in related arguments. For instance, when we use 'apt' module, we certainly need to tell which package we intend to install. That is why we provide a value for the 'name' argument.

Run you playbook
----------------------------------------------------------------------

In the same folder, execute

.. code-block:: bash

   ansible-playbook apache.yml --ask-sudo-pass

After a successful run, open a browser and fill in your server IP. you should se a 'It works!' Apache2 Ubuntu default page. Make sure the security policy on your cloud opens port 80 to let the HTTP traffic go through.


Ansible playbook can have more complex and fancy structure and syntaxes. Go explore!
this sample is based on: https://www.digitalocean.com/community/tutorials/how-to-configure-apache-using-ansible-on-ubuntu-14-04

We are going to offer an advanced Ansible in next chapter.