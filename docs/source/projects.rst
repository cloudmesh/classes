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
| | NFIQ                                                |                                | | Image Software (NBIS) `v5.0 Userguide_              | 
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


_NISTFIngerprint: http://www.nist.gov/itl/iad/ig/nbis.cfm

_NISTDataset27A: http://www.nist.gov/itl/iad/ig/sd27a.cfm

_NISTBiometric: http://nigos.nist.gov:8080/nist/nbis/nbis_v5_0_0.zip

_Userguide: https://soic.scholargrid.org/courses/course-v1:iudatascience+I523-I423-ENG599+FALL_2016/info

_CRSP: https://wrds-web.wharton.upenn.edu/wrds/

Other Possible Projects
-----------------------

These are projects for which there may be tentative, or no, direct
support on FutureSystems resources.






| **Title**                            | **Data set**                                                              | **Software**                                   |
| Census                               | Data1_ csv files downloadable (click "Internet tables" to select subsets) | n/a                                            |
| Amazon Movie Reviews (1997-2012)     | Data3_ 3GB (compressed)                                                   |                                                |
| Medicare Part-B (2000-2013)          | `Data4_ <30 MB, CSV ('00-'09), Excel ('10-'13) files                      | n/a                                            |
| HiBench (each) - sort                | n/a                                                                       | HibenchSuite_                                  |
| HiBench (each) - wordcount           | n/a                                                                       | HibenchSuite_                                  |
| HiBench (each) - terasort            | n/a                                                                       | HibenchSuite_                                  |
| HiBench (each) - scan/join/aggregate | n/a                                                                       | HibenchSuite_                                  |
| HiBench (each) - pagerank            | n/a                                                                       | HibenchSuite_                                  |
| HiBench (each) - netchindexing       | n/a                                                                       | HibenchSuite_                                  |
| HiBench (each) - bayes               | n/a                                                                       | HibenchSuite_                                  |
| HiBench (each) - kmeans              | n/a                                                                       | HibenchSuite_                                  |
| HiBench (each) - dfsio               | n/a                                                                       | HibenchSuite_                                  |
| Movie Reviews using IPython          | Data from Rottentomatoes.com                                              | IPython1_                                      |
| Red Wine Quality using IPython       | REDWINE_                                                                  | IPython2_                                      |
| Airline Delays with Hadoop           | AIRLINE                                                                   | IPython3_                                      |
| BigBench                             | n/a                                                                       | BDBench_                                       |
| Genome sequence data                 | .cfa sample data (unstructured text file) ]   SANDDATA_                   | `*SAND*                                        |
| Category: Streaming Data Analytics   |                                                                           |                                                |
| Face Detection                       | Data2_ images from INRIA dataset (< 1GB)                                  | OpenCV (c++ library, possible python bindings) |
| Live Twitter Feed analysis           | Live Twitter feed                                                         |                                                |
| Drug-Drug interactions on Twitter    | Live Twitter Data                                                         | DRUG_                                          |




_Data1: http://www.census.gov/population/www/cen2010/glance/
_Data2: http://pascal.inrialpes.fr/data/human/
_Data3: http://snap.stanford.edu/data/web-Movies.html
_Data4: https://www.cms.gov/Research-Statistics-Data-and-Systems/Downloadable-Public-Use-Files/Part-B-National-Summary-Data-File/Overview.html
_HibenchSuite: https://github.com/intel-hadoop/HiBench>

_iPython1: http://nbviewer.ipython.org/github/cs109/content/blob/master/HW3_solutions.ipynb
_iPython2: http://nbviewer.ipython.org/github/cs109/2014/blob/master/homework-solutions/HW5-solutions.ipynb
_iPython3: http://nbviewer.ipython.org/github/ofermend/IPython-notebooks/blob/master/blog-part-1.ipynb
_BDBench: https://github.com/intel-hadoop/Big-Data-Benchmark-for-Big-Bench
_Drugs:  https://github.com/cloud-class-projects/drug-drug-interaction
_SAND: http://ccl.cse.nd.edu/software/sand/
_SANDDATA: http://ccl.cse.nd.edu/software/sand/
_REDWINE:  https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/
_AIRLINE:  http://stat-computing.org/dataexpo/2009/the-data.html



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

KALEIDOSCOPE_: http://hpc-abds.org/kaleidoscope
RECOMENDER_: http://bdaafall2015.readthedocs.org/en/latest/tp1-recommender.html#tp1-recommender


NIST Examples
----------------------------------------------------

-  **NIST**

   -  **NFIQ**: NIST Fingerprint Image Quality (NFIQ): Tabassi, Elham,
          C. Wilson, and C. Watson. "Nist fingerprint image
          quality."NIST Res. Rep. NISTIR7151 (2004).
          [`*pdf* <http://biometrics.nist.gov/cs_links/standard/archived/workshops/workshop1/presentations/Tabassi-Image-Quality.pdf>`__]

   -  **PCASYS**: Fingerprint Pattern Classification: Candela, G. T., et
          al. "PCASYS-A pattern-level classification automation system
          for fingerprints." *NIST technical report NISTIR* 5647 (1995).
          [`*pdf* <http://www.nist.gov/manuscript-publication-search.cfm?pub_id=900754>`__]

   -  MINDTCT

   -  BOZORTH3

   -  NFSEG

   -  SIVV
          [`*pdf* <http://www.nist.gov/manuscript-publication-search.cfm?pub_id=903078>`__]

