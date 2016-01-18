Package Management
======================================================================

Overview
----------------------------------------------------------------------

This lesson will introduce you to using yum, apt-get and brew.

.. tip:: Duration: 30 minutes

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have knowledge of

* Using the linux shell (see :doc:`shell`)
* Package installation using ``pip`` (see :doc:`python`)

Description
----------------------------------------------------------------------

If you use Windows of Mac OS X you are already familiar with the
installation of programs for those systems. Package management is a
slightly different angle to the sample problem: how do you get
software, and everything it needs to run, installed on a computer.

All three software packages, yum, apt-get, and brew, are attempts to
solve this problem.

If you want to install something on Windows or OS X, you typically go
to the producer's website, find a download link, and run the result.

For example, I want to install Python. How would I accomplish this using ``brew``?

.. code:: bash

   $ brew search python
   boost-python    python          python3         wxpython        zpython
   ...
   $ brew install python

Here I did not need to go to the Python webpage. I asked ``brew`` to
search for python for me. It provided me with a list of options, and I
then selected one to install.

A package manager like yum, apt-get, and brew contains a **database**
of software packages and their and their state: installed or not,
version installed, version available, name, description.
When you want to install a particular package, you need to know the name and then you can issue the appropriate install directive.

.. tip::

   In the case of ``yum``, ``apt-get``, and ``brew``, the install
   directirve is the same: ``install``.


.. important::

   The key point of using package managers like these is the ability
   to automate the installation of many packages. If you need to
   install packages many times, you can save them to a shell script
   and then run the script on each machine instead of manually
   installing each by hand.

  
..
   Exercises
   ----------------------------------------------------------------------

   Exercise I
   ^^^^^^^^^^^^^^^^^^

   Exercise II
   ^^^^^^^^^^^^^^^^^^

   Next Step
   -----------

   In the next page, ...

   `Link here <link>`_
