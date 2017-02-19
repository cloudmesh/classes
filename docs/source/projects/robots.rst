:orphan:

.. _robotswarm:

Virtual Robot Swarm
===================

Your task is to build a swarm of robots that communicate with each
other and do a realistic task. The task could include running a
detection system or conduct an activity that a swarm of robots could
do together.

Example for such tasks would be:

* The swarm cuts the lawn of a house and works in conjunction to
  complete cutting the lawn. Develop a benchmark that simulates the
  cutting of lawns of different sizes and number of robots.
  Incorporate runtime of the robots with recharging stations

* The swarm is used to clean a window and walks on the window itself.
  Just as with the lawn, simulate different shapes and numbers of
  robots and consider recharge.

* The swarm is send out over an area that is hit by an earthquake.
  Sound and heat sensors are used to locate humans in destroyed
  buildings. The robots fly to a variety of houses, land and engage in
  a sensor search of the houses. Simulate this behavior.

The first part of the project will be to use DevOps to deploy the
operating system for such robots. Lets assume wee have 100 or 1000
robots it will be infeasable to manage ubgrade and reload of such
robots by hand. Instead. we will be using ansible to deploy an
operating system such as the one defined buty ros.org (or other, you
let us know which is a good choice). A systems is to be developed that
does roling updates when the robots rechareg their batteries.
Naturally, the update can only be conducted if the recharge of the
battery is above a specific point. Build this into your simulation.
You will be using cloud computing to simulate such a robot swarm that
uses devops for the operating system deployment and update.

All programming is to be conducted in python. If you have special
knowledge of non python libraries for this project, please get in
contact with us to identify if non python programming could be applied
for a subset (deployment is to be conducted with ansible though).

The second part of the project contains the conduct of a realistic
task of your choice. Please make sure you get approval for your task
before you start it. Other examples than the above could be used. They
could include medical devices and other areas also.

You will be using cloud computing either with virtual machines or
containers and use cloudmesh to start your ansible playbooks. The
cluster simulating the virtual swarm is to be created with cloudmesh
also.

You will be writing a joint paper with Dr. Gregor von Laszewski to
present your results in a scientific conference or workshop. You ar
eaware that this last step is optional, and could lead to an A+ in
class.

Refernces
---------

* http://www.ros.org/
* build up your own list of references that is useful for this project.

  
