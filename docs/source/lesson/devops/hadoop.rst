Hadoop Virtual Cluster Installation (under preparation)
=======================================================

Cloudmesh Cluster Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  .. important::
     Before you start this lesson, you MUST finish
     :ref:`cm_install_`.

To manage virtual cluster on cloud, the command is ``cm cluster``. Try
``cm cluster help`` to see what other commands are and what options they
supported.

Create Cluster
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
To create a virtual cluster on cloud, we use ``cm cluster create``.
For example, we will create a cluster with three nodes:

  ::

    $ cm cluster create --count 3


  .. tip::
     All options will use the default setting if not specified during cluster
     create. Try ``cm cluster help`` command to see what options
     ``cm cluster create`` has and mean, here is part of the usage information:
     ::

       $ cm cluster help
       usage:
       cluster create [-n NAME] [-c COUNT] [-C CLOUD] [-u NAME] [-i IMAGE]
        [-f FLAVOR] [-k KEY] [-s NAME] [-AI]
       Options:
        -A --no-activate               Don't activate this cluster
        -I --no-floating-ip            Don't assign floating IPs
        -n NAME --name=NAME            Name of the cluster
        -c COUNT --count=COUNT         Number of nodes in the cluster
        -C NAME --cloud=NAME           Name of the cloud
        -u NAME --username=NAME        Name of the image login user
        -i NAME --image=NAME           Name of the image
        -f NAME --flavor=NAME          Name of the flavor
        -k NAME --key=NAME             Name of the key
        -s NAME --secgroup=NAME        NAME of the security group
       ...

  .. tip::
     Floating IP is a valuable and limited resource on cloud.
     ``cm cluster create`` will assign floating IP to every node within
     the cluster by default.
     We recommend to use option ``-I`` or ``--no-floating-ip`` to avoid
     assigning floating IPs during cluster creation:

     ::

       $ cm cluster create --count 3 -I

     Then manually assign floating IP to one of the nodes. Use this node as
     a logging node or head node to log in to all the other nodes.

Every time a new cluster is created, the counter of the default cluster name will
increment. Hence, the default cluster name will be
``cluster-001``, ``cluster-002``, ``cluster-003`` and so on.

Check Created Cluster
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
With ``cm cluster list``, we can see the cluster with the default name
``cluster-001`` we just created::

  $ cm cluster list
  cluster-001

Delete Cluster
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Using ``cm cluster delete NAME``, we are able to delete the cluster
we created

  ::

    $ cm cluster delete cluster-001

  .. tip::
     Option ``--all`` will delete all the clusters created:
     ::

      $ cm cluster delete cluster --all


Hadoop Cluster Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. important::
   Before you start this lesson, you MUST finish
   :ref:`cm_install_`.

Create Hadoop Cluster
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Before we start a Hadoop cluster, we need to find out the username on
the image we are going to use. For instance, I am using ``CC-Ubuntu14.04``
on Chameleon, the username of this image is ``cc``.

To install a Hadoop cluster with 3 nodes, use ``cm hadoop start COUNT`` command

  ::

    $ cm hadoop start 3 --username cc


  .. warning::
     DO NOT use ``cc`` when create Hadoop cluster on your machine! The username
     on the image you are using could be something else!
  .. tip::
     This process will take 10 minutes or longer.


To check Hadoop is working or not. Use ``cm vm ssh`` to log into the head node.

  ::

    $ cm vm ssh node-001
    cc@hostname$

Switch to user ``hadoop`` and check HDFS is set up or not.

  ::

    cc@hostname$ sudo su - hadoop
    hadoop@hostname$ hdfs dfs -ls /
    Found 1 items
    drwxrwx---   - hadoop hadoop,hadoopadmin          0 2017-02-15 17:26 /tmp

Now the Hadoop cluster is properly installed.

To delete the Hadoop cluster we created, use ``cm cluster delete NAME``

  ::

    $ cm cluster delete cluster-001


Advanced Topics with Hadoop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Hadoop Virtual Cluster with Spark, Yarn or Pig
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
To install Spark, Yarn or Pig with Hadoop cluster, it's quite simple.
We still use command ``cm hadoop start COUNT`` but with ``ADDON``.

For example, we create a Spark cluster with 3 nodes. To do that, all we need is
to specify ``spark`` as an ``ADDON`` during creation:

  ::

    $ cm hadoop start 3 --username cc spark

  .. tip::
       This process will take even longer than a cluster creation. It could
       take 15 minutes or longer.

  .. tip::
     For a full list implemented ``ADDON`` with Cloudmesh Client, go to
     https://github.com/cloudmesh/big-data-stack.
