Hadoop Virtual Cluster Installation
===================================

Cloudmesh Cluster Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. important::
   Before you start this lesson, you MUST finish
   :ref:`cm_install_`.

.. warning::
   This lesson is created and test under the newest version of
   Cloudmesh client. Update yours if not.

To manage virtual cluster on cloud, the command is ``cm cluster``. Try
``cm cluster help`` to see what other commands are and what options they
supported.

Create Cluster
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
To create a virtual cluster on cloud, we must define an active cluster
specification with ``cm cluster define`` command.
For example, we define a cluster with 3 nodes:

  ::

    $ cm cluster define --count 3


  .. tip::
     All options will use the default setting if not specified during cluster
     define. Try ``cm cluster help`` command to see what options
     ``cm cluster define`` has and means, here is part of the usage information:
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
        -o PATH --path=PATH            Output to this path
       ...

  .. tip::
     Floating IP is a valuable and limited resource on cloud.
     ``cm cluster define`` will assign floating IP to every node within
     the cluster by default.
     We recommend to use option ``-I`` or ``--no-floating-ip`` to avoid
     assigning floating IPs during cluster creation:

     ::

       $ cm cluster define --count 3 -I

     Then manually assign floating IP to one of the nodes. Use this node as
     a logging node or head node to log in to all the other nodes.

We can have multiple specifications defined at the same time. Every time
a new cluster specification is defined, the counter of the default cluster
name will increment. Hence, the default cluster name will be ``cluster-001``,
``cluster-002``, ``cluster-003`` and so on. Use
``cm cluster avail`` to check all the available cluster specifications:

  ::

    $ cm cluster avail
      cluster-001
        count                         : 3
        image                         : CC-Ubuntu14.04
        key                           : xl41
        flavor                        : m1.small
        secgroup                      : default
        assignFloatingIP              : True
        cloud                         : chameleon
    > cluster-002
        count                         : 3
        image                         : CC-Ubuntu14.04
        key                           : xl41
        flavor                        : m1.small
        secgroup                      : default
        assignFloatingIP              : False
        cloud                         : chameleon

With ``cm cluster use [NAME]``, we are able to switch between different
specifications with given cluster name:

  ::

    $ cm cluster use cluster-001
    $ cm cluster avail
    > cluster-001
        count                         : 3
        image                         : CC-Ubuntu14.04
        key                           : xl41
        flavor                        : m1.small
        secgroup                      : default
        assignFloatingIP              : True
        cloud                         : chameleon
      cluster-002
        count                         : 3
        image                         : CC-Ubuntu14.04
        key                           : xl41
        flavor                        : m1.small
        secgroup                      : default
        assignFloatingIP              : False
        cloud                         : chameleon

This will activate specification ``cluster-001`` which assigns floating IP
during creation rather than the latest one ``cluster-002``.


With our cluster specification ready, we create the cluster with command
``cm cluster allocate``. This will create a virtual cluster on the cloud
with the activated specification:

  ::

    $ cm cluster allocate

  .. important::
     Each specification can have one active cluster, which means ``cm cluster
     allocate`` does nothing if there is a successfully active cluster.


Check Created Cluster
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
With command ``cm cluster list``, we can see the cluster with the default name
``cluster-001`` we just created:

  ::

    $ cm cluster list
    cluster-001

Using ``cm cluster node [NAME]``, we can also see the nodes of the cluster along
with their assigned floating IPs of the cluster:

  ::

    $ cm cluster nodes cluster-001
    xl41-001 129.114.33.147
    xl41-002 129.114.33.148
    xl41-003 129.114.33.149

If option ``--no-floating-ip`` is included during definition, you will see nodes
without floating IP:

  ::

    $ cm cluster nodes cluster-002
    xl41-004 None
    xl41-005 None
    xl41-006 None

To log in one of them, use command ``cm vm assign IP [NAME]`` to assign a
floating IP to one of them:

  ::

    $ cm vm ip assign xl41-006
    $ cm cluster nodes cluster-002
    xl41-004 None
    xl41-005 None
    xl41-006 129.114.33.150

Then you can log in this node as a head node of your cluster
by ``cm vm ssh [NAME]``:

  ::

    $ cm vm ssh xl41-006
    cc@xl41-006 $


