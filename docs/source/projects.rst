Software Projects
=================

.. sidebar:: Contents

   .. contents::
      :local:


.. warning::

   This page is still under construction

There are several categories of software projects, which are detailed in
lower sections:

#. Deployment
#. Analytics

You may propose a project in one of these categories, if you are doing
a software projects.

.. warning::

   These are non-trivial and involve a lot of complexity.  Many
   students vastly underestimate the difficulty and the amount of time
   required.


Common Requirements
-------------------

All software projects must:

#. Be submitted via gitlab (a repository will be created for you)
#. Be reproducibly deployed

   Assume you are given a username and a set of IP addresses.  From
   this starting point, you should be able to deploy everything in a
   single commandline invocation.

   .. warning::

      Do not assume that the username or IP address will be the ones
      you use during development and testing.

#. Provide a report in the ``docs/report`` directory

   LaTeX or Word may be used. Include the original sources as well as a PDF called ``report.pdf``
   (See :ref:`overview-software-project` for additional details on the report format)

#. Provide a properly formatted ``README.rst`` or ``README.md`` in the root directory

   The README should have the following sections:

   - Authors: list the authors
   - Project Type: one of "Deployment", "Analytics"
   - Problem: describe the task and/or problem
   - Requirements: describe your assumptions and requirements for deployment/running.
     This should include any software requirements with a link to their webpage.
     Also indicate which versions you have developed/tested with.

   - Running: describe the steps needed to deploy and run
   - Acknowledgements: provide proper attribution to any websites, or
     code you may have used or adapted

#. A ``LICENSE`` file (this should be the ``LICENSE`` for Apache License Version 2.0)


Deployment Projects
-------------------

Deployment projects focuses on automated software deployments on
multiple nodes using automation tools such as Ansible, Chef, Puppet,
Salt, or Juju. For example, you could work on deploying Hadoop to a
cluster of several machines. Use of Ansible is recommended and
supported. Other tools such as Chef, Puppet, etc, will not be
supported.

Note that it is not sufficient to merely deploy the software on the
cluster. You must also demonstrate the use of the cluster by running
some program on it and show the utilization of your entire cluster.
You should also benchmark the deployment and running of your
demonstration on several sizes of a cluster (eg 1, 3, 6, 10 nodes)
(Note that these numbers are for example only).

We expect to see figures showing times for each (deployment, running)
pair on for each cluster size, with error bars.  This means that you
need to run each benchmark multiple times (at least three times) in
order to get the error bars. You should also demonstrate cluster
utilization for each cluster size.

The program used for demonstration can be simple and straightforward.
This is not the focus of this type of project.


Requirements
~~~~~~~~~~~~

.. todo:: list requirements as differing from "Common Requirements"


Example projects
~~~~~~~~~~~~~~~~

- deploy Apache Spark on top of Hadoop
- deploy Apache Pig on top of Hadoop
- deploy Apache Storm
- deploy Apache Flink
- deploy a Tensorflow cluster
- deploy a PostgreSQL cluster
- deploy a MongoDB cluster
- deploy a CouchDB cluster
- deploy a Memcached cluster
- deploy a MySQL cluster
- deploy a Redis cluster
- deploy a Mesos cluster
- deploy a Hadoop cluster


Analytics Projects
------------------

Analytics projects focus on data exporation.  For this type of
projects, you should focus on analysis of a dataset (see
:doc:`datasets` for starting points).  The key here is to take a
dataset and extract some meaningful information from in using tools
such as ``scikit-learn``, ``mllib``, or others.  You should be able to
provide graphs, descriptions for your graphs, and argue for
conclusions drawn from your analysis.

Your deployment should handle the process of downloading and
installing the required datasets and pushing the analysis code to the
remote node.  You should provide instructions on how to run and
interpret your analysis code in your README.


Requirements
~~~~~~~~~~~~

.. todo:: list requirements as differing from "Common Requirements"


