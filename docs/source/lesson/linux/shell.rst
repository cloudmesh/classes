.. _s-shell-lesson:

Shell
======================================================================

.. sidebar:: Page Contents

   .. contents::
      :local:


Overview
----------------------------------------------------------------------


This lesson will introduce you to using the shell, which is required
for using FutureSystems resources.

Acknowledgments
----------------------------------------------------------------------

Parts of this lesson were adapted from the `Software Carpentry
lesson`_ on using the Shell, which is distributed under a `Creative
Commons Attribution license v4`_ and is copyright `Software Carpentry`_.

.. _Software Carpentry lesson: http://swcarpentry.github.io/shell-novice/
.. _Creative Commons Attribution license v4: https://creativecommons.org/licenses/by/4.0/
.. _Software Carpentry: http://software-carpentry.org/


Description
----------------------------------------------------------------------

.. include:: shell-description.rst

.. tip::

   Command line shell is often called a Command Line Interface, or CLI
   for short.

.. note:: Adventurous readers may be interested to know that both
   Windows and Mac OS X provide a command shell.  On Windows you can
   run ``cmd.exe`` from `Start --> Run`.  On OS X open `Applications
   --> Utilities --> Terminal`. Be aware that the Windows and OS X CLI
   may be different than on FutureSystems.

.. tip::
   If you wish to follow along please log into your FutureSystems
   account (see :doc:`../system/futuresystemsuse`).


Introduction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: shell-intro.rst


Prompts and Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shell Concepts Introduced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``whoami``: display user id

Prompt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you log into the appropriate machine you will be presented with
the **prompt**, typically represented as the following::

  $

Command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the **prompt** you enter a **command** to run a program.
For instance, the ``whoami`` program indicates the username
you logged in under.
To see this type ``whoami`` and press enter (the result will be different
but you should recognize your username)::

  $ whoami
  nelle


.. tip::
 
   On Windows you start a program by double-clicking an icon to going
   to `Start --> <Program>` to launch it (the commands described here
   are Unix commands and are unlikely to work on Windows).  On OS X
   you might go to the dock at the bottom of the screen.  In a
   commandline shell you type the name of the program.


When you execute the ``whoami`` command the shell:

#. finds the program called ``whoami``
#. runs that program
#. displays the program's output
#. displays a new shell prompt (ready for more commands)


Files and Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shell Concepts Introduced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``pwd``: print working directory
- ``ls``: list directory contents
- ``cd``: change directory
- ``TAB``: using tab-completion

.. include:: shell-filedir.rst


Creating and Deleting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shell Concepts Introduced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``mkdir``: make a directory
- ``nano``: a text editor
- ``rm``: remove directory entries
- ``rmdir``: remove directories
- ``cp``: copy files
- ``mv``: move files

.. include:: shell-create.rst

Pipes and Filters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shell Concepts Introduced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``wc``: word count
- ``*``: globbing
- ``>``: redirection to file
  ``stdout``: standard output stream
- ``cat``: concatenate
- ``sort``: sorting
- ``|``: pipe
- ``head``: get first few lines
- ``uniq``: remove duplicate adjacent lines
- ``cut``: cut selected portions of text

.. include:: shell-pipefilter.rst

Loops
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shell Concepts Introduced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``for``: starts a **for loop**
- ``$name``: a variable called ``name``
- ``echo``: display text

.. include:: shell-loop.rst

Finding Things
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shell Concepts Introduced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``grep``: file pattern searcher
- ``find``: walk a file hierarchy
- ``man``: display manual pages
- ``$()``: execute in a subshell

.. include:: shell-find.rst


Shell Scripting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One of the most power uses of the shell is via scripting.  Instead of
using an interactive prompt, a series of commands can be written to a
file and then executed.  This has the benefit that changes to scripts
can be tracked, and script can be shared.

Let's create a simple script::

  $ nano script.sh

Add the following::

  me=$(whoami)
  where=$(pwd)

  echo "My name is $me"
  echo "I am running in $where"

  echo "Let's create a directory"
  mkdir -v hello-script

  echo "Now delete the directory"
  rmdir hello-script


You can now execute the script::

  $ bash script.sh
  My name is ada
  I am running in /home/ada
  Let's create a directory
  /home/data/hello-directory
  Now delete the directory"


What happens is that you use the ``bash`` command, which is the name
of the shell, and passed it the script you wrote.  Another way of
executing a script is by making it executable and adding a "shebang"
at the top of the file. Edit ``script.sh`` and make this the very
first line::

  #!/bin/bash

This is called a "shebang" because the first character is a hash mark
and the second the exclamation point, or "bang", symbol.

Now make it executable::

  $ chmod +x script.sh

You can run the script directly now::

  $ ./script.sh

The shebang indicates the location of the executable that will
interpret the script. Check for yourself that ``/bin/bash`` exists::

  $ file /bin/bash



Conclusion
----------------------------------------------------------------------

The Unix shell is older than most of the people who use it. It has
survived so long because it is one of the most productive
programming environments ever created --- maybe even *the* most
productive. Its syntax may be cryptic, but people who have mastered
it can experiment with different commands interactively, then use
what they have learned to automate their work. Graphical user
interfaces may be better at the first, but the shell is still
unbeaten at the second. And as Alfred North Whitehead wrote in 1911,
"Civilization advances by extending the number of important
operations which we can perform without thinking about them."


Further Reading
----------------------------------------------------------------------

What is covered here is a small overview of using the commandline
shell.
For further reading please consult the `Bash Guide for Beginners`_
Additionally, there are numerous shell summaries `a Google Search away`_

.. _Bash Guide for Beginners: http://www.tldp.org/LDP/Bash-Beginners-Guide/html/
.. _a Google Search away: https://www.google.com/search?q=linux+shell+cheat+sheet


.. _lab-shell:

Lab - Shell Usage
----------------------------------------------------------------------

Log into ``india`` for this.

#. Create a cirectory. Create a file in it and write "hello world" in it.
#. Which commands are used to list the contents of a file?
#. Why should you not use ``rm -r *`` or ``rm -r /``?
#. Alias the ``rm`` command to ``rm -i``.
#. Find a text editor you like. Common choices are emacs, vi, vim,
   pico, nano, but there are many more.
#. Write a simple shell script and execute it. The script should
   create a file called ``hello.txt`` and write the string "Hello
   World" to it.


Next Step
----------------------------------------------------------------------

In the next page, ...

`Editors <editors.html>`_
