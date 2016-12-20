.. _ref-ansible-roles:


Ansible Roles
-------------------------------------------------------------------------------

There are two ways to use a role in your project:

1. Use a predefined role found on either Ansible Galaxy or Github
2. Write your own.

If you end up writing your own role, please follow these guidelines:

1. Create the role template by running ``ansible-galaxy init <role name>``
2. Put variables in ``defaults/main.yml``, delete ``vars`` (it should not be used)
3. Fill out ``meta/main.yml`` with appropriate values, and delete the others to clean up the file
4. When defining tasks in ``tasks/main.yml`` use `modules`_ whenever possible
5. Follow the `best practices`_ advice


For example:

Create the role::

   $ cd roles
   $ ansible-galaxy init foobar
   $ cd foobar
   $ rm -rf vars

Fill out the meta data::

   $ emacs meta/main.yml

Define the tasks and variables::

   $ emacs tasks/main.yml defaults/main.yml

Use the role in your playbook::

   $ cd ../..
   $ emacs site.yml



.. _modules: https://docs.ansible.com/ansible/list_of_all_modules.html

.. _best practices: https://docs.ansible.com/ansible/playbooks_best_practices.html