Example projects
~~~~~~~~~~~~~~~~

- analysis of US Census data
- analysis of Uber ride sharing GPS data
- analysis of Health Care data
- analysis of images for Human Face detection
- analysis of streaming Twitter data
- analysis of airline prices, flights, etc
- analysis of network graphs (social networks, disease networks, protein networks, etc)
- analysis of music files for recomender engines



.. _sampleprojects:

Sample Project suggestions
===========================


Example Projects
------------------

These are projects that will be supported on FutureSystems resources.
Certain projects, such as NIST Fingerprint, may be accomplished by
running a subset of 1 or more of the software packages.


+-------------------------------------------------------+--------------------------------+-------------------------------------------------------+
| **Title**                                             | **Data set**                   | **Software**                                          |
+-------------------------------------------------------+--------------------------------+-------------------------------------------------------+
| | **Category: Batch Data Analytics**                  |                                |                                                       |
+-------------------------------------------------------+--------------------------------+-------------------------------------------------------+
| | NIST_Fingerprint_ (a subset of):                    | | NISTDatabase27A_ [4GB]       | | NISTBiometric_                                      |
| | NFIQ                                                |                                | | Image Software (NBIS) v5.0 Userguide_              |
| | PCASYS                                              |                                | |                                                     |
| | MINDTCT                                             |                                | |                                                     |
| | BOZORTH3                                            |                                | |                                                     |
| | NFSEG                                               |                                | |                                                     |
| | SIVV                                                |                                | |                                                     |
+-------------------------------------------------------+--------------------------------+-------------------------------------------------------+
| | Hadoop Benchmark                                    |                                |                                                       |
| | TeraSort Suite                                      | | Teragen                      | hadoop-examples.jar                                   |
+-------------------------------------------------------+--------------------------------+-------------------------------------------------------+
| | Hadoop Benchmark                                    |                                |                                                       |
| | DFSIO (HDFS Performance)                            |                                | hadoop-mapreduce-client-jobclient                     |
+-------------------------------------------------------+--------------------------------+-------------------------------------------------------+
| | Hadoop Benchmark                                    |                                |                                                       |
| | NNBench (NameNode Perf.)                            |                                | hadoop-mapreduce-client-jobclient                     |
+-------------------------------------------------------+--------------------------------+-------------------------------------------------------+
| | Hadoop Benchmark                                    |                                |                                                       |
| | MRBench (MapReduce Perf.)                           |                                | src/test/org/apache/hadoop/mapred/MRBench.java        |
+-------------------------------------------------------+--------------------------------+-------------------------------------------------------+
| | Stock Data Analysis with MPI                        | | CRSP_ Stock Analysis         | | Streaming Data Analytics                            |
| |                                                     | | e.g. Trading Symbol,         | |                                                     |
| |                                                     | | Price                        | |                                                     |
| |                                                     | | Number of Shares Outstanding | |                                                     |
| |                                                     | | Factor to adjust price       | |                                                     |
| |                                                     | | Factor to adjust shares      | |                                                     |
+-------------------------------------------------------+--------------------------------+-------------------------------------------------------+

Note: 
* TeraSort: hadoop-examples.jar is included in hadoop package.

* MRBench, NNBench, DFSIO: hadoop-mapreduce-client-jobclient-2.7.1.jar is included as well. If not, it can be downloaded directly from
  `*here* <https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-mapreduce-client-jobclient/2.7.1/hadoop-mapreduce-client-jobclient-2.7.1.jar>`__.

 Brief guidelines for these benchmark tools from last year:

-  `TeraSort Hadoop
   Benchmark <http://bdaafall2015.readthedocs.io/en/latest/terasort.html#terasort>`__

-  `DFSIO Distributed I/O
   Benchmark <http://bdaafall2015.readthedocs.io/en/latest/dfsio.html#dfsio>`__

-  `MRBench MapReduce
   Benchmark <http://bdaafall2015.readthedocs.io/en/latest/mrbench.html#mrbench>`__

