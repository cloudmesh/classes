.. _ref-class-lesson-mongodb-sharded-cluster:

MongoDB Sharded Cluster
=======================

This tutorial shows deploying a sharded mongodb cluster on india.futuresystems.org.

.. tip:: Approximate time: 30 minutes

.. contents:: Table of Contents
   :depth: 2

MongoDB Sharding Overview
-------------------------

.. image:: images/mongodb-overview.png
Figure 1. Sharding Mongodb
*Image reference: http://docs.mongodb.org/master/MongoDB-sharding-guide.pdf*

* Shards store the data. To provide high availability and data consistency, in
  a production sharded cluster, each shard is a replica set 1
* Query Routers, or mongos instances, interface with client applications and
  direct operations to the appropriate shard or shards. The query router
  processes and targets operations to shards and then returns results to the
  clients. A sharded cluster can contain more than one query router to divide
  the client request load. A client sends requests to one query router. Most
  sharded clusters have many query routers.
* Config servers store the cluster’s metadata. This data contains a mapping of
  the cluster’s data set to the shards. The query router uses this metadata to
  target operations to specific shards. Production sharded clusters have
  exactly 3 config servers

Start Virtual Cluster for Database
----------------------------------

In this test environment, three instances are required to connect mongodb
databases on the cloud. Try *cm cluster* command to create virtual machines in
the OpenStack India. See the page:

.. toctree::
   :maxdepth: 1

   virtual_cluster

Install Mongodb Server
----------------------

Install mongodb server on each of the three virtual instances. If you have
other operating systems, please use its package management program e.g. yum or
brew.

::

   (Ubuntu)
   sudo apt-get install mongodb-server

   (CentOS)
   sudo yum install mongodb-server

   (Mac OS)
   sudo brew install mongodb-server

Configure Instances
-------------------

* Create data directories for each of the three config server instances. By
  default, a config server stores its data files in the /data/configdb
  directory.  You can choose a different location. To create a data directory,
  issue a command similar to the following::

        sudo mkdir -p /data/configdb
        
* Start the three config server instances. Start each by issuing a command
  using the following syntax:: 
  
        mongod --configsvr --dbpath <path> --port <port>

  The default port for config servers is 27019. You can specify a different
  port. The following example starts a config server using the default port and
  default data directory:: 
  
        sudo mongod --configsvr --dbpath /data/configdb --port 27019 &

For additional command options, see mongod or Configuration File Options.

.. note:: All config servers must be running and available when you first initiate a sharded cluster.

Start mongos Instances
----------------------

The mongos instances are lightweight and do not require data directories. You
can run a mongos instance on a system that runs other cluster components, such
as on an application server or a server running a mongod process. By default, a
mongos instance runs on port 27017.

When you start the mongos instance, specify the hostnames of the three config
servers, either in the configuration file or as command line parameters.

To start a mongos instance, issue a command using the following syntax::

        mongos --configdb <config server hostnames>

For example, to start a mongos that connects to config server instance running
on the following hosts and on the default ports::

        albert_1-i
        albert_2-i
        albert_3-i

You would issue the following command::

        mongos --configdb albert_1-i:27019,albert_2-i:27019,albert_3-i:27019

*albert_1-i, albert_2-i, and albert_3-i are hostnames for internal IPs*

Each mongos in a sharded cluster must use the same configDB string, with
identical host names listed in identical order.

If you start a mongos instance with a string that does not exactly match the
string used by the other mongos instances in the cluster, the mongos return a
Config Database String Error error and refuse to start.

Add Shards to the Cluster
-------------------------

A shard can be a standalone mongod or a replica set. In a production
environment, each shard should be a replica set. Use the procedure in Deploy a
Replica Set to deploy replica sets for each shard.

* From a mongo shell, connect to the mongos instance. Issue a command using the following syntax::

    mongo --host <hostname of machine running mongos> --port <port mongos listens on>

  For example, if a mongos is accessible at mongos0.example.net on port 27017, issue the following command::

    mongo --host albert_1-i --port 27017


* Add each shard to the cluster using the sh.addShard() method, as shown in the
  examples below. Issue sh.addShard() separately for each shard. If the shard
  is a replica set, specify the name of the replica set and specify a member of
  the set. In production deployments, all shards should be replica sets.

