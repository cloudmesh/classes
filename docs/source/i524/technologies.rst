
.. index:: I524 technologies

Technologies
======================================================================


In this section we find a number of technologies that are related to
big data. Certainly a number of these projects are hosted as an Apache
project. One important resource for a general list of all apache
projects is at


* Apache projects: https://projects.apache.org/projects.html?category


Workflow-Orchestration
----------------------------------------------------------------------

1. ODE
2. ActiveBPEL
   S17-IR-2002
3. Airavata
4. Pegasus
5. Kepler
6. Swift
7. Taverna

   Taverna is workflow management system. According to
   :cite:`www-taverna`, Taverna is transitioning to Apache Incubator
   as of Jan 2017.  Taverna suite includes 2 products:

   (1). Taverna Workbench is desktop client where user can define the workflow.
   (2). Taverna Server is responsible for executing the remote workflows.

   Taverna workflows can also be executed on command-line.  Taverna
   supports wide range of services including WSDL-style and RESTful
   Web Services, BioMart, SoapLab, R, and Excel. Taverna also support
   mechanism to monitor the running workflows using its web browser
   interface.  In his :cite:`taverna-paper` paper, Daniele Turi
   presented the formal syntax and operational semantics of Taverna.

8. Triana
9. Trident

   In :cite:`www-trident-tutorial`, it is explained that Apache Trident 
   is a "high-level abstraction for doing realtime computing on top of 
   [Apache] Storm." Similarly to Apache Storm, Apache Trident was 
   developed by Twitter. Furthermore, :cite:`www-trident-tutorial` 
   introduces Trident as a tool that "allows you to seamlessly intermix 
   high throughput (millions of messages per second), stateful stream 
   processing with low latency distributed querying." In 
   :cite:`www-trident-overview`, the five kinds of operations in 
   Trident are described as "Operations that apply locally to each 
   partition and cause no network transfer", "repartitioning operations 
   that repartition a stream but otherwise don't change the contents 
   (involves network transfer)", "aggregation operations that do 
   network transfer as part of the operation", "operations on grouped 
   streams" and "merges and joins." In :cite:`www-trident-tutorial`, 
   these five kinds of operations (i.e. joins, aggregations, grouping, 
   functions, and filters) and the general concepts of Apache Trident 
   are described as similar to "high level batch processing tools like 
   Pig or Cascading."

10. BioKepler
11. Galaxy
12. IPython
13. Jupyter
14. (Dryad)
15. Naiad
16. Oozie
17. Tez
18. Google FlumeJava
19. Crunch

20. Cascading

    :cite:`www-cascading` Cascading software authored by Chris Wensel
    is development platform for building the application in Hadoop.
    It basically act as an abstraction for Apache Hadoop used for
    creating complex data processing workflow using the scalability of
    hadoop however hiding the complexity of mapReduce jobs.  User can
    write their program in java without having knowledge of
    mapReduce. Applications written on cascading are portable.
 
    Cascading Benefits
    1. With Cascading application can be scaled as per the data sets.
    2. Easily Portable
    3. Single jar file for application deployment.

21. Scalding
22. e-Science Central
23. Azure Data Factory
24. Google Cloud Dataflow
25. NiFi (NSA)
26. Jitterbit
27. Talend
28. Pentaho
29. Apatar
30. Docker Compose
31. KeystoneML


Application and Analytics
----------------------------------------------------------------------

32. Mahout :cite:`www-mahout`

    "Apache Mahout software provides three major features:
    (1) A simple and extensible programming environment and framework
    for building scalable algorithms
    (2) A wide variety of premade algorithms for Scala + Apache Spark,
    H2O, Apache Flink
    (3) Samsara, a vector math experimentation environment with R-like
    syntax which works at scale"


33. MLlib
34. Mbase
35. DataFu

    The Apache DataFu project was created out of the need for stable,
    well-tested libraries for large scale data processing in Hadoop.
    As detailed in :cite:`www-DataFu` Apache DatFu consists of two
    libraries Apache DataFu Pig and Apache DataFu Hourglass.  Apache
    DataFu Pig is a collection of useful user-defined functions for
    data analysis in Apache Pig. The functions are in areas of
    Statistics, Bag Operations, Set Operations, Sessions, Sampling,
    Estimation, Hashing and Link Analysis.  Apache DataFu Hourglass is
    a library for incrementally processing data using Hadoop
    MapReduce. It is designed to make computations over sliding windows
    more efficient. For these types of computations, the input data is
    partitioned in some way, usually according to time, and the range
    of input data to process is adjusted as new data arrives.
    Hourglass works with input data that is partitioned by day, as
    this is a common scheme for partitioning temporal data.

36. R
37. pbdR

    Programming with Big Data in R (pbdR) :cite:`www-pbdR` is an
    environment having series of R packages for statistical computing
    with Big Data using high-performance statistical computation. It
    uses R, a popular language between statisticians and data
    miners. "pbdR" focuses on distributed memory system, where data is
    distributed accross several machines and processed in batch
    mode. It uses MPI for inter process communications. R focuses on
    single machines for data analysis using a interactive
    GUI. Currenly there are two implementation of pbdR, one Rmpi and
    another being pdbMpi.  Rmpi uses SPMD parallelism while pbdRMpi
    uses manager/worker parallelism.

38. Bioconductor
39. ImageJ
40. OpenCV
41. Scalapack
42. PetSc
43. PLASMA MAGMA
44. Azure Machine Learning
    
    Azure Machine Learning is a cloud based service that can be used
    to do predictive analytics, machine learning or data mining. It
    has features like in-built algorithm library, machine learning
    studio and a webservice :cite:`www-azureMLSite`. In built
    algorithm library has implementation of various popular machine
    learning algorithms like decision tree, SVM, linear regression,
    neural networks etc. Machine learning studio facilitates creation
    of predictive models using graphical user interface by dragging,
    dropping and connecting of different modules that can be used by
    people with minimal knowledge in the machine learning
    field. Machine learning studio is a free service for basic version
    and comes with a monthly charge for advanced versions. Apart from
    building models, studio also has options to do preprocessing like
    clean, transform and normalize the data. Webservice provides
    option to deploy the machine learning algorithm as ready to
    consume APIs that can be reused in future with minimal effort and
    can also be published.
    
45. Google Prediction API & Translation API
46. mlpy
47. scikit-learn
48. PyBrain
49. CompLearn
50. DAAL(Intel)
51. Caffe
52. Torch
53. Theano
54. DL4j
55. H2O
56. IBM Watson
57. Oracle PGX
58. GraphLab

    :cite:`www- GraphLab` is a graph-based, distributed computation,
    high performance framework for machine learning written in C++. It
    is an open source project started by Prof. Carlos Guestrin of
    Carnegie Mellon University in 2009, designed considering the
    scale, variety and complexity of real world data. It integrates
    various high level algorithms such as Stochastic Gradient Descent,
    Gradient Descent & Locking and provides high performance
    experience. It includes scalable machine learning toolkits which
    has implementation for deep learning, factor machines, topic
    modeling, clustering, nearest neighbors and almost everything
    required to enhance machine learning models. This framework is
    targeted for sparse iterative graph algorithms. It helps data
    scientists and developers easily create and install applications
    at large scale.
    
59. GraphX
60. IBM System G
61. GraphBuilder(Intel)
62. TinkerPop
    
    ThinkerPop is a graph computing framework from Apache software
    foundation. :cite :`www-ApacheTinkerPop` Before coming under the
    Apache project, ThinkerPop was a stack of technologies like
    Blueprint, Pipes, Frames, Rexters, Furnace and Gremlin where each
    part was supporting graph-based application development. Now all
    parts are come under single TinkerPop project
    repo. :cite:`www-news` It uses Gremlin, a graph traversal machine
    and language. It allows user to write complex queries (traversal),
    that can use for real-time transactional (OLTP) queries, graph
    analytic system (OLAP) or combination of both as in
    hybrid. Gremlin is written in
    java. :cite:`www-ApacheTinkerPopHome` TinkerPop has an ability to
    create a graph in any size or complexity. Gremlin engine allows
    user to write graph traversal in Gremlin language, Python,
    JavaScript, Scala, Go, SQL and SPARQL. It is capable to adhere
    with small graph which requires a single machine or massive graphs
    that can only be possible with large cluster of machines, without
    changing the code.

63. Parasol
64. Dream:Lab

    DREAM:Lab stands for “Distributed Research on Emerging
    Applications and Machines Lab.” :cite:`dream` DREAM:Lab is centered
    around distributed systems research to enable expeditious
    utilization of distributed data and computing systems. :cite:`dream`
    DREAM:Lab utilizes the “capabilities of hundereds of personal
    computers” to allow access to supercomputing resources to average
    individuals. :cite:`rao` The DREAM:Lab pursues this goal by utilizing
    distributed computing. :cite:`rao` Distributed computing consists of
    independent computing resources that communicate with each other
    over a network. :cite:`denero` A large, complex computing problem is
    broken down into smaller, more manageable tasks and then these
    tasks are distributed to the various components of the distributed
    computing system. :cite:`denero`
    
65. Google Fusion Tables
    
    Fusion Tables is a cloud based services, provided by Google for
    data management and integration. Fusion Tables allow users to
    upload the data in tabular format using data files like
    spreadsheet, CSV, KML, .tsv up to
    250MB. :cite:`www-FusionTableSupport` It used for data management,
    visualizing data (e.g. pie-charts, bar-charts, lineplot,
    scatterplot, timelines) :cite:`wiki-FusionTable` , sharing of
    tables, filter and aggregation the data. It allows user to take
    the data privately, within controlled collaborative group or in
    public. It allows to integrate the data from different tables from
    different users or tables.Fusion Table uses two-layer storage,
    Bigtable and Magastore. The information rows are stored in bigdata
    table called “Rows”, user can merge the multiple table in to one,
    from multiple users. “Megastore is a library on top of
    bigtable”. :cite:`GoogleFusionTable2012` Data visualization is one
    the feature, where user can see the visual representation of their
    data as soon as they upload it. User can store the data along with
    geospatial information as well.