OLD
====

NIST Fingerprint
---------------------------------------------------------------------

A subset of:

* NFIQ: NIST Fingerprint Image Quality (NFIQ): Tabassi, Elham, C. Wilson, and C. Watson.
  "Nist fingerprint image quality."NIST Res. Rep. NISTIR7151 (2004)
  [pdf] - http://biometrics.nist.gov/cs_links/standard/archived/workshops/workshop1/presentations/Tabassi-Image-Quality.pdf
* PCASYS: Fingerprint Pattern Classification: Candela, G. T., et al. "PCASYS-A pattern-level
  classification automation system for fingerprints." NIST technical report NISTIR 5647 (1995).
  [pdf] - http://www.nist.gov/manuscript-publication-search.cfm?pub_id=900754
* MINDTCT
* BOZORTH3
* NFSEG
* SIVV [pdf] - http://www.nist.gov/manuscript-publication-search.cfm?pub_id=903078

Data Set:
  * NIST Special
  * Database 27A [4GB]
  * http://www.nist.gov/itl/iad/ig/sd27a.cfm

Software:
  * http://www.nist.gov/customcf/get_pdf.cfm?pub_id=51097

Category:
    Batch Data Analytics


HadoopBenchmark - TeraSort Suite
---------------------------------

Data Set:
    Teragen

Software:
    hadoop-examples.jar

Category:
    Batch Data Analytics        |


Hadoopbenchmark DFS10 (HDF Performance)
----------------------------------------------------------------------

Data Set:
    N/A

Software:
    hadoop-mapreduce-job client

Category:
    Batch Data Analytics


HadoopBenchmark - NNBench NameNodeperformance
----------------------------------------------------------------------

Data Set:
    N/A

Software:
    hadoop-mapreduce-job client

Category:
    Batch Data Analytics



HadoopBenchmark - NNBench NameNodeperformance
----------------------------------------------------------------------

Data Set:
    N/A

Software:
    src/test/org/apache/hadoop/mapred/MRBench.java

Category:
    Batch Data Analytics



Stock Data Analysis with MPI
----------------------------------------------------------------------

Data Set:
    CRSP - https://wrds-web.  wharton.upenn.edu/wrds/
    Ex : Tradingsymbol Price,# of Outstanding Factor to adjust Price, Share

Software:
    Stock Analysis - https://github.com/iotcloud/stock-analysis

Category:
    Streaming Data Analytics



Other Possible Projects
------------------------

* These are projects for which there may be tentative, or no, direct support on FutureSystems resources.

Census
---------------------------------------------------------------------

Data Set:
      Data: csv files downloadable (click "Internet tables" to select subsets)

Software:
      n/a

Category:
      Batch Data Analytics

Face Detection
---------------------------------------------------------------------

Data Set:
      Data: images from INRIA dataset (< 1GB)

Software:
      OpenCV (c++ library, possible python bindings)

Category:
      Streaming Data Analytics

Amazon Movie Reviews (1997-2012)
---------------------------------------------------------------------

Data Set:
      Data: 3GB (compressed)

Software:
      n/a

Category:
      Batch Data Analytics

Live Twitter Feed Analysis
---------------------------------------------------------------------

Title:
      Live Twitter Feed Analysis

Data Set:
      Live Twitter feed

Software:
      n/a

Category:
      Streaming Data Analytics

Medicare Part-B (2000-2013)
---------------------------------------------------------------------

Title:
      Medicare Part-B (2000-2013)

Data Set:
      Data: <30 MB, CSV ('00-'09), Excel ('10-'13) files

Software:
      n/a

Category:
      Batch Data Analytics

HiBench (each) - Sort
---------------------------------------------------------------------

Title:
      HiBench (each) - sort

Data Set:
      n/a

Software:
      Hibench Suite -

Category:
      Batch Data Analytics

HiBench (each) - WordCount
---------------------------------------------------------------------

