Configure
======================================================================

Due to the many different computer systems it is important o note that
libraries compiled on one system may not exist on another system or
that different files need to be involved as part of the make process
on the various systems. For example a command may not exist with the
same name on the different computers.

To assit in this task developers use configure scripts that adapt to
the underlaying enviorinment by abstarcting system related
dependencies and fulfilling them with concrete implementations. As
part of this process the Makefile will typically created and also a
target install will be defined in the Makefile tu guide the
insatlation process. Hence the process usually looks like::

  ./confugure
  make
  make install

A good image showcaseing all component involved in the configure
process is available in `Wikipedia
<http://en.wikipedia.org/wiki/File:Autoconf-automake-process.svg>`_.
It depicts how a compatible Makefile can be generated. Developers will
work on creating a Makefile.in with the available tools, that than
will be used as the input to configure to create the actual makefile. 

Excersises
----------------------------------------------------------------------

#. What is autoconf and auomake?

#. Showcase the development of a Makefile.in for our Hello cloud example.

#. Use configure to deploy it 


	
