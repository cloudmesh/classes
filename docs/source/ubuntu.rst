Ubuntu Virtual Machine
======================================================================

.. warning:: THIS SECTION IS UNDER DEVELOPMENT AND NOT YET COMPLETED.

For development purposses we recommend tha you use for this class an
ubuntu virtual machine that you set up with the help of virtualbox.

Only after you have successfully used ubuntu in a virtaul machine you
will be allowed to use virtual machine son clouds.

A "cloud drivers license test" will be conducted to let you gain
access to the cloud infrastructure. We will annaounce this
test. Before you have not passed the test, you will not be able to use
the clouds. Furthermore, you do not have to ask us for join requests
before you have not passed the test. Please be patient. Only students
enrolled in the class can get access to the cloud.


Creation
--------

First you will need to install virtualbox. It is easy to install and
details can be found at

* https://www.virtualbox.org/wiki/Downloads

After you have installed virtualbox you also need to use an image. For
this calss we will be using ubuntu Desktop 16.04 which you can find
at:

* http://www.ubuntu.com/download/desktop

Please note the recommended requirements that also apply to a virtual
machine:

* 2 GHz dual core processor or better
* 2 GB system memory
* 25 GB of free hard drive space

A video to showcase such an install is avalable at:

* https://youtu.be/NWibDntN2M4


Guest additions
----------------

The virtual guest additions allow you to easily do the follwoing
tasks:

* Resize the windows of the vm
* Copy and paste content between the Guest operating system and the
  host operating system windows.

This way you can use many native programs on you host and copy
contents easily into for example a terminal or an editor that you run
in the Vm.

A video is located at
  
* https://youtu.be/wdCoiNdn2jA

.. note:: Please reboot the machine after instalation and configuration.
   

On OSZ you can once you have enabled bidirectiona copying in the
Device tab with 

OSX -> Vbox:
  commad c -> shift CONTRL v

Vbox to OSX:
  shift CONTRL v -> shift CONTRL v -> 
  
On Windows the key combination is naturally different. Please consult
your windows manual.


Development Configuration
-------------------------

The documenation on how to configure the virtual machine and
installmany useful programs is posted at:

* https://github.com/cloudmesh/ansible-cloudmesh-ubuntu-xenial


You simply have to execute the following commands in the teraminal of
the virtual machine. In order to eliminate confusion with other
terminals, we use the prefix `vm> $` to indicate any command that is to
be started on the virtual machine. Otherwise it is clear from the
context::

  
   vm>$ wget https://raw.githubusercontent.com/cloudmesh/ansible-cloudmesh-ubuntu-xenial/master/bootstrap.sh
   vm>$ bash bootstrap.sh

   
Homework Virtualbox
-------------------

1. Install ubuntu desktop on your computer with guest additions.
2. Make sure you know how to paste and copy between your host and
   geust operating system
3. Install the programs defined by the development configuration
