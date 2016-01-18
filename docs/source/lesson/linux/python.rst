Python Programming
======================================================================

.. sidebar:: Page Contents

   .. contents::
      :local:


Overview
----------------------------------------------------------------------

This lesson will introduce you to programming in Python.

.. tip:: Duration: 1 hour

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should

* Log onto your FutureSystems account
* Completed the :doc:`shell` lesson
* Completed the :doc:`editors` lesson


Learning Goals
----------------------------------------------------------------------

At the end of this lesson you will be able to:

- use Python in your FutureSystems account
- use the interactive Python interface
- understand the basic syntax of Python
- write and run Python programs stored in a file
- have an overview of the standard library
- install Python libraries using ``virtualenv``

Description
----------------------------------------------------------------------

.. include:: /class/lesson/linux/python/description.rst

Acknowledgments
----------------------------------------------------------------------

Portions of this lesson have been adapted from the `official Python
Tutorial`_ copyright `Python Software Foundation`_.

.. _official Python Tutorial: https://docs.python.org/2/tutorial/
.. _Python Software Foundation: http://www.python.org/

Introduction
----------------------------------------------------------------------

.. include:: /class/lesson/linux/python/introduction.rst

Using Python on FutureSystems
----------------------------------------------------------------------

.. include:: /class/lesson/linux/python/on-futuresystems.rst

Interactive Python
----------------------------------------------------------------------

.. include:: /class/lesson/linux/python/interactive.rst


Syntax
----------------------------------------------------------------------

.. include:: /class/lesson/linux/python/syntax.rst


Writing and Saving Programs
----------------------------------------------------------------------

Make sure you are no longer in the interactive interpreter.
If you are you can type ``quit()`` and press Enter to exit.

.. include:: /class/lesson/linux/python/saving.rst

Installing Libraries
----------------------------------------------------------------------

.. include:: /class/lesson/linux/python/pip-install.rst

Resources
----------------------------------------------------------------------

.. include:: /class/lesson/linux/python/resources.rst

  
Exercises
----------------------------------------------------------------------

.. _lab-python-1:

Lab - Python - FizzBuzz
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Write a python program called fizzbuzz.py that accepts an integer n
from the command line.  Pass this integer to a function called
fizzbuzz.

The fizzbuzz function should then iterate from 1 to n.  If the ith
number is a multiple of three, print "fizz", if a multiple of 5 print
"buzz", if a multiple of both print "fizzbuzz", else print the value.


.. _lab-python-2:

Lab - Python - Setup for FutureSystems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Create a virtualenv ``~/ENV``
#. Modify your ``~/.bashrc`` shell file to activate your environment
   upon login.
#. Install the ``docopt`` python package using ``pip``
#. Write a program that uses ``docopt`` to define a commandline
   program. Hint: modify the FizzBuzz program.
#. Demonstrate the program works and submit the code and output.
