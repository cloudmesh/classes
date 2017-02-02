Linux Shell
===========

There are many good tutorials out there that explain why one needs a
linux shell and not just a GUI. Randomly we picked the firts one that
came up with a google query (This is not an endorsement for the
material we point to, but could be a worth while read for someone that
has no experience in Shell programming:

* http://linuxcommand.org/lc3_learning_the_shell.php

Certainly you are welcome to use other resources that may suite you
best. We will however summarize in table form a number of useful
commands that you may als find in a link to a RefCard.

* http://www.cheat-sheets.org/#Linux

  

File commands
-------------

Find included a number of commands related to file manipulation.

+-------------------+-------------------------------------+
| Command           | Description                         |
+===================+=====================================+
| ls                | Directory listing                   |
+-------------------+-------------------------------------+
| ls -lisa          | list details                        |
+-------------------+-------------------------------------+
| cd *dirname*      | Change directory to *dirname*       |
+-------------------+-------------------------------------+
| mkdir *dirname*   | create the directory                |
+-------------------+-------------------------------------+
| pwd               | print working directory             |
+-------------------+-------------------------------------+
| rm *file*         | remove the file                     |
+-------------------+-------------------------------------+
| cp *a* *b*        | copy file *a* to *b*                |
+-------------------+-------------------------------------+
| mv *a* *b*        | move/rename file *a* to *b*         |
+-------------------+-------------------------------------+
| cat *a*           | print content of file\ *a*          |
+-------------------+-------------------------------------+
| less *a*          | print paged content of file *a*     |
+-------------------+-------------------------------------+
| head -5 *a*       | Display first 5 lines of file *a*   |
+-------------------+-------------------------------------+
| tail -5 *a*       | Display last 5 lines of file *a*    |
+-------------------+-------------------------------------+

Search commands
---------------

Find included a number of commands related to seraching.

+----------------------------------+---------------+
| Command                          | Description   |
+==================================+===============+
| fgrep                            | TBD           |
+----------------------------------+---------------+
| grep -R "xyz" .                  | TBD           |
+----------------------------------+---------------+
| find . -name "\*.py" \| TBD \|   |               |
+----------------------------------+---------------+

Help
----

Find included a number of commands related to manual pages.

+-----------------+---------------------------------+
| Command         | Description                     |
+=================+=================================+
| man *command*   | manual page for the *command*   |
+-----------------+---------------------------------+

Keyboard Shortcuts
------------------

These shortcuts will come in handy. Note that many overlap with emacs
short cuts.

+------------+----------------------------------------------------------+
| Keys       | Description                                              |
+============+==========================================================+
| Up Arrow   | Show the previous command                                |
+------------+----------------------------------------------------------+
| Ctrl + z   | Stops the current command                                |
+------------+----------------------------------------------------------+
|            | resume with fg in the foreground                         |
+------------+----------------------------------------------------------+
|            | resume with bg in the background                         |
+------------+----------------------------------------------------------+
| Ctrl + c   | Halts the current command                                |
+------------+----------------------------------------------------------+
| Ctrl + l   | Clear the screen                                         |
+------------+----------------------------------------------------------+
| Ctrl + a   | Return to the start of the command you're typing         |
+------------+----------------------------------------------------------+
| Ctrl + e   | Go to the end of the command you're typing               |
+------------+----------------------------------------------------------+
| Ctrl + k   | Cut everything after the cursor to a special clipboard   |
+------------+----------------------------------------------------------+
| Ctrl + y   | Paste from the special clipboard                         |
+------------+----------------------------------------------------------+
| Ctrl + d   | Log out of current session, similar to exit              |
+------------+----------------------------------------------------------+

.. _bashrc:
   
.bashrc and .bash_profile
-----------------------------

.. warning:: Not yet implemented.

Exercise
--------

Linux.1:
    Familiarize yourself with the commands

Linux.2:
    Find more commands that you find useful and add them to this page.

Linux.3:
    Use the `sort` command to sort all lines of a file while removing duplicates.
