README
========
 
This repository contains class material. The class is published and updated on a regular basis at:

* https://cloudmesh.github.io/classes/

We are in the process of reorgannizing this directory and all of the class materials will be in docs/sources.

Working with Git
================

When working with git, do not forget to set it up properly. Often users seem to forget 
the following important commands to initialize it::

  $ git config --global user.name "Albert Zweistein"
  $ git config --global user.email albert.zweistein@gmail.com

Developing
==========

Requirements:
- python
- pip
- virtualenv

Preliminary steps:

#. clone the repository
#. create/activate a virtualenv
#. install the requirements::
  $ pip install -r requirements.txt

Making changes:

Files are under `docs/sources`

Use `make` to build html.

Use `make view` to open the index.html in a browser window.

Submitting changes
==================

Please only fork and work in the master branch.

Pull requests can be submitted against the master branch.
Please `synchronize against master <https://help.github.com/articles/syncing-a-fork/>`_ before submitting a request.

Make sure you have this repository added as `upstream`::

  $ git remote -v
  origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
  origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
  upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)
  upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)

To add the upstream repo::

  $ git remote add upstream https://github.com/cloudmesh/classes
  
To synchronize your changes::

  $ git fetch upstream
  $ git rebase upstream/master

Push your changes and submit a pull request::

  $ git push origin master

Please, do not work on gh-pages or try to create a merge from gh-pages into master. gh-pages is managed by us and is **always** overwritten and all changes will be lost from it. 


.. ................................................................  links

Known External Repositores
============================

These are older repositories:

- `fall-2016`_: ``git@gitlab.com:cloudmesh/fall2016.git``
- `spring-2016`_: ``git@github.com:cglmoocs/bdossspring2016.git``








.. _spring-2017: ./spring-2017
.. _fall-2016: ./fall-2016
.. _spring-2016: ./spring-2016

.. _Spring 2017, RTD: http://cloudmesh-classes.readthedocs.io/projects/spring-2017/en/latest/
.. _Fall 2016, RTD: http://cloudmesh-classes.readthedocs.io/projects/fall-2016/en/latest/

.. _Read the Docs: http://cloudmesh-classes.readthedocs.io/en/latest/
.. _RTD Admin Page: https://readthedocs.org/dashboard/cloudmesh-classes/edit/
.. _RTD Advanced Settings: https://readthedocs.org/dashboard/cloudmesh-classes/advanced/
.. _RTD Subprojects: https://readthedocs.org/dashboard/cloudmesh-classes/subprojects/
.. _RTD Maintainer: https://readthedocs.org/dashboard/cloudmesh-classes/users/
