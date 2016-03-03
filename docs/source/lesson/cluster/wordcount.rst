.. _ref-class-lesson-hadoop-word-count:

Word Count Map Reduce Application
===============================================================================

Overview
-------------------------------------------------------------------------------

Word Count program is a simple program that counts the number of occurrences of
each word in a given input set (files).  Executing this program on a single
node or on a cluster is a good example to get a flavor for how Hadoop works
with MapReduce framework.

.. tip:: Duration: 1 hour

Prerequisite
-------------------------------------------------------------------------------

You must have a Hadoop installed machine up and running to execute Word Count.
If you don't have a hadoop installation, one of the following pages help you
install and configure a Hadoop cluster on OpenStack FutureSystems. 

* :ref:`Hadoop Cluster with Cludmesh <ref-class-lesson-deploying-hadoop-cluster-with-cloudmesh>`
* :ref:`Hadoop Cluster Manual Installation with Chef<ref-class-lesson-deploying-hadoop-cluster-manual>`

Word Count v1.0
-------------------------------------------------------------------------------

If you run a Hadoop cluster, the following tutorial must take place in a master
node (namenode). Also,  we assume that you run the tutorial commands on ``root``.

Understand the requirements: 

* Write a program on ``namenode``
* Be on ``root`` account
* Have ``hadoop`` installed
* Have ``namenode``, ``yarn manager``, and ``yarn resource manager`` running

WordCount.java
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, create a ``WordCount.java`` file to implement Map and Reduce functions.


.. literalinclude:: WordCount.java

Or, you can download the file.::

  wget https://raw.githubusercontent.com/cloudmesh/introduction_to_cloud_computing/master/docs/source/class/lesson/cluster/WordCount.java

Environment Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To compile the ``WordCount.java``, environment variables need to be configured.
There are ``JAVA_HOME``, ``PATH`` and ``HADOOP_CLASSPATH`` to be set.

You may have ``JAVA_HOME`` set like this::
 
  ubuntu@hadoop1:~$ echo $JAVA_HOME
  /usr/lib/jvm/java-6-oracle-amd64

Then update ``PATH`` and ``HADOOP_CLASSPATH``,::

  export PATH=$JAVA_HOME/bin:$PATH
  export HADOOP_CLASSPATH=$JAVA_HOME/lib/tools.jar

Compile and Package ``WordCount.java``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compile ``WordCount.java``::

  hadoop com.sun.tools.javac.Main WordCount.java

Package ``WordCount.class``::

  jar cf word_count.jar WordCount*.class

Directories in HDFS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Input files and output files of the Word Count program will be stored in HDFS.

Confirm that you have a base directory ``/user/root``::

  hdfs dfs -ls /user/root

Create a directory ``wordcount``::

  hdfs dfs -mkdir /user/root/wordcount

Create a input directory ``input`` where text files stay::

  hdfs dfs -mkdir /user/root/wordcount/inputs

Create sample text files and upload to HDFS::

  echo "Welcome Hadoop Enjoy Hadoop" > welcome.txt
  hdfs dfs -copyFromLocal welcome.txt /user/root/wordcount/inputs/
  echo "Mapper and Reducer will be used Enjoy MayReduce" > welcome2.txt
  hdfs dfs -copyFromLocal welcome2.txt /user/root/wordcount/inputs/

Run WordCount
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's simple, just run this command::

  hadoop jar word_count.jar WordCount /user/root/wordcount/inputs /user/root/wordcount/outputs-v1

This command runs ``WordCount`` class from ``word_count.jar`` Jar file with the
input directory ``../inputs`` and the output directory ``../outputs-v1``.
Output directory will be automatically created.

The expected output looks like this::

        15/04/21 19:26:56 INFO Configuration.deprecation: session.id is deprecated. Instead, use dfs.metrics.session-id
        15/04/21 19:26:56 INFO jvm.JvmMetrics: Initializing JVM Metrics with processName=JobTracker, sessionId=
        15/04/21 19:26:57 WARN mapreduce.JobSubmitter: Hadoop command-line option parsing not performed. Implement the Tool interface and execute your application with ToolRunner to remedy this.
        15/04/21 19:26:57 WARN mapreduce.JobSubmitter: No job jar file set.  User classes may not be found. See Job or Job#setJar(String).
        ... (skip) ...
        15/04/21 19:30:54 INFO input.FileInputFormat: Total input paths to process : 2
        ... (skip) ...
        15/04/21 19:30:57 INFO mapreduce.Job:  map 100% reduce 0%
        15/04/21 19:30:58 INFO mapred.LocalJobRunner: reduce task executor complete.
        15/04/21 19:30:58 INFO mapreduce.Job:  map 100% reduce 100%
        15/04/21 19:30:58 INFO mapreduce.Job: Job job_local1244998837_0001 completed successfully
        ... (skip) ...
        File Input Format Counters 
        Bytes Read=674582
        File Output Format Counters 
        Bytes Written=196200

Result
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's see the result.
``/user/root/wordcount/outputs-v1`` contains result files including
``part-r-00000`` file.

::
   
   hdfs dfs -cat /user/root/wordcount/outputs-v1/part-r-00000

   Enjoy        2
   Hadoop       2
   Mapper       1
   MayReduce    1
   Reducer      1
   Welcome      1
   and  1
   be   1
   used 1
   will 1

Word Count v3.0 (TBD)
-------------------------------------------------------------------------------

Acknowledgement
-------------------------------------------------------------------------------

This tutorial is adopted from:

* `WordCount v1.0 <http://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html#Example:_WordCount_v1.0>`_
