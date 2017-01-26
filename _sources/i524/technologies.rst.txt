
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
3. Airavata   
4. Pegasus 
5. Kepler 
6. Swift  
7. Taverna
   
   Taverna is workflow management system. According to :cite:`www-taverna`,
   Taverna is transitioning to Apache Incubator as of Jan 2017.
   Taverna suite includes 2 products: 

   (1). Taverna Workbench is desktop client where user can define the workflow.
   (2). Taverna Server is responsible for executing the remote workflows.

   Taverna workflows can also be executed on command-line.
   Taverna supports wide range of services including WSDL-style and RESTful
   Web Services, BioMart, SoapLab, R, and Excel. Taverna also support
   mechanism to monitor the running workflows using its web browser interface.
   In his :cite:`taverna-paper` paper, Daniele Turi presented the formal
   syntax and operational semantics of Taverna.

8. Triana 
9. Trident 
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
59. GraphX
60. IBM System G
61. GraphBuilder(Intel)
62. TinkerPop
63. Parasol
64. Dream:Lab
65. Google Fusion Tables
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
82. Red Hat OpenShift
83. Heroku
84. Aerobatic
85. AWS Elastic Beanstalk
86. Azure
    
    Microsoft Corporation markets its cloud products under the *Azure* brand
    name. At its most basic, Azure acts as an *infrastructure-as-a-service* (IaaS)
    provider.  IaaS virtualizes hardware components, a key differentiation from
    other *-as-a-service* products.  The Wikipedia entry on IaaS notes that IaaS
    "abstract[s] the user from the details of infrasctructure like physical
    computing resources, location, data partitioning, scaling, security, backup,
    etc." :cite:www-wikipedia-cloud

    However, Azure offers a host of closely-related tool and products to enhance
    and improve the core product, such as raw block storage, load balancers,
    and IP addresses :cite:`www-azure-msft`.  For instance, Azure users can access
    predictive analytics, Bots and Blockchain-as-a-Service :cite:www-azure-msft as
    well as more-basic computing, networking, storage, database and management
    components :cite:`www-sec-edgar-msft`.  The Azure website shows twelve major
    categories under *Products* and twenty *Solution* categories, e.g., e-commerce
    or Business SaaS apps.

    Azure competes against Amazon's *Amazon Web Service*, :cite:www-aws-amzn
    even though IBM (*SoftLayer* :cite:www-softlayer-ibm and *Bluemix* :cite
    :`www-bluemix-ibm`) and Google (*Google Cloud Platform*) :cite:`www-cloud-
    google` offer IaaS to the market.  As of January 2017, Azure's datacenters
    span 32 Microsoft-defined *regions*, or 38 *declared regions*, throughout
    the world. :cite:`www-azure-msft`

87. Cloud Foundry
88. Pivotal
89. IBM BlueMix
90. (Ninefold)

    no longer active
    
91. Jelastic
92. Stackato
93. appfog
94. CloudBees
95. Engine Yard
96. (CloudControl)

    No Longer active as of Feb. 2016
    
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

     In the first quarter of 2013, Salesforce.com released its proprietary SQL-like
     interface and query engine for HBase, *Phoenix*, to the open source community.
     The company appears to have been motivated to develop Phoenix as a way to 1)
     increase accessiblity to HBase by using the industry-standard query language
     (SQL); 2) save users time by abstracting away the complexities of coding native
     HBase queries; and, 3) implementing query best practices by implementing them
     automatically via Phoenix. :cite:`www-phoenix-cloudera`  Although Salesforce.com
     initially *open-sourced* it via Github, by May of 2014 it had become a top-level
     Apache project. :cite:`www-phoenix-wikipedia`

     Phoenix, written in Java, "compiles [SQL queries] into a series of HBase scans,
     and orchestrates the running of those scans to produce regular JDBC result
     sets." :cite:`www-apachephoenix-org`  In addition, the program directs compute
     intense portions of the calls to the server.  For instance, if a user queried
     for the top ten records across numerous regions from an HBase database
     consisting of a billion records, the program would first select the top ten
     records for each region using server-side compute resources.  After that, the
     client would be tasked with selecting the overall top ten. :cite:`www-phoenix-
     salesforcedev`

     Despite adding an abstraction layer, Phoenix can actually speed up queries
     because it optimizes the query during the translation process. :cite:`www-
     phoenix-cloudera`  For example, "Phoenix beats Hive for a simple query spanning
     10M-100M rows." :cite:`www-phoenix-infoq`

     Finally, another program can enhance HBase's accessibility for those inclined
     towards graphical interfaces.  SQuirell only requires the user to set up the
     JDBC driver and specify the appropriate connection string. :cite:`www-phoenix-
     bighadoop`

