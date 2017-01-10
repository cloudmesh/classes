.. _ref-class-lesson-openmpi-with-cloudmesh:

Deploying Open MPI Cluster with Cloudmesh ``launcher``
======================================================

To support Message Passing Interface (MPI) programs with a cluster, Cloudmesh
provides a new command ``launcher`` to start, configure, manage or update
compute nodes (VMs) with Open MPI. ``launcher`` command applies default settings
to configure clusters with applications so users can avoid hassles of building
clusters.

Table of Contents

* `Start Cluster with launcher <#start-cluster>`_
* `Check Status <#check-status-of-cluster>`_
* `Login to Cluster <#id1>`_
* `Terminate Cluster <#id2>`_

.. `Next Tutorial>> Deploying MongoDB Shard Cluster <mongodb_cluster.html>`_

Tutorial: Deploying Open MPI Cluster with ``cm launcher``
---------------------------------------------------------

.. tip:: approximate time 10-15 minutes

In this tutorial, we are going to deploy a Open MPI cluster using Cloudmesh
``launcher`` command.

Start Cluster
~~~~~~~~~~~~~~

``launcher start`` command deploys a cluster with a selected application.

::

        cm launcher start openmpi

Check Status of Cluster
~~~~~~~~~~~~~~~~~~~~~~~

Initializing a cluster requires some time for installing packages, configuring
networks, etc.  While it is initiated, you can check the status of your cluster
deployment.

::

        cm launcher list

You expect the result similar to:

.. parsed-literal::

        +--------------------------------------+--------------------------------+-------------------------------------+--------------------+----------------------+----------+
        | launcher_id                          | stack_name                     | description                         | stack_status       | creation_time        | cm_cloud |
        +--------------------------------------+--------------------------------+-------------------------------------+--------------------+----------------------+----------+
        | 14ec7ceb-ce12-4b18-9c31-d398c6e76b78 | launcher-albert-openmpi-DB8JDK | Open MPI cluster with OpenStackHeat | CREATE_IN_PROGRESS | 2015-01-22T16:25:23Z | india    |
        +--------------------------------------+--------------------------------+-------------------------------------+--------------------+----------------------+----------+

* CREATE_IN_PROGRESS: cluster is not available because creating the cluster is
  in progress.
* CREATE_COMPLETE: cluster has been created and it is ready to use.

Login to Cluster
~~~~~~~~~~~~~~~~

We use ``cm vm login`` command to ssh to one of the nodes in the cluster.
Issue ``vm list`` first to see the list of virtual instances.

* Checking a node name to login

::

        cm vm list

You expect the result similar to:

.. parsed-literal::

        +----------------------------+----------+----------------------------+----------+----------------------------+
        | name                      | status   | addresses                  | flavor   | image                      |
        +============================+==========+============================+==========+============================+
        | **openmpi1**                   | ACTIVE   | 10.39.1.48, 149.165.159.02 | m1.small | futuresystems/ubuntu-14.04 |
        +----------------------------+----------+----------------------------+----------+----------------------------+
        | openmpi2                   | ACTIVE   | 10.39.1.52                 | m1.small | futuresystems/ubuntu-14.04 |
        +----------------------------+----------+----------------------------+----------+----------------------------+
        | openmpi3                   | ACTIVE   | 10.39.1.51                 | m1.small | futuresystems/ubuntu-14.04 |
        +----------------------------+----------+----------------------------+----------+----------------------------+
        | openmpi4                   | ACTIVE   | 10.39.1.53                 | m1.small | futuresystems/ubuntu-14.04 |
        +----------------------------+----------+----------------------------+----------+----------------------------+
        | openmpi5                   | ACTIVE   | 10.39.1.54                 | m1.small | futuresystems/ubuntu-14.04 |
        +----------------------------+----------+----------------------------+----------+----------------------------+

We found that openmpi1 is a node to log in.

* SSH to a node

::

        cm vm login [node name]

In this example, we try to ssh to ``openmpi1`` with ``ec2-user`` user name.

::

        cm vm login openmpi1 --ln=ec2-user

You expect the result similar to:

