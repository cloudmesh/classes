Makefile
======================================================================

To manage large software programs it is often necessary to recompile
them and to just focus on the peaces of code that are new. Thus
software developers have early on focussed on building software
components and libraries that can be separately compiled and
integrated in the overall program executable through for example
libraries. 

Unfortunately, this comes also at a price that the management of such
"assembled" software can be quite complex and involves the compilation
of code ina particular order or the creation of artifacts during
compile time. 

To coordinate such execution `Makefiles` have been popular as they
provide the ability to integrate a simple structure in the compile
process, while detecting changes to source code that itself invoke
actions as part of the make process.

The coordination of the process is specified in a `makefile` that
contains targets that get invoked based on conditions such as that a
source file has changed. The target has a body attached with it that
will be executed when the precondition to the target is fulfilled. 

Through a series of targets relatively sophisticated compile workflows
can be specified and often the developer has to just call the
command::

  make

In addition make has also the ability to execute the programs in
parallel while using the option `-j`. For large programs this can
provide a significant speedup during the program assembly.


A sample Makefile looks as follows::

    all: ring

    ring: main.o message.o ring.o
	    g++ main.o message.o ring.o -o ring

    main.o: main.cpp
	    g++ -c main.cpp

    message.o: message.cpp
	    g++ -c message.cpp

    ring.o: ring.cpp
	    g++ -c ring.cpp

    clean:
	    rm -rf *o ring

This example makefile creates a program with the name ring while
integrating the `ring.c` and the `message.c` code into a single executable
called `ring`. 


On Unix systems one can find out more about make when saying::

  man make

Much more detailed information is provided at 

* http://www.gnu.org/software/make/manual/make.html

Practical Other Applications of Make
----------------------------------------------------------------------

If you look at the process on how we create the documentation of this
Web page, you will also see a number of Makefiles. Although we do not
create c, we do create a web pages based on Sphinx translating rst
files to html pages. This indicates the versatility of make.

Exercises
----------------------------------------------------------------------

#. Write a c++ program that prints "Hello Cloud". Use a library
   cloud.o and create the program hello with a Makefile
