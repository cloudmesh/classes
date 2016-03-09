.. _ref-class-lesson-zookeeper:

Apache ZooKeeper
===============================================================================

ZooKeeper is a open source project to provide a configuration and
synchronization service for cluster computing. With ZooKeeper, Hadoop YARN
ResourceManager (RM) is supported with high availability. HBase, Storm and
other software use ZooKeeper for coordinating the cluster.

Overview
-------------------------------------------------------------------------------

ZooKeeper is a distributed, open-source coordination service for distributed
applications. It exposes a simple set of primitives that distributed
applications can build upon to implement higher level services for
synchronization, configuration maintenance, and groups and naming. It is
designed to be easy to program to, and uses a data model styled after the
familiar directory tree structure of file systems. It runs in Java and has
bindings for both Java and C. (as quoted in ZooKeeper overview:
http://zookeeper.apache.org/doc/trunk/zookeeperOver.html)

.. figure:: ../../../images/lesson/zkservice.jpg

   Figure 1. ZooKeeper Service

Key points
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Data replication
* Ensemble is a group of ZooKeeper servers to use replication to achieve high
  availability and performance
* Odd number of servers due to simple majority voting
* Single (Standalone) installation is not for a production model
* Leader election
* Configuration, Name Service, Group Membership
* Wait-free for fault tolerance, performance (compared to Chubby)
* Started by Yahoo

Chubby is a locking service with strong synchronization guarantees.

Zab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Zab is a leader-based atomic broadcast protocol used in ZooKeeper to guarantee
that update operations satisfy linearizability.

Implementation
-------------------------------------------------------------------------------

ZooKeeper synchronizes every changes to the tree of znodes across the ZooKeeper
servers, ensemble. This way prevents inconsistency of the data by sharing the
information. If one of the servers fails, the rest of them will replicate state
and trees.

* Leader election
* Atomic broadcast

Znodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Znodes is a hierarchical name space of data registers and each znode has a path
with a delimeter "/" like a directory structure. There are parent and child
znodes.

Apache Qurator
-------------------------------------------------------------------------------

Apache Qurator is a set of Java libraries for automatic ZooKeeper connection
management with retries and easy development of new ZooKeeper recipes.

Github: https://github.com/apache/curator

ZooKeeper Installation
-------------------------------------------------------------------------------

Required Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ZooKeeper runs in Java, release 1.6 or greater (JDK 6 or greater).

Java JDK

::

  sudo apt-get update
  sudo apt-get install openjdk-7-jdk

You can find other installation packages here:
http://java.sun.com/javase/downloads/index.jsp

ZooKeeper Server Package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download latest here: http://www.apache.org/dyn/closer.cgi/zookeeper/

Download 3.4.6 

::

  wget http://supergsego.com/apache/zookeeper/stable/zookeeper-3.4.6.tar.gz
  tar xzf zookeeper*.tar.gz
  ln -s zookeeper-3.4.6 zookeeper
  
Configuration ``zoo.cfg``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  cp zookeeper/conf/zoo_sample.cfg zookeeper/conf/zoo.cfg
  nano zookeeper/conf/zoo.cfg

Confirm the settings and update with::

  tickTime=2000
  dataDir=/var/lib/zookeeper
  clientPort=2181

* tickTime: the basic time unit in milliseconds used by ZooKeeper. It is used
  to do heartbeats and the minimum session timeout will be twice the tickTime.

* dataDir: the location to store the in-memory database snapshots and, unless
  specified otherwise, the transaction log of updates to the database.

* clientPort: the port to listen for client connections

If you have multiple severs, ``zoo.cfg`` has more values, for example::

  server.1=10.0.0.2:2888:3888  
  server.2=10.0.0.3:2888:3888  
  server.3=10.0.0.4:2888:3888

It is ``server.id=host:port:port``

.. tip:: Ensemble setup (multi-server)
    http://zookeeper.apache.org/doc/trunk/zookeeperAdmin.html#sc_zkMulitServerSetup

myid in ``var/lib/zookeeper`` (For multi-server)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The myid file which stays in ``dataDir`` contains a machine's id. If you have 3
servers, first server has 1 in the myid, and second one has 2.  The id must be
unique within the ensemble and should have a value between 1 and 255.

node 1

::
  
  mkdir -r /var/lib/zookeeper
  echo "1" > /var/lib/zookeeper/myid  

node 2

::
  
  mkdir -r /var/lib/zookeeper
  echo "2" > /var/lib/zookeeper/myid  


Start ZooKeeper Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that you created the configuration file, you can start ZooKeeper::

  zookeeper/bin/zkServer.sh start

ZooKeeper Client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  zookeeper/bin/zkCli.sh
  ...
  [zk: localhost:2181(CONNECTED) 0]

If you get access to other nodes::

  zookeeper/bin/zkCli.sh -server [node ip address]:2181  

Citation
-------------------------------------------------------------------------------

Hunt, Patrick, et al. "ZooKeeper: Wait-free Coordination for Internet-scale
Systems." USENIX Annual Technical Conference. Vol. 8. 2010. `[pdf] 
<https://www.usenix.org/event/usenix10/tech/full_papers/Hunt.pdf>`_

Reading List
-------------------------------------------------------------------------------

* Reed, Benjamin, and Flavio P. Junqueira. "A simple totally ordered broadcast
  protocol." proceedings of the 2nd Workshop on Large-Scale Distributed Systems
  and Middleware. ACM, 2008. `[pdf] 
  <http://diyhpl.us/~bryan/papers2/distributed/distributed-systems/zab.totally-ordered-broadcast-protocol.2008.pdf>`_
* Junqueira, Flavio Paiva, Benjamin C. Reed, and Marco Serafini. "Zab:
  High-performance broadcast for primary-backup systems." Dependable Systems &
  Networks (DSN), 2011 IEEE/IFIP 41st International Conference on. IEEE, 2011.
  `[pdf] <http://web.stanford.edu/class/cs347/reading/zab.pdf>`_ 
* Design Paper for Hadoop and Zookeeper `[pdf]
  <https://issues.apache.org/jira/secure/attachment/12486023/MapReduce_NextGen_Architecture.pdf>`_
* Chapter 14: ZooKeeper in Hadoop: The Definitive Guide By Tom White

Additional Readling List
-------------------------------------------------------------------------------

* Kirsch, Jonathan, and Yair Amir. "Paxos for system builders." Dept. of CS,
  Johns Hopkins University, Tech. Rep (2008). `[pdf]
  <http://www.cnds.jhu.edu/pub/papers/psb_ladis_08.pdf>`_
* Baker, Jason, et al. "Megastore: Providing Scalable, Highly Available Storage
  for Interactive Services." CIDR. Vol. 11. 2011.  `[pdf]
  <http://pdos.csail.mit.edu/6.824-2012/papers/jbaker-megastore.pdf>`_
* Kadambi, Sudarshan, et al. "Where in the world is my data." Proceedings
  International Conference on Very Large Data Bases (VLDB). 2011. `[pdf]
  <http://www.vldb.org/pvldb/vol4/p1040-kadambi.pdf>`_
* Burrows, Mike. "The Chubby lock service for loosely-coupled distributed
  systems." Proceedings of the 7th symposium on Operating systems design and
  implementation. USENIX Association, 2006.  `[html]
  <http://static.usenix.org/events/osdi06/tech/full_papers/burrows/burrows_html/>`_
* Taylor, Ronald C. "An overview of the Hadoop/MapReduce/HBase framework and
  its current applications in bioinformatics." BMC bioinformatics 11.Suppl 12
  (2010): S1. `[html] <http://www.biomedcentral.com/1471-2105/11/S12/S1>`_

Acknowledgement
-------------------------------------------------------------------------------
      
This lesson is adopted from Apache ZooKeeper Documentation:
http://zookeeper.apache.org/doc/trunk/zookeeperOver.html

