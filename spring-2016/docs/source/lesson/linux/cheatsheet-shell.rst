
Shell
----------------------------------------------------------------------

.. tip::

   You can loop up information about commands by executing::

     $ man <name>

   For example, to lookup ``ls`` execute::

     $ man ls

Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``uname`` display operating system name
* ``date`` display the date
* ``uptime`` show how long the operating system has been running
* ``whoami`` show the current user id
* ``man`` display the manual page for a command

Directory Operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  
* ``pwd`` display working directory
* ``mkdir`` make a directory
* ``cd`` change directory
* ``ls`` list directory contents


``ls`` Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``-a`` include directory entries whose name begins with a ``.``
* ``-R`` recuresively list subdirectories encountered
* ``-r`` reverse the order of the sort
* ``-t`` sort by time modified
* ``-S`` sort files by size
* ``-l`` list in log format
* ``-1`` output one entry per line
* ``-m`` list files accross the page separated by commas
* ``-Q`` enclose entry names in double quotes
  

Searching
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``grep`` print lines matching a pattern
* ``find dir -name "pattern"`` search ``dir`` for files matching ``pattern``
* ``find dir -iname "pattern"`` the above but ignore case
* ``whereis`` locate the binary, source, manual page files for a command
* ``locate`` find files by name

``grep`` Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``-i`` ignore case
* ``-r`` recursive
* ``-v`` select non-matching lines
* ``-o`` show only the matching part of matching lines


File Operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``touch`` change file timestamps
* ``cat`` concatenate files and print to ``stdout``
* ``more`` file perusal filter for viewing
* ``less`` like ``more`` but supports backward movement
* ``file`` determine file type
* ``cp`` copy files and directories
* ``mv`` move (rename) files
* ``rm`` remove files or directories
* ``head`` display the first lines of files
* ``tail`` display the last lines of files
* ``chmod`` change file access permissions


Process Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  
* ``ps`` report a snapshot of current processes
* ``top`` display linux process table
* ``kill`` terminate a process using process id
* ``pgrep`` lookup process based on name
* ``pkill`` kill process based on name
* ``killall`` kill processes by name
