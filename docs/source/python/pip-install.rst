Often you may need functionality that is not present in Python's standard library.
In this case you have two option:

- implement the features yourself
- use a third-party library that has the desired features.

Often you can find a previous implementation of what you need.
Since this is a common situation, there is a service supporting it:
the `Python Package Index`_ (or PyPi for short).


Our task here is to install the `autopep8`_ tool from PyPi.
This will allow us to illustrate the use if virtual environments using
the ``virtualenv`` command, and installing and uninstalling PyPi
packages using ``pip``.


Virtual Environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often when you use shared computing resources, such as
``india.futuresystems.org`` you will not have permission to install
applications in the default global location.

Let's see where ``grep`` is located::

  $ which grep
  /bin/grep

It seems that there are many programs installed in ``/bin`` such as
``mkdir`` and ``pwd``::

  $ ls /bin
  alsacard    dbus-cleanup-sockets  env             hostname         mailx          pwd
  alsaunmute  dbus-daemon           ex              igawk            mkdir          raw
  ...

If we wished to add a new program it seems like putting it in ``/bin`` is the place to start.
Let's create an empty file ``/bin/hello-$PORTALNAME``::

  $ touch /bin/hello-$(whoami)
  touch: cannot touch `/bin/hello-albert': Permission denied


.. tip::

   Recall that $PORTALNAME is your username on FutureSystems, which can
   also be obtained using the ``whoami`` shell command.


It seems that this is not possible.  Since ``india`` is a shared
resources not all users should be allowed to make changes that could
affect everyone else.  Only a small number of users, the
administrators, have the ability to globally modify the system.

We can still create our program in our home directory::

  $ touch ~/hello-$(whoami)

but this becomes cumbersome very quickly if we have a large number of
programs to install.  Additionally, it is not a good idea to modify
the global environment of one's computing system as this can lead to
instability and bizarre errors.

A virtual environment is a way of encapsulating and automating the
creation and use of a computing environment that is consistent and
self-contained.

The tool we use with Python to accomplish this is called ``virtualenv``.

Let's try it out. Start by cleaning up our test earlier and going
into the home directory::

  $ rm ~/hello-$(whoami)
  $ cd ~


Now lets create a virtual env::

  $ virtualenv ENV
  PYTHONHOME is set.  You *must* activate the virtualenv before using it
  New python executable in ENV/bin/python
  Installing setuptools............done.
  Installing pip...............done.


When using ``virtualenv`` you pass the directory where you which to
create the virtual environment, in this case ``ENV`` in the current
(home) directory.  We are then told that we must activate the virtual
environment before using it and that the python program, setuptools,
and pip are installed.

Let's see what we have::

  $ ls ENV/bin
  activate  activate.csh  activate.fish  activate_this.py  easy_install
  easy_install-2.7  pip  pip-2.7  python  python2  python2.7

It seems that there are several programs installed.  Let's see where
our current ``python`` is and what happens after activating this
environment::

  $ which python
  /N/soft/python/2.7/bin/python
  $ source ENV/bin/activate
  (ENV) $ which python
  ~/ENV/bin/python

.. important::

   As virtualenv stated, you **must** activate the virtual environment
   before it can be used.

.. tip::

   Notice how the shell prompt changed upon activation.


Fixing Bad Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's now look at another important tool for Python development: the
Python Package Index, or PyPI for short.  PyPI provides a large set of
third-party python packages.  If you want to do something in python,
first check pypi, as odd are someone already ran into the problem and
created a package solving it.

I'm going to demonstrate creating a user python environment,
installing a couple packages from pypi, and use them to examine some
code.

First, get the bad code like so::

   $ wget --no-check-certificate http://git.io/pXqb -O bad_code_example.py

Let's examine the code::

  $ nano bad_code_example.py

As you can see, this is very dense and hard to read.  Cleaning it up
by hand would be a time-consuming and error-prone process.  Luckily,
this is a common problem so there exist a couple packages to help in
this situation.

Using ``pip`` to install packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to install package from PyPI, use the ``pip`` command.
We can search for PyPI for packages::

  $ pip search --trusted-host pypi.python.org autopep8 pylint

It appears that the top two results are what we want so install them::

  $ pip install --trusted-host pypi.python.org autopep8 pylint

This will cause ``pip`` to download the packages from PyPI, extract
them, check their dependencies and install those as needed, then
install the requested packages.

.. note:: You can skip '--trusted-host pypi.python.org' option if you have a
        patch on urllib3 on Python 2.7.9.

Using ``autopep8``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can now run the bad code through autopep8 to fix formatting
problems::

  $ autopep8 bad_code_example.py >code_example_autopep8.py

Let's look at the result.
This is considerably better than before.
It is easy to tell what the example1 and example2 functions are doing.

It is a good idea to develop a habit of using ``autopep8`` in your
python-development workflow.  For instance: use ``autopep8`` to check
a file, and if it passes, make any changes in place using the ``-i``
flag::

  $ autopep8 file.py    # check output to see of passes
  $ autopep8 -i file.py # update in place




.. _Python Package Index: https://pypi.python.org/pypi
