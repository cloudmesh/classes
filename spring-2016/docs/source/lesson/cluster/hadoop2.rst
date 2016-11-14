.. _ref-class-lesson-hadoop2:

Hadoop v2 
===============================================================================

.. tip:: Approximate time: 1 hour 

Quick Guide
-------------------------------------------------------------------------------

In this tutorial, remember a few things below.

* REPLACE ``albert`` with your portal id.
* Distinguish ``Master`` and ``Slaves`` for different installation.
* ``Master`` contains HDFS NameNode and YARN ResourceManager.
* ``Slaves`` contain HDFS DataNode and YARN NodeManager.
* Internal IPs (private) are used. You can use Floating IPs, if you have.

Deploying Virtual Cluster
-------------------------------------------------------------------------------

Create Virtual Cluster with 4 VM instances.

There will be **1 MASTER** and **3 SLAVES** in this tutorial using these four VM instances.

Operating System Configuration
-------------------------------------------------------------------------------

From here, You SHOULD be **on a VC node** which is one of your VM instances.


Switch to ``root`` Account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   ubuntu@:~$ sudo su -


Update of ``/etc/hostname`` File (Master)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We will update $HOSTNAME in a master and slaves. In this tutorial, we have 4 VM
instances (nodes) from ``albert_1`` to ``albert_4``. One of the nodes is going
to be a master and rest of them are going to be slaves. ``albert_1`` is
selected as a master.

::

  echo hc-master > /etc/hostname
  hostname hc-master
  logout
  logout

Remember, we make changes to:

* Hostname of albert_1 vm: ``hc-master``
* Hostname of albert_2 vm: ``hc-slave1``
* Hostname of albert_3 vm: ``hc-slave2``
* Hostname of albert_4 vm: ``hc-slave3``

*Hostname and vm name are different.*

.. note:: ``albert_1 - 4`` are VM names. Actual $HOSTNAME(s) will be like
   ``albert-1``.  Underscore(_) is replaced to hypen(-) in $HOSTNAME. Dont' get
   confused. VM name is a name OpenStack uses. $HOSTNAME is a name Operating
   System e.g. Linux uses.

SSH to a Node 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's go to your
VC node again to see the new hostname ``hc-master``.::

  ssh albert_1 -l ubuntu

*Replace ``albert_1`` with your vm name* 

.. tip:: Again, ``albert_1`` is your vm name. It is not your $HOSTNAME and
   can't be changed once created. We updated $HOSTNAME in your Operating
   System.

You expect to see::

  ubuntu@hc-master:~$

Update of ``/etc/hostname`` Files (Slaves)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's update ``hostname`` in slaves which are from ``albert_2`` to
``albert_4``. Note that, this is a same task you did above on ``hc-master``
which was ``albert_1``. 


Since you are in ``hc-master``, let's update hostname(s) from the
master node.

::

  ubuntu@hc-master:~$ ssh albert_2
  The authenticity of host 'albert_2 (xxx.xxx.xxx.xx)' can't be established.
  ECDSA key fingerprint is 98:ef:90:d7:69:b4:22:00:00:00:00:00:00:00:06:c1.
  Are you sure you want to continue connecting (yes/no)?

Type ``yes`` and you will be ``albert_2``.

::
  
  ubuntu@albert-2:~$ 

Switch to ``root``

::

  ubuntu@albert-2:~$ sudo su -
  root@albert-2:~#

Now, be careful for the naming. Typical mistake is a typo or mismatch of
numbering.

::

  echo hc-slave1 > /etc/hostname
  hostname hc-slave1
  logout
  logout

do the same thing on ``albert_3`` and ``albert_4``.
**REPLACE** ``albert_3`` and ``albert_4`` with your vm names.

::

   ssh -o StrictHostKeyChecking=no albert_3
   sudo su -
   echo hc-slave2 > /etc/hostname
   hostname hc-slave2
   logout
   logout

This is for ``albert_4``.

::

   ssh -o StrictHostKeyChecking=no albert_4
   sudo su -
   echo hc-slave3 > /etc/hostname
   hostname hc-slave3
   logout
   logout

Update of ``/etc/hosts``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update this file on ``Master`` and ``Slaves`` both.

Your ``/etc/hosts/`` file must have all VC nodes and looks like so::

  127.0.0.1       localhost
  127.0.1.1       [your host name]

  # The following lines are desirable for IPv6 capable hosts
  ::1     localhost ip6-localhost ip6-loopback
  ff02::1 ip6-allnodes
  ff02::2 ip6-allrouters

  10.20.30.1 hc-master
  10.20.30.2 hc-slave1
  10.20.30.3 hc-slave2
  10.20.30.4 hc-slave3

Remember the **last four lines** which contain all VC nodes. You should
probably delete other hostnames to your VM nodes, if exist.

Sed for replacing Hostname (Optional)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This is an optional guide to update ``/etc/hosts`` file using ``sed``.

