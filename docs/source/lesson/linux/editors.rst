Editing Files
======================================================================


Overview
----------------------------------------------------------------------

This lesson will introduce you to using a text editor in the command
line shell.

.. tip:: Duration: 30 minutes

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have knowledge of

* How to use a shell (see :doc:`shell`)
* Log into your FutureSystems shell (see :doc:`../system/futuresystemsuse`)

Description
----------------------------------------------------------------------

.. include:: /class/lesson/linux/editors-description.rst

When we say, "``nano`` is a text editor," we really do mean
"text": it can only work with plain character data, not tables,
images, or any other human-friendly media. We use it in examples
because almost anyone can drive it anywhere without training, but
please use something more powerful for real work. On Unix systems
(such as Linux and Mac OS X), many programmers use `Emacs
<http://www.gnu.org/software/emacs/>`__ or `Vim
<http://www.vim.org/>`__ (both of which are completely
unintuitive, even by Unix standards), or a graphical editor such
as `Gedit <http://projects.gnome.org/gedit/>`__. On Windows, you
may wish to use `Notepad++ <http://notepad-plus-plus.org/>`__.

..
   No matter what editor you use, you will need to know where it
   searches for and saves files. If you start it from the shell, it
   will (probably) use your current working directory as its default
   location. If you use your computer's start menu, it may want to
   save files in your desktop or documents directory instead. You can
   change this by navigating to another directory the first time you
   "Save As..."


To follow along, please log into your account on ``india``.
Let's start by creating a directory in which to work::

  $ mkdir editors-lesson
  $ cd editors-lesson
  $ ls

Printing the list of directory contents with ``ls`` shows that this is
empty. Let us open a file to write some text::

  $ nano fish.txt

Note that this changes the window a bit.
We used to be in the shell, which is an interactive program.
We are now presented with a text editor, which is another interactive program.
Interaction with the editor is also done using the keyboard, though
the commands are different than in the shell.
Each editor will have a different interface.
In the case of ``nano``, the available commands are shown at the bottom:
The format for ``nano`` commands is caret,character, then description.
The caret represents the ``control`` key, the next character is the
character to press (X, O,  G, etc), and the description indicates
the function of the command

The important commands are:
- ``^X`` to exit, optionally saving the file
- ``^O`` to save the file
- ``^G`` to get help

If  you are not sure what to do in nano, look to the bottom
for the available commands.


Let start writing some text::

  one fish
  two fish
  red fish
  blue fish


At this point we wish to save the file and exit.
Press ``^O`` to write, then ``^X`` to exit.

We can now ``ls`` again and see that the file now exists::

  $ ls
  fish.txt

Print the contents to screen using ``cat``::

  $ cat fish.txt
  one fish
  two fish
  red fish
  blue fish

  
Exercises
----------------------------------------------------------------------

Exercise I
^^^^^^^^^^^^^^^^^^

Edit ``fish.txt`` and append the following text::

  Black fish
  Blue fish
  Old fish
  New fish.

  This one has a little star.
  This one has a little car.
  Say! What a lot
  Of fish there are.



Exercise II
^^^^^^^^^^^^^^^^^^

Create a new file ``eggs.txt`` and write the following text::

  Do you like 
  green eggs and ham?

  I do not like them, 
  Sam-I-am.
  I do not like
  green eggs and ham.


Save the file and print the directory listing.  How many files are
there?  Count the number of lines, words, and characters in each file
without opening them.


Exercise III
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To cleanup this lesson, remove the files and directory you created.


Next Step
-----------

In the next page, ...

`Python <python.html>`_
