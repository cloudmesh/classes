Ansible Roles
-------------------------------------------------------------------------------

Ansible roles provide encapsulation of software deployment and reusable
abstraction than a single large ansible playbooks. Use an Ansible role as a
single function to install/configure software.  For example, the big-data-stack
hadoop cluster uses limits, java, supervisord and zookeeper as a base role and
has hbase, pig and spark as an additional role to deploy. Each individual role
works together to build a software stack e.g. big-data-stack hadoop cluster and
any roles can be easily included or excluded in the main playbook. Ansible
Galaxy, the public roles repository, shares 5271 ansible roles and you can
download roles from Ansible Galaxy to include them in your playbook for server
configuration or software installation.

Sub Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your role may have 8 initial sub directories, if you created a new role by
``ansible-galaxy init`` command.

::

  defaults  files  handlers  meta  tasks  templates  tests  vars


* defaults: default lower priority variables for this role
* files: files for use with the copy or script resource
* handlers: handlers are defined in this directory
* meta: description for a role, if it is shared via Ansible Galaxy
* tasks: tasks are defined in this directory
* templates: files for use with the template resource
* tests: local test purpose
* vars: variables associated with this role

Each sub directory has ``main.yml`` as a default to start writing Ansible plays
except files and templates directories.

Using Roles in Main Playbook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A playbook includes roles with ``roles:`` key name. For example,::

  ---
  ...
  roles:
    - roleA
    - roleB
    - ...

A role should exist as a sub directory with its name, otherwise the playbook
can't find roles.

The directory layout of the Hadoop cluster, for instance, looks like::

  $ ls
  java  limits  site.yml        supervisord  zookeeper
  
  $ ls *
  site.yml

  java:
  defaults  files  handlers  meta  README.md  tasks  templates  tests  vars

  limits:
  defaults  files  handlers  meta  README.md  tasks  templates  tests  vars

  supervisord:
  defaults  files  handlers  meta  README.md  tasks  templates  tests  vars

  zookeeper:
  defaults  files  handlers  meta  README.md  tasks  templates  tests  vars


where ``site.yml`` is a main playbook which includes java, limits, supervisord,
and zookeeper roles.

``defaults`` (least precedence)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ansible allows you to use variables with conditionals and loops in
configuring/managing different systems. It is also easy to make changes in
which variables are defined rather than updating all files. You may define
variables in ``defaults`` directory. 

For example, the ``hadoop_install`` role has default variables such as::

  hadoop_version: 2.7.1
  hadoop_archive_ext: .tar.gz
  ...

The variables can be used with the Jinja2 template, for example, ::

  hadoop_archive_name: "hadoop-{{ hadoop_version }}{{ hadoop_archive_ext }}"

`Jinja2 <http://jinja.pocoo.org/docs/dev/>`_ is a templating engine for Python
and the double curl braces ``{{`` and ``}}`` indicate a variable. Ansible
replaces it with a real value associated with the variable. ``{{ hadoop_version
}}`` is replaced with ``2.7.1`` and ``{{hadoop_archive_ext }}`` is replaced
with ``.tar.gz`` based on the definition in defaults.

Least precedence means that variables are easily overridden in this directory.
If you define a same variable in the ``vars`` directory, the value will be
replaced when Ansible runs play. The precedence of variables is like ``defaults
< vars``. There are specific orders, please find out details here:
http://docs.ansible.com/ansible/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable

.. note:: YAML syntax requires that if you start a value with {{ foo }} you
        quote the whole line, since it wants to be sure you aren’t trying to
        start a YAML dictionary. This is covered on the `YAML Syntax
        <http://docs.ansible.com/ansible/YAMLSyntax.html>`_ page.

There are other useful features and rules such as Facts, Registered variables
or variable precedence, you can find more information here:
http://docs.ansible.com/ansible/playbooks_variables.html


Find the original file from here:
https://github.com/futuresystems/ansible-role-hadoop_install/blob/master/defaults/main.yml

``tasks``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tasks are defined in this ``tasks`` directory and variables can be used to
complete the tasks.  For example, ``hadoop_install`` role has a first task to
download a compressed tarball like this::

  - name: fetch hadoop
    get_url:
      url: "{{ hadoop_url }}"
      dest: "{{ ansible_env.PWD }}/{{ hadoop_archive_name }}"
      sha256sum: "{{ hadoop_archive_sha256[hadoop_version] }}"
      timeout: "{{ hadoop_download_timeout }}"

The ``get_url`` module downloads a hadoop from the ``hadoop_url`` variable and
stores it to destination. Let's look at the ``{{ ansible_env.PWD }}`` variable,
which is not defined in ``defaults`` or ``vars`` directory. You may find other
variables though.  The ``PWD`` (print working directory) will be obtained from
remote environment variables via ansible Facts in the `ansible_env` variable.

Find the original file from here:
https://github.com/futuresystems/ansible-role-hadoop_install/blob/master/tasks/main.yml

Conditionals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes a single task is not suitable to deal with multiple operating systems
although it is a same task e.g. installing software.  With Ansible
Conditionals, particular tasks can be chosen based on variables.
``ansible_os_family`` from Facts can be used with ``when`` statement. For
example, *nginx* is installed via *apt-get* on Debian-based operating system
but *nginx* is installed via *yum* on Redhad-based OS. The conditionals look like::

  tasks:
    - name: "nginx installation on RedHat"
      yum:
        name: "{{ nginx_package_name }}"
        state: installed
        when: ansible_os_family == 'RedHat'

    - name: "nginx installation on Debian"
      apt-get:
        name: "{{ nginx_package_name }}"
        state: installed
        when: ansible_os_family == 'Debian'