**REPLACE** from ``albert_1`` to ``albert_4`` with your vm names accordingly.

::
  
   sudo sed -i "s/\balbert_1-i\b/hc-master/" /etc/hosts
   sudo sed -i "s/\balbert_2-i\b/hc-slave1/" /etc/hosts
   sudo sed -i "s/\balbert_3-i\b/hc-slave2/" /etc/hosts
   sudo sed -i "s/\balbert_4-i\b/hc-slave3/" /etc/hosts

.. tip:: 
        ``sed`` is string editor we will use, 
        ``sudo sed -i 's/\b[original word]\b/[new word]/' [filename]`` It
        replaces ``[original word]`` to ``[new word]`` in a ``[filename]``
        file, if there is a matched string(s).  ``-i`` option edits a file in
        place, starting ``\b`` and ending ``\b`` works with an exact match.



.. comment
        ``hadoop`` user account
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ::
          useradd hadoop -m -s /bin/bash
        Switch to ``hadoop``
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        You are now installing Hadoop on the ``hadoop`` account. Don't get confused.
        :: 
          su - hadoop

Java Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run these commands on ``Master`` and ``Slaves`` both.

::

  sudo apt-get update
  sudo apt-get install default-jre -y

``Master`` Only

::

  sudo apt-get install openjdk-7-jdk -y

ENV configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run these commands on ``Master`` and ``Slaves`` both.

::

   cat <<EOF >> ~/.bashrc

   export JAVA_HOME=/usr/lib/jvm/default-java/
   export PATH=\$JAVA_HOME/bin:\$PATH
   export HADOOP_COMMON_HOME=\$HOME/hadoop
   export HADOOP_MAPRED_HOME=\$HADOOP_COMMON_HOME
   export HADOOP_HDFS_HOME=\$HADOOP_COMMON_HOME
   export YARN_HOME=\$HADOOP_COMMON_HOME
   export PATH=\$PATH:\$HADOOP_COMMON_HOME/bin
   export PATH=\$PATH:\$HADOOP_COMMON_HOME/sbin

   EOF

Press ``Enter`` or ``Return``

Hadoop Installation
-------------------------------------------------------------------------------

Run these commands on ``Master`` and ``Slaves`` both.

2.7.0 download from the mirror site:

::

  wget get http://mirrors.sonic.net/apache/hadoop/common/hadoop-2.7.0/hadoop-2.7.0.tar.gz 


Uncompress and symlink
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run these commands on ``Master`` and ``Slaves`` both.

::

  tar xzf hadoop-2.7.0.tar.gz
  ln -s hadoop-2.7.0 hadoop

Hadoop Configuration
-------------------------------------------------------------------------------

Do the following steps on ``Master``. We will use ``rsync`` to propagate these
configuration files to ``Slaves``.

core-site.xml
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your ``~/hadoop/etc/hadoop/core-site.xml`` should look like this::

        <configuration>
        <property>
        <name>fs.defaultFS</name>
        <value>hdfs://hc-master/</value>
        <description>NameNode URI</description>
        </property>
        </configuration>

Important line is::

        <value>hdfs://hc-master/</value>

yarn-site.xml
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your ``~/hadoop/etc/hadoop/yarn-site.xml`` should look like this::

        <configuration>
        <property>
        <name>yarn.resourcemanager.hostname</name>
        <value>hc-master</value>
        <description>The hostname of the ResourceManager</description>
        </property>
        <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
        <description>shuffle service for MapReduce</description>
        </property>
        </configuration>

mapred-site.xml
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Copy a template to a real file.

::
   
   cp ~/hadoop/etc/hadoop/mapred-site.xml.template ~/hadoop/etc/hadoop/mapred-site.xml

Your ``~/hadoop/etc/hadoop/mapred-site.xml`` should look like this::

        <configuration>
        <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
        <description>Execution framework.</description>
        </property>
        </configuration>


slaves
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your ``~/hadoop/etc/hadoop/slaves`` should look like this::

   hc-slave1
   hc-slave2
   hc-slave3

Run this command::

   echo <<EOF > ~/hadoop/etc/hadoop/slaves
   hc-slave1
   hc-slave2
   hc-slave3
   EOF

Configuration Slaves using rync
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These four configuration files will be copied to ``Slaves``.

::
  
  for slave in `cat ~/hadoop/etc/hadoop/slaves`; do \
    echo $slave; rsync -avxP --exclude=logs ~/hadoop/etc/hadoop/ $slave:~/hadoop/etc/hadoop/; \
  done

HDFS Initialization (Master)
-------------------------------------------------------------------------------

This is one-time command to format HDFS at first use.

::

  hdfs namenode -format

Start Hadoop Cluster
-------------------------------------------------------------------------------

You have to start Hadoop processes on ``Master`` and ``Slaves`` individually.

Remember, ``Master`` has

* HDFS NameNode
* YARN ResourceManager
 
And ``Slaves`` have

