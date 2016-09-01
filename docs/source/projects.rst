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