Title:
      HiBench (each) - wordcount

Data Set:
      n/a

Software:
      Hibench Suite -

Category:
      Batch Data Analytics

HiBench (each) - TeraSort
---------------------------------------------------------------------

Title:
      HiBench (each) - terasort

Data Set:
      n/a

Software:
      Hibench Suite -

Category:
      Batch Data Analytics

HiBench (each) - Scan/Join/Aggregate
---------------------------------------------------------------------

Title:
      HiBench (each) - scan/join/aggregate

Data Set:
      n/a

Software:
      Hibench Suite -

Category:
      Batch Data Analytics

HiBench (each) - PageRank
---------------------------------------------------------------------

Title:
      HiBench (each) - pagerank

Data Set:
      n/a

Software:
      Hibench Suite -

Category:
      Batch Data Analytics

HiBench (each) - NetchIndexing
---------------------------------------------------------------------

Title:
      HiBench (each) - netchindexing

Data Set:
      n/a

Software:
      Hibench Suite -

Category:
      Batch Data Analytics

HiBench (each) - Bayes
---------------------------------------------------------------------

Title:
      HiBench (each) - bayes

Data Set:
      n/a

Software:
      Hibench Suite -

Category:
      Batch Data Analytics

HiBench (each) - Kmeans
---------------------------------------------------------------------

Title:
      HiBench (each) - kmeans

Data Set:
      n/a

Software:
      Hibench Suite -

Category:
      Batch Data Analytics

HiBench (each) - DFSIO
---------------------------------------------------------------------

Title:
      HiBench (each) - dfsio

Data Set:
      n/a

Software:
      Hibench Suite -

Category:
      Batch Data Analytics

Movie Reviews using IPython
---------------------------------------------------------------------

Title:
      Movie Reviews using IPython

Data Set:
      Data from Rottentomatoes.com

Software:
      IPython Notebook 1

Category:
      Batch Data Analytics

Red Wine Quality using IPython
---------------------------------------------------------------------

Title:
      Red Wine Quality using IPython

Data Set:
      UCI’s Red Wine Data

Software:
      IPython Notebook 2

Category:
      Batch Data Analytics

Airline Delays with Hadoop
---------------------------------------------------------------------

Title:
      Airline Delays with Hadoop

Data Set:
      Airline Delay Dataset 2007, 2008

Software:
      IPython Notebook 3

Category:
      Batch Data Analytics

BigBench
---------------------------------------------------------------------

Title:
      BigBench

Data Set:
      n/a

Software:
      Big Data Benchmark for BigBench

Category:
      Batch Data Analytics

Drug-Drug interactions on Twitter
---------------------------------------------------------------------

Title:
      Drug-Drug interactions on Twitter

Data Set:
      Live Twitter Data

Software:
      drug-drug-interaction

Category:
      Streaming Data Analytics

Genome Sequence Data
---------------------------------------------------------------------

Title:
      Genome sequence data

Data Set:
      .cfa sample data (unstructured text file) [link]

Software:
      SAND

Category:
      Batch Data Analytics


Your Own Projects
------------------

You have an option to create your own project with your idea. You can
use Python, Java, R, or other languages that you prefer. The size or
the domain of your datasets is open as long as they can be handled and
reproduced by course instructors.


Non-Software Projects
----------------------

If you have selected non-software projects, you or your team can
develop your project without software development or applications. Use
examples given below to choose a project. You can follow one of these
examples or choose your own.

Survey HPC-ABDS
---------------------------------------------------------------------

Title:
      Survey HPC-ABDS

Description:
     Several topics such as review level 17 (orchestration), Compare level 6 (DevOps)
     and level 15B (PaaS Frameworks) and level 17

Reference:
     http://hpc-abds.org/kaleidoscope/

Review of Recommender Systems: Technology & Applications
---------------------------------------------------------------------

Title:
     Review of Recommender Systems: Technology & Applications

Description:
     Define classification of information filtering system with current technologies
     and applications

Review of Big Data in BioInformatics
---------------------------------------------------------------------
Title:
     Review of Big Data in BioInformatics

Description:
     Find current challenges and understand state of bioinformatics solutions for big
     data including analytics, security and privacy.


Review of Data Visualization including High Dimensional Data
---------------------------------------------------------------------

Title:
     Review of Data Visualization including High Dimensional Data

Description:
     Explore data mining methods for knowledge  discovery with data visualization tools.
     Example : D3.js, matplotlib

Design of NoSQL database for a specialized application
---------------------------------------------------------------------

Title:
     Design of NoSQL database for a specialized application

Description:
     Explore design of databases for big data including HBase, MongoDB, etc.



