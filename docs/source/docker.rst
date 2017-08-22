Docker
======================================================================

This is an experimental effort with little documentation


Start a virtual machine that runs docker in it::

  make docker-machine

The machine is called cloudmesh, do not confuse this with the docker image
that is bing created and is also called cloudmesh.

Login to the started vm so you can execute docker commands::
  
  make docker-machine-login

Create the cloudmesh docker image with the name 'cloudmesh'::
  
  make docker-build

Publish the image on docker hub (only Gregor)::

  make docker-login

  make docker-publish

Get the image (does not work)::

  make docker-pull

  
Not working or incomplete::

  make docker-run
  make docker-clean-images