Furthermore, you may consider to use ``when`` statement in *roles* and
*includes*, if you have streamlined tasks on certain conditions.::

  - include: setup-RedHat.yml
    when: ansible_os_family == 'RedHat'

or with a role::

  - hosts: webservers
    roles:
      - role: nginx-RedHat
        when: ansible_os_family == 'RedHat'

If you like to include operating systems specific variables, create a variable definition file per OS and import it with a variable syntax like::

  # variable import where 
  # - vars/RedHat.yml and 
  # - vars/Debian.yml exist
  - name: include os-specific variables
    include_vars: "{{ ansible_os_family }}.yml"

Find more information about Ansible Conditionals here:
http://docs.ansible.com/ansible/playbooks_conditionals.html

Loops
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ansible provides powerful interation tools over different variable types:
string, nested, hashes, files, and so on. Let's talk about a simple loop in
this lesson but you can find more details here:
http://docs.ansible.com/ansible/playbooks_loops.html

In a standard loop, you use ``{{ item }}`` where each item will be located and
``with_items:`` is followed by list of items. For example, ``export`` is
repeated with items like::

  - name: set environment exports
    lineinfile:
      dest: "/etc/profile.d/hadoop.sh"
      line: "export {{ item }}"
      create: yes
    with_items:
      - HADOOP_HOME={{ hadoop_home }}
      - HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
      - HADOOP_INSTALL=$HADOOP_HOME
      - PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
      - HADOOP_PID_DIR=$HADOOP_HOME/pid
      - YARN_LOG_DIR={{ hadoop_yarn_log_dir }}
      - HADOOP_LOGLEVEL={{ hadoop_loglevel }}
      - LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HADOOP_HOME/lib/native

Find the original file here:
https://github.com/futuresystems/ansible-role-hadoop_install/blob/master/tasks/main.yml#L72

Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Actual work is done by Ansible modules and we describe how to run modules in
*tasks* with other arguments. There are 495 modules available, let's review
some modules with simple examples.

Find all modules here: http://docs.ansible.com/ansible/modules_by_category.html

get_url
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

get_url: downloads files from HTTP, HTTPS or FTP to node. `[documentation]
  <http://docs.ansible.com/ansible/get_url_module.html>`_

A simple download can be done like::

  - name: download a file
    get_url: url=http://address.com/abc.tar.gz dest=/tmp/abc.tar.gz

In a real example of Hadoop download::

  - name: fetch hadoop
    get_url:
      url: "{{ hadoop_url }}"
      dest: "{{ ansible_env.PWD }}/{{ hadoop_archive_name }}"
      sha256sum: "{{ hadoop_archive_sha256[hadoop_version] }}"
      timeout: "{{ hadoop_download_timeout }}"

* url: actual link to download a file
* dest: destination path to store a file
* sha256sum: a SHA-256 checksum to make sure a file is valid
* timeout: timeout in seconds for URL request
You can use other options, find more details, `[documentation]
  <http://docs.ansible.com/ansible/get_url_module.html>`_

file
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

file: sets attributes of files / directories

A simple use of file is like this to update a permission with a owner
read/write only::

  - file: path="{{ lookup('env','HOME') }}"/.ssh/id_rsa mode=0600

A symlink is created like this in the ``hadoop_install`` role::

  - name: create symlink shortcut
    file:
      src: "{{ hadoop_home_dir }}/{{ hadoop_extracted_name }}"
      dest: "{{ hadoop_home }}"
      state: link

``state: link`` indicates a symbolic link. ``state: directory`` can be used if
a new directory is necessary.  ``state: absent`` is used to delete
files/directories.  Other choices are available e.g. *file*, *hard*, *touch*,
and *absent*

You can use other options, find more details here:
`[documentation] <http://docs.ansible.com/ansible/file_module.html>`_

lineinfile
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

lineinfile: Ensure a particular line is in a file, or replace an existing line
using a back-referenced regular expression.

Replacing a loopback IP address with a hostname in *hosts* file is like::

  - lineinfile: dest=/etc/hosts regexp='^127\.0\.0\.1' line='127.0.0.1 localhost'

In the ``hadoop_install`` role, we use *lineinfile* to add lines like::

  - name: set environment exports
    lineinfile:
      dest: "/etc/profile.d/hadoop.sh"
      line: "export {{ item }}"
      create: yes
    with_items:
      - HADOOP_HOME={{ hadoop_home }}
      - ...
 
You can use other options, find more details here:
`[documentation] <http://docs.ansible.com/ansible/lineinfile_module.html>`_

command
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

command: Executes a command on a remote node (similar to shell but redirection
or pipe is not allowed)

In the ``hadoop_install`` role, *tar* command is executed via *command* module
like this ::

  - name: extract hadoop
    command: tar xvf {{ hadoop_archive_name }} -C {{ hadoop_home_dir }}
    args:
      creates: "{{ hadoop_home_dir }}/{{ hadoop_extracted_name }}"

``creates:`` parameter works like conditionals. This *command* module only runs
when a file defined in ``creates:`` does not exist

You can use other options, find more details here:
`[documentation] <http://docs.ansible.com/ansible/command_module.html>`_
You may check out shell module as well here:
`[documentation] <http://docs.ansible.com/ansible/shell_module.html>`_

Useful Links
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ansible glossary: http://docs.ansible.com/ansible/glossary.html#handlers