.. optional:: You can instead use the addShard database command, which lets you
   specify a name and maximum size for the shard. If you do not specify these,
   MongoDB automatically assigns a name and maximum size. To use the database
   command, see addShard.

The following are examples of adding a shard with sh.addShard()::

  * To add a shard for a replica set named rs1 with a member running on port
    27017 on mongodb0.example.net, issue the following command::

          sh.addShard( "rs1/albert_1-i:27017" )

    For MongoDB versions prior to 2.0.3, you must specify all members of the
    replica set. For example::


          sh.addShard(
          "rs1/albert_1-i:27017,albert_2-i:27017,albert_3-i:27017"
          )

 * To add a shard for a standalone mongod on port 27017 of
   mongodb0.example.net, issue the following command::

        sh.addShard( "albert_1-i:27017" )

.. note:: It might take some time for chunks to migrate to the new shard.

Enable Sharding for a Database
------------------------------

Before you can shard a collection, you must enable sharding for the
collection’s database. Enabling sharding for a database does not redistribute
data but make it possible to shard the collections in that database.

Once you enable sharding for a database, MongoDB assigns a primary shard for
that database where MongoDB stores all data before sharding begins.

* From a mongo shell, connect to the mongos instance. Issue a command using the
  following syntax::

  mongo --host <hostname of machine running mongos> --port <port mongos listens on>

* Issue the sh.enableSharding() method, specifying the name of the database for
  which to enable sharding. Use the following syntax::

  sh.enableSharding("<database>")

Optionally, you can enable sharding for a database using the enableSharding
command, which uses the following syntax::

  db.runCommand( { enableSharding: <database> } )

Enable Sharding for a Collection
---------------------------------

You enable sharding on a per-collection basis.

* Determine what you will use for the shard key. Your selection of the shard
  key affects the efficiency of sharding. See the selection considerations
  listed in the Considerations for Selecting Shard Key.

* If the collection already contains data you must create an index on the shard
  key using ensureIndex(). If the collection is empty then MongoDB will create
  the index as part of the sh.shardCollection() step.

* Enable sharding for a collection by issuing the sh.shardCollection() method
  in the mongo shell. The method uses the following syntax::

  sh.shardCollection("<database>.<collection>", shard-key-pattern)

  Replace the <database>.<collection> string with the full namespace of your
  database, which consists of the name of your database, a dot (e.g. .), and
  the full name of the collection. The shard-key-pattern represents your shard
  key, which you specify in the same form as you would an index key pattern.

  ::

          EXAMPLE
          The following sequence of commands shards four collections:

          sh.shardCollection("records.people", { "zipcode": 1, "name": 1 } )
          sh.shardCollection("people.addresses", { "state": 1, "_id": 1 } )
          sh.shardCollection("assets.chairs", { "type": 1, "_id": 1 } )
          sh.shardCollection("events.alerts", { "_id": "hashed" } )

In order, these operations shard::

* The people collection in the records database using the shard key {
  "zipcode": 1, "name": 1 }.  This shard key distributes documents by the value
  of the zipcode field. If a number of documents have the same value for this
  field, then that chunk will be splittable by the values of the name field.
* The addresses collection in the people database using the shard key {
  "state": 1, "_id": 1 }.  This shard key distributes documents by the value of
  the state field. If a number of documents have the same value for this field,
  then that chunk will be splittable by the values of the _id field.
* The chairs collection in the assets database using the shard key { "type": 1,
  "_id": 1 }.  This shard key distributes documents by the value of the type
  field. If a number of documents have the same value for this field, then that
  chunk will be splittable by the values of the _id field.
* The alerts collection in the events database using the shard key { "_id":
  "hashed" }.

*New in version 2.4.*

This shard key distributes documents by a hash of the value of the _id field.
MongoDB computes the hash of the _id field for the hashed index, which should
provide an even distribution of documents across a cluster.

Next Step
---------

We have additional tutorial for using cloud resources on FutureSystems.
In the next page, we explore several examples such as IPython, Chef, etc.

.. toctree::
   :maxdepth: 1

   Next - Other examples <additional_examples>
