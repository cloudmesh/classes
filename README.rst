========
 README
========

This repository contains class material.
The `Read the Docs`_ page points to the most recent class.
To access previous classes, see the RTD links in the `Classes`_ section.


=========
 Classes
=========

The following directories contain the class materials:

- `spring-2017`_: Big Data Open Source Software Projects, `Spring 2017, RTD`_
- `fall-2016`_: Big Data Applications and Analytics, `Fall 2016, RTD`_
- `spring-2016`_: Big Data Open Source Software Projects, Spring 2016

==========================
 Switching to a new class
==========================

#. Go to the `RTD Admin Page`_
#. Go to `RTD Advanced Settings`_
#. Change the path to the requirements file
#. Change the path to the python configuration file
#. Create a RTD for the new class
#. Go to `RTD Subprojects`_
#. Enter the RTD project name in the ``Subproject`` field
#. Enter the name that should show up in the url (eg ``spring-2017``)
   in the ``Alias`` field

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




.. _spring-2017: ./spring-2017
.. _fall-2016: ./fall-2016
.. _spring-2016: ./spring-2016

.. _Spring 2017, RTD: http://cloudmesh-classes.readthedocs.io/projects/spring-2017/en/latest/
.. _Fall 2017, RTD: http://cloudmesh-classes.readthedocs.io/projects/fall-2016/en/latest/

.. _Read the Docs: http://cloudmesh-classes.readthedocs.io/en/latest/
.. _RTD Admin Page: https://readthedocs.org/dashboard/cloudmesh-classes/edit/
.. _RTD Advanced Settings: https://readthedocs.org/dashboard/cloudmesh-classes/advanced/
.. _RTD Subprojects: https://readthedocs.org/dashboard/cloudmesh-classes/subprojects/
