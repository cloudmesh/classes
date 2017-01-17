Shell Scripts
======================================================================

Often shells are used to interact with computers n the
command line. they provide convenient access to a number of commands
and functionality that makes interactive experiments through a series
of command possible. Shells are interpreters that provide a minimal
environment to allow easy scripting of commands as part of schell
scripts. Features that are of the used are aliasses, command
definition, function, and clearly batch operations by listing commands
sequentially in a shell script. Programming language features such as
loops and conditions are also provided. 

As shell scripts are executed as part of the OS no further install is
necessary to run them.

However in contrast to modern programming languages and interpreters
some functionality is missing. Also large amount of shell scripts
become quite difficult to maintain due to the lack of more modern
programming language features. 

Therefor it is today common to use perl and more important;y python
for the development of large scale scripts. 

However, a large number of "tricks" and existing scripts makes shell
scripts still a viable option for many developers. In addition it has
the advantage that it will be immediately available after the install
of the OS, thus it is of great help in case of managing distributed
machines.

Variants of shells exist that can execute the same command in parallel
on multiple distributed machines which comes in handy for cluster
management.

Exercises:
----------------------------------------------------------------------

#. Write a shell script that prints you username and lists the files
   in your home directory.
#. Write a shell script that converts all jpg files to png. (If you
   copy the example form http://en.wikipedia.org/wiki/Shell_script
   please make sure to walk through the example and understand in
   detail the syntax and the meaning of the program).
#. Search in our page for the term "pdsh"