66. CINET
67. NWB
68. Elasticsearch
69. Kibana
70. Logstash
71. Graylog
72. Splunk
73. Tableau
74. D3.js
75. three.js
76. Potree
77. DC.js

    According to :cite:`www-dcjs`: “DC.js is a javascript charting
    library with native crossfilter support, allowing exploration on
    large multi-dimensional datasets. It uses d3 to render charts in
    CSS-friendly SVG format. Charts rendered using dc.js are data
    driven and reactive and therefore provide instant feedback to user
    interaction.” DC.js library can be used to perform data anlysis
    on both mobile devices and different browsers. Under the dc
    namespace the following chart classes are included: barChart,
    boxplot, bubbleChart, bubbleOverlay, compositeChart, dataCount,
    dataGrid, dataTable, geoChoroplethChart, heatMap,
    legend,lineChart, numberDisplay, pieChart, rowChart, scatterPlot,
    selectMenu and seriesChart.
      
78. TensorFlow
79. CNTK


Application Hosting Frameworks
----------------------------------------------------------------------

80. Google App Engine  :cite:`www-gae`

    On purpose we put in here a "good" example of a bad entry that woudl
    receive 10 out of 100 points, e.g. an F:

    "Google App Engine" provides platform as a service.
    There are major advantages from this framework:

    1. Scalable Applications
    2. Easier to maintain
    3. Publishing services easily

    Reasons: (a) "major advantages is advertisement" if you add word
    major (b) grammar needs to be improved (c) the three points do not
    realy say anything about Google App Engine (d) the reader will
    after reading this have not much information about what it is (e)
    a refernce is not included. (f) enumeration should be in this page
    avoided. We like to see a number of paragraphs with text.

    **Note: This is an example for a bad entry**

81. AppScale

    AppScale is an application hosting platform. This platform helps
    to deploy and scale the unmodified Google App Engine application,
    which run the application on any cloud infrastructure in public,
    private and on premise cluster. :cite:`www-AppScale` AppScale
    provide rapid, API development platform that can run on any cloud
    infrastructure. The platform separates the app logic and its
    service part to have control over application deployment, data
    storage, resource use, backup and migration.  AppScale is based on
    Google’s App Engine APIs and has support for Python, Go, PHP and
    Java applications. It supports single and multimode deployment,
    which will help with large, dataset or CPU. AppScale allows to
    deploy app in thee main mode i.e. dev/test, production and
    customize deployment.  :cite:`www-apscale-deployment`

82. Red Hat OpenShift
83. Heroku
84. Aerobatic

    According to :cite:`www-aero`: Aerobatic is a platform that allows
    hosting static websites. It used to be an ad-on for Bitbucket but
    now Aerobatic is transitioning to standalone CLI(command Line
    Tool) and web dashboard . Aerobatic allows automatic builds to
    different branches. New changes to websites can be deployed using
    aero deploy command which can be executed from local desktop or
    any of CD tools and services like Jenkins, Codeship,Travis and so
    on.  It also allows users to configure custom error pages and
    offers authentication which can also be customized. Aerobatic is
    backed by AWS cloud. Aerobatic has free plan and pro plan options
    for customers.
    

85. AWS Elastic Beanstalk
86. Azure

    Microsoft Corporation (MSFT) markets its cloud products under the
    *Azure* brand name. At its most basic, Azure acts as an
    *infrastructure- as-a-service* (IaaS) provider.  IaaS virtualizes
    hardware components, a key differentiation from other
    *-as-a-service* products. IaaS "abstract[s] the user from the
    details of infrasctructure like physical computing resources,
    location, data partitioning, scaling, security, backup, etc."
    :cite:`www-wikipedia-cloud`

    However, Azure offers a host of closely-related tool and products
    to enhance and improve the core product, such as raw block
    storage, load balancers, and IP addresses
    :cite:`www-azure-msft`. For instance, Azure users can access
    predictive analytics, Bots and Blockchain-as-a-Service
    :cite:`www-azure-msft` as well as more-basic computing,
    networking, storage, database and management components
    :cite:`www-sec-edgar-msft`.  The Azure website shows twelve major
    categories under *Products* and twenty *Solution* categories,
    e.g., e-commerce or Business SaaS apps.

    Azure competes against Amazon's *Amazon Web Service*,
    :cite:`www-aws-amzn` even though IBM (*SoftLayer*
    :cite:`www-softlayer-ibm` and *Bluemix* :cite:`www-bluemix-ibm`)
    and Google (*Google Cloud Platform*) :cite:`www-cloud-google`
    offer IaaS to the market.  As of January 2017, Azure's datacenters
    span 32 Microsoft-defined *regions*, or 38 *declared regions*,
    throughout the world. :cite:`www-azure-msft`

87. Cloud Foundry
88. Pivotal
89. IBM BlueMix
90. (Ninefold)

    The Australian based cloud computing platform has shut down their
    services since January 30, 2016. Refer :cite:`www-ninefoldSite`

91. Jelastic
92. Stackato
93. appfog

    According to :cite:`wee`, “AppFog is a platform as a service (PaaS)
    provider.” Platform as a service provides a platform for the
    development of web applications without the necessity of
    purchasing the software and infrastructure that supports
    it. :cite:`kepes` PaaS provides an environment for the creation of
    software. :cite:`kepes` The underlying support infrastructure that AppFog
    provides includes things such as runtime, middleware, o/s,
    virtualization, servers, storage, and networking. :cite:`appfog` AppFog
    is based on VMWare’s CloudFoundry project. :cite:`wee` It gets things
    such as MySQL, Mongo, Reddis, memCache, etc. running and then
    manages them. :cite:`tweney`
    
94. CloudBees
95. Engine Yard
96. (CloudControl)

    No Longer active as of Feb. 2016 :cite:`www-wiki`

97. dotCloud
98. Dokku
99. OSGi
100. HUBzero
101. OODT
102. Agave
103. Atmosphere


High level Programming
----------------------------------------------------------------------

104. Kite
105. Hive
106. HCatalog
107. Tajo
108. Shark
109. Phoenix

     In the first quarter of 2013, Salesforce.com released its
     proprietary SQL-like interface and query engine for HBase,
     *Phoenix*, to the open source community.  The company appears to
     have been motivated to develop Phoenix as a way to 1) increase
     accessiblity to HBase by using the industry-standard query
     language (SQL); 2) save users time by abstracting away the
     complexities of coding native HBase queries; and, 3) implementing
     query best practices by implementing them automatically via
     Phoenix. :cite:`www-phoenix-cloudera` Although Salesforce.com
     initially *open-sourced* it via Github, by May of 2014 it had
     become a top-level Apache project. :cite:`www-phoenix-wikipedia`

     Phoenix, written in Java, "compiles [SQL queries] into a series
     of HBase scans, and orchestrates the running of those scans to
     produce regular JDBC result sets." :cite:`www-apachephoenix-org`
     In addition, the program directs compute intense portions of the
     calls to the server.  For instance, if a user queried for the top
     ten records across numerous regions from an HBase database
     consisting of a billion records, the program would first select
     the top ten records for each region using server-side compute
     resources.  After that, the client would be tasked with selecting
     the overall top ten. :cite:`www-phoenix-salesforcedev`

     Despite adding an abstraction layer, Phoenix can actually speed
     up queries because it optimizes the query during the translation
     process. :cite:`www-phoenix-cloudera` For example, "Phoenix
     beats Hive for a simple query spanning 10M-100M rows."
     :cite:`www-phoenix-infoq`

     Finally, another program can enhance HBase's accessibility for
     those inclined towards graphical interfaces.  SQuirell only
     requires the user to set up the JDBC driver and specify the
     appropriate connection string. :cite:`www-phoenix-bighadoop`

110. Impala
111. MRQL

     MapReduce Query Language (MRQL, pronounced miracle) "is a query
     processing and optimization system for large-scale, distributed
     data analysis". :cite:`www-apachemrql` MRQL provides a SQL
     like language for use on Apache Hadoop, Hama, Spark, and Flink.
     MRQL allows users to perform complex data analysis using only SQL
     like queries, which are translated by MRQL to efficient Java
     code. :cite:`www-apachemrql`

     MRQL was created in 2011 by Leaonids
     Fegaras :cite:`www-mrqlhadoop` and is currently in the Apache
     Incubator.  All projects accepted by the Apache Software
     Foundation (ASF) undergo an incubation period until a review
     indicates that the project meets the standards of other ASF
     projects. :cite:`www-apacheincubator`

112. SAP HANA

     As noted in :cite:`www-sap-hana`, SAP HANA is in-memory massively
     distributed platform that consists of three components:
     analytics, relational ACID compliant database and
     application. Predictive analytics and machine learning
     capabilities are dynamically allocated for searching and
     processing of spatial, graphical, and text data. 
     SAP HANA accommodates flexible development and deployment of 
     data on premises, cloud and hybrid configurations.  In a 
     nutshell, SAP HANA acts as a warehouse that integrates live 
     transactional data from various data sources on a single 
     platform :cite:`olofson-2014`. It provides extensive 
     administrative, security features and data access that ensures 
     high data availability, data protection and data quality.
	 

113. HadoopDB
114. PolyBase
115. Pivotal HD/Hawq
116. Presto

     .. include:: techs/presto.rst

117. Google Dremel
118. Google BigQuery
119. Amazon Redshift
120. Drill
121. Kyoto Cabinet

     Kyoto Cabinet as specified in :cite:`www-KyotoCabinet` is a
     library of routines for managing a database which is a simple
     data file containing records. Each record in the database is a
     pair of a key and a value. Every key and value is serial bytes
     with variable length. Both binary data and character string can
     be used as a key and a value. Each key must be unique within a
     database.  There is neither concept of data tables nor data
     types. Records are organized in hash table or B+ tree. Kyoto
     Cabinet runs very fast. The elapsed time to store one million
     records is 0.9 seconds for hash database, and 1.1 seconds for B+
     tree database. Moreover, the size of database is very small. The,
     overhead for a record is 16 bytes for hash database, and 4 bytes
     for B+ tree database. Furthermore, scalability of Kyoto Cabinet
     is great. The database size can be up to 8EB (9.22e18 bytes).

