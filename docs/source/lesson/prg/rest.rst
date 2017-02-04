REST with Eve 
==============

Overview of REST
----------------

REST stands for REpresentational State Transfer. REST is an
architecture style for designing networked applications. It is based
on stateless, client-server, cacheable communications
protocol. Although not based on http, in most cases, the HTTP protocol
is used.  In contrast to what some others write or say, REST is not a
*standard*.


RESTful applications use HTTP requests to:

* post data: while creating and/or updating it,
* read data: while making queries, and
* delete data.

Hence REST uses HTTP for the four CRUD operations:

* Create
* Read
* Update
* Delete

As part of the HTTP protocol we have methods such as GET, PUT, POST,
and DELETE. These methods can than be used to implement a REST
service. As REST introduces collections and items we need to implement
the CRUD functions for them. The semantics is explained in the Table
illustrationg how to implement them with HTTP methods.

.. list-table:: IMplementing REST with HTTP methods
   :widths: 10 10 10 10 10
   :header-rows: 1

   * - URL
     - GET
     - PUT
     - POST
     - DELETE
   * - http://.../resources/
     - List the URIs and perhaps other details of the collection's
       members.
     - Replace the entire collection with another collection.
     - Create a new entry in the collection. The new entry's URI is
       assigned automatically and is usually returned by the
       operation.
     - Delete the entire collection.
   * - http://.../resources/item17
     - Retrieve a representation of the addressed member of the
       collection, expressed in an appropriate Internet media type.
     - Replace the addressed member of the collection, or if it does
       not exist, create it.
     - Not generally used. Treat the addressed member as a collection
       in its own right and create a new entry within it.
     - Delete the addressed member of the collection.

Source: https://en.wikipedia.org/wiki/Representational_state_transfer

REST and eve
------------

Now that we have outlined the basic functionality that we need, we lke
to introduce you to Eve that makes this process rather trivial. IN
fact we will provide you with an implementation example that showcases
that we can create REST services without writing a single line of
code. The code for this is located at https://github.com/cloudmesh/eve

Installation
~~~~~~~~~~~~~~

First we havt to install mongodb. The instalation will depend on your
operating system. Note that for this example we do not need to
integrate mongodb into the system upon reboot. IN fact for us it is
better if we can start and stop the services by hand.

On ubuntu, you need to do the following steps:

::

   TO BE CONTRIBUTED BY THE STUDENTS OF THE CLASS as homework

On windows 10, you need to do the following steps:

::

   TO BE CONTRIBUTED BY THE STUDENTS OF THE CLASS as homework, if you
   elect Windows 10

On OSX you can use homebrew and install it with

::
   
   brew update
   brew install mongodb
   # brew install mongodb --with-openssl


Starting the service
~~~~~~~~~~~~~~~~~~~~

We have provided a convenient Makefile that currently only works for
OSX. But you can replicate the steps while looking at the targets we
defined in the makefile in a shell program.

::

   TODO Provide a shell progra, that runs on all three operating
   systems. To be completed by students of the class

When using the makefile you can start the services with::

  make deploy

To test the services you can say::

  make test

The program relies on evegenie that we will be added to the repository
by executing

::

   SOME MAKEFILE TARGET. TO BE COMPLETED BY STUDENT. ITS ALREADY IN MAKEFILE


TODO by student add logging