.. parsed-literal::

        Welcome to Ubuntu 14.04.1 LTS (GNU/Linux 3.13.0-40-generic x86_64)

         * Documentation:  https://help.ubuntu.com/

           System information as of Thu Jan 22 19:28:05 UTC 2015

           System load:  0.01              Processes:           72
           Usage of /:   6.9% of 19.65GB   Users logged in:     0
           Memory usage: 23%               IP address for eth0: 10.39.1.48
           Swap usage:   0%

           Graph this data and manage this system at:
             https://landscape.canonical.com/

           Get cloud support with Ubuntu Advantage Cloud Guest:
             http://www.ubuntu.com/business/services/cloud


       $ 

* Switch to ``root`` user

  You are expected to run openmpi commands as a root superuser.
 
::

        sudo su -

Run a "Hello World" MPI program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's try a simple example to try a MPI program. Here is hello.c:

::

  #include <stdio.h>
  #include <mpi.h>

  int main(int argc, char *argv[]) {
    int numprocs, rank, namelen;   
    char processor_name[MPI_MAX_PROCESSOR_NAME];

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Get_processor_name(processor_name, &namelen);

    printf("Process %d on %s out of %d\n", rank, processor_name, numprocs);

    MPI_Finalize();
  }

Compile hello.c
^^^^^^^^^^^^^^^^^^^

Since we are running Ubuntu 14.04 in this example, we complie with ``mpicc``:

::

  mpicc hello.c -o hello

MPI hostfile
^^^^^^^^^^^^^^^^^^^

We create a hostfile for MPI process which contains the hostnames (nodes) of
the cluster.

::

  echo -e "mpi1\nmpi2\nmpi3\nmpi4\nmpi5" > my_mpi_hosts

::

  [expected output]

  cat my_mpi_hosts
  mpi1
  mpi2
  mpi3
  mpi4
  mpi5

.. tip:: If you have more than a single CPU per node, use slots=N where N is a
         number of processors.
         e.g. mpi1 slots=2

Copy ``hello`` program to each node
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``hello`` program should to be found on each node. We propagate the binary using ``scp``:

::

  scp hello mpi1:
  scp hello mpi2:
  scp hello mpi3:
  scp hello mpi4:
  scp hello mpi5:

Run MPI program
^^^^^^^^^^^^^^^^

We now run ``hello`` program on the given nodes with ``mpirun`` program:

::

  mpirun -np 5 --hostfile my_mpi_hosts hello

*-np option is used to tell how many copies of the program will be run. We have
five nodes in this example.*

Expected result looks like this:

::

  Process 0 on mpi1 out of 5
  Process 1 on mpi2 out of 5
  Process 3 on mpi3 out of 5
  Process 2 on mpi4 out of 5
  Process 4 on mpi5 out of 5


Terminate Cluster
~~~~~~~~~~~~~~~~~

Once you completed your task on the cluster, you can terminate the cluster with
``cm launcher stop [name]`` command.

* Check a cluster name to stop

::

        cm launcher list

You expect the result similar to:

.. parsed-literal::

        +--------------------------------------+--------------------------------+-------------------------------------+-----------------+----------------------+----------+
        | launcher_id                          | stack_name                     | description                         | stack_status    | creation_time        | cm_cloud |
        +--------------------------------------+--------------------------------+-------------------------------------+-----------------+----------------------+----------+
        | 14ec7ceb-ce12-4b18-9c31-d398c6e76b78 | **launcher-albert-openmpi-DB8JDK** | Open MPI cluster with OpenStackHeat | CREATE_COMPLETE | 2015-01-22T16:25:23Z | india    |
        +--------------------------------------+--------------------------------+-------------------------------------+-----------------+----------------------+----------+

* Terminate a cluster

::

        cm launcher stop [name]

In this tutorial, we terminate ``launcher-albert-openmpi-DB8JDK`` like this:

::

        cm launcher stop launcher-albert-openmpi-DB8JDK


* DELETE_IN_PROGRESS: shutting down instances is in progress.
* DELETE_COMPLETE: the lease of resources is ended, all resources are returned.


.. `Next Tutorial>> Deploying MongoDB Shard Cluster <mongodb_cluster.html>`_
