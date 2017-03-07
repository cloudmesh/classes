CMD5
====

CMD is a very useful package in python to create command line
shells. However it does not allow the dynamic integration of newly
defined commands. Furthermore, addition to cmd need to be done within
the same source tree. To simplify developping commands by a number of
people and to have a dynamic plugin mechnism, we developed cmd5.
It is a rewrite on our ealier effords in cloudmesh and cmd3.

Resources
---------

The source code for cmd5 is located in github:

* https://github.com/cloudmesh/cmd5

Installation from source
-----------------------

We recommend that you use a virtualenv either with virtualenv or
pyenv. This can be either achieved vor virtualenv with::

    virtualenv ~/ENV2

or for pyenv, with::

    pyenev virtualenv 2.7.13 ENV2

Next, you must install cloudmesh_client with::

    pip install cloudmesh_client

Now you need to get two source directories. We assume yo place them in
~/github::

    mkdir ~/github
    cd ~/github
    git clone https://github.com/cloudmesh/cmd5.git
    git clone https://github.com/cloudmesh/extbar.git

The cmd5 repository contains the shell, while the extbar directory
contains the sample to add the dynamic commands foo and bar.

To install them simply to the following::

    cd ~/github/cmd5
    python setup.py install
    cd ~/github/extbar
    python setup.py install

Execution
---------

to run the shell you can activate it with the cms command. cms stands
for cloudmesh shell::

    (ENV2) $ cms

It will print the banner and enter the shell::

    +-------------------------------------------------------+
    |   ____ _                 _                     _      |
    |  / ___| | ___  _   _  __| |_ __ ___   ___  ___| |__   |
    | | |   | |/ _ \| | | |/ _` | '_ ` _ \ / _ \/ __| '_ \  |
    | | |___| | (_) | |_| | (_| | | | | | |  __/\__ \ | | | |
    |  \____|_|\___/ \__,_|\__,_|_| |_| |_|\___||___/_| |_| |
    +-------------------------------------------------------+
    |                  Cloudmesh CMD5 Shell                 |
    +-------------------------------------------------------+

    cms>


To see the list of commands you can say

    cms> help

To see the manula page for a specific command, please use::

    help COMMANDNAME

Create your own Extension
-------------------------

One of the most important features of CMD5 is its ability to extend it
with new commands.  This is done via packaged name spaces. This is
defined in the setup.py file of your enhancement. The best way to
create an enhancement is to take a look at the code in

* https://github.com/cloudmesh/extbar.git

Simply copy the code and modify the bar and foo commands to fit yor
needs. It is important that all objects are defined in the command
itself and that no global variables be use in order to allow each
shell command to stand alone. Naturally you should develop API
libraries outside of the cloudmesh shell command and reuse them in
order to keep the command code as small as possible. We place the
command in::

    cloudmsesh/ext/command/COMMANDNAME.py

An example for the bar command is presented at:

* https://github.com/cloudmesh/extbar/blob/master/cloudmesh/ext/command/bar.py

It shows how simple the command definition is (bar.py)::

    from __future__ import print_function
    from cloudmesh_client.shell.command import command
    from cloudmesh_client.shell.command import PluginCommand

    class BarCommand(PluginCommand):

        @command
        def do_bar(self, args, arguments):
            """
            ::
              Usage:
                    command -f FILE
                    command FILE
                    command list
              This command does some useful things.
              Arguments:
                  FILE   a file name
              Options:
                  -f      specify the file
            """
            print(arguments)

An important difference to other CMD solutions is that our commands
can leverage (besides the standrad definition), docopts as a way to
define the manual page. This allows us to use arguments as dict and
use simple if conditions to interpret the command. Using docopts has
the advantage that contributors are forced to think about the command
and its options and document them from the start. Previously we used
not to use docopts and argparse was used. However we noticed that for
some contributions the lead to commands that were either not properly
documented or the developers delivered ambiguous commands that
resulted in confusion and wrong ussage by the users. Hence, we do
recommend that you use docopts.

The transformation is enabled by the @command decorator that takes
also the manual page and creates a proper help message for the shell
automatically. Thus there is no need to introduce a sepaarte help
method as would normally be needed in CMD.


Excersise
---------

CMD5.1:
    Install cmd5 on your computer.

CMD5.2:
    Write a new command with your firstname as teh command name.

CMD5.3:
    Write a new command and experiment with docopt syntax and argument
    interpretation of the dict with if conditions.

CMD5.4:
    If you have useful extensions that you like us to add by default,
    please work with us.