* HDFS DataNode
* YARN NodeManager

We will start these applications.

Start Master
-------------------------------------------------------------------------------

Run these commands on ``Master`` only.

HDFS NameNode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  hadoop-daemon.sh --script hdfs start namenode

If NameNode is started, you will see::

  $ ps -ef|grep namenode
  ubuntu    8443     1  0 05:07 ?        00:00:25 /usr/lib/jvm/default-java//bin/java -Dproc_namenode -Xmx1000m -Djava.net.preferIPv4Stack=true -Dhadoop.log.dir=/home/ubuntu/hadoop-2.7.0/logs ...
  ...  org.apache.hadoop.hdfs.server.namenode.NameNode


YARN ResourceManager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run this command on ``Master``.

::

  yarn-daemon.sh start resourcemanager

If ResourceManager is started, you will see:

::

  $ ps -ef|grep resourcemanager
  ubuntu    8675     1  0 05:07 ?        00:01:07 /usr/lib/jvm/default-java//bin/java -Dproc_resourcemanager -Xmx1000m -Dhadoop.log.dir=/home/ubuntu/hadoop-2.7.0/logs ... 
  ... org.apache.hadoop.yarn.server.resourcemanager.ResourceManager

Start Slaves
-------------------------------------------------------------------------------

Run these commands on each ``slave``.

HDFS DataNode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

 hadoop-daemon.sh --script hdfs start datanode


YARN NodeManager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  yarn-daemon.sh start nodemanager


Status Check
-------------------------------------------------------------------------------

Once you started the Hadoop software on ``Master`` and ``Slaves``, you can
check wheter it is working or not.

* HDFS: ``hdfs dfsadmin -report``
* YARN: ``yarn node -list``

Example of ``hdfs`` report::

  Configured Capacity: 21103243264 (60.65 GB)
  Present Capacity: 18373120000 (67.11 GB)
  DFS Remaining: 18372071424 (67.11 GB)
  DFS Used: 1048576 (1 MB)
  DFS Used%: 0.01%
  Under replicated blocks: 43
  Blocks with corrupt replicas: 0
  Missing blocks: 0
  Missing blocks (with replication factor 1): 0

  -------------------------------------------------
  Live datanodes (3):

  Name: 10.20.30.1:50010 (hc-slave1)
  Hostname: hc-slave1
  Decommission Status : Normal
  Configured Capacity: 21103243264 (19.65 GB)
  DFS Used: 1048576 (1 MB)
  Non DFS Used: 2730123264 (2.54 GB)
  DFS Remaining: 18372071424 (17.11 GB)
  DFS Used%: 0.00%
  DFS Remaining%: 87.06%
  Configured Cache Capacity: 0 (0 B)
  Cache Used: 0 (0 B)
  Cache Remaining: 0 (0 B)
  Cache Used%: 100.00%
  Cache Remaining%: 0.00%
  Xceivers: 1
  Last contact: Sat May 09 08:45:39 UTC 2015

  Name: 10.20.30.2:50010 (hc-slave2)
  Hostname: hc-slave2
  ...(supressed)...

  Name: 10.20.30.3:50010 (hc-slave2)
  Hostname: hc-slave2
  ...(supressed)...
 

Example of ``yarn`` list::

  15/05/09 08:49:48 INFO client.RMProxy: Connecting to ResourceManager at hc-master/10.20.30.1:8032
  Total Nodes:3
           Node-Id             Node-State Node-Http-Address       Number-of-Running-Containers
   hc-slave1:56868                RUNNING    hc-slave1:8042                                  0
   hc-slave2:56868                RUNNING    hc-slave2:8042                                  0
   hc-slave3:56868                RUNNING    hc-slave3:8042                                  0

MapReduce Example: Word Count
-------------------------------------------------------------------------------

Once you installed a Hadoop cluster, you may want to run a program using the
cluster. One of the popular examples of Hadoop is a Word Count MapReduce
program which counts how often words occur from the input text file. We have a
separate page for this program here.

:ref:`Word Count Program <ref-class-lesson-hadoop-word-count>`

FAQs
-------------------------------------------------------------------------------

Q. How to stop Masters or Slaves?
A. Use the commands below::

   (On Master)
   yarn-daemon.sh stop resourcemanager
   hadoop-daemon.sh --script hdfs stop namenode

   (On Slaves)
   yarn-daemon.sh stop nodemanager
   hadoop-daemon.sh --script hdfs stop datanode

Q. Where can I see log files?
A. ``~/hadoop/logs/`` contains log files.
   See files with ``.log`` extention. e.g.
   ``hadoop-ubuntu-namenode-hc-master.log``

Q. DataNode won't start. If I remove data storage, would it help?
A. Probably, yes. Stop datanode and remove the storage. If you used default
configuration, the HDFS storage is located under ``/tmp``.  ::

   hadoop-daemon.sh --script hdfs stop datanode
   rm -rf /tmp/hadoop-*


