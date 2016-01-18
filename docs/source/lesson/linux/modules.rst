Software Modules
======================================================================

Overview
----------------------------------------------------------------------

This lesson will introduce you using Softare Modules on FutureSystems

.. tip:: Duration: 15 minutes

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have knowledge of

* How to log into you FutureSystems account (see
  :doc:`../system/futuresystemsuse`)
* Use of the Shell (see :doc:`shell`)
* Some understanding of software installation on Linux (see for
  example :doc:`packagemanagement`)

Description
----------------------------------------------------------------------

If a software application is not present in a package manager like
``yum``, ``apt-get``, or ``brew``, it may be installed manually.  In
this case, the system administrators may install the application so
that it is globally accessible (similar to the behavior of a package
manager).

In the case of specialized software however, a global installation may
not be desirable in a multiuser system. This is an example of
encapsulation: only individuals (or software) that need to know about
a software should have that knowlege.

To encapsulate a software installation there exists a software
application called Modules. This allows a new software to be installed
such that it is accessible only if needed.

Let's explore this on FutureSystems: start by logging into
``india.futuresystems.org``. You will be at the shell prompt.

Now, lets run the Ruby interactive interpreter. The command to do so
is just ``irb``::

  $ irb

.. note::

   Ruby is a programming language with some similarities to Python.


You should see output like the following::

  -bash: irb: command not found

This means that Ruby is currently not available.
To see if it is available to us we can use the ``module`` command::

  $ module avail ruby
  ---------- /opt/Modules/3.2.8/modulefiles/applications -----------
  ruby/1.9.3
  
Now we know that Ruby is installed, but not currently available.  To
load the appropriate environment to use Ruby we use the ``module
load`` command::

  $ module load ruby/1.9.3
  ruby version 1.9.3 loaded
  $ irb
  irb(main):001:0>

We are now at the Ruby prompt.
Let enter a quick check to see Ruby in action::

  irb(main):001:0> 21*2
  => 42

Since everything looks good so exit the interpreter using ``exit``::

  irb(main):001:0> exit
  $

.. tip::

   Some usefull Module commands are:

   - ``module avail`` with no paramaters lists everything available
   - ``module load`` with one or more space-separated names (as shown
     my ``module avail``) will load those modules
   - ``module list`` will list the currently loaded modules
   - ``module unload`` with one ore more names will unload any modules
     loaded by ``module load``.
   - ``module whatis`` followed by zero or more names will give some
     information about the individual modules.
   - ``module switch old new`` will replace the module named ``old``
     with the one named ``new``.

Exercises
----------------------------------------------------------------------

Exercise I
^^^^^^^^^^^^^^^^^^

There are several python modules available. Take a look by running::

  $ module avail python

Load the default one and get the version and where the command is located (using ``which``)::

  $ module load python
  $ python -V
  Python 2.7
  $ which python
  /N/soft/python/2.7/bin/python

Now, for each of the python modules you saw in the output of ``module avail python`` above, do the following:

#. unload the current python module
#. load the new one
#. print the version using ``python -V``
#. get the location using ``which python``

You will be running something like the following, except replace
``[redacted]`` with the appropriate commands:

.. code:: bash

   $ [redacted]
   $ [redacted]
   $ python -V
   2.7.2
   $ which python
   /N/soft/python/2.7.2/bin/python
   $ [redacted]
   $ [redacted]
   $ python -V
   [etc etc]