122. Pig
123. Sawzall

     Google engineers created the domain-specific programming language
     (DSL) *Sawzall* as a productivity enhancement tool for Google
     employees.  They targeted the analysis of large data sets with
     flat, but regular, structures spread across numerous servers.
     The authors designed it to handle "simple, easily distributed
     computations: filtering, aggregation, extraction of statistics,"
     etc. from the aforementioned data sets.
     :cite:`google-sawzall`

     In general terms, a Sawzall job works as follows: multiple
     computers each create a Sawzall instance, perform some operation
     on a single record out of (potentially) petabytes of data, return
     the result to an aggregator function on a different computer and
     then shut down the Sawzall instance.

     The engineer's focus on simplicity and parallelization led to
     unconventional design choices.  For instance, in contrast to most
     programming languages Sawzall operates on one data record at a
     time; it does not even preserve state between records.
     :cite:`www-bytemining-sawzall` Addtionally, the language provides
     just a single primitive result function, the *emit* statement.
     The emitter returns a value from the Sawzall program to a
     designated virtual receptacle, generally some type of aggregator.
     In another example of pursuing language simplicity and
     parallelization, the aggregators remain separate from the formal
     Sawzall language (they are written in C++) because "some of the
     aggregation algorithms are sophisticated and best implemented in
     a native language [and] [m]ore important[ly] drawing an explicit
     line between filtering and aggregation enables a high degree of
     parallelism, even though it hides the parallelism from the
     language itself".  :cite:`google-sawzall`

     Important components of the Sawzall language include: *szl*, the
     binary containing the code compiler and byte-code interpreter
     that executes the program; the *libszl* library, which compiles
     and executes Sawzall programs "[w]hen szl is used as part of
     another program, e.g. in a [map-reduce] program"; the Sawzall
     language plugin, designated *protoc_gen_szl*, which generates
     Sawzall code when run in conjunction with Google's own *protoc*
     protocol compiler; and libraries for intrinsic functions as well
     as Sawzall's associated aggregation functionality.
     :cite:`www-google-code-wiki-sawzall`

124. Google Cloud DataFlow
125. Summingbird
126. Lumberyard

Streams
----------------------------------------------------------------------

127. Storm
128. S4
129. Samza
130. Granules
131. Neptune
132. Google MillWheel
133. Amazon Kinesis

     Kinesis is Amazon’s :cite:`www-kinesis` real time data processing
     engine. It is designed to provide scalable, durable and reliable
     data processing platform with low latency. The data to Kinesis
     can be ingested from multiple sources in different format. This
     data is further made available by Kinesis to multiple
     applications or consumers interested in the data. Kinesis
     provides robust and fault tolerant system to handle this high
     volume of data. Data sharding mechanism is Kinesis makes it
     horizontally scalable. Each of these shards in Kinesis process a
     group of records which are partitioned by the shard key. Each
     record processed by Kinesis is identified by sequence number,
     partition key and data blob. Sequence number to records is
     assigned by the stream. Partition keys are used by partitioner(a
     hash function) to map the records to the shards i.e. which
     records should go to which shard. Producers like web servers,
     client applications, logs push the data to Kinesis whereas
     Kinesis applications act as consumers of the data from Kinesis
     engine. It also provides data retention for certain time for
     example 24 hours default. This data retention window is a sliding
     window. Kinesis collects lot of metrics which can used to
     understand the amount of data being processed by Kinesis.  User
     can use this metrics to do some analytics and visualize the
     metrics data.  Kinesis is one of the tools part of AWS
     infrastructure and provides its users a complete
     software-as-a-service. Kinesis :cite:`big-data-analytics-book` in
     the area of real-time processing provides following key benefits:
     ease of use, parellel processing, scalable, cost effective, fault
     tolerant and highly available.

134. LinkedIn
135. Twitter Heron
136. Databus
137. Facebook Puma/Ptail/Scribe/ODS
138. Azure Stream Analytics
139. Floe
140. Spark Streaming
141. Flink Streaming
142. DataTurbine


Basic Programming model and runtime, SPMD, MapReduce
----------------------------------------------------------------------

143. Hadoop
144. Spark
145. Twister

146. MR-MPI

     :cite:`www-mapreducempi` MR-MPI stands for Map Reduce-Message
     Passing Interface is open source library build on top of standard
     MPI. It basically implements mapReduce operation providing a
     interface for user to simplify writing mapReduce program.  It is
     written in C++ and needs to be linked to MPI library in order to
     make the basic map reduce functionality to be executed in
     parallel on distributed memory architecture.  It provides
     interface for c, c++ and python. Using C interface the library
     can also be called from Fortrain.

147. Stratosphere (Apache Flink)
148. Reef
149. Disco
150. Hama
151. Giraph
152. Pregel
153. Pegasus
154. Ligra
155. GraphChi
156. Galois
     
     Galois system was built by intelligent software systems team at
     University of Texas, Austin. As explained in
     :cite:`www-galoisSite`, “Galois is a system that automatically
     executes 'Galoized' serial C++ or Java code in parallel on
     shared-memory machines. It works by exploiting amorphous
     data-parallelism, which is present even in irregular codes that
     are organized around pointer-based data structures such as graphs
     and trees”. By using Galois provided data structures programmers
     can write serial programs that gives the performance of parallel
     execution. Galois employs annotations at loop levels to
     understand correct context during concurrent execution and
     executes the code that could be run in parallel. The key idea
     behind Galois is Tao-analysis, in which parallelism is exploited
     at compile time rather than at run time by creating operators
     equivalent of the code by employing data driven local computation
     algorithm :cite:`taoParallelismPaper`. Galois currently supports
     C++ and Java.
	   
157. Medusa-GPU
158. MapGraph
159. Totem


Inter process communication Collectives
----------------------------------------------------------------------

160. point-to-point
161. publish-subscribe: MPI

162. HPX-5

     Based on :cite:`www-hpx-5`, High Performance ParallelX (HPX-5)
     is an open source, distributed model that provides opportunity
     for operations to run unmodified on one-to-many nodes. The
     dynamic nature of the model accommodates effective “computing
     resource management and task scheduling”. It is portable and
     performance-oriented. HPX-5 was developed by IU Center for
     Research in Extreme Scale Technologies (CREST). Concurrency is
     provided by lightweight control object (LCO) synchronization and
     asynchronous remote procedure calls. ParallelX component allows
     for termination detection and supplies per-process
     collectives. It “addresses the challenges of starvation, latency,
     overhead, waiting, energy and reliability”. Finally, it supports
     OpenCL to use distributed GPU and coprocessors. HPX-5 could be
     compiled on various OS platforms , however it was only tested on
     several Linux and Darwin (10.11) platforms. Required
     configurations and environments could be accessed via
     :cite:`www-hpx-5-user-guide`.
	 
	 
163. Argo BEAST HPX-5 BEAST PULSAR

     Search on the internet was not successsful.
     
164. Harp
165. Netty
166. ZeroMQ

     In :cite:`www-zeromq`, ZeroMQ is introduced as a software product 
     that can "connect your code in any language, on any platform" by 
     leveraging "smart patterns like pub-sub, push-pull, and 
     router-dealer" to carry "messages across inproc, IPC, TCP, TIPC, 
     [and] multicast." In :cite:`www-zeromq2`, it is explained that 
     ZeroMQ's "asynchronous I/O model" causes this "tiny library" to 
     be "fast enough to be the fabric for clustered products." In 
     :cite:`www-zeromq`, it is made clear that ZeroMQ is "backed by a 
     large and open source community" with "full commercial support." 
     In contrast to Message Passing Interface (i.e. MPI), which is 
     popular among parallel scientific applications, ZeroMQ is 
     designed as a fault tolerant method to communicate across highly 
     distributed systems. 

167. ActiveMQ
168. RabbitMQ

     RabbitMQ is a message broker :cite:`www-rabbitmq` which allows
     services to exchange messages in a fault tolerant manner. It
     provides variety of features which “enables software applications
     to connect and scale”. Features are: reliability, flexible
     routing, clustering, federation, highly available queues,
     multi-protocol, many clients, management UI, tracing, plugin
     system, commercial support, large community and user
     base. RabbitMQ can work in multiple scenarios:

     1. Simple messaging: producers write messages to the queue and
        consumers read messages from the the queue. This is synonymous
        to a simple message queue.

     2. Producer-consumer: Producers produce messages and consumers
        receive messages from the queue. The messages are delivered to
        multiple consumers in round robin manner.

     3. Publish-subscribe: Producers publish messages to exchanges
        and consumers subscribe to these exchanges. Consumers receive
        those messages when the messages are available in those
        exchanges.

     4. Routing: In this mode consumers can subscribe to a subset
        of messages instead of receiving all messages from the queue.

     5. Topics: Producers can produce messages to a topic multiple
        consumers registered to receive messages from those topics get
        those messages. These topics can be handled by a single
        exchange or multiple exchanges.

     6. RPC:In this mode the client sends messages as well as
        registers a callback message queue. The consumers consume the
        message and post the response message to the callback queue.

        RabbitMQ is based on AMPQ :cite:`ampq-article` (Advanced
        Message Queuing Protocol) messaging model. AMPQ is described
        as follows “messages are published to exchanges, which are
        often compared to post offices or mailboxes. Exchanges then
        distribute message copies to queues using rules called
        bindings. Then AMQP brokers either deliver messages to
        consumers subscribed to queues, or consumers fetch/pull
        messages from queues on demand”

169. NaradaBrokering
170. QPid
171. Kafka

     Apache Kafka is a streaming platform, which works based on
     publish-subscribe messaging system and supports distributed
     environment. Kafka lets publish and subscribe to the messages.

     In a publish-subscribe messaging system, publishers are sender of
     messages. They publish the messages without the knowledge of who
     is going to ‘subscribe’ to them for processing. Subscribers are
     users of these messages. They subscribe to only those messages
     which they are interested in, without knowing who the publishers
     are. Kafka maintains message feeds based on ‘topic’. A topic is a
     category or feed name to which records are
     published. Applications can use Kafka’s Connector APIs to publish
     the messages to one or more Kafka topics. Similarly, applications
     can use Consumer API to subscribe to one or more topics.
     Kafka has the capability to process the stream of data at real time.

     Kafka’s stream processor takes continual stream of data from
     input topics, processes the data in real time and produces
     streams of data to output topics. Kafka’s Streams API are used
     for data transformation. Kafka allows to store the stream of data
     in distributed clusters.

     Kafka acts as a storage system for incoming data stream. Data is
     categorised into ‘topics’. As Kafka is a distributed system, data
     streams are partitioned and replicated across nodes. Thus, a
     combination of messaging, storage and processing data stream
     makes Kafka a ‘streaming platform’.

     Kafka is a commonly used for building data pipelines where data is
     transferred between systems or applications. :cite:`www-kafka`
     Kafka can also be used by applications that transform real time
     incoming data.

