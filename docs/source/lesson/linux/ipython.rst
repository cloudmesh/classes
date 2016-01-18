IPython
======================================================================

.. sidebar:: Page Contents

   .. contents::
      :local:


Overview
----------------------------------------------------------------------

This lesson will introduce you to using the IPython shell

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have knowledge of

* the linux shell (see :doc:`shell`)
* the Python language (see :doc:`python`)

Description
----------------------------------------------------------------------

IPython provides a rich architecture for interactive computing with:

- Powerful interactive shells (terminal and Qt-based).
- A browser-based notebook with support for code, text, mathematical
  expressions, inline plots and other rich media.
- Support for interactive data visualization and use of GUI toolkits.
- Flexible, embeddable interpreters to load into your own projects.
- Easy to use, high performance tools for parallel computing.


Setup
----------------------------------------------------------------------

To install IPython log into your account on ``india``.
Next load the python module::

  $ module load python

Load the virtual environment::

  $ source ~/ENV/bin/activate

Install IPython::

  $ pip install ipython


Using IPython Shell
----------------------------------------------------------------------

To start the IPython shell, type::

  $ ipython
  Python 2.7 (r27:82500, Aug 10 2010, 11:35:15) 
  Type "copyright", "credits" or "license" for more information.

  IPython 3.0.0 -- An enhanced Interactive Python.
  ?         -> Introduction and overview of IPython's features.
  %quickref -> Quick reference.
  help      -> Python's own help system.
  object?   -> Details about 'object', use 'object??' for extra details.

  In [1]:

You can now use the IPython REPL just like the regular Python REPL.
Some enhancements include:

- using ``?`` for help (try: ``help?``)
- using some shell commands (try: ``ls``, and ``pwd``)
- tab-completion for python (try: ``helTAB``)

.. important::

   There are many many more features of IPython. Please read more on the `IPython website`_.

   .. _IPython website: http://ipython.org/