`NNBench NameNode
Benchmark <http://bdaafall2015.readthedocs.io/en/latest/nnbench.html#nnbench>`__


.. _NISTFIngerprint: http://www.nist.gov/itl/iad/ig/nbis.cfm

.. _NISTDataset27A: http://www.nist.gov/itl/iad/ig/sd27a.cfm

.. _NISTBiometric: http://nigos.nist.gov:8080/nist/nbis/nbis_v5_0_0.zip

.. _Userguide: https://soic.scholargrid.org/courses/course-v1:iudatascience+I523-I423-ENG599+FALL_2016/info

.. _CRSP: https://wrds-web.wharton.upenn.edu/wrds/

Other Possible Projects
-----------------------

These are projects for which there may be tentative, or no, direct
support on FutureSystems resources.





+--------------------------------------+------------------------------------------------+------------------+
| **Title**                            | **Data set**                                   | **Software**     |
+--------------------------------------+------------------------------------------------+------------------+
| **Category: Batch Data Analytics**                                                                       |
+--------------------------------------+------------------------------------------------+------------------+
| Census                               | | Data1_ csv files downloadable                | | n/a            |
|                                      | | click "Internet tables" to select subsets)   | |                |
+--------------------------------------+------------------------------------------------+------------------+
| Amazon Movie Reviews (1997-2012)     | Data3_ 3GB (compressed)                        |                  |
+--------------------------------------+------------------------------------------------+------------------+
| Medicare Part-B (2000-2013)          | Data4_ <30 MB, CSV ('00-'09), Excel ('10-'13)  | n/a              |
+--------------------------------------+------------------------------------------------+------------------+
| HiBench        - sort                | n/a                                            | HibenchSuite_    |
+--------------------------------------+------------------------------------------------+------------------+
| HiBench        - wordcount           | n/a                                            | HibenchSuite_    |
+--------------------------------------+------------------------------------------------+------------------+
| HiBench        - terasort            | n/a                                            | HibenchSuite_    |
+--------------------------------------+------------------------------------------------+------------------+
| HiBench        - scan/join/aggregate | n/a                                            | HibenchSuite_    |
+--------------------------------------+------------------------------------------------+------------------+
| HiBench        - pagerank            | n/a                                            | HibenchSuite_    |
+--------------------------------------+------------------------------------------------+------------------+
| HiBench        - netchindexing       | n/a                                            | HibenchSuite_    |
+--------------------------------------+------------------------------------------------+------------------+
| HiBench        - bayes               | n/a                                            | HibenchSuite_    |
+--------------------------------------+------------------------------------------------+------------------+
| HiBench        - kmeans              | n/a                                            | HibenchSuite_    |
+--------------------------------------+------------------------------------------------+------------------+
| HiBench        - dfsio               | n/a                                            | HibenchSuite_    |
+--------------------------------------+------------------------------------------------+------------------+
| Movie Reviews using IPython          | Data from Rottentomatoes.com                   | IPython1_        |
+--------------------------------------+------------------------------------------------+------------------+
| Red Wine Quality using IPython       | REDWINE_                                       | IPython2_        |
+--------------------------------------+------------------------------------------------+------------------+
| Airline Delays with Hadoop           | AIRLINE                                        | IPython3_        |
+--------------------------------------+------------------------------------------------+------------------+
| BigBench                             | n/a                                            | BDBench_         |
+--------------------------------------+------------------------------------------------+------------------+
| Genome sequence data                 | .cfa sample data (unstructured)                | SANDDATA_        |
+--------------------------------------+------------------------------------------------+------------------+
| **Category: Streaming Data Analytics**                                                                   |
+--------------------------------------+------------------------------------------------+------------------+
| Face Detection                       | Data2_ images from INRIA dataset (< 1GB)       | OpenCV           |
+--------------------------------------+------------------------------------------------+------------------+
| Live Twitter Feed analysis           | Live Twitter feed                              |                  |
+--------------------------------------+------------------------------------------------+------------------+
| Drug-Drug interactions on Twitter    | Live Twitter Data                              | DRUG_            |
+--------------------------------------+------------------------------------------------+------------------+



