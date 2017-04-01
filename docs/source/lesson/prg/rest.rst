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
to introduce you to Eve that makes this process rather trivial. We
will provide you with an implementation example that showcases that we
can create REST services without writing a single line of code. The
code for this is located at https://github.com/cloudmesh/rest

This code will have a master branch but will also have a dev branch in
which we will add gradually more objects. Objects in the dev branch
will include:

* virtual directories
* virtual clusters
* job sequences
* inventories

;You may want to check our active development work in the dev branch.
However for the purpose of this class the master branch will be
sufficient.

Installation
~~~~~~~~~~~~~~

First we havt to install mongodb. The instalation will depend on your
operating system. For the use of the rest service it is not important
to integrate mongodb into the system upon reboot, which is focus of
many online documents. However, for us it is better if we can start
and stop the services explicitly for now.

On ubuntu, you need to do the following steps::

   TO BE CONTRIBUTED BY THE STUDENTS OF THE CLASS as homework

On windows 10, you need to do the following steps::

   TO BE CONTRIBUTED BY THE STUDENTS OF THE CLASS as homework, if you
   elect Windows 10. YOu could be using the online documentation
   provided by starting it on Windows, or rinning it in a docker container.

On OSX you can use homebrew and install it with::
   
   brew update
   brew install mongodb


.. note:: In future we may want to add ssl authentication in which case you may
          need to install it as follows::

	    brew install mongodb --with-openssl



Starting the service
~~~~~~~~~~~~~~~~~~~~

We have provided a convenient Makefile that currently only works for
OSX. It will be easy for you to adapt it to Linux. Certainly you can
look at the targes in the makefile and replicate them one by
one. Improtaht targest are `deploy` and `test`.


When using the makefile you can start the services with::

  make deploy

IT will start two terminals. IN one you will see the mongo service, in
the other you will see the eve service. The eve service will take a
file called `sample.settings.py` that is base on `sample.json` for the
start of the eve service. The mongo servide is configured in suc a
wahy that it only accepts incimming connections from the local host
which will be suffiicent fpr our case. The mongo data is written into
the `$USER/.cloudmesh` directory, so make sure it exists.

To test the services you can say::

  make test

YOu will se a number of json text been written to the screen.

Creating your own objects
-------------------------

The example demonstrated how easy it is to create a mongodb and an eve
rest service. Now lets use this example to creat your own. FOr this we
have modified a tool called evegenie to install it onto your system.

The original documentation for evegenie is located at:

* http://evegenie.readthedocs.io/en/latest/

However, we have improved evegenie while providing a commandline tool
based on it. The improved code is located at:

* https://github.com/cloudmesh/evegenie

You clone it and install on your system as follows::

  cd ~/github
  git clone https://github.com/cloudmesh/evegenie
  cd evegenie
  python setup.py install
  pip install .

This shoudl install in your system evegenie. YOu can verify this by
typing::

  which evegenie

If you see the path evegenie is installed. With evegenie installed its
usaage is simple::

  $ evegenie

  Usage:
      evegenie --help
      evegenie FILENAME

It takes a json file as input and writes out a settings file for the
use in eve. Lets assume the file is called `sample.json`, than the
settings file will be called `sample.settings.py`.
Having the evegenie programm will allow us to generate the settings
files easily. You can include them into your project and leverage the
Makefile targets to start the services in your project.
In case you generate new objects, make sure you rerun evegenie, kill
all previous windows in whcih you run eve and mongo and restart. In
case of changes to objects that you have designed and run previously,
you need to also delete the mongod database.

Towards cmd5 extensions to manage eve and mongo
-----------------------------------------------

NAturally it is of advantage to have in cms administration commands to
manage mongo and eve from cmd instead of targets in the
Makefile. Hence, we propose that the class develops such an
extension. We will create in the repository the extension called admin
and hobe that students through collaborative work and pull requests
complete such an admin command. I will provide a simple start.

And I will provide more information on this here shortely.