110. Impala
111. MRQL
112. SAP HANA
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
157. Medusa-GPU
158. MapGraph
159. Totem


Inter process communication Collectives
----------------------------------------------------------------------

160. point-to-point
161. publish-subscribe: MPI
162. HPX-5
163. Argo BEAST HPX-5 BEAST PULSAR
164. Harp
165. Netty
166. ZeroMQ
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
175. Stomp
176. MQTT
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

     Gora has a query interface to query the underlying data store. Its
     configuration is stored in gora.properties which should be present in
     classpath. In the file you can specify default data store used by Gora
     engine. Gora also has a CI/CD library call GoraCI which is used to write
     integration tests.

184. Memcached
185. Redis
186. LMDB (key value)
187. Hazelcast
188. Ehcache
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

     SQL Server :cite:`www-sqlserver-wiki` is a relational database management system
     from Microsoft. As of Jan 2017, SQL Server is available in below editions

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
203. PostgreSQL

204. CUBRID

	 CUBRID name is deduced from the combination of word CUBE(security within box) and BRIDGE(data bridge).
	 It is an open source Relational DataBase Management System designed in C programming language with high
	 performance, scalability and availability features. During its development by NCL, korean IT service provider
	 the goal was to optimize database performance for web-applications. :cite:`www-cubrid`
	 Importantly most of the SQL syntax from MYSQL and ORACLE can work on cubrid.CUBRID also provides manager tool
	 for database administration and migration tool for migrating the data from DBMS to CUBRID bridging the dbs.
	 CUBRID enterprise version and all the tools are free and suitable database candidate for web-application development.	

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
     by LinkedIN, is a non-relational database of key-value type that
     supports eventual consistency. The distributed nature of the
     system allows pluggable data placement and provides horizontal
     scalability and high consistency. Replication and partitioning of
     data is automatic and performed on multiple servers. Independent
     nodes that comprise the server support transparent handling of
     server failure and ensure absence of a central point of
     failure. Essentially, Voldemort is a hashtable. It uses APIs for
     data replication. In memory caching allows for faster
     operations. It allows cluster expansion with no data
     rebalancing. When Voldemort performance was benchmarked with the
     other key-value databases such as Cassandra, Redis and HBase as
     well as MySQL relational database
     (:cite:`rabl_sadoghi_jacobsen_2012`), the Voldemart's throughput
     was twice lower than MySQL and Cassandra and six times higher
     than HBase. Voldemort was slightly underperforming in comparison
     with Redis.  At the same time, it demonstrated consistent linear
     performance in maximum throughput that supports high scalability.
     The read latency for Voldemort was fairly consistent and only
     slightly underperformed Redis. Similar tendency was observed with
     the read latency that puts Voldermort in the cluster of databases
     that require good read-write speed for workload
     operations. However, the same authors noted that Voldemort
     required creation of the node specific configuration and
     optimization in order to successfully run a high throughput
     tests. The default options were not sufficient and were quickly
     saturated that stall the database.

