README
========

This repository contains class material. The class is published and updated oon regular basis at:

* https://cloudmesh.github.io/classes/

We are in the process of reorgannizing this directory and all cals material will be in docs/sources.

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