Delete Cluster
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Using ``cm cluster delete [NAME]``, we are able to delete the cluster
we created:

  ::

    $ cm cluster delete cluster-001

  .. tip::
     Option ``--all`` can delete all the clusters created, so be careful:
     ::

      $ cm cluster delete --all

Then we need to undefine our cluster specification with command
``cm cluster undefine [NAME]``:

  ::

    $ cm cluster undefine cluster-001

  .. tip::
     Option ``--all`` can delete all the cluster specifications:
     ::

       $ cm cluster undefine --all


Hadoop Cluster Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. important::
   This section is built upon the previous one. Please finish the previous one
   before start this one.

Create Hadoop Cluster
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
To create a Hadoop cluster, we need to first define a cluster with
``cm cluster define`` command:

  ::

    $ cm cluster define --count 3

  .. warning::
     To deploy a Hadoop cluster, we only support image ``CC-Ubuntu14.04``
     on Chameleon. DO NOT use ``CC-Ubuntu16.04`` or any other images.
     You will need to specify it if it's not the default image.

     ::

       $ cm cluster define --count 3 --image CC-Ubuntu14.04


Then we define the Hadoop cluster upon the cluster we defined
using ``cm hadoop define`` command:

  ::

    $ cm hadoop define

Same as ``cm cluster define``, you can define multiple specification for the
Hadoop cluster and check them with ``cm hadoop avail``:

  ::

    $ cm hadoop avail
    > stack-001
      local_path                    : /Users/tony/.cloudmesh/stacks/stack-001
      addons                        : []

We can use ``cm hadoop use [NAME]`` to activate the specification with the
given name:

  ::

    $ cm hadoop use stack-001

  .. warning::
     May not be available for current version of Cloudmesh Client.


Before deploy, we need to use ``cm hadoop sync`` to checkout / synchronize the
Big Data Stack from Github.com:

  ::

    $ cm hadoop sync

  .. important::
     To avoid errors, make sure you are able to connect to Github.com using SSH:
     https://help.github.com/articles/connecting-to-github-with-ssh/.


Finally, we are ready to deploy our Hadoop cluster:

  ::

    $ cm hadoop deploy

  .. tip::
     This process could take up to 10 minutes based on your network.


To check Hadoop is working or not. Use ``cm vm ssh`` to log into the
``Namenode`` of the Hadoop cluster. It's usually the first node of
the cluster:

  ::

    $ cm vm ssh node-001
    cc@hostname$

Switch to user ``hadoop`` and check HDFS is set up or not:

  ::

    cc@hostname$ sudo su - hadoop
    hadoop@hostname$ hdfs dfs -ls /
    Found 1 items
    drwxrwx---   - hadoop hadoop,hadoopadmin          0 2017-02-15 17:26 /tmp

Now the Hadoop cluster is properly installed and configured.

Delete Hadoop Cluster
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
To delete the Hadoop cluster we created, use command
``cm cluster delete [NAME]`` to delete the cluster with given name:

  ::

    $ cm cluster delete cluster-001


Then undefine the Hadoop specification and the cluster specification:

  ::

    $ cm hadoop undefine stack-001
    $ cm cluster undefine cluster-001

    .. warning::
       May not be available for current version of Cloudmesh Client.


Advanced Topics with Hadoop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Hadoop Virtual Cluster with Spark and/or Pig
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
To install Spark and/or Pig with Hadoop cluster, it's quite simple.
We just need to use command ``cm hadoop define`` but with ``ADDON``.

For example, we create a 3-nodes Spark cluster with Pig. To do that, all we
need is to specify ``spark`` as an ``ADDON`` during Hadoop definition:

  ::

    $ cm hadoop define spark pig

With ``cm hadoop avail``, we can see the detail of the specification for the
Hadoop cluster:

  ::

    $ cm hadoop avail
    > stack-001
      local_path                    : /Users/tony/.cloudmesh/stacks/stack-001
      addons                        : [u'spark', u'pig']

Then we use ``cm hadoop sync`` and ``cm hadoop deploy`` to deploy our Spark
cluster:

  ::

    $ cm hadoop sync
    $ cm hadoop deploy

  .. tip::
       This process will take even longer than a cluster creation. It could
       take 15 minutes or longer.

  .. tip::
     For a full list implemented ``ADDON`` with Cloudmesh Client, go to
     https://github.com/cloudmesh/big-data-stack.
