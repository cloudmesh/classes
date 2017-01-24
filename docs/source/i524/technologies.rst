
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

   1. Taverna Workbench is desktop client where user can define the workflow.
   2. Taverna Server is responsible for executing the remote workflows.

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
    
    The Apache DataFu project was created out of the need for stable ,
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

    However, Azure offers a host of c+losely-related tool and products to enhance
    and improve the core product, such as raw block storage, load balancers,
    and IP addresses :cite:`www-azure-msft`.  For instance, Azure users can access
    predictive analytics, Bots and Blockchain-as-a-Service :cite:www-azure-msft} as
    well as more-basic computing, networking, storage, database and management
    components :cite:`www-sec-edgar-msft`.  The Azure website shows twelve major
    categories under *Products* and twenty *Solution* categories, e.g., e-commerce
    or Business SaaS apps.

    Azure competes against Amazon's *Amazon Web Service*, even though a
    IBM (*SoftLayer and Bluemix*) and Google (*Google Cloud Platform*)
    offer IaaS to the market.  As of January 2017, Azure's datacenters span 32
    Microsoft-defined *regions*, or 38 *declared regions*, throughout the world.

    **IMPROVE: References missing, aws, softlayer, bluemix, google cp**

    **IMPROVE: does the term c+losely-related realy exist?**
    
87. Cloud Foundry
88. Pivotal
89. IBM BlueMix
90. Ninefold
91. Jelastic
92. Stackato
93. appfog
94. CloudBees
95. Engine Yard
96. CloudControl
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
110. Impala
111. MRQL
112. SAP HANA
113. HadoopDB
114. PolyBase
115. Pivotal HD/Hawq
116. Presto
117. Google Dremel
118. Google BigQuery
119. Amazon Redshift
120. Drill
121. Kyoto Cabinet
     
     Kyoto Cabinet as specified in :cite:`www-KyotoCabinet` is a
     library of routines for managing a database which is a simple
     data file containing records. Each record in the database is a
     pair of a key and a value.Every key and value is serial bytes
     with variable length. Both binary data and character string can
     be used as a key and a value. Each key must be unique within a
     database.  There is neither concept of data tables nor data
     types. Records are organized in hash table or B+ tree. Kyoto
     Cabinet runs very fast. The elapsed time to store one million
     records is 0.9 seconds for hash database, and 1.1 seconds for B+
     tree database. Moreover, the size of database is very small. The,
     overhead for a record is 16 bytes for hash database, and 4 bytes
     for B+ tree database. Furthermore, scalability of Kyoto Cabinet
     is great.  The database size can be up to 8EB (9.22e18 bytes).

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
169. NaradaBrokering
170. QPid
171. Kafka
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

     Ross Mistry and Stacia Misner in :cite:`book-sqlserver` explain
     the technical architecture of SQL Server in OLTP(online
     transaction processing), hybrid cloud and business intelligence
     modes.

     **IMPROVE: It is inappropriate to mention authors**

201. SQLite
202. MySQL
203. PostgreSQL
204. CUBRID
205. Galera Cluster
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
     Google Cloud Platform and Open Stack. In his book
     :cite:`chef-book` Matthias Marschall explains how user can
     implement recipes in Chef to manage server applications and
     utilities such as database servers like MySQL, or HTTP servers
     like Apache HTPP and systems like Apache Hadoop.

     Chef is available in open source version and it also has commercial
     products for the companies which need it :cite:`www-chef-commercial`

     **IMPROVE: Mention names is inappropriate**
    
312. Ansible
313. SaltStack
314. Boto
315. Cobbler
316. Xcat
317. Razor
318. CloudMesh
319. Juju
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
     cloudinit.d, Phantom and Context Broker.  In the 2013 paper
     :cite:`nimbus-paper` Dmitry Duplykin and others from University
     of Colorado, used Nimbus Phantom to deploy auto-scaling solution
     across multiple NSF FutureGrid clouds. In this implementation
     Phantom was responsible for deploying instances across multiple
     clouds and monitoring those instance.  Nimbus platform supports
     Nimbus, Open Stack, Amazon and several other clouds.

     **IMPROVE: Mention names is inappropriate**

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
     being very flexible. :cite:`nagios-paper-2012` Besides its open source components, Nagios
     also has commercial products to serve needing clients.


364. Inca


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


      
