.. _Virtual_Environments:

Virtual Environments (on india)
-------------------------------

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

If we wished to add a new program it seems like putting it in ``/bin``
is the place to start.  Let's create an empty file
``/bin/hello-$PORTALNAME``::

  $ touch /bin/hello-$(whoami)
  touch: cannot touch `/bin/hello-albert': Permission denied


.. tip::

   Recall that $PORTALNAME is your username on FutureSystems, which
   can also be obtained using the ``whoami`` shell command.  t seems
   that this is not possible.  Since ``india`` is a shared resources
   not all users should be allowed to make changes that could affect
   everyone else.  Only a small number of users, the administrators,
   have the ability to globally modify the system.

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