.. _Data1: http://www.census.gov/population/www/cen2010/glance/

.. _Data2: http://pascal.inrialpes.fr/data/human/

.. _Data3: http://snap.stanford.edu/data/web-Movies.html

.. _Data4: https://www.cms.gov/Research-Statistics-Data-and-Systems/Downloadable-Public-Use-Files/Part-B-National-Summary-Data-File/Overview.html

.. _HibenchSuite: https://github.com/intel-hadoop/HiBench

.. _iPython1: http://nbviewer.ipython.org/github/cs109/content/blob/master/HW3_solutions.ipynb

.. _iPython2: http://nbviewer.ipython.org/github/cs109/2014/blob/master/homework-solutions/HW5-solutions.ipynb

.. _iPython3: http://nbviewer.ipython.org/github/ofermend/IPython-notebooks/blob/master/blog-part-1.ipynb

.. _BDBench: https://github.com/intel-hadoop/Big-Data-Benchmark-for-Big-Bench

.. _DRUG:  https://github.com/cloud-class-projects/drug-drug-interaction

.. _SAND: http://ccl.cse.nd.edu/software/sand/

.. _SANDDATA: http://ccl.cse.nd.edu/software/sand/

.. _REDWINE:  https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/

.. _AIRLINE:  http://stat-computing.org/dataexpo/2009/the-data.html


Your Own Projects
-----------------

You have an option to create your own project with your idea. You can
use Python, Java, R, or other languages that you prefer. The size or the
domain of your datasets is open as long as they can be handled and
reproduced by course instructors.

Non-Software Projects
---------------------

If you have selected non-software projects, you or your team can develop
your project without software development or applications.

Use examples given below to choose a project. You can follow one of
these examples or choose your own.



* Survey HPC-ABDS; Several topics such as review level 17 (orchestration),
  Compare level 6 (DevOps) and level 15B (PaaS Frameworks) and level 17;
  KALEIDOSCOPE_

* Review of Recommender Systems: Technology & Applications ; Define
  classification of information filtering system with current technologies
  and applications ; RECOMENDER_

* Review of Big Data in Bioinformatics; Find current challenges and
  understand state of bioinformatics solutions for big data including
  analytics, security and privacy.

* Review of Data visualization including high dimensional data; Explore
  data mining methods for knowledge discovery with data visualization
  tools e.g. D3.js, matplotlib

* Design of a NoSQL database for a specialized application; Explore
  design of databases for big data including HBase, MongoDB, etc.

.. _KALEIDOSCOPE: http://hpc-abds.org/kaleidoscope
.. _RECOMENDER: http://bdaafall2015.readthedocs.org/en/latest/tp1-recommender.html#tp1-recommender


NIST Examples
----------------------------------------------------

-  **NIST**

   -  **NFIQ**: `NIST Fingerprint Image Quality (NFIQ) <http://biometrics.nist.gov/cs_links/standard/archived/workshops/workshop1/presentations/Tabassi-Image-Quality.pdf>`__,
          Tabassi, Elham,
          C. Wilson, and C. Watson. "Nist fingerprint image
          quality." NIST Res. Rep. NISTIR7151 (2004).
   -  **PCASYS**: `Fingerprint Pattern Classification <http://www.nist.gov/manuscript-publication-search.cfm?pub_id=900754>`__,
          Candela, G. T., et al. "PCASYS-A pattern-level classification automation system
          for fingerprints." *NIST technical report NISTIR* 5647 (1995).

   -  MINDTCT

   -  BOZORTH3

   -  NFSEG

   -  SIVV: `pdf <http://www.nist.gov/manuscript-publication-search.cfm?pub_id=903078>`__
