Ansible Advanced
======================================================================

In this example, we are going to install R package onto your cloud VMs. R is a useful statistic programing language commonly used in many scientific and statistics computing projects, maybe also the one you chose for this class.

In addition to last basic example, we are going to illustrate the concept of Ansible Roles, install source code through Github, and make use of variables. These are key features you will find useful in your project deployments.

We are going to use a top-down fashion in this example. We first start from a playbook that is already good to go. You can execute this playbook (don't do it yet) to get R installed in your remote hosts. We then further complicate this concise playbook by introducing functionalities to do the same tasks but in different ways. Although these detours are not necessary in this simply case, it helps you grasp the power of Ansible and ease your life when they are needed in your real projects.

Prerequisite
----------------------------------------------------------------------

- Finished Ansible Lesson I
- Have VMs reserved on cloud and SSH Key setup

A completed playbook
----------------------------------------------------------------------

From the earlier example, we already can compose a playbook 'example.yml' that install a software package, for example::

   ---
   - hosts: R_hosts
     become: yes
     tasks:
       - name: install the R package
         apt: name=r-base update_cache=yes state=latest

the hosts are defined in a file 'hosts', which we configured in 'ansible.cfg'::

   [R_hosts]
   <cloud_server_ip> ansible_ssh_user=<cloud_server_username>

This should get the installation job done. But we are going to extend it via new features next.

Introducing Roles
----------------------------------------------------------------------

Role is an important concept used very often in large Ansible projects. You divide a series of tasks into different groups. Each group corresponds to certain role of the whole project.

For example, if your project is to deploy a web site, you may need to install the back end database, the web server that responses HTTP requests and the web application itself. They are three different roles and should carry out their own installation and configuration tasks.

Even though we only need to install the R package in this example, we can still do it by defining a role 'r'. Modify your 'example.yml' to be::

   ---
   - hosts: R_hosts

     roles:
       - r

and create directory structure in your top project directory::

   $ mkdir -p roles/r/tasks
   $ touch roles/r/tasks/main.yml

edit this 'main.yml' to be::

   ---
   - name: install the R package
     apt: name=r-base update_cache=yes state=latest
     become: yes

You probably already get the point. We take the 'tasks' section out of the one-for-all example.yml and re-organize them into roles. Each role specified in example.yml should have its own directory under roles/ and the tasks need be done by this role is listed in a file 'tasks/main.yml' as above.

Install source code from Github
----------------------------------------------------------------------

Although R can be installed through the OS package manager (apt-get etc.), the software used in your projects may not. Many research projects are available by Git instead. Here we are going to show you how to install packages from their Git repositories. Instead of directly executing the module 'apt', we pretend Ubuntu does not provide this package and you have to find it on Git. The source code of R can be found at https://github.com/wch/r-source.git. We are going to clone it to a remote VM's hard drive, build the package and install the binary there.

To do so, we need a few new Ansible modules. You may remember from last example that Ansible modules assist us to do various kinds of jobs when fed correct arguments. No surprise, Ansible has a module 'git' to take care of git-related works, and a 'command' module to run shell commands. Let's modify 'roles/r/tasks/main.yml' to be::

   ---
   - name: get R package source
     git:
       repo: https://github.com/wch/r-source.git
       dest: /tmp/R

   - name: build and install R
     become: yes
     command: chdir=/tmp/R "{{ item }}"
     with_items:
       - ./configure
       - make
       - make install

The role 'r' carries out its two tasks now. One to clone the R source code into /tmp/R, the other uses a series of shell commands to build and install the packages.

.. warning:: Note that the commands executed by the second task may not be available on a fresh VM image. But the point of this example is to show an alternative way to install packages, so we conveniently assume conditions are all met.

Using variables in a separate file
----------------------------------------------------------------------

We typed several string constants in our Ansible scripts so far. In general, it is a good practice to give these values names and use them by referring to their names. This way, you complex Ansible project can be less error prone. Create a file in the same directory, and name it 'vars.yml'::

   ---
   repository: https://github.com/wch/r-source.git
   tmp: /tmp/R

Accordingly, we will update our 'example.yml'::

   ---
   - hosts: R_hosts
     vars_files:
       - vars.yml
     roles:
       - r

As shown, we specify a 'vars_files' telling the script that the file 'vars.yml' is going to supply variable values, whose keys are denoted by Double curly brackets like in 'roles/r/tasks/main.yml'::

   ---
   - name: get R package source
     git:
       repo: "{{ repository }}"
       dest: "{{ tmp }}"

   - name: build and install R
     become: yes
     command: chdir="{{ tmp }}" "{{ item }}"
     with_items:
       - ./configure
       - make
       - make install

Summarize
----------------------------------------------------------------------

Now, just edit the 'hosts' file with your target VMs' IP addresses and execute the playbook.

You should be able to extend the Ansible playbook for your project. Configuration tools like Ansible are important components to master the cloud environment. There is much to explore and it's worth it.