172. Kestrel
173. JMS
174. AMQP

     :cite:`www-amqp` AMQP stands for Advanced Message Queueing
     Protocol. AMQP is open interenet protocol that allows secure and
     reliable communication between applications in different
     orginization and different applications which are on diffferent
     platforms. AMQP allows businesses to implement middleware
     applications interoperability by allowing secure message transfer
     bewteen the applications on timly manner. AMQP is mainly used by
     financial and banking business. Other sectors that aslo use AMQP
     are Defence, Telecommunication, cloud Computing and so on.
     Apache Qpid, StormMQ, RabbitMQ, MQlight, Microsoft's Windows
     Azure Service Bus, IIT Software's SwiftMQ and JORAM are some of
     the products that implement AMQP protocol.

175. Stomp
176. MQTT
     
     According to :cite:`www-mqtt`, Message Queueing Telemetry
     Transport (MQTT) protocol is an Interprocess communication
     protocol that could serve as better alternative to HTTP in
     certain cases. It is based on a publish-subscribe messaging
     pattern. Any sensor or remote machine can publish it's data and
     any registered client can subscribe the data. A broker takes care
     of the message being published by the remote machine and updates
     the subscriber in case of new message from the remote
     machine. The data is sent in binary format which makes it use
     less bandwidth. It is designed mainly to cater to the needs to
     devices that has access to minimal network bandwidth and device
     resources without affecting reliability and quality assurance of
     delivery. MQTT protocol has been in use since 1999. One of the
     notable work is project Floodnet :cite:`www-floodnet`, which
     monitors river and floodplains through a set of sensors.

177. Marionette Collective
178. Public Cloud: Amazon SNS
179. Lambda
180. Google Pub Sub
181. Azure Queues
182. Event Hubs

In-memory databases/caches
----------------------------------------------------------------------


183. Gora (general object from NoSQL)

     Gora is a in-memory data model :cite:`www-gora` which also
     provides persistence to the big data. Gora provides persistence
     to different types of data stores. Primary goals of Gora are:

     1. data persistence
     2. indexing
     3. data access
     4. analysis
     5. map reduce support

     Unlike ORM models which mostly work with relational databases for
     example hibernate gora works for most type of data stores like
     documents, columnar, key value as well as relational. Gora uses
     beans to maintain the data in-memory and persist it on
     disk. Beans are defined using apache avro schema. Gora provides
     modules for each type of data store it supports.  The mapping
     between bean definition and datastore is done in a mapping file
     which is specific to a data store.  Type Gora workflow will be:

     1. define  the bean used as model for persistence
     2. use gora compiler to compile the bean
     3. create a mapping file to map bean definition to datastore
     4. update gora.properties to specify the datastore to use
     5. get an instance of corresponding data store using datastore factory.

     Gora has a query interface to query the underlying data
     store. Its configuration is stored in gora.properties which
     should be present in classpath. In the file you can specify
     default data store used by Gora engine. Gora also has a CI/CD
     library call GoraCI which is used to write integration tests.

184. Memcached
185. Redis
186. LMDB (key value)
187. Hazelcast

     Hazelcast is a java based, in memory data grid. :cite:`www-wikihazel` 
     It is open source software, released under the Apache 2.0 License. 
     :cite:`www-githubhazel`  

     Hazelcast uses a grid to distribute data evenly across a cluster.  
     Clusters allow processing and storage to scale horizontally.  
     Hazelcast enables predictable scaling for applications by providing 
     in memory access to data. :cite:`www-wikihazel`

     Hazelcast can run locally, in the cloud, in virtual machines, or 
     in Docker containers. :cite:`www-wikihazel`

188. Ehcache

     EHCACHE is an open-source Java-based cache. It supports distributed
     caching and could scale to hundred of caches. It comes with REST APIs
     and could be integrated with popular frameworks like Hibernate
     :cite:`www-ehcache-features`. It offers storage tires such that less
     frequently data could be moved to slower tires
     :cite:`www-ehcache-documentation`. It's XA compliant and supports two-
     phase commit and recovery for transactions. It's developed and
     maintained by Terracotta and is available under Apache 2.0 license.
     It conforms to Java caching standard JSR 107. 

189. Infinispan
190. VoltDB
191. H-Store

     H-Store is an in memory and parallel database management system
     for on-line transaction processing (OLTP). Specifically ,
     :cite:`www-Hstore` illustrates that H-Store is a highly
     distributed, row-store-based relational database that runs on a
     cluster on shared-nothing, main memory executor nodes.As Noted in
     :cite:`kallman2008` "the architectural and application shifts
     have resulted in modern OLTP databases increasingly falling short
     of optimal performance.In particular, the availability of
     multiple-cores, the abundance of main memory, the lack of user
     stalls, and the dominant use of stored procedures are factors
     that portend a clean-slate redesign of RDBMSs".The H-store which
     is a complete redesign has the potential to outperform legacy
     OLTP databases by a significant factor.  As detailed in
     :cite:`www-Hstorewiki` H-Store is the first implementation of a
     new class of parallel DBMS, called NewSQL, that provides the
     high-throughput and high-availability of NoSQL systems, but
     without giving up the transactional guarantees of a traditional
     DBMS.  The H-Store system is able to scale out horizontally
     across multiple machines to improve throughput, as opposed to
     moving to a more powerful , more expensive machine for a
     single-node system.

Object-relational mapping
----------------------------------------------------------------------

192. Hibernate
193. OpenJPA
194. EclipseLink
195. DataNucleus
196. ODBC/JDBC


Extraction Tools
----------------------------------------------------------------------

197. UIMA

381. Tika

     "The Apache Tika toolkit detects and extracts metadata and text
     from over a thousand different file types (such as PPT, XLS, and
     PDF). All of these file types can be parsed through a single
     interface, making Tika useful for search engine indexing, content
     analysis, translation, and much more. :cite:`www-tika`"


SQL(NewSQL)
----------------------------------------------------------------------

198. Oracle
199. DB2
200. SQL Server

     SQL Server :cite:`www-sqlserver-wiki` is a relational database
     management system from Microsoft. As of Jan 2017, SQL Server is
     available in below editions

     1. Standard - consists of core database engine
     2. Web - low cost edition for web hosting
     3. Business Intelligence - includes standard edition and business
        intelligence tools like PowerPivot, PowerBI, Master Data Services
     4. Enterprise - consists of core database engine and enterprise services
        like cluster manager
     5. SQL Server Azure - :cite:`www-azuresql` core database engine
        integrated with Microsoft Azure cloud platform and available in
        platform-as-a-service mode.

     It is explained that technical architecture of SQL Server in
     OLTP(online transaction processing), hybrid cloud and business
     intelligence modes :cite:`book-sqlserver`.



201. SQLite
202. MySQL

     MySQL is a relational database management system. :cite:`devmysql` SQL
     is an acronym for Structured Query Language and is a standardized
     language used to interact with the databases. :cite:`devmysql`
     Databases provide structure to a collection of data
     while. :cite:`devmysql` A database management system allows for the
     addition, accessing, and processing of the data stored in a
     database. :cite:`devmysql` Relational databases utilize tables that are
     broken down into columns, representing the various fields of the
     table, and rows, which correspond to individual entries in the
     table. :cite:`howmysql`
     
203. PostgreSQL

204. CUBRID

     CUBRID name is deduced from the combination of word CUBE(security
     within box) and BRIDGE(data bridge).  It is an open source
     Relational DataBase Management System designed in C programming
     language with high performance, scalability and availability
     features. During its development by NCL, korean IT service
     provider the goal was to optimize database performance for
     web-applications. :cite:`www-cubrid` Importantly most of the SQL
     syntax from MYSQL and ORACLE can work on cubrid.CUBRID also
     provides manager tool for database administration and migration
     tool for migrating the data from DBMS to CUBRID bridging the dbs.
     CUBRID enterprise version and all the tools are free and suitable
     database candidate for web-application development.

205. Galera Cluster

     Galera cluster :cite:`www-galera-cluster` is a type of database
     clustering which has all multiple masters and works on
     synchronous replication. At a deeper level, it was created by
     extending MySql replication API to provide all support for true
     multi master synchronous replication.  This extended api is
     called as Write-Set Replication API and is the core of the
     clustering logic.  Each transaction of wsrep API not only
     contains the record but also other meta-info to requires to
     commit each node separately or asynchronously. So though it seems
     synchronous logically but works independently on each node.  The
     approach is also called virtually synchronous replication. This
     helps in directly read-write on a specific node and can lose a
     node without handling any complex failover scenarios (zero
     downtime).

206. SciDB
207. Rasdaman
208. Apache Derby
209. Pivotal Greenplum
210. Google Cloud SQL
211. Azure SQL
212. Amazon RDS
213. Google F1
214. IBM dashDB
215. N1QL
216. BlinkDB
217. Spark SQL

NoSQL
----------------------------------------------------------------------

218. Lucene

     Apache Lucene :cite:`www-lucene` is a high-performance,
     full-featured text search engine library.  It is originally
     written in pure Java but also has been ported to few other
     languages chiefly python.  It is suitable for applications that
     requires full-text search.  One of the key implementation of
     Lucene is Internet search engines and local, single-site
     searching.  Another important implementation usage is its
     recomendation system. The core idea of Lucene is to extract text
     from any document that contains text (not image) field, making it
     format idependent.

219. Solr
220. Solandra
221. Voldemort

     According to :cite:`www-voldemort`, project Voldemort, developed
     by LinkedIn, is a non-relational database of key-value type that
     supports eventual consistency. The distributed nature of the
     system allows pluggable data placement and provides horizontal
     scalability and high consistency. Replication and partitioning of
     data is automatic and performed on multiple servers. Independent
     nodes that comprise the server support transparent handling of
     server failure and ensure absence of a central point of
     failure. Essentially, Voldemort is a hashtable. It uses APIs for
     data replication. In memory caching allows for faster
     operations. It allows cluster expansion with no data rebalancing.
     When Voldemort performance was benchmarked with the other
     key-value databases such as Cassandra, Redis and HBase as well as
     MySQL relational database :cite:`rabl-sadoghi-jacobsen-2012`, the
     Voldemart's throughput was twice lower than MySQL and Cassandra
     and six times higher than HBase. Voldemort was slightly
     underperforming in comparison with Redis. At the same time, it
     demonstrated consistent linear performance in maximum throughput
     that supports high scalability. The read latency for Voldemort
     was fairly consistent and only slightly underperformed
     Redis. Similar tendency was observed with the read latency that
     puts Voldermort in the cluster of databases that require good
     read-write speed for workload operations. However, the same
     authors noted that Voldemort required creation of the node
     specific configuration and optimization in order to successfully
     run a high throughput tests. The default options were not
     sufficient and were quickly saturated that stall the database.
     
