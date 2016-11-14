========
 README
========

This repository contains class material.


=========
 Classes
=========

The following directories contain the class materials:

- `fall-2016`_: Big Data Applications and Analytics, Fall 2016
- `spring-2016`_: Big Data Open Source Software Projects, Spring 2016

===========================
 Adding other repositories
===========================


If class material has been developed in another repository, it can be
added to this repository using ``git subtree``.

For instance, say a class had been taugh in the spring of 1971 and was
located at git as::

  git@github.com/somegroup/class-material.git

It may be added here like so:

.. code-block:: sh

   $ git subtree add -P spring-1971 git@github.com/somegroup/class-material.git master


This has the effect of keeping the history of the added subtree
repository intact, merging it with the current repositories history.


============================
 Known External Repositores
============================

Several of the courses have been developed in separate
repositories. If a class is updated externally, the new history will
need to be merged by rerunning the ``git subtree add`` command above.

- `fall-2016`_: ``git@gitlab.com:cloudmesh/fall2016.git``
- `spring-2016`_: ``git@github.com:cglmoocs/bdossspring2016.git``



.. ................................................................  links





.. _fall-2016: ./fall-2016
.. _spring-2016: ./spring-2016