222. Riak
223. ZHT
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
232. IBM Cloudant
233. Pivotal Gemfire
234. HBase
235. Google Bigtable
236. LevelDB
237. Megastore and Spanner
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
264. HTTP
265. FTP
266. SSH
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
269. Sqoop
270. Pivotal GPLOAD/GPFDIST

Cluster Resource Management
----------------------------------------------------------------------

271. Mesos
272. Yarn
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

     1. Views: abstracts functionality from a specific vendor and allow user to write
        more generic code. For example odbc abstracts the underlying relational data
        source. However, odbc driver converts to native format. In this case user can
        switch databases without rewriting the application. Jcloud provide following
        views: blob store, compute service, loadBalancer service

     2. API: APIs are requests to execute a particular functionality. Jcloud provide a
        single set of APIs for all cloud vendors which is also location aware. If a
        cloud vendor doesn’t support customers from a particular region the API will
        not work from that region.

     3. Provider: a particular cloud vendor is a provider. Jcloud uses provider
        information to initialize its context.

     4. Context: it can be termed as a handle to a particular provider. Its like a
        ODBC connection object. Once connection is initialized for a particular
        database, it can used to make any api call.

        Jclouds provides test library to mock context, APIs etc to different providers so
        that user can write unit test for his implementation rather than waiting to
        test with the cloud provider. Jcloud library certifies support after testing
        the interfaces with live cloud provider. These features make jclouds robust
        and adoptable, hiding most of the complexity of cloud providers.

303. TOSCA
304. OCCI
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
328. OpenStack Ironic
329. Google Kubernetes
330. Buildstep
331. Gitreceive
332. OpenTOSCA
333. Winery
334. CloudML
335. Blueprints
336. Terraform
337. DevOpSlang
338. Any2Api

IaaS Management from HPC to hypervisors
----------------------------------------------------------------------

339. Xen
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
366. Eduroam
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
375. Giraffe
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

TechList.1:
  In class you will be given an HID and you will be assigned a number
  of technologies that you need to research and create a summary as
  well as one or more relevant refernces to be added to the Web
  page. An example is given for Nagios.  Please create a pull request
  with your responses. You are responsible for making sure the request
  shows up and each commit is using gitchangelog "new:usr: added
  paragraph about <PUTTECHHERE>" For the repository and create a
  single pull request with your response for all technologies you are
  responsible to invesitgate.  Make sure to add your refernce to
  refs.bib.  Many technologies may have additional refernces than the
  Web page. Please add the most important once while limiting it to
  three if you can. Avoid plagearism and use proper quotations or
  better rewrite the text.
  
  You must look at :ref:`techlist-tips` to sucessfully complete the homework

  A video about this hoemwork is posted at
  https://www.youtube.com/watch?v=roi7vezNmfo showing how to
  do references in emacs and jabref, it shows you how to configure
  git, it shows you how to do the forkrequest while asking you to add
  "new:usr ...." to the commit messages). As this is a homework
  realated video we put a lot of information in it that is not only
  useful for beginners. We recommend you watch it.


  This homework can be done in steps. First you can collect all the
  content in an editor. Second you can create a fork. Third you can
  add the new content to the fork. Fourth you can commit. Fith you
  can push. SIx if the TAs have commend improve. The commit message
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
  Identify technologies from the Apache project that ar enot yet
  listed here and add the name and descriptions as well as references.
  
TechList.2:
  As some students may not complete this assignment because
  they for example dropped the class, identify a number of not
  submitted descriptions and complete them. Coordinate with your class
  mates to identify a non overlapping assignment. The TA's will
  assign you additional technologies.

TechList.3:
  Identify technologies that are not listed here and add
  them. Provide a description and a refrence just as you did before.
  Make sure duplicated entries will be merged. Before you start do a
  pull to avoid adding technologies that have already been done by
  others.


  

Refernces
---------

.. bibliography:: ../refs.bib
   :cited:


      