222. Riak

     Riak is a set of scalable distributed NoSQL databases developed by
     Basho Technologies. Riak KV is a key-value :cite:`www-riak-kv` database
     with time-to-live feature so that older data is deleted automatically.
     It can be queried through secondary indexes, search via Apache Solr,
     and MapReduce. Riak TS is designed for time-series data. It co-
     locates related data on the same physical cluster for faster access
     :cite:`www-riak-ts`. Riak S2 is designed to store large objects like media
     files and software binaries :cite:`www-riak-s2`. The databases are available
     in both open source and commercial versions with multicluster
     replication provided only in later. REST APIs are available for these
     databases.

223. ZHT

     According to :cite:`datasys`, “ZHT is a zero-hop distributed hash
     table.” Distributed hash tables effectively break a hash table up
     and assign different nodes responsibility for managing different
     pieces of the larger hash table. :cite:`wiley` To retrieve a value in a
     distributed hash table, one needs to find the node that is
     responsible for the managing the key value pair of
     interest. :cite:`wiley` In general, every node that is a part of the
     distributed hash table has a reference to the closest two nodes
     in the node list. :cite:`wiley` In a ZHT, however, every node contains
     information concerning the location of every other node. :cite:`Li`
     Through this approach, ZHT aims to provide “high availability,
     good fault tolerance, high throughput, and low latencies, at
     extreme scales of millions of nodes.” :cite:`Li` Some of the defining
     characteristics of ZHT are that it is light-weight, allows nodes
     to join and leave dynamically, and utilizes replication to obtain
     fault tolerance among others. :cite:`Li`
     
224. Berkeley DB
225. Kyoto/Tokyo Cabinet
226. Tycoon
227. Tyrant

     Tyrant provides network interfaces to the database management
     system called Tokyo Cabinet. Tyrant is also called as Tokyo
     Tyrant. Tyrant is implemented in C and it provides APIs for Perl,
     Ruby and C. Tyrant provides high performance and concurrent
     access to Tokyo Cabinet. In his blog :cite:`www-tyrant-blog` Matt
     Yonkovit has explained the results of performance experiments he
     conducted to compare Tyrant against Memcached and MySQL.

     Tyrant was written and maintained by FAL Labs
     :cite:`www-tyrant-fal-labs`.  However, according to FAL Labs,
     their latest product :cite:`www-kyoto-tycoon` Kyoto Tycoon is
     more powerful and convenient server than Tokyo Tyrant.


228. MongoDB
229. Espresso
230. CouchDB
231. Couchbase

     Couchbase, Inc. offers Couchbase Server (CBS) to the marketplace
     as a NoSQL, document-oriented database alternative to traditional
     relationship- oriented database managgement systems as well as
     other NoSQL competitors.  The basic storage unit, a *document*,
     is a "data structure defined as a collection of named fields".
     The document utilizes JSON, thereby allowing each document to
     have its own individual schema. :cite:`www-infoworld-cbs`

     CBS combines the in-memory capabilities of Membase with CouchDB's
     inherent data store reliability and data persistency.  Membase
     functions in RAM only, providing the highest-possible speed
     capabilities to end users.  However, Membase's in-ram existence
     limits the amount of data it can use.  More importantly, it
     provides no mechanism for data recovery if the server crashes.
     Combining Membase with CouchDB provides a persistent data source,
     mitigating the disadvantages of either product.  In addition,
     CouchDB + membase allows the data size "to grow beyond the size
     of RAM".  :cite:`www-safaribooks-cbs`

     CBS is written in Erlang/OTP, but generally shortened to just
     Erlang.  In actuality, t is written in "Erlang using components
     of OTP alongside some C/C++":cite:`www-erlangcentral-cbs`, It
     runs on an Erlang virtual machine known as
     BEAM. :cite:`www-wikipedia-erlang-cbs`

     Out-of-the-box benefits of Erlang/OTP include dynamic type
     setting, pattern matching and, most importantly, actor-model
     concurrency.  As a result, Erlang code virtually eliminates the
     possibility of inadvertent deadlock scenarios.  In addition,
     Erlang/OTP processes are lightweight, spawning new processes does
     not consume many resources and message passing between processes
     is fast since they run in the same memory space.  Finally, OTP's
     process supervision tree makes Erlang/OTP extremely
     fault-tolerant.  Error handling is indistinguishable from a
     process startup, easing testing and bug detection.
     :cite:`www-couchbase-blog-cbs`

     CouchDB's design adds another layer of reliability to CBS.
     CouchDB operates in *append-only* mode, so it adds user changes
     to the tail of database.  This setup resists data corruption
     while taking a snapshot, even if the server continues to run
     during the procedure.  :cite:`www-hightower-cbs`

     Finally, CB uses the Apache 2.0 License, one of several
     open-source license alternatives. :cite:`www-quora-cbs`

232. IBM Cloudant
233. Pivotal Gemfire
234. HBase
235. Google Bigtable

     Google Bigtable is a NoSQL database service, built upon several
     Google technologies, including Google File System, Chubby Lock
     Service, and SSTable.  Designed for Big Data, Bigtable provides
     high performance and low latency and scales to hundreds of
     petabytes.  :cite:`www-cloudbigtable` Bigtable powers many core
     Google products, such as Search, Analytics, Maps, Earth, Gmail,
     and YouTube.  :cite:`www-wikibigtable` Since May 6, 2015, a
     version of Bigtable has been available to the public.  Bigtable
     also drives Google Cloud Datastore :cite:`www-wikibigtable` and
     Spanner, a distributed NewSQL also developed by
     Google. :cite:`www-wikispanner`

