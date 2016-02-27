List of Possible Projects
-------------------------------------------------------------------------------

You can choose one of the possible projects here to start developing your
projects.

Projects From NIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Possible Projects From NIST* (http://bigdatawg.nist.gov/_uploadfiles/M0399_v2_8471652990.doc)
   :widths: 10 5 5 5
   :header-rows: 1

   * - Title
     - Category
     - Data Sets
     - Technologies
   * - :ref:`Fingerprint Matching <ref-class-project-fingerprint-matching>`
     - Batch Data Analytics
     - - NIST Special Database 27a (Free)
       - NIST Special Database 14, 29, 30 (non-Free)
     - - Apache Hadoop
       - Spark
       - HBase 
   * - :ref:`Human and Face Detection from Video (simulated streaming data) <ref-class-project-human-and-face-detection>`
     - Streaming Data Analytics
     - OpenCV, INRIA Person Dataset
     - - Apache Hadoop
       - Spark
       - OpenCV
       - Mahout
       - MLlib
   * - :ref:`Live Twitter Analysis <ref-class-project-live-twitter>`
     - Streaming Data Analytics
     - Live Twitter feed
     - - Apache Strom
       - HBase
       - Twitter's Search and Streaming APIs, 
       - D3.js
       - Tableau
   * - :ref:`Big data Analytics for Healthcare Data/Health informatics <ref-class-project-healthcare>`
     - Batch Data Analytics
     - Medicare Part-B in 2014
     - - Apache Hadoop
       - Spark
       - HBase
       - Mahout
       - Lucene/Solr
       - MLlib
   * - :ref:`Spatial Big data/Spatial Statistics/Geographic Information Systems <ref-class-project-spatial-bigdata>`
     - Batch Data Analytics
     - Uber Ride Sharing GPS Data 
     - - Apache Hadoop 
       - Spark
       - GIS-tools
       - Mahout
       - MLlib 
   * - :ref:`Data Warehousing and Data mining <ref-class-project-data-warehousing>`
     - Batch Data Analytics
     - 2010 Census Data Products: United States
     - - Apache Hadoop
       - Spark
       - HBase
       - MongoDB
       - Hive
       - Pig
       - Mahout
       - Lucene/Solr
       - MLlib

* \*Reference URL of these projects:
  http://bigdatawg.nist.gov/_uploadfiles/M0399_v2_8471652990.doc

Projects from Software Deployments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Projects related to the hadoop stack consist of either extending the
functionality or using the current features. This repository is intended to
define a simple, easily deployable, customizable, data analytics stack built on
hadoop. Currently, deployment is done to a virtual cluster running on OpenStack
Kilo on FutureSystems.

.. list-table:: ansible-hadoop-stack
   :widths: 30 10 10 10
   :header-rows: 1

   * - Title
     - Category
     - Data Sets
     - Technologies
   * - :ref:`ref-ansible-hadoop-stacks`
     - Software Deployments
     - n/a
     - Ansible

Projects Derived from Benchmarking Sets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are many benchmark sets such as BigDataBench, HiBench, Graph 500,
BigBench, LinkBench, MineBench, BG Benchmark, Berkeley Big Data Benchmark,
TPCx-HS, and CloudSuite. See
http://dsc.soic.indiana.edu/publications/OgreFacetsv9.pdf

.. list-table:: BigDataBench, ICT, Chinese Academy of Sciences**
   :widths: 30 10 10 10
   :header-rows: 1

   * - Title
     - Category
     - Data Sets
     - Technologies
   * - `Amazon Movie Reviews <http://snap.stanford.edu/data/web-Movies.html>`_
     - Batch Data Analytics
     - `8 million reviews <http://snap.stanford.edu/data/movies.txt.gz>`_
     - - Hadoop
       - Spark
       - MPI
   * - `Google web graph <http://snap.stanford.edu/data/web-Google.html>`_
     - Batch Data Analytics
     - `Webgraph from Google, 2002 <http://snap.stanford.edu/data/web-Google.txt.gz>`_
     - - Hadoop
       - Spark
       - MPI
   * - `Facebook Social Network <http://snap.stanford.edu/data/egonets-Facebook.html>`_
     - Batch Data Analytics
     - `Facebook data <http://snap.stanford.edu/data/facebook.tar.gz>`_
     - - Hadoop
       - Spark
       - MPI
   * - `Genome sequence data <http://ccl.cse.nd.edu/software/sand/>`_
     - Batch Data Analytics
     - ``.cfa`` sample data (unstructured text file)
     - Work Queue (master/worker framework)

Wang, Lei, et al. "Bigdatabench: A big data benchmark suite from internet services." High Performance Computer Architecture (HPCA), 2014 IEEE 20th International Symposium on. IEEE, 2014. `link <http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=6835958&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D6835958>`_

.. comment::

        You can find more examples in the following link.

        * \**Reference URL of these projects:
          http://prof.ict.ac.cn/BigDataBench/#Benchmarks

.. list-table:: Storm, Hadoop, Hive, Mahout from Intel and Yahoo
   :header-rows: 1

   * - Title
     - Category
     - Data Sets
     - Technologies
   * - Storm Benchmark
     - Batch Data Analytics
     - https://github.com/intel-hadoop/storm-benchmark
     - Storm
   * - Big Data Benchmark for Big Bench
     - Batch Data Analytics
     - https://github.com/intel-hadoop/Big-Data-Benchmark-for-Big-Bench
     - Hadoop, Hive, Mahout
 
.. list-table:: HiBench
   :header-rows: 1

   * - Title
     - Category
     - Data Sets
     - Technologies
   * - Micro Benchmarks
        - Sort
        - WordCount
        - TeraSort
        - EnhancedDFSIO
     - Batch Data Analytics
     - https://github.com/intel-hadoop/HiBench
     - Hadoop
   * - Web Search
        - Nutch Indexing
        - Page Rank
     - Batch Data Analytics
     - https://github.com/intel-hadoop/HiBench
     - Mahout
   * - Machine Learning
        - Bayesian Classification
        - K-means Clustering
     - Batch Data Analytics
     - https://github.com/intel-hadoop/HiBench
     - Mahout
   * - OLAP Analytical Query
        - Hive Join
        - Hive Aggregation
     - Batch Data Analytics
     - https://github.com/intel-hadoop/HiBench
     - Hive

.. list-table:: Other Benchmarking Sets 
   :header-rows: 1

   * - Title
     - Category
     - Data Sets
     - Technologies
   * - Graph 500
     - Batch Data Analytics
     - http://www.graph500.org/
     - MPI
   * - BigBench 
     - Batch Data Analytics
     - http://www.msrg.org/project/BigBench
     - - MapReduce
       - Hadoop 
   * - LinkBench
     - Batch Data Analytics
     - https://github.com/facebook/linkbench 
     - - Java
       - MySQL
   * - BG Benchmark
     - Batch Data Analytics
     - http://www.bgbenchmark.org/BG/overview.html
     - - MongoDB
       - HBase
       - VoltDB
   * - Berkeley Big Data Benchmark
     - Data Systems
     - https://amplab.cs.berkeley.edu/benchmark/#workload
     - - Redshift
       - Hive
       - SparkSQL
       - Impala
       - Stinger/Tez
   * - TPCx-HS
     - Data Systems
     - http://www.tpc.org/tpcx-hs/
     - Hadoop
   * - CloudSuite
     - Batch Data Analytics
     - http://parsa.epfl.ch/cloudsuite/downloads.html
     - MapReduce
   * - MineBench
     - Batch Data Analytics
     - http://cucis.ece.northwestern.edu/projects/DMS/MineBench.html
     - 

.. csv-table:: 2015 Fall Suggested Projects
   :header: Title, Data set, Software, Category

        "`NIST Fingerprint <http://www.nist.gov/itl/iad/ig/nbis.cfm>`_ (a subset of): NFIQ PCASYS MINDTCT BOZORTH3 NFSEG SIVV",NIST Special Database 27A `[4GB] <http://www.nist.gov/itl/iad/ig/sd27a.cfm>`_,NIST Biometric Image Software (NBIS) `v5.0 <http://nigos.nist.gov:8080/nist/nbis/nbis_v5_0_0.zip>`_ [`userguide <http://www.nist.gov/customcf/get_pdf.cfm?pub_id=51097>`_],Batch Data Analytics
        Hadoop Benchmark (each) - TeraSort Suite,Teragen,hadoop-examples.jar,Batch Data Analytics
        Hadoop Benchmark (each) - DFSIO (HDFS Performance),,hadoop-mapreduce-client-jobclient,Batch Data Analytics
        Hadoop Benchmark (each) - NNBench (NameNode Perf.),,hadoop-mapreduce-client-jobclient,Batch Data Analytics
        Hadoop Benchmark (each) - MRBench (MapReduce Perf.),,src/test/org/apache/hadoop/mapred/MRBench.java,Batch Data Analytics


Projects from Other Sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Projects From Ohter Sources
   :widths: 30 10 10 10
   :header-rows: 1

   * - Title
     - Category
     - Data Sets
     - Technologies
   * - :ref:`MapReduce Implementation for Longest Common Substring Problem <ref-class-project-lcs>`
     - Batch Data Analytics
     - Escherichia coli K-12
     - - Python
       - Amazon
       - MapReduce
   * - :ref:`MapReduce Implementation for GFF Parsing <ref-class-project-gff>`
     - Batch Data Analytics
     - 
     - - Python
       - Disco
       - Amazon EC2
       - MapReduce
