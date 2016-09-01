Ubuntu Virtual Machine
======================================================================

.. warning:: THIS SECTION IS UNDER DEVELOPMENT AND NOT YET COMPLETED.

For development purposses we recommend tha you use for this class an
ubuntu virtual machine that you set up with the help of virtualbox.


Creation
--------

TBD. Put Gregors video here.


Guest additions
----------------

* TBD. shoot a video (probably gregor)

* do bidirectional past and copy as well as drag


* dont forget to reboot

Paste and copy

* OSX -> Vbox

  commad c -> shift CONTRL v

* Vbox to OSX

  shift CONTRL v -> shift CONTRL v -> 
  


Configuration
-------------

The documenation on how to configure the virtual machine is posted
here:

* https://github.com/cloudmesh/ansible-cloudmesh-ubuntu-xenial


You simply have to execute the following commands in the teraminal of
the virtual machine. IN order to eliminate confusion with other
terminals, we use the prefix `vm> $` to indicate any command that is to
be started on the virtual machine. Otherwise it is clear from the
context::

  
   vm>$ wget https://raw.githubusercontent.com/cloudmesh/ansible-cloudmesh-ubuntu-xenial/master/bootstrap.sh
   vm>$ bash bootstrap.sh

   