236. LevelDB
237. Megastore and Spanner

     Spanner :cite:`corbett-spanner` is Google's distributed database
     which is used for managing all google services like play, gmail,
     photos, picasa, app engine etc Spanner is distributed database
     which spans across multiple clusters, datacenters and geo
     locations.  Spanner is structured in such a way so as to provide
     non blocking reads, lock free transactions and atomic schema
     modification. This is unlike other noSql databases which follow
     the CAP theory i.e. you can choose any two of the three:
     Consistency, Availability and Partition-tolerance. However,
     spanner gives an edge by satisfying all three of these. It gives
     you atomicity and consistency along with availability, partition
     tolerance and synchronized replication.  Megastore bridges the
     gaps found in google's bigtable. As google realized that it is
     difficult to use bigtable where the application requires
     constantly changing schema. Megastore offers a solution in terms
     of semi-relational data model.  Megastore
     :cite:`www-magastore-spanner` also provides a transactional
     database which can scale unlike relational data stores and
     synchronous replication.  Replication in megastore is supported
     using Paxos. Megastore also provides versioning. However,
     megastore has a poor write performance and lack of a SQL like
     query language. Spanners basically adds what was missing in
     Bigtable and megastore. As a global distributed database spanner
     provides replication and globally consistent reads and
     writes. Spanner deployment is called universe which is a
     collections of zones. These zones are managed by singleton
     universe master and placement driver. Replication in spanner is
     supported by Paxos state machine. Spanner was put into evaluation
     in early 2011 as F1 backend(F1 is Google's advertisement system)
     which was replacement to mysql. Overall spanner fulfils the needs
     of relational database along with scaling of noSQL database.  All
     these features make google run all their apps seamlessly on
     spanner infrastructure.

238. Accumulo
239. Cassandra

     Apache Cassandra :cite:`www-cassandra` is an open-source
     distributed database managemment for handling large volume of
     data accross comodity servers. It works on asynchronous
     masterless replication technique leading to low latency and high
     availability. It is a hybrid between a key-value and column
     oriented database. A table in cassandra can be viewed as a multi
     dimensional map indexed by a key. It has its own "Cassandra Query
     language (CQL)" query language for data extraction and
     mining. One of the demerits of such structure is it does not
     support joins or subqueries. It is a java based system which can
     be administered by any JMX compliant tools.

240. RYA

     Rya is a “scalable system for storing and retrieving RDF data in
     a cluster of nodes.” :cite:`Punnoose` RDF stands for Resource
     Description Framework. :cite:`Punnoose` RDF is a model that facilitates
     the exchange of data on a network. :cite:`w3` RDF utilizes a form
     commonly referred to as a triple, an object that consists of a
     subject, predicate, and object. :cite:`Punnoose` These triples are used
     to describe resources on the Internet. :cite:`Punnoose` Through new
     storage and querying techniques, Rya aims to make accessing RDF
     data fast and easy. :cite:`apacherya`
     
241. Sqrrl
242. Neo4J
243. graphdb
244. Yarcdata
245. AllegroGraph
246. Blazegraph
247. Facebook Tao
248. Titan:db
249. Jena
250. Sesame
251. Public Cloud: Azure Table

     Microsoft offers its NoSQL Azure Table product to the market as a
     low-cost, fast and scalable data storage
     option. :cite:`www-what-to-use` Table stores data as collections
     of key-value combinations, which it terms *properties*.  Table
     refers to a collection of properties as an *entity*.  Each entity
     can contain a mix of properties.  The mix of properties can vary
     between each entity, although each entity may consist of no more
     than 255 properties. :cite:`www-blobqueuetable`

     Although data in Azure Table will be structured via key-value
     pairs, Table provides just one mechanism for the user to define
     relationships between entities: the entity's *primary key*.  The
     primary key, which Microsoft sometimes calls a *clustered index*,
     consists of a PartitionKey and a RowKey.  The PartitionKey
     indicates the group, a.k.a partition, to which the user assigned
     the entity.  The RowKey indicates the entity's relative position
     in the group.  Table sorts in ascending order by the PartitionKey
     first, then by the RowKey using lexical comparisons.  As a
     result, numeric sorting requires fixed-length, zero-padded
     strings.  For instance, Table sorts *111* before *2*, but will
     sort *111* after *002*. :cite:`www-scalable-partitioning`

     Azure Table is considered best-suited for infrequently accessed
     data storage.

252. Amazon Dynamo
253. Google DataStore

File management
----------------------------------------------------------------------

254. iRODS
255. NetCDF
256. CDF
257. HDF
258. OPeNDAP
259. FITS

     FITS stand for 'Flexible Image Trasnport System'. It is a
     standard data format used in astronomy. FITS data format is
     endorsed by NASA and International Astronomical Union. According
     to :cite:`www-fits-nasa`, FITS can be used for transport,
     analysis and archival storage of scientific datasets and support
     multi-dimensional arrays, tables and headers sections.  FITS is
     actively used and developed - according to
     :cite:`www-news-fits-2016` newer version of FITS standard
     document was released in July 2016. FITS can be used for
     digitization of contents like books and
     magzines. :cite:`www-fits-vatican-library` used FITS for long
     term preservation of their book, manuscripts and other
     collection. Matlab, a language used for technical computing
     supports fits :cite:`www-fits-matlab`. In his 2011 paper, Keith
     Wiley :cite:`paper-fits-2011` explained how they performed
     processing of astronomical images on Hadoop. They used FITS
     format for data storage.

260. RCFile
261. ORC
262. Parquet

Data Transport
----------------------------------------------------------------------

263. BitTorrent

     Bittorrent is P2P communication protocol commonly used for
     sending and receiving the large digital files like movies and
     audioclips.In order to upload and download file, user have to
     download bittorrent client which implement the bittorrent
     protocol. Bittorrent uses the principle of swarning and
     tracking. :cite:`www-bittorrent` It divides the files in large
     number of chunck and as soon as file is received it can be server
     to the other users for downloading.  So rather than downloading
     one entire large file from one source, user can download small
     chunk from the different sources of linked users in
     swarn. Bittorrent trackers keeps list of files available for
     transfer and helps the swarn user find each other.

     Using the protocol, machine with less configuration can serve as
     server for distributing the files. It result in increase in the
     downloading speed and reduction in origin server configuration.

     Few popular bittorrent client in μTorrent, qBittorrent.

264. HTTP
265. FTP
266. SSH

     SSH is a cryptographic network protocol :cite:`www-ssh-wiki` to
     provide a secure channel between two clients over an unsecured
     network. It uses public-key cryptography for authenticating the
     remote machine and the user. The public-private key pairs could
     be generated automatically to encrypt the network connection.
     ssh-keygen utility could be used to generate the keys manually.
     The public key then could be placed on the all the computers to
     which the access is required by the owner of the private key.
     SSH runs on the client-server model where a server listens for
     incoming ssh connection requests. It's generally used for remote
     login and command execution. It's other important uses include
     tunneling(required in cloud computing) and file transfer(SFTP).
     OpenSSH is an open source implementation of network utilities
     based on SSH :cite:`www-openssh-wiki`.

267. Globus Online (GridFTP)

     GridFTP is a enhancement on the File Tranfer Protocol (FTP) which
     provides high-performance , secure and reliable data transfer for
     high-bandwidth wide-area networks. As noted in
     :cite:`www-GlobusOnline` the most widely used implementation of
     GridFTP is Globus Online. GridFTP achieves efficient use of
     bandwidth by using multiple simultaneous TCP streams.  Files can
     be downloaded in pieces simultaneously from multiple sources; or
     even in separate parallel streams from the same source. GridFTP
     allows transfers to be restarted automatically and handles
     network unavailability with a fault tolerant implementation of
     FTP.The underlying TCP connection in FTP has numerous settings
     such as window size and buffer size. GridFTP allows automatic (or
     manual) negotiation of these settings to provide optimal transfer
     speeds and reliability .


268. Flume

     Flume is distributed, reliable and available service for
     efficiently collecting, aggregating and moving large amounts of
     log data :cite:`apche-flume. Flume was created to allow you to
     flow data from a source into your Hadoop® environment.  In Flume,
     the entities you work with are called sources, decorators, and
     sinks. A source can be any data source, and Flume has many
     predefined source adapters. A sink is the target of a specific
     operation. A decorator is an operation on the stream that can
     transform the stream in some manner, which could be to compress
     or uncompress data, modify data by adding or removing pieces of
     information, and more :cite: `ibm-flume`.

269. Sqoop
     
     Apache Sqoop is a tool to transfer large amounts of data between Apache Hadoop
     and sql databases :cite:`www-sqoop`. The name is a Portmanteau of
     SQL + Hadoop. It is a command line interface application which
     supports incremental loads of complete tables, free form (custom)
     SQL Queries and allows the use of saved and scheduled jobs to import
     latest updates made since the last import. The imports can also be
     used to populate tables in Hive or Hbase. Sqoop has the option of
     export, which allows data to be transferred from Hadoop into a
     relational database. Sqoop is supported in many different business
     integration suits like Informatica Big Data Management, Pentaho
     Data Integration, Microsoft BI Suite and Couchbase :cite:`sqoop-wiki`. 

270. Pivotal GPLOAD/GPFDIST

Cluster Resource Management
----------------------------------------------------------------------

271. Mesos

272. Yarn

     Yarn (Yet Another Resource Negotiator) is Apache Hadoop’s cluster
     management project :cite:`www-cloudera` . It’s a resource
     management technology which make a pace between, the way
     applications use Hadoop system resources & node manager
     agents. Yarn, “split up the functionalities of resource
     management and job scheduling/monitoring”. The NodeManager watch
     the resource (cpu, memory, disk,network) usage the container and
     report the same to ResourceManager. Resource manager will take a
     decision on allocation of resources to the
     applications. ApplicationMaster is a library specific to
     application, which requests/negotiate resources from
     ResourceManager and launch and monitoring the task with
     NodeManager(s) :cite:`www-architecture`.  ResourceManager have
     two majors: Scheduler and ApplicationManager. Scheduler have a
     task to schedule the resources required by the
     application. ApplicationManger holds the record of application
     who require resource. It validates (whether to allocate the
     resource or not) the application’s resource requirement and
     ensure that no other application already have register for the
     same resource requirement. Also it keeps the track of release of
     resource. :cite:`www-HadoopApache`

273. Helix
274. Llama
275. Google Omega
276. Facebook Corona
277. Celery
278. HTCondor
279. SGE
280. OpenPBS
281. Moab
282. Slurm :cite:`www-slurm`

     Simple Linux Utility for Resource Management (SLURM) workload
     manager is an open source, scalable cluster resource management
     tool used for job scheduling in small to large Linux cluster
     using multi-core architecture. As per,
     :cite:`www-slurmSchedmdSite` SLURM has three key
     functions. First, it allocates resources to users for some
     duration with exclusive and/or non-exclusive access. Second, it
     enables users to start, execute and monitor jobs on the resources
     allocated to them. Finally, it intermediates to resolve conflicts
     on resources for pending work by maintaining them in a queue. The
     slurm architecture has following components: a centralized
     manager to monitor resources and work, may have a backup manager,
     daemon on each server to provide fault-tolerant communications,
     an optional daemon for clusters with multiple mangers and tools
     to initiate, terminate and report about jobs in a graphical view
     with network topology. It also provides around twenty additional
     plugins that could be used for functionalities like accounting,
     advanced reservation, gang scheduling, back fill scheduling and
     multifactor job prioritization. Though originally developed for
     Linux, SLURM also provides full support on platforms like AIX,
     FreeBSD, NetBSD and Solaris :cite:`www-slurmPlatformsSite`.
     
283. Torque
284. Globus Tools
285. Pilot Jobs

File systems
----------------------------------------------------------------------

286. HDFS
287. Swift
288. Haystack
289. f4
290. Cinder
291. Ceph
292. FUSE
293. Gluster
294. Lustre
295. GPFS

     IBM General Parallel File System (GPFS) was rebranded to IBM 
     Spectrum Scale on February 17, 2015.  :cite:`www-wikigpfs`
     See 380.

380. IBM Spectrum Scale

     General Parallel File System (GPFS) was rebranded as IBM Spectrum 
     Scale on February 17, 2015. :cite:`www-wikigpfs`

     Spectrum Scale is a clustered file system, developed by IBM, providing 
     high performance.  It "provides concurrent high-speed file access to 
     applications executing on multiple nodes of clusters" and can be 
     deployed in either shared-nothing or shared disk modes. Spectrum Scale 
     is available on AIX, Linux, Windows Server, and IBM System Cluster 
     1350. :cite:`www-wikigpfs`

     Due to its focus on performance and scalability, Spectrum Scale has 
     been utilized in compute clusters, big data and analytics (including 
     support for Hadoop Distributed File System (HDFS), backups and 
     restores, and private clouds. :cite:`www-spectrumscale`

296. GFFS
297. Public Cloud: Amazon S3
298. Azure Blob
299. Google Cloud Storage


Interoperability
----------------------------------------------------------------------

300. Libvirt
301. Libcloud
302. JClouds

     :cite:`cloud-portability-book` Primary goals of cross-platform
     cloud APIs is that application built using these APIs can be
     seamlessly ported to different cloud providers. The APIs also
     bring interoperability such that cloud platforms can communicate
     and exchange information using these common or shared interfaces.
     Jclouds or apache jclouds :cite:`www-jclouds` is a java based
     library to provide seamless access to cloud platforms. Jclouds
     library provides interfaces for most of cloud providers like
     docker, openstack, amazon web services, microsoft azure, google
     cloud engine etc. It will allow users build applications which
     can be portable across different cloud environments.  Key
     components of jcloud are:

     1. Views: abstracts functionality from a specific vendor and
        allow user to write more generic code. For example odbc
        abstracts the underlying relational data source. However, odbc
        driver converts to native format. In this case user can switch
        databases without rewriting the application. Jcloud provide
        following views: blob store, compute service, loadBalancer
        service

     2. API: APIs are requests to execute a particular
        functionality. Jcloud provide a single set of APIs for all
        cloud vendors which is also location aware. If a cloud vendor
        doesn’t support customers from a particular region the API
        will not work from that region.

     3. Provider: a particular cloud vendor is a provider. Jcloud uses
        provider information to initialize its context.

     4. Context: it can be termed as a handle to a particular
        provider. Its like a ODBC connection object. Once connection
        is initialized for a particular database, it can used to make
        any api call.

        Jclouds provides test library to mock context, APIs etc to
        different providers so that user can write unit test for his
        implementation rather than waiting to test with the cloud
        provider. Jcloud library certifies support after testing the
        interfaces with live cloud provider. These features make
        jclouds robust and adoptable, hiding most of the complexity of
        cloud providers.

303. TOSCA


304. OCCI

     The Open Cloud Computing Interface (OCCI) is a RESTful
     Protocol and API that provides specifications  and remote
     management for the development of “interoperable tools”
     :cite:`www-occi`. It supports IaaS, PaaS and SaaS and
     focuses on integration, portability, interoperability,
     innovation and extensibility. It provides a set of documents
     that describe an OCCI Core model, contain best practices
     of interaction with the model, combined into OCCI Protocols,
     explain methods of communication between components via
     HTTP protocol introduced in the OCCI Renderings, and
     define infrastructure for IaaS presented in the OCCI
     Extensions.

     The current version 1.2 OCCI consists of seven documents that
     identify require and optional components. Of the Core Model.  In
     particular, the following components are required to implement:
     a)Core Model, b)HTTP protocol, c)Text rendering and d)JSON
     rendering. Meanwhile, Infrastructure, Platform and SLA models are
     optional.  The OCCI Core model defines instance types and

     provides a layer of abstraction that allows the OCCI client
     to interact with the model without knowing of its potential
     structural changes. The model supports extensibility via
     inheritance and using mixin types that represent ability to
     add new components and capabilities at run-time.
     :cite:`nyren-edmonds-papaspyrou-2016`

     The OCCI Protocol defines the common set of names provided
     for the IaaS cloud services user that specify requested
     system requirements. It is often denoted as “resource
     templates” or “flavours”   :cite:`drescher-parak-wallom-2015`.

     OCCI RESTful HTTP Protocol describes communications between
     server and client on OCCI platform via HTTP protocol
     :cite:`nyren-edmonds-metsch-2016`. It defines a minimum set of HTTP
     headers and status codes to ensure compliance with the
     OCCI Protocol. Separate requirements for Server and Client
     for versioning need to be implemented using HTTP 'Server'
     header and 'User-Agent' header respectively.

     JSON rendering  :cite:`nyren-feldhaus-parak-2016` protocol provides
     JSON specifications to allow "render OCCI instances
     independently of the protocol being used." In addition, it
     provides details of the JSON object declaration, OCCI Action
     Invocation, object members required for OCCI Link Instance
     Rendering, "location maps to OCCI Core's source and target
     model attributes and kind maps to OCCI Core's target" to
     satisfy OCCI Link Instance Source/Target Rendering requirements.
     Finally, it specifies various attributes and collection
     rendering requirements.
     The text rendering process is depricated and will be
     removed from the next major version  :cite:`edmonds-metsch-2016`.
	 
305. CDMI
306. Whirr
307. Saga
308. Genesis

DevOps
----------------------------------------------------------------------

309. Docker (Machine, Swarm)
310. Puppet
311. Chef

     Chef is a configuration management tool. It is implemented in
     Ruby and Erlang. Chef can be used to configure and maintain
     servers on-premise as well as cloud platforms like Amazon EC2,
     Google Cloud Platform and Open Stack. In this book
     :cite:`chef-book`, it is mentioned how implementation recipes in
     Chef to manage server applications and utilities such as database
     servers like MySQL, or HTTP servers like Apache HTPP and systems
     like Apache Hadoop.

     Chef is available in open source version and it also has
     commercial products for the companies which need it
     :cite:`www-chef-commercial`

312. Ansible
313. SaltStack
314. Boto
315. Cobbler
316. Xcat
317. Razor
318. CloudMesh
319. Juju

     Juju (formerly Ensemble) :cite:`juju-paper` is software from
     Canonical that provides open source service orchestration. It is
     used to easily and quickly deploy and manage services on cloud
     and physical servers. Juju charms can be deployed on cloud
     services such as Amazon Web Services (AWS), Microsoft Azure and
     OpenStack. It can also be used on bare metal using MAAS.
     Specifically :cite:`www-juju` lists around 300 charms available
     for services available in the Juju store. Charms can be written
     in any language. It also supports Bundles which are
     pre-configured collection of Charms that helps in quick
     deployment of whole infrastructure.

320. Foreman
321. OpenStack Heat
322. Sahara

     The Sahara product provides users with the capability to
     provision data processing frameworks (such as Hadoop, Spark and
     Storm) on OpenStack :cite:`www-openStack` by specifying several
     parameters such as the version,cluster topology and hardware node
     details.As specified in :cite:`www-Sahara` the solution allows
     for fast provisioning of data processing clusters on OpenStack
     for development and quality assurance and utilisation of unused
     computer power from a general purpose OpenStack Iaas Cloud.Sahara
     is managed via a REST API with a User Interface available as part
     of OpenStack Dashboard.

323. Rocks
324. Cisco Intelligent Automation for Cloud
325. Ubuntu MaaS
326. Facebook Tupperware
327. AWS OpsWorks

     AWS Opsworks is a configuration service provided by Amazon Web
     Services that uses Chef, a Ruby and Erlang based configuration
     management tool :cite:`www-wikichef`, to automate the
     configuration, deployment, and management of servers and
     applications. There are two versions of AWS Opsworks.
     The first, a fee based offering called AWS OpsWorks for Chef
     Automate, provides a Chef Server and suite of tools to enable
     full stack automation. The second, AWS OpsWorks Stacks, is a
     free offering in which applications are modeled as stacks
     containing various layers. Amazon Elastic Cloud Compute (EC2)
     instances or other resources can be deployed and configured
     in each layer. :cite:`www-awsopsworks`

328. OpenStack Ironic
329. Google Kubernetes
330. Buildstep
     
     Buildsteps is an open software developed under MIT license. 
     It is a base for Dockerfile and it activates Heroku-style 
     application. Heroku is a platform-as-service (PaaS) that 
     automates deployment of applications on the cloud. The 
     program is pushed to the PaaS using git push, and then 
     PaaS detects the programming language, builds, and runs 
     application on a cloud platform :cite:`plassnig_2015`.
     Buildstep takes two parameters: a tar file that contains 
     the application and a new application container name to 
     create a new container for this application. Build script 
     is dependent on buildpacks that are pre-requisites for 
     buildstep to run. The builder script runs inside the new 
     container.  The resulting build app can be run with Docker 
     using docker build -t your_app_name command.
     :cite:`gonzalez_2015`. 

331. Gitreceive
332. OpenTOSCA
333. Winery
334. CloudML
335. Blueprints

     In :cite:`www-blueprints`, it is explained that "IBM Blueprint 
     has been replaced by IBM Blueworks Live." In 
     :cite:`www-blueworks-live2`, IBM Blueworks Live is described "as 
     a cloud-based business process modeller, belonging under the set 
     of IBM SmartCloud applications" that as 
     :cite:`www-blueworks-live` states "drive[s] out inefficiencies 
     and improve[s] business operations." Similarly to Google Docs, 
     IBM Blueworks Live is "designed to help organizations discover 
     and document their business processes, business decisions and 
     policies in a collaborative manner." While Google Docs and IBM 
     Blueworks Live are both simple to use in a collaborative manner, 
     :cite:`www-blueworks-live2` explains that IBM Blueworks Live 
     has the "capabilities to implement more complex models." 

336. Terraform
337. DevOpSlang
338. Any2Api

     This framework :cite:`wettinger-any2api` allows user to wrap an
     executable program or scripts, for example scripts, chef
     cookbooks, ansible playbooks, juju charms, other compiled
     programs etc. to generate APIs from your existing code.  These
     APIs are also containerized so that they can be hosted on a
     docker container, vagrant box etc Any2Api helps to deal with
     problems like scale of application, technical expertise, large
     codebase and different API formats. The generated API hide the
     tool specific details simplifying the integration and
     orchestration different kinds of artifacts. The APIfication
     framework contains various modules:

     1. Invokers, which are capable of running a given type of
        executable for example cookbook invoker can be used to run Chef
        cookbooks

     2. Scanners, which are capable of scanning modules of certain type for
        example cookbook scanner scans Chef cookbooks.

     3. API impl generators, which are doingthe actual work to
        generate the API implementation.

     The final API implementation :cite:`www-any2api` is is packages
     with executable in container.  The module is packaged as npm
     module. Currently any2api-cli provides a command line interface
     and web based interface is planned for future
     development. Any2Api is very useful for by devops to orchestrate
     open source ecosystem without dealing with low level details of
     chef cookbook or ansible playbook or puppet. It can also be very
     useful in writing microservices where services talk to each other
     using well defined APIs.

IaaS Management from HPC to hypervisors
----------------------------------------------------------------------

339. Xen

     Xen is the only open-source bare-metal hypervisor based on
     microkernel design :cite:`www-xen-wikipedia`. The hypervisor
     runs at the highest privilege among all the processes on the
     host. It's responsibility is to manage CPU and memory and
     handle interrupts :cite:`www-xen-overview`. Virtual
     machines are deployed in the guest domain called DomU which
     has no access privilege to hardware. A special virtual machine
     is deployed in the control domain called Domain 0. It contains
     hardware drivers and the toolstack to control the VMs and is
     the first VM to be deployed. Xen supports both Paravirtualization
     and hardware assisted virtualization. The hypervisor itself has
     a very small footprint. It's being actively maintained by Linux
     Foundation under the trademark "XEN Project". Some of the
     features included in the latest releases include "Reboot-free
     Live Patching" (to enable application of security patches without
     rebooting the system) and KCONFIG support (compilation support to
     create a lighter version for requirements such as embedded
     systems) :cite:`www-xen-fl`.
          
340. KVM
341. QEMU
342. Hyper-V
343. VirtualBox
344. OpenVZ
345. LXC
346. Linux-Vserver
347. OpenStack
348. OpenNebula
349. Eucalyptus
350. Nimbus

     Nimbus Infrastructure :cite:`www-nimbus-wiki` is an open source
     IaaS implementation. It allows deployment of self-configured
     virtual clusters and it supports configuration of scheduling,
     networking leases, and usage metering.

     Nimbus Platform :cite:`www-nimbus` provides an integrated set of
     tools which enable users to launch large virtual clusters as well
     as launch and monitor the cloud apps. It also includes service
     that provides auto-scaling and high availability of resources
     deployed over multiple IaaS cloud.  The Nimubs Platform tools are
     cloudinit.d, Phantom and Context Broker.  In this paper
     :cite:`nimbus-paper` it is mentioned how to used Nimbus Phantom
     to deploy auto-scaling solution across multiple NSF FutureGrid
     clouds. In this implementation Phantom was responsible for
     deploying instances across multiple clouds and monitoring those
     instance.  Nimbus platform supports Nimbus, Open Stack, Amazon
     and several other clouds.

351. CloudStack
352. CoreOS
     
     :cite:`www-core` states that “CoreOS is a linux operating system
     used for clustered deployments.” CoreOS allows applications to
     run on containers. CoreOS can be run on clouds, virtual or
     physical servers. CoreOS allows the ability for automatic software
     updates inorder to make sure containers in cluster are secure and
     reliable. It also makes managing large cluster environements
     easier. CoreOS provides open source tools like CoreOS Linux,
     etcd,rkt and flannel. CoreOS also has commercial products
     Kubernetes and CoreOS stack. Core OS. In CoreOS linux service
     discovery is achieved by etcd, applications are run on Docker and
     process management is achieved by fleet.

353. rkt
354. VMware ESXi
355. vSphere and vCloud
356. Amazon
357. Azure
358. Google and other public Clouds
359. Networking: Google Cloud DNS
360. Amazon Route 53


Cross-Cutting Functions
----------------------------------------------------------------------

Monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

361. Ambari
362. Ganglia
363. Nagios :cite:`www-nagios`

     Nagios is a platform, which provides a set of software for
     network infrastructure monitoring. It also offers administrative
     tools to diagnose when failure events happen, and to notify
     operators when hardware issues are detected. Specifically,
     illustrates that Nagios is consist of modules including
     :cite:`nagios-book`: a core and its dedicated tool for core
     configuration, extensible plugins and its frontend. Nagios core
     is designed with scalability in mind.  Nagios contains a
     specification language allowing for building an extensible
     monitoring systems.  Through the Nagios API components can
     integrate with the Nagios core services. Plugins can be developed
     via static languages like C or script languages. This mechanism
     empowers Nagios to monitor a large set of various scenarios yet
     being very flexible. :cite:`nagios-paper-2012` Besides its open
     source components, Nagios also has commercial products to serve
     needing clients.


364. Inca

     Inca is a grid monitoring :cite:`inca-book` software suite. It
     provides grid monitoring features. These monitoring features
     provide operators failure trends, debugging support, email
     notifications, environmental issues etc. :cite:`www-inca`. It
     enables users to automate the tests which can be executed on a
     periodic basis. Tests can be added and configured as and when
     needed. It helps users with different portfolios like system
     administrators, grid operators, end users etc Inca provides
     user-level grid monitoring. For each user it stores results as
     well as allows users to deploy new tests as well as share the
     results with other users. The incat web ui allows users to view
     the status of test, manage test and results. The architectural
     blocks of inca include report repository, agent, data consumers
     and depot. Reporter is an executable program which is used to
     collect the data from grid source. Reporters can be written in
     perl and python. Inca repository is a collection of pre build
     reporters.  These can be accessed using a web url. Inca
     repository has 150+ reporters available. Reporters are versioned
     and allow automatic updates. Inca agent does the configuration
     management. Agent can be managed using the incat web ui. Inca
     depot provides storage and archival of reports. Depot uses
     relational database for this purpose. The database is accessed
     using hibernate backend.  Inca web UI or incat provides real time
     as well as historical view of inca data.  All communication
     between inca components is secured using SSL certificates. It
     requires user credentials for any access to the
     system. Credentials are created at the time of the setup and
     installation. Inca's performance has been phenomenal in
     production deployments. Some of the deployments are running for
     more than a decade and has been very stable. Overall Inca
     provides a solid monitoring system which not only monitors but
     also detects problems very early on.

Security & Privacy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
365. InCommon
366. Eduroam :cite:`www-eduroam`

     Eduroam is an initiative started in the year 2003 when the number
     of personal computers with in the academia are growing
     rapidly. The goal is to solve the problem of secure access to
     WI-FI due to increasing number of students and reasearch teams
     becoming mobile which was increasing the administrative problems
     for provide access to WI-FI. Eduroam provides any user from an
     eduroam participating site to get network access at any
     instituion connected through eduroam. According to the
     orgnizatioin it uses a combination of radius-based infrastructuor
     with 802.1X standard techonology to provide roaming acess across
     reasearch and educational networks. The role of the RADIUS
     hierarchy is to forward user crednetials to the users home
     instituion where they can be verified. This proved to be a
     successful solution when compared to other traditonal ways like
     using MAC-adress, SSID, WEP, 802.1x(EAP-TLS, EAP-TTLS), VPN
     Clients, Mobile-IP etc which have their own short comings when
     used for this purpose :cite:`eduroam-paper-2005`. Today by
     enabling eduroam users get access to internet across 70 countries
     and tens of thousands of access points worldwide.


367. OpenStack Keystone
368. LDAP
369. Sentry
370. Sqrrl
371. OpenID
372. SAML OAuth

Distributed Coordination
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

373. Google Chubby
374. Zookeeper
 
     Zookeeper provides coordination services to distributed applications.
     It includes synchronization, configuration management and naming
     services among others. The interfaces are available in Java and C
     :cite:`www-zoo-overiew`. The services themselves can be distributed
     across multiple Zookeeper servers to avoid single point of failure.
     If the leader fails to answer, the clients can fall-back to other
     nodes. The state of the cluster is maintained in an in-memory image
     along with a persistent storage file called znode by each server. The
     cluster namespace is maintained in a hierarchical order. The changes to the
     data are totally ordered :cite:`www-zoo-wiki` by stamping each update
     with a number. Clients can also set a watch on a znode to be notified
     of any change :cite:`www-zoo-ibm`. The performance of the ZooKeeper
     is optimum for "read-dominant" workloads. It's maintained by Apache
     and is open-source.

375. Giraffe

     Giraffe is a scalable distributed coordination
     service. Distributed coordination is a media access technique
     used in distributed systems to perform functions like providing
     group membership, gaining lock over resources, publishing,
     subscribing, granting ownership and synchronization together
     among multiple servers without issues. Giraffe was proposed as
     alternative to coordinating services like Zookeeper and Chubby
     which were efficient only in read-intensive scenario and small
     ensembles. To overcome this three important aspects were included
     in the design of Giraffe :cite:`giraffePaper`. First feature is
     Giraffe uses interior-node joint trees to organize coordination
     servers for better scalability. Second, Giraffe uses Paxos
     protocol for better consistency and to provide more
     fault-tolerance. Finally, Giraffe also facilitates hierarchical
     data organization and in-memory storage for high throughput and
     low latency.
     
376. JGroups

Message and Data Protocols
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

377. Avro
378. Thrift
379. Protobuf

     Protocol Buffer :cite:`www-protobuf` is a way to serialize
     structured data into binary form (stream of bytes) in order to
     transfer it over wires or for storage. It is used for inter
     apllication communication or for remote procedure call (RPC). It
     involves a interface description that describes the structure of
     some data and a program that can generate source code or parse it
     back to the binary form. It emphasizes on simplicity and
     performance over xml. Though xml is more readable but requires
     more resources in parsing and storing.  This is developed by
     Google and available under open source licensing. The parser
     program is available in many languages including java and python.


New Technologies to be integrated
---------------------------------

382. TBD

.. _techs-exercise:

Excersise
---------

TechList.1: In class you will be given an HID and you will be assigned
  a number of technologies that you need to research and create a
  summary as well as one or more relevant refernces to be added to the
  Web page. All technologies for TechList.1 are marked with a (1)
  behind the technology.  An example text is given for Nagios in this
  page.  Please create a pull request with your responses. You are
  responsible for making sure the request shows up and each commit is
  using gitchangelog in the commit message::

    new:usr: added paragraph about <PUTTECHHERE>

  You can create one or more pull requests for the technology and the
  refernces. We have created in the referens file a placeholder using
  your HID to simplify the management of the refernces while avoiding
  conflicts.  For the technologies you are responsible to invesitgate
  them and write an academic summary of the technology. Make sure to
  add your refernce to refs.bib.  Many technologies may have
  additional refernces than the Web page. Please add the most
  important once while limiting it to three if you can. Avoid
  plagearism and use proper quotations or better rewrite the text.

  You must look at :doc:`technologies-hw` to sucessfully complete the
  homework

  A video about this hoemwork is posted at
  https://www.youtube.com/watch?v=roi7vezNmfo showing how to
  do references in emacs and jabref, it shows you how to configure
  git, it shows you how to do the fork request while asking you to add
  "new:usr ...." to the commit messages). As this is a homework
  realated video we put a lot of information in it that is not only
  useful for beginners. We recommend you watch it.


  This homework can be done in steps. First you can collect all the
  content in an editor. Second you can create a fork. Third you can
  add the new content to the fork. Fourth you can commit. Fith you
  can push. Six if the TAs have commend improve. The commit message
  must have new:usr: at the beginning.

  While the Nagios entry is a good example (make sure grammer is ok
  the Google app engine is an example for a bad entry.

  Do Techlist 1.a 1.b 1.c first. We  will assign Techlist 1.d and
  TechList 2 in February.

TechList.1.a:
  Complete the pull request with the technologies assigned to you.
  Details for the assignment are posted in Piazza. Search for TechList.

TechList.1.b: Identify how to cite. We are using "scientific" citation
  formats such as IEEEtran, and ACM. We are **not** using citation
  formats such as Chicago, MLA, or ALP. The later are all for non
  scientific publications and thus of no use to us. Also when writing
  about a technology do not use the names of the person, simply say
  something like. In [1] the definition of a turing machine is given
  as follows, ...  and do not use elaborate sentences such as: In his
  groundbraking work conducted in England, Allan Turing, introduced
  the turing machine in the years 1936-37 [2]. Its definition is base
  on ... The difference is clear, while the first focusses on results
  and technological concepts, the second introduces a colorful
  description that is more suitable for a magazine or a computer
  history paper.

TechList 1.c:
  Learn about Plagearism and how to avoid it.
  Many Web pages will conduct self advertisement while adding
  suspicious and subjective adjectives or phrases such as cheaper,
  superior, best, most important, with no equal, and others that you
  may not want to copy into your descriptions. Please focus on facts
  not on what the author of the Web page claims.

TechList 1.d:
  Identify technologies from the Apache project or other
  Big Data related Web pages and projects that are not yet listed here
  and add the name and descriptions as well as references and that you
  find important.

TechList.2:
  In this hopweork we provide you with additional technologies
  that you need to compleate They are marked with (2) in the HID
  assignment.

TechList.3:
  Identify technologies that are not listed here and add
  them. Provide a description and a refrence just as you did before.
  Make sure duplicated entries will be merged. Before you start doing a
  technology to avoid adding technologies that have already been done by
  others.




Refernces
---------

.. bibliography:: ../refs.bib
   :cited:
