
.. index:: I524 technologies

Technologies
============


In this section we find a number of technologies that are related to
big data. Certainly a number of these projects are hosted as an Apache
project. One important resource for a general list of all apache
projects is at


* Apache projects: https://projects.apache.org/projects.html?category


Workflow-Orchestration
----------------------

1. ODE

   Apache ODE (Orchestration Director Engine) is an open source
   implementation of the WS-BPEL 2.0 standard. WS- BPEL which stands
   for  Web Services Business Process Execution Language, is an
   executable language for writing business processes with web
   services :cite:`www-bpel-wiki`.  It includes control structures
   like conditions or loops as well as elements to invoke web services
   and receive messages from services.  ODE uses WSDL (Web Services
   Description Language) for interfacing with web services
   :cite:`www-ode-wiki`. Naming a few of its features, It supports two
   communication layers for interacting with the outside world, one
   based on Axis2 (Web Services http transport) and another one based
   on the JBI standard. It also supports both long and short living
   process executions for orchestrating services for applications
   :cite:`www-ode-web`.

2. ActiveBPEL

   Business Process Execution Language for Web Services (BPEL4WS or
   just BPEL) is an XML-based grammar for describing the logic to
   coordinate and control web services that seamlessly integrate
   people, processes and systems, increasing the efficiency and
   visibility of the business. ActiveBPEL is a robust Java/J2EE
   runtime environment that is capable of executing process
   definitions created to the Business Process Execution Language for
   Web Services. The ActiveBPEL also provides an administration
   interface that is accessible via web service invocations;and it can
   also be use to administer, to control and to integrate web services
   into a larger application. :cite:`www-bpel`


3. Airavata

   Apache Airavata :cite:`www-airavata` is a software framework that
   enables you to compose, manage, execute, and monitor large scale
   applications and workflows on distributed computing resources such
   as local clusters, supercomputers, computational grids, and
   computing clouds. Scientific gateway developers use Airavata as
   their middleware layer between job submissions and grid
   systems. Airavata supports long running applications and workflows
   on distributed computational resources. Many scientific gateways
   are already using Airavata to perform computations (e.g. Ultrascan
   :cite:`www-ultrascan`, SEAGrid :cite:`www-seagrid` and GenApp
   :cite:`www-genapp`).

4. Pegasus

   The Pegasus :cite:`www-Pegasus` is workflow management system 
   that alows to compose and execute a workflow in an application
   in different environment without the need  for any 
   modifications. It allows users to make high level workflow 
   without thinking about the low level details. It locates
   the required input data and computational resources automatically. 
   Pegasus also maintains information about tasks done and data 
   produced. In case of errors Pegasus tries to recover by retrying 
   the whole workflow and providing check pointing at workflow-level. 
   It cleans up the storage as the workflow gets executed so that 
   data-intensive workflows can have enough required space to execute 
   on storage-constrained resources. Some of the other advantages of 
   Pegasus are:scalability, reliability and high performance. Pegasus 
   has been used in many scientific domains like astronomy, 
   bioinformatics, earthquake science , ocean science, gravitational 
   wave physics and others.


5. Kepler
 
   Kepler, scientific workflow application, is designed to help
   scientist, analyst, and computer programmer create, execute and
   share models and analyses across a broad range of scientific and
   engineering disciplines.  Kepler can operate on data stored in a
   variety of formats, locally and over the internet, and is an
   effective environment for integrating disparate software components
   such as merging *R* scripts with compiled *C* code, or facilitating
   remote, distributed execution of models. Using Kepler's GUI, users
   can simply select and then connect pertinent analytical components
   and data sources to create a *scientific workflow*. Overall, the
   Kepler helps users share and reuse data, workflow, and components
   developed by the scientific community to address common needs
   :cite:`www-kepler`.

6. Swift

   Swift is a general-purpose, multi-paradigm, compiled programming
   language. It has been developed by Apple Inc. for iOS, macOS,
   watchOS, tvOS, and Linux. This programming language is intended to
   be more robust and resilient to erroneous code than Objective-C,
   and more concise. It has been built with the LLVM compiler
   framework included in Xcode 6 and later and, on platforms other
   than Linux. C, Objective-C, C++ and Swift code can be run within
   one program as Swift uses the Objective-C runtime
   library. :cite:`www-swift-wikipedia`

   Swift supports the core concepts that made Objective-C flexible,
   notably dynamic dispatch, widespread late binding, extensible
   programming and similar features. Swift features have well-known
   safety and performance trade-offs. A system that helps address
   common programming errors like null pointers was introduced to
   enhance safety. Apple has invested considerable effort in
   aggressive optimization that can flatten out method calls and
   accessors to eliminate this overhead to handle performance issues.
      
7. Taverna

   Taverna is workflow management system. According to
   :cite:`www-taverna`, Taverna is transitioning to Apache Incubator
   as of Jan 2017.  Taverna suite includes 2 products:

   1. Taverna Workbench is desktop client where user can define the
      workflow.
   2. Taverna Server is responsible for executing the remote
      workflows.

   Taverna workflows can also be executed on command-line.  Taverna
   supports wide range of services including WSDL-style and RESTful
   Web Services, BioMart, SoapLab, R, and Excel. Taverna also support
   mechanism to monitor the running workflows using its web browser
   interface.  In the :cite:`taverna-paper` paper, the formal syntax
   and operational semantics of Taverna is explained.

8. Triana

   Triana is an open source problem solving software that comes with 
   powerful data analysis tools :cite:`trianaDocumentation-1`.
   Having been developed at Cardiff University, it has a good and
   easy-to-understand User Interface and is typically used for signal,
   text and image processing.  Although it has its own set of analysis
   tools, it can also easily be integrated with custom tools.  Some of
   the already available toolkits include signal-analysis toolkit, an
   image-manipulation toolkit, etc.  Besides, it also checks the data
   types and reports the usage of any incompatible tools.  It also
   reports errors, if any, as well as useful debug messages in order
   to resolve them.  It also helps track serious bugs, so that the
   program does not crash.  It has two modes of representing the
   data - a text-editor window or a graph-display window.  The
   graph-display window has the added advantage of being able to zoom
   in on particular features.  Triana is specially useful for
   automating the repetitive tasks, like finding-and-replacing a
   character or a string.
   
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
    
    BioKepler is a Kepler module of scientific workflow components to
    execute a set of bioinformatics tools using distributed execution
    patterns :cite:`www-biokepler`. It contains a specialized set of
    actors called "bioActors" for running bioinformatic tools,
    directors providing distributed data-parallel(DPP) execution on
    Big Data platforms such as Hadoop and Spark they are also
    configurable and reusable :cite:`www-biokepler-demos`. BioKepler
    contains over 40 example workflows that demonstrate the actors and
    directors :cite:`bioActors`.
    
11. Galaxy

    Ansible Galaxy is a website platform and command line tool that
    enables users to discover, create, and share community developed
    roles. Users' GitHub accounts are used for authentication,
    allowing users to import roles to share with the ansible
    community. :cite:`www-galaxy-ansible` describes how Ansible roles
    are encapsulated and reusable tools for organizing automation
    content. Thus a role contains all tasks, variables, and handlers
    that are necessary to complete that
    role. :cite:`Ansible-book-2016` depicts roles as the most powerful
    part of Ansible as they keep playbooks simple and readable. "They
    provide reusable definitions that you can include whenever you
    need and customize with any variables that the role exposes."
    :cite:`www-github-galaxy` provides the project documents for
    Ansible Galaxy on github.
    
12. IPython
13. Jupyter

    The Jupyter Notebook is a language-agnostic HTML notebook web
    application that allows you to create and share documents that
    contain live code, equations, visualizations and explanatory
    text. :cite:`www-jupyter-1` The notebook extends the console-based
    approach to interactive computing in a qualitatively new
    direction, providing a web-based application suitable for
    capturing the whole computation process: developing, documenting,
    and executing code, as well as communicating the
    results. :cite:`www-jupyter-2` The Jupyter notebook combines two
    components:
    
    1. A web application: a browser-based tool for interactive
    authoring of documents which combine explanatory text,
    mathematics, computations and their rich media output.

    2. Notebook documents: a representation of all content visible in
    the web application, including inputs and outputs of the
    computations, explanatory text, mathematics, images, and rich
    media representations of objects.

    Notebooks may be exported to a range of static formats, including
    HTML (for example, for blog posts), reStructuredText, LaTeX, PDF,
    and slide shows, via the nbconvert command. :cite:`www-jupyter-3`
    Notebook documents contains the inputs and outputs of a
    interactive session as well as additional text that accompanies
    the code but is not meant for execution. :cite:`www-jupyter-4` In
    this way, notebook files can serve as a complete computational
    record of a session, interleaving executable code with explanatory
    text, mathematics, and rich representations of resulting
    objects. :cite:`www-jupyter-5` These documents are internally JSON
    files and are saved with the .ipynb extension. Since JSON is a
    plain text format, they can be version-controlled and shared with
    colleagues. :cite:`www-jupyter-6`

14. Dryad

    Dryad is a general-purpose distributed execution engine for
    coarse-grain data-parallel applications. According to
    :cite:`www-DryadIntro` it was created with the objective of
    automatically managing scheduling, distribution, fault tolerance
    etc. Dryad concentrates on the throughput instead of latency and
    it assumes that a private data centre is used. It creates a
    dataflow graph by using computational 'vertices' and communication
    'channels'. The computational vertices are written using C++ base
    classes and objects. During runtime, the dataflow graph is
    parallelized by distributing the vertices across multiple
    processor cores on the same computer or different physical
    computers connected by a network. The Dryad runtime handles this
    scheduling without any explicit intervention. The data flow from
    one vertex to another is realized by TCP/IP streams, shared
    memory, or temporary files. In the directed acyclic graph created
    by Dryad, each vertex is a program and the edges represent data
    channels. Each graph is represented as G = (VG, EG, IG, OG) in
    :cite:`DryadPaper` where VG is a sequence of vertices with EG
    directed edges and two sets IG is a subset of VG and OG is a
    subset of VG that indicate the input and output vertices
    respectively. Other technologies used for the same purpose as
    Dryad include Map Reduce, MPI etc.
    
15. Naiad

    Naiad :cite:`paper-naiad` is a distributed system based on
    computational model called *Timely Dataflow* developed for
    execution of data-parallel, cyclic dataflow programs. It provides
    an in-memory distributed dataflow framework which exposes control
    over data partitioning and enables features like the high
    throughput of batch processors, the low latency of stream
    processors, and the ability to perform iterative and incremental
    computations. The Naiad architecture consists of two main
    components: (1) incremental processing of incoming updates and (2)
    low-latency real-time querying of the application state.
    
    Compared to other systems supporting loops or streaming
    computation, Naiad provides support for the combination of the
    two, nesting loops inside streaming contexts and indeed other
    loops, while maintaining a clean separation between the many
    reasons new records may flow through the computation
    :cite:`www-naiad`.
    
    This model enriches dataflow computation with timestamps that
    represent logical points in the computation and provide the basis
    for an efficient, lightweight coordination mechanism.  All the
    above capabilities in one package allows development of High-level
    programming models on Naiad which can perform tasks as streaming
    data analysis, iterative machine learning, and interactive graph
    mining. On the contrary, it's public reusable low-level
    programming abstractions leads Naiad to outperforms many other
    data parallel systems that enforce a single high-level programming
    model.
    
16. Oozie

    Oozie is a workflow manager and scheduler. Oozie is designed to
    scale in a Hadoop cluster. Each job will be launched from a
    different datanode :cite:`paper-Oozie` :cite:`www-Oozie1`.  Oozie
    :cite:`www-Oozie2` is architected from the ground up for
    large-scale Hadoop workflow. Scales to meet the demand, provides a
    multi-tenant service, is secure to protect data and processing,
    and can be operated cost effective ly. As demand for workflow and
    the sophistication of applications increase, it must continue to
    mature in these areas :cite:`paper-Oozie`.Is well integr ated with
    Hadoop security. Is the only workflow manager with built-in Hadoo
    p actions, making workflow development, maintenance and
    troubleshooting easi er. It’s UI makes it easier to drill down to
    specific errors in the data nodes. Proven to scale in some of the
    world’s largest clusters :cite:`paper-Oozie`. Gets callbacks from
    MapReduce jobs so it knows when they finish and whether they hang
    without expensive polling. Oozie Coordinat or allows triggering
    actions when files arrive at HDFS. Also supported by Hadoop
    vendors :cite:`paper-Oozie`.
	
17. Tez

    Apache Tez is open source distributed execution framework build
    for writing native YARN application. It provides architecture
    which allows user to convert complex computation as dataflow
    graphs and the distributed engine to handle the directed acyclic
    graph for processing large amount of data. It is highly
    customizable and pluggable so that it can be used as a platform
    for various application.It is used by the Apache Hive, Pig as
    execution engine to increase the performance of map reduce
    functionality.  :cite:`www-apache-tez` Tez focuses on running
    application efficiently on Hadoop cluster leaving the end user to
    concentrate only on its business logic. Tez provides features like
    distributed parallel execution on hadoop cluster,horizontal
    scalability, resource elasticity,shared library reusable
    components and security features. Tez provides capability to
    naturally map the algorithm into the hadoop cluster execution
    engine and it also provides the interface for interaction with
    different data sources and configurations.
	
    Tez is client side application and just needs Tez client to be
    pointed to Tez jar libraries path makes it easy and quick to
    deploy. User can have have multiple tez version running
    concurrently. Tez provides DAG API's which lets user define
    structure for the computation and Runtime API's which contain the
    logic or code that needs to be executed in each transformation or
    task.

18. Google FlumeJava

    FlumeJava :cite:`www-flumejava-google` is a java library that
    allows users to develop and run data parallel pipelines. Its goal
    is to allow a programmer to express his data-parallel computations
    in a clear way while simultaneously executing it in the best
    possible optimized manner. The MapReduce function eases the task
    of data parallelism. However, a pipeline of MapReduce functions is
    desired by many real time computation systems. FlumeJava provides
    these abstractions of data parallel computations by providing
    support for pipelined execution. To provide optimized parallel
    execution, FlumeJava defers the execution of these pipelines and
    instead contsructs an execution plan dataflow graph depending on
    the results needed by each stage of the pipeline. "When the final
    results of the parallel operations are eventually needed,
    FlumeJava first optimizes the execution plan, and then executes
    the optimized operations on appropriate underlying primitives"
    :cite:`flumejava-paper`. FlumeJava library is written on top of
    the collection framework in Java.

    When developing a large pipeline, it is timeconsuming to find a
    bug in the later stages and then re-compile and re-evaluate all
    the operations. FlumeJava library supports a cached execution mode
    to aid in this scenario. In this mode, it automatically creates
    temporary files to hold the outputs of each operation it
    executes :cite:`flumejava-paper`. Thus, rather than recomputing
    all the operations once the pipeline has been rectified to fix all
    the bugs, it simply reads the output from these temporary files
    and later deletes them once they are no longer in use.    
    
19. Crunch

    Arvados Crunch :cite:`www-arvados` is a containerized workflow
    engine for running complex, multi-part pipelines or workflows in a
    way that is flexible, scalable, and supports versioning,
    reproducibilty, and provenance while running in virtualized
    computing environments. The Arvados Crunch :cite:`www-crunch`
    framework is designed to support processing very large data
    batches (gigabytes to terabytes) efficiently. Arvados Crunch
    increases concurrency by running tasks asynchronously, using many
    CPUs and network interfaces at once (especially beneficial for
    CPU-bound and I/O-bound tasks respectively). Crunch also tracks
    inputs, outputs, and settings so you can verify that the inputs,
    settings, and sequence of programs you used to arrive at an output
    is really what you think it was. Crunch ensures that your programs
    and workflows are repeatable with different versions of your code,
    OS updates, etc. and allows you to interrupt and resume
    long-running jobs consisting of many short tasks and maintains
    timing statistics automatically.

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

    In :cite:`e-science-central-paper-2010`, it is explained that
    e-Science Central is designed to address some of the pitfalls
    within current Infrastructure as a Service (e.g.  Amazon EC2) and
    Platform as a Service (e.g. force.com) services. For instance, in
    :cite:`e-science-central-paper-2010`, the "majority of potential
    scientific users, access to raw hardware is of little use as they
    lack the skills and resources needed to design, develop and
    maintain the robust, scalable applications they require" and
    furthermore "current platforms focus on services required for
    business applications, rather than those needed for scientific
    data storage and analysis." In :cite:`www-e-science-central`, it
    is explained that e-Science Central is a "cloud based platform for
    data analysis" which is "portable and can be run on Amazon AWS,
    Windows Azure or your own hardware." In
    :cite:`e-science-central-paper-2010`, e-Science Central is further
    described as a platform, which "provides both Software and
    Platform as a Service for scientific data management, analysis and
    collaboration." This collaborative platform is designed to be
    scalable while also maintaining ease of use for scientists. In
    :cite:`e-science-central-paper-2010`, "a project consisting of
    chemical modeling by cancer researchers" demonstrates how
    e-Science Central "allows scientists to upload data, edit and run
    workflows, and share results in the cloud."

23. Azure Data Factory
    
    Azure data factory is a cloud based data integration service that
    can ingest data from various sources, transform/ process data and
    publish the result data to the data stores. A data management
    gateway enables access to data on SQL Databases
    :cite:`www-jamesserra`. The data processing is done by It works by
    creating pipelines to transform the raw data into a format that
    can be readily used by BI Tools or applications. The services
    comes with rich visualization aids that aid data analysis. Data
    Factory supports two types of activities: data movement activities
    and data transformation activities. Data Movement
    :cite:`www-microsoft-azure` is a Copy Activity in Data Factory
    that copies data from a data source to a Data sink. Data Factory
    supports the following data stores. Data from any source can be
    written to any sink.  Data Transformation: Azure Data Factory
    supports the following transformation activities such as Map
    reduce, Hive transformations and Machine learning activities.Data
    factory is a great tool to analyze web data, sensor data and
    geo-spatial data.

24. Google Cloud Dataflow
    
    Google Cloud Dataflow is a unified programming model and a managed
    service for developing and executing a wide variety of data
    processing patterns (pipelines). Dataflow includes SDKs for
    defining data processing workflows and a Cloud platform managed
    services to run those workflows on a Google cloud platform
    resources such as Compute Engine, BigQuery amongst others
    :cite:`www-Dataflow`. Dataflow pipelines can operate in both batch
    and streaming mode. The platform resources are provided on demand,
    allowing users to scale to meet their requirements, it’s also
    optimized to help balance lagging work dynamically.

    Being a cloud offering, Dataflow is designed to allow users to focus
    on devising proper analysis without worrying about the installation
    and maintaining :cite:`www-GoogleLiveStream` the underlying data
    piping and process infrastructure.
    
25. NiFi (NSA)

    :cite:`www-nifi` Defines NiFi as "An Easy to use, powerful and
    realiable system to process and distribute data".  This tool aims
    at automated data flow from sources with different sizes , formats
    and following diffent protocals to the centralized location or
    destination. :cite:`www-hortanworks`.
    
    This comes equipped with an easy use UI where the data flow can be
    conrolled with a drag and a drop.  NiFi was initiatially developed
    by NSA ( called Niagarafiles ) using the concepts of flowbased
    programming and latter submitted to Apachi Software
    foundation. :cite:`www-forbes`
    
26. Jitterbit

    Jitterbit :cite:`datasheet` is an integration tool that delivers a
    quick, flexible and simpler approach to design, configure, test,
    and deploy integration solutions. It delivers powerful, flexible,
    and easy to use integration solutions that connect modern on
    premise, cloud, social, and mobile infrastructures. Jitterbit
    employs high performance parallel processing algorithms to handle
    large data sets commonly found in ETL initiatives
    :cite:`www-jitetl`. This allows easy synchronization of disparate
    computing platforms quickly. The Data Cleansing and Smart
    Reconstruction tools provides complete reliability in data
    extraction, transformation and loading.

    Jitterbit employs a no-code GUI (graphical user interface) and
    work with diverse applications such as : ETL
    (extract-transform-load), SaaS (Software as a Service),SOA
    (service-oriented architecture).

    Thus it provides centralized platform with power to control all
    data. It supports many document types and protocols: XML, web
    services, database, LDAP, text, FTP, HTTP(S), Flat and Hierarchic
    file structures and file shares :cite:`tech-manual`. It is
    available for Linux and Windows, and is also offered through
    Amazon EC2 (Amazon Elastic Compute Cloud). Jitterbit Data Loader
    for Salesforce is a free data migration tool that enables
    Salesforce administrators automated import and export of data
    between flat files, databases and Salesforce.

27. Talend

    Talend is Apache Software Foundation sponsor Big data integration
    tool design to ease the development and integration and management
    of big data, Talend provides well optimised auto generated code to
    load transform, enrich and cleanse data inside Hadoop, where one
    don’t need to learn write and maintain Hadoop and spark code.  The
    product has 900+ inbuild components feature data integration
     
    Talend features multiple products that simplify the digital
    transformation tools such as Big data integration, Data
    integration, Data Quality, Data Preparation, Cloud Integration,
    Application Integration, Master Data management, Metadata Manager.
    Talend Integration cloud is secure and managed integration
    Platform-as-a-service (iPaas), for connecting, cleansing and
    sharing cloud on premise data.

28. Pentaho

    Pentaho is a business intelligence corporation that provides data
    mining, reporting, dashboarding and data integration
    capabilities. Generally, organizations tend to obtain meaningful
    relationships and useful information from the data present with
    them. Pentaho addresses the obstacles that obstruct them from
    doing so :cite:`pent1`. The platform includes a wide range of
    tools that analyze, explore, visualize and predict data easily
    which simplifies blending any data. The sole objective of pentaho
    is to translate data into value. Being an open and extensible
    source, pentaho provides big data tools to extract, prepare and
    blend any data :cite:`pent2`. Along with this, the visualizations
    and analytics will help in changing the path that the
    organizations follow to run their business. From spark and hadoop
    to noSQL, pentaho transforms big data into big insights.

29. Apatar
30. Docker Compose

    Docker is an open-source container based technology.A container
    allows a developer to package up an application and all its part
    includig the stack it runs on, dependencies it is associated with
    and everything the application requirs to run within an isolated
    enviorment . Docker seperates Application from the underlying
    Operating System in a similar way as Virtual Machines seperates
    the Operating System from the underlying Hardware.Dockerizing an
    application is very lightweight in comparison with running the
    application on the Virtual Machine as all the containers share the
    same underlying kernel, the Host OS should be same as the
    container OS (eliminating guest OS) and an average machine cannot
    have more than few VMs running o them.

    :cite:'docker-book' Docker Machine is a tool that lets you install
    Docker Engine on virtual hosts, and manage the hosts with
    docker-machine commands. You can use Machine to create Docker
    hosts on your local Mac or Windows box, on your company network,
    in your data center, or on cloud providers like AWS or Digital
    Ocean. For Docker 1.12 or higher swarm mode is integerated with
    the Docker Engine, but on the older versions with Machine's swarm
    option, we can configure a swarm cluster Docker Swarm provides
    native clustering capabilities to turn a group of Docker engines
    into a single, virtual Docker Engine. With these pooled resources
    ,:cite:'www-docker'"you can scale out your application as if it
    were running on a single, huge computer" as swarm can be scaled
    upto 1000 Nodes or upto 50,000 containers
    
31. KeystoneML
    
    A framework for building and deploying large-scale
    machine-learning pipelines within Apache Spark. It captures and
    optimizes the end-to-end large-scale machine learning applications
    for high-throughput training in a distributed environment with a
    high-level API :cite:`sparks2016keystoneml`. This approach
    increases ease of use and higher performance over existing systems
    for large scale learning :cite:`sparks2016keystoneml`. It is
    designed to be a faster and more sophisticated alternative to
    SparkML, the machine learning framework that’s a full member of
    the Apache Spark club. Whereas SparkML comes with a basic set of
    operators for processing text and numbers, KeystoneML includes a
    richer set of operators and algorithms designed specifically for
    natural language processing, computer vision, and speech
    processing :cite:`building`. It has enriched set of operations for
    complex domains:vision,NLP,Speech, plus,advanced math And is
    Integrated with new BDAS technologies: Velox, ml-matrix, soon
    Planck, TuPAQ and Sample Clean :cite:`spark`.


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

    MLlib is Apache Spark’s scalable machine learning library
    :cite:`www-mllib`. Its goal is to make machine learning scalable
    and easy. MLlib provides various tools such as, algorithms,
    feature extraction, utilities for data handling and tools for
    constructing, evaluating, and tuning machine learning
    pipelines. MLlib uses the linear algebra package Breeze, which
    depends on netlib-java for optimized numerical processing. MLlib
    is shipped with Spark and supports several languages which
    provides functionality for wide range of learning settings. MLlib
    library includes Java, Scala and Python APIs and is released as a
    part of Spark project under the Apache 2.0 license
    :cite:`MLlib-article`.

34. MLbase
    
    MLBase :cite:`www-mlbase` is a distributed machine learning
    system built with Apache Spark :cite:`www-spark`. Machine Learning
    (ML) and Statistical analysis are tools for extracting insights
    from big data. MLbase is a tool for execute machine learning
    algorithms on a scalable platform.It consist of three components
    MLLib, MLI and ML Optimizer. MLLib was initially developed as a
    part of MLBase project but is now a part of Apache Spark. MLI is
    an experimental API for developing ML algorithm and to extract
    information. It provides high-level abstraction to the core ML
    algorithms. A prototype is currently implemented against Spark. ML
    optimizer on the other hand is use to automate the MLI pipeline
    construction. It solves for the search problem over feature
    extractors and ML algorithms included in MLI and ML lib. This
    library is its in early stage and under active
    development. Publications like :cite:`mlbasepub1`,
    :cite:`mlbasepub2` and :cite:`mlbasepub3` are available on
    distributed machine learning with MLBase.


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

    R, a GNU project, is a successor to S - a statistical programming
    language. It offers a range of capabilities – "programming
    language, high level graphics, interfaces to other languages and
    debugging". "R is an integrated suite of software facilities for
    data manipulation, calculation and graphical display". The
    statistical and graphical techniques provided by R make it popular
    in the statistical community. The statistical techniques provided
    include linear and nonlinear modelling, classical statistical
    tests, time-series analysis, classification and clustering to name
    a few :cite:`www-R`. The number of packages available in R has
    made it popular for use in machine learning, visualization, and
    data operations tasks like data extraction, cleaning, loading,
    transformation, analysis, modeling and visualization. It's
    strength lies in analyzing data using its rich library but falls
    short when working with very large datasets :cite:`book-R`.
    
37. pbdR

    Programming with Big Data in R (pbdR) :cite:`www-pbdR` is an
    environment having series of R packages for statistical computing
    with Big Data using high-performance statistical computation. It
    uses R, a popular language between statisticians and data
    miners. *pbdR* focuses on distributed memory system, where data is
    distributed accross several machines and processed in batch
    mode. It uses MPI for inter process communications. R focuses on
    single machines for data analysis using a interactive
    GUI. Currenly there are two implementation of pbdR, one Rmpi and
    another being pdbMpi.  Rmpi uses SPMD parallelism while pbdRMpi
    uses manager/worker parallelism.

38. Bioconductor

    Bioconductor is an open source and open development platform used
    for analysis and understanding of high throughput genomic
    data. Bioconductor is used to analyze DNA microarray, flow,
    sequencing, SNP, and other biological data. All contributions to
    Bioconductor are under an open source
    license. :cite:`bioconductor-article-2004` describes the goals of
    Bioconductor "include fostering collaborative development and
    widespread use of innovative software, reducing barriers to entry
    into interdisciplinary scientific research, and promoting the
    achievement of remote reproducibility of research results"
    :cite:`www-bioconductor-about` described that Bioconductor is
    primarily based on R, as most components of Bioconductor are
    released in R packages. Extensive documentation is provided for
    each Bioconductor package as vignettes, which include
    task-oriented descriptions for the functionalities of each
    package. Bioconductor has annotation functionality to associate
    "genemoic data in real time with biological metadata from web
    databases such as GenBank, Entrez genes and PubMed."  Bioconductor
    also has tools to process genomic annotation data.
    
39. ImageJ

    ImageJ is a Java-based image processing program developed at the
    National Institutes of Health (NIH). ImageJ was designed with an
    open architecture that provides extensibility via Java plugins and
    recordable macros.  Using ImageJ's built-in editor and a Java
    compiler, it has enabled to solve many image processing and
    analysis problems in scientifif research from three-dimensional
    live-cell imaging to radiological image processing.  ImageJ's
    plugin architecture and built-in development environment has made
    it a popular platform for teaching image
    processing. :cite:`www-imagej`

40. OpenCV

    OpenCV stands for Open source Computer Vision. It was designed for
    computational efficiency and with a strong focus on real-time
    applications. It has C++, C, Python and Java interfaces and
    supports Windows, Linux, Mac OS, iOS and Android. It can take
    advantage of the hardware acceleration of the underlying
    heterogeneous compute platform as it is enabled with OpenCL(Open
    Computing Language) :cite:`www-opencv`. OpenCV 3.2 is the latest
    version of the software that is currently available
    :cite:`opencv-version`.

41. Scalapack

    ScaLAPACK is a library of high-performance linear algebra routines for
    parallel distributed memory machines. It solves dense and banded
    linear systems, least squares problems, eigenvalue problems, and
    singular value problems. It is designed for heterogeneous computing
    and is portable on any computer that supports Message Passing
    Interface or Parallel Virtual Machine. :cite:`www-scalapack`

    ScaLAPACK is a open source software package and is available from
    netlib via anonymous ftp and the World Wide Web. It contains driver
    routines for solving standard types of problems, computational
    routines to perform a distinct computational task, and auxiliary
    routines to perform a certain subtask or common low-level
    computation. ScaLAPACK routines are based on block-partitioned
    algorithms in order to minimize the frequency of data movement between
    different levels of the memory hierarchy.
    
42. PetSc
43. PLASMA MAGMA

    PLASMA is built to address the performance shortcomings of the
    LAPACK and ScaLAPACK libraries on multicore processors and
    multi-socket systems of multicore processors and their inability
    to efficiently utilize accelerators such as Graphics Processing
    Units (GPUs). Real arithmetic and complex arithmetic are supported
    in both single precision and double precision.  PLASMA has been
    designed by restructuring the software to achieve much greater
    efficiency, where possible, on modern computers based on multicore
    processors. PLASMA does not support band matrices and does not
    solve eigenvalue and singular value problems. Also, PLASMA does
    not replace ScaLAPACK as software for distributed memory
    computers, since it only supports shared-memory
    machines. :cite:`paper-plasma-magma-1` :cite:`www-plasma-1` Recent
    activities of major chip manufacturers, such as Intel, AMD, IBM
    and NVIDIA, make it more evident than ever that future designs of
    microprocessors and large HPC systems will be hybrid/heterogeneous
    in nature, relying on the integration (in varying proportions) of
    two major types of components: :cite:`paper-plasma-magma-2`
    :cite:`paper-plasma-magma-3`
    1. Many-cores CPU technology, where the number of cores will
    continue to escalate because of the desire to pack more and more
    components on a chip while avoiding the power wall, instruction
    level parallelism wall, and the memory wall;
    2. Special purpose hardware and accelerators, especially Graphics
    Processing Units (GPUs), which are in commodity production, have
    outpaced standard CPUs in floating point performance in recent
    years, and have become as easy, if not easier to program than
    multicore CPUs.  While the relative balance between these
    component types in future designs is not clear, and will likely to
    vary over time, there seems to be no doubt that future generations
    of computer systems, ranging from laptops to supercomputers, will
    consist of a composition of heterogeneous components.
    :cite:`paper-plasma-magma-4`:cite:`paper-plasma-magma-5`:cite:`paper-plasma-magma-6`

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

    Google Prediction API & Translation API are part of Cloud ML API
    family with specific roles. Below is a description of each and
    their use.

    Google Prediction API provides pattern-matching and machine
    learning capabilities. Built on HTTP and JSON, the prediction API
    uses training data to learn and consecutively use what has been
    learned to predict a numeric value or choose a category that
    describes new pieces of data. This makes it easier for any
    standard HTTP client to send requests to it and parse the
    responses. The API can be used to predict what users might like,
    categorize emails as spam or non-spam, assess whether posted
    comments sentiments are positive or negative or how much a user
    may spend in a day. Prediction API has a 6 month limited free
    trial or a paid use for $10 per project which offers up to 10,000
    predictions a day :cite:`www-prediction`.

    Google Translation API is a simple programmatic interface for
    translating an arbitrary string into any supported
    language. Google Translation API is highly responsive allowing
    websites and applications to integrate for fast dynamic
    translation of source text from source language to a target
    language. Translation API also automatically identifies and
    translate languages with a high accuracy from over a hundred
    different languages.  Google Translation API is charged at $20 per
    million characters making it an affordable localization
    solution. Translation API is also distributed in two editions,
    premium edition which is tailored for users with precise long-form
    translation services like livestream, high volumes of emails or
    detailed articles and documents. There’s also standard edition
    which is tailored for short, real-time
    conversations :cite:`www-translation`.
46. mlpy
    
    mlpy is an open source python library made for providing machine
    learning functionality.It is built on top of popular existing
    python libraries of NumPy, SciPy and GNU scientific libraries
    (GSL).It also makes extensive use of Cython language. These form
    the prerequisites for
    mlpy. :cite:`DBLP:journals/corr/abs-1202-6548` explains the
    significanceq of its components: NumPy, SciPy provide
    sophisticated N-dimensional arrays, linear algebra functionality
    and a variety of learning methods, GSL, which is written in C,
    provides complex numerical calculation functionality.

    mlpy provides a wide range of machine learning methods for both
    supervised and unsupervised learning problems. mlpy is multiplatform
    and works both on Python 2 and 3 and is distributed under GPL3. Mlpy
    provides both classic and new learning algorithms for classification,
    regression and dimensionality reduction. :cite:`www-mlpy`
    provides a detailed list of functionality offered by mlpy. Though
    developed for general machine learning applications, mlpy has special
    applications in computational biology, particularly in functional
    genomics modeling.
    
47. scikit-learn

    Scikit-learn is an open source library that provides simple and
    efficient tools for data analysis and data mining. It is
    accessible to everybody and reusable in various contexts. It is
    built on numpy, Scipy and matplotlib and is commercially usable as
    it is distributed under many linux distributions
    :cite:`scik1`. Through a consistent interface, scikit-learn
    provides a wide range of learning algorithms. Scikits are the
    names given to the modules for SciPy, a fundamental library for
    scientific computing and as these modules provide different
    learning algorithms, the library is named as sciki-learn
    :cite:`scik2`. It provides an in-depth focus on code quality,
    performance, collaboration and documentation. Most popular models
    provided by scikit-learn include clustering, cross-validation,
    dimensionality reduction, parameter tuning, feature selection and
    extraction.

48. PyBrain :cite:`article-pybrain`

    The goal of PyBrain is to provide flexible, easyto-use algorithms
    that are not just simple but are also powerful for machine
    learning tasks. The algorithms implemented are Long Short-Term
    Memory (LSTM), policy gradient methods, (multidimensional)
    recurrent neural networks and deep belief networks. These
    algorithms include a variety of predefined environments and
    benchmarks to test and compare algorithms.

    PyBrain provides a toolbox for supervised, unsupervised and
    reinforcement learning as well as black-box and multi-objective
    optimization as it is much larger than Python libraries.

    PyBrain implements many recent learning algorithms and
    architectures while emphasizing on sequential and nonsequential
    data and tasks. These algorithms range from areas such as
    supervised learning and reinforcement learning to direct search /
    optimization and evolutionary methods.  For application-oriented
    users, PyBrain contains reference implementations of a number of
    algorithms at the bleeding edge of research and this is in
    addition to standard algorithms which are not available in Python
    library. Besides this PyBrain sets itself apart by its versatility
    for composing custom neural networks architectures that range from
    (multi-dimensional) recurrent networks to restricted Boltzmann
    machines or convolutional networks.
    
49. CompLearn

    Complearn is a system that makes use of data compression
    methodologies for mining patterns in a large amount of data. So,
    it is basically a compression-based machine learning system. For
    identifying and learning different patterns, it provides a set of
    utilities which can be used in applying standard compression
    mechanisms. The most important characteristic of complearn is its
    power in mining patterns even in domains that are unrelated. It
    has the ability to identify and classify the language of different
    bodies of text :cite:`comp1`. This helps in reducing the work of
    providing background knowledge regarding a particular
    classification. It provides such generalization through a library
    that is written in ANSI C which is portable and works in many
    environments :cite:`comp1`. Complearn provides immediate to access
    every core functionality in all the major languages as it is
    designed to be extensible.

50. DAAL(Intel)

    DAAL stands for Data Analytics Acceleration Library. DAAL is
    software library offered by Intel which is written in C++, python,
    and Java which implements algorithm for doing efficient and
    optimized data analysis tasks to solve big-data
    problems. :cite:`www-daal-wiki`. The library is designed to use
    data platforms like Hadoop, Spark, R, and Matlab.The important
    algorithms which DAAL implements are 'Lower Order Moments' which
    is used to find out max, min standard deviation of a dataset,
    'Clustering' which is used to do unsupervised learning by grouping
    data into unlabelled group.It also inlude 10-12 other important
    algorithms.

    :cite:`www-daal-official` It supports three processing modes
    namely batch processing, online processing and distributed
    processing.Intel DAAL addresses all stages of data analytics
    pipeline namely pre-processing, transformation, analysis,
    modelling,validation, and decision making.
    
    
51. Caffe

    Caffe is a deep learning framework made with three terms namely
    expression, speed and modularity :cite:`www-caffe`. Using
    Expressive architecture, switching between CPU and GPU by setting
    a single flag to train on a GPU machine then deploy to commodity
    cluster or mobile devices.Here the concept of configuration file
    will comes without hard coding the values . Switching between CPU
    and GPU can be done by setting a flag to train on a GPU machine
    then deploy to commodity clusters or mobile devices.

    It can process over 60 million images per day with a single NVIIA
    k40 GPU It is being used bu academic research projects, startup
    prototypes, and even large-scale industrial applications in
    vision, speech, and multimedia.
    
52. Torch

    Torch is a open source machine learning library, a scientific
    computing framework :cite:`www-torch` .It implements LuaJIT
    programming language and implements C/CUDA. It implements
    N-dimensional array. It does routines of indexing, slicing,
    transposing etc. It has in interface to C language via scripting
    language LuaJIT. It supports different artificial intelligence
    models like neural network and energy based models. It is
    compatible with GPU.  The core package of is ‘torch’. It provides
    a flexible N dimensional array which supports basic routings. It
    has been used to build hardware implementation for data flows like
    those found in neural networks.
    
    
53. Theano
    
    Theano is a Python library. It was written at the LISA lab.
    Initially it was created with the purpose to support efficient
    development of machine learning(ML) algorithms.  Theano uses
    recent GPUs for higher speed.  It is used to evaluate mathematical
    expressions and especially those mathematical expressions that
    include multi-dimensional arrays.  Theano’s working is dependent
    on combining aspects of a computer algebra system and an
    optimizing compiler.  This combination of computer algebra system
    with optimized compilation is highly beneficial for the tasks
    which involves complicated mathematical expressions and that need
    to be evaluated repeatedly as evaluation speed is highly critical
    in such cases.  It can also be used to generate customized C code
    for number of mathematical operations.  For cases where many
    different expressions are there and each of them is evaluated just
    once, Theano can minimize the amount of compilation and analyses
    overhead :cite:`www-theano`.
    
54. DL4j

    DL4j stands for Deeplearning4j. :cite:`www-dl4j` It is a deep
    learning programming library written for Java and the Java virtual
    machine (JVM) and a computing framework with wide support for deep
    learning algorithms. Deeplearning4j includes implementations of
    the restricted Boltzmann machine, deep belief net, deep
    autoencoder, stacked denoising autoencoder and recursive neural
    tensor network, word2vec, doc2vec, and GloVe. These algorithms all
    include distributed parallel versions that integrate with Apache
    Hadoop and Spark. It is a open-source software released under
    Apache License 2.0.

    Training with Deeplearning4j occurs in a cluster. Neural nets are
    trained in parallel via iterative reduce, which works on
    Hadoop-YARN and on Spark. Deeplearning4j also integrates with CUDA
    kernels to conduct pure GPU operations, and works with distributed
    GPUs.
	
55. H2O

    It is an open source software for big data analysis. It was
    launched by the Start-up H2O in 2011. It provides an in-memory,
    distributed, fast and a scalable machine learning and predictive
    analytics platform that allows the users to build machine learning
    models on big data :cite:`www-H2O-website`. It is written in
    Java. It is currently implemented in 5000 companies. It provides
    APIs for R(3.0.0 or later), Python(2.7.x, 3.5.x), Scala(1.4-1.6)
    and JSON :cite:`www-H2O-book`. The software also allows online
    scoring and modeling on a single platform.  It is scalable and has
    a wide range of OS and language support. It works perfectly on the
    conventional operating systems, and big data systems such as
    Hadoop, Cloudera, MapReduce, HortonWorks.  It can be used on cloud
    computing environments such as Amazon and Microsoft Azure
    :cite:`www-H2O-wiki`.


56. IBM Watson

    IBM Watson :cite:`www-ibmwatson-wiki` is a super computer built on
    cognitive technology that processes information like the way human
    brain does by understanding the data in a natural language as well
    as analyzing structured and unstructured data. It was initially
    developed as a question and answer tool more specifically to
    answer questions on the quiz show *Jeopardy* but now it has been
    seen as helping doctors and nurses in the treatment of cancer. It
    was developed by IBM's DeepQA research team led by David
    Ferrucci. :cite:`www-ibmwatson` illustrates that with Watson you
    can create bots that can engage in conversation with you. You can
    even provide personalized recommendations to Watson by
    understanding a user's personality, tone and emotion. Watson uses
    the Apache Hadoop framework in order to process the large volume
    of data needed to generate an answer by creating in-memory
    datasets used at run-time. Watson's DeepQA UIMA (Unstructured
    Information Management Architecture) annotators were deployed as
    mappers in the Hadoop Map-Reduce framework. Watson is written in
    multiple programming languages like Java, C++, Prolog and it runs
    on the SUSE Linux Enterprise Server. :cite:`www-ibmwatson`
    mentions that today Watson is available as a set of open source
    APIs and Software As a Service product as well.
    
57. Oracle PGX

    Numerous information is revealed from graphs. Information like
    direct and indirect relations or patterns in the elements of the
    data, can be easily seen through graphs. The analysis of graphs
    can unveil significant insights. Oracle PGX (Parallel Graph
    AnalytiX) is a toolkit for graph analysis.  "It is a fast,
    parallel, in-memory graph analytic framework that allows users to
    load up their graph data, run analytic algorithms on them, and to
    browse or store the result" :cite:`www-pgx`. Graphs can be loaded
    from various sources like SQL and NoSQL databases, Apache Spark
    and Hadoop :cite:`www-ora`.
    
58. GraphLab

    GraphLab :cite:`www-graphlab` is a graph-based, distributed
    computation, high performance framework for machine learning
    written in C++. It is an open source project started by
    Prof. Carlos Guestrin of Carnegie Mellon University in 2009,
    designed considering the scale, variety and complexity of real
    world data. It integrates various high level algorithms such as
    Stochastic Gradient Descent, Gradient Descent & Locking and
    provides high performance experience. It includes scalable machine
    learning toolkits which has implementation for deep learning,
    factor machines, topic modeling, clustering, nearest neighbors and
    almost everything required to enhance machine learning
    models. This framework is targeted for sparse iterative graph
    algorithms. It helps data scientists and developers easily create
    and install applications at large scale.
    
59. GraphX

    GraphX is Apache Spark's API for graph and graph-parallel
    computation.  :cite:`www-graphX`
	  
    GraphX provides:
    
    Flexibility: It seamlessly works with both graphs and
    collections. GraphX unifies ETL, exploratory analysis, and
    iterative graph computation within a single system. You can view
    the same data as both graphs and collections, transform and join
    graphs with RDDs efficiently, and write custom iterative graph
    algorithms using the Pregel API.
    
    Speed: Its performance is comparable to the fastest specialized
    graph processing systems while retaining Apache Spark's
    flexibility, fault tolerance, and ease of use.
    
    Algorithms: GraphX comes with a variety of algorithms such as
    PageRank, Connected Components, Label propagations, SVD++,
    Strongly connected components and Triangle Count.

    It combines the advantages of both data-parallel and
    graph-parallel systems by efficiently expressing graph
    computataion within the Spark data-parallel
    framework. :cite:`www-graphX1`

    It gets developed as a part of Apache Spark project. It thus gets
    tested and updated with each Spark release.
    
60. IBM System G

    IBM System G provides a set of Cloud and Graph computing tools and
    solutions for Big Data :cite:`IBMSystemGDocumentation-1`.  In
    fact, the G stands for Graph and typically spans a database,
    visualization, analytics library, middleware and Network Science
    Analytics tools.  It assists the easy creating of graph stores 
    and queries and exploring them via interactive visualizations 
    :cite:`IBMSystemGDocumentation-2`.  Internally, it uses the property
    graph model for its working.  It consists of five individual
    components - gShell, REST API, Python interface to gShell, Gremlin
    and a Visualizer.  Some of the typical applications wherein it
    can be used include Expertise Location, Commerce, Recommendation, 
    Watson, Cybersecurity, etc :cite:`IBMSystemGPaper`.

    However, it is to be noted that the current version does not work
    in a distributed environment and it is planned that future
    versions would support it.
    
61. GraphBuilder(Intel)

    Intel GraphBuilder for Apache Hadoop V2 is a software that is used
    to build graph data models easily enabiling data scientists to
    concentrate more on the business solution rather than
    preparing/formatting the data. The software automates a)Data
    cleaning, b)transforming data and c)creating graph models with
    high throughput parallel processing using hadoop, with the help of
    prebuilt libraries. Intel Graph Builder helps to speed up the time
    to insight for data scientists by automating heavy custom
    workflows and also by removing the complexities of cluster
    computing for constructing graphs from Big Data. Intel Graph
    Building uses Apache Pig scripting language to simplify data
    preparation pipeline.  "Intel Graph Builder also includes a
    connector that parallelizes the loading of the graph output into
    the Aurelius Titan open source graph database—which further speeds
    the graph processing pipeline through the final stage".  Finally
    being an open source there is a possibility of adding a load of
    functionalities by various contributors.:cite:`graphbuilder`

    
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

    The parasol laboratory is a multidisciplinary research program 
    founded at Texas A&M University with a focus on next generation 
    computing languages.  The core focus is centered around algorithm 
    and application development to find solutions to data concentrated 
    problems. :cite:`www-parasol` The developed applications are being 
    applied in the following areas: computational biology, geophysics, 
    neuroscience, physics, robotics, virtual reality and computer aided 
    drug design(CAD).  The program has organized a number of workshops 
    and conferences in the areas such as software, intelligent systems, 
    and parallel architecture.
    
64. Dream:Lab

    DREAM:Lab stands for "Distributed Research on Emerging
    Applications and Machines Lab." :cite:`dream` DREAM:Lab is
    centered around distributed systems research to enable expeditious
    utilization of distributed data and computing
    systems. :cite:`dream` DREAM:Lab utilizes the "capabilities of
    hundereds of personal computers" to allow access to supercomputing
    resources to average individuals. :cite:`rao` The DREAM:Lab
    pursues this goal by utilizing distributed computing. :cite:`rao`
    Distributed computing consists of independent computing resources
    that communicate with each other over a network. :cite:`denero` A
    large, complex computing problem is broken down into smaller, more
    manageable tasks and then these tasks are distributed to the
    various components of the distributed computing
    system. :cite:`denero`
    
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
    table called *Rows*, user can merge the multiple table in to one,
    from multiple users. "Megastore is a library on top of
    bigtable". :cite:`GoogleFusionTable2012` Data visualization is one
    the feature, where user can see the visual representation of their
    data as soon as they upload it. User can store the data along with
    geospatial information as well.

66. CINET

    A representation of connected entities such as "physical,
    biological and social phenomena" :cite:`www-bi-vt-edu` predictive
    model. Network science has grown its importance understanding
    these phenomena Cyberinfrastructure is middleware tool helps study
    Network science, :cite:`www-portal-futuresystems-org-projects-233`
    "by providing unparalleled computational and analytic environment
    for researcher".
 
    Network science involves study of graph a large volume which
    requires high power computing which usually cant be achieve by
    desktop. Cyberinfrastructure provides cloud based infrastructure
    (e.g. FutureGrid) as well as use of HPC (e.g. Shadowfax,
    Pecos). With use of advance intelligent Job mangers, it select the
    infrastructure smartly suitable for submitted job.
     
    It provides structural and dynamic network analysis, has number of
    algorithms for "network analysis such as shortest path, sub path,
    motif counting, centrality and graph traversal". CiNet has number
    of range of network visualization modules.  CiNet is actively
    being used by several universities, researchers and analysist.

67. NWB

    :cite:`www-nwb.edu` NWB stands for Network workbench is analysis,
    modelling and visualization toolkit for the network scientists.
    It provides an environment which help scientist researchers and
    practitioner to get online access to the shared resource
    environment and network datasets for analysis, modelling and
    visualization of large scale networking application.  User can
    access this network datasets and algorithms previously obtained by
    doing lot of research and can also add their own datasets helps in
    speeding up the process and saving the time for redoing the same
    analysis.

    NWB provides advanced tools for users to understand and interact
    with different types of networks.  NWB members are largely the
    computer scientist, biologist, engineers, social and behavioural
    scientist. The platform helps the specialist researchers to
    transfer the knowledge within the broader scientific and research
    communities.
	
68. Elasticsearch

    Elasticsearch :cite:`www-elasticsearch` is a real time
    distributed, RESTful search and analytics engine which is capable
    of performing full text search operations for you. It is not just
    limited to full text search operations but it also allows you to
    analyze your data, perform CRUD operations on data, do basic text
    analysis including tokenization and
    filtering. :cite:`www-elasticsearch-intro` For example while
    developing an E-commerce website, Elasticsearch can be used to
    store the entire product catalog and inventory and can be used to
    provide search and autocomplete suggestions for the
    products. Elasticsearch is developed in Java and is an open source
    search engine which uses standard RESTful APIs and JSON on
    top of Apache's Lucene - which is a full text search engine
    library. Clinton Gormley & Zachary Tong :cite:`elasticsearch-book`
    describes elastic search as "A distributed real time document
    store where every field is indexed and searchable". They also
    mention that "Elastic search is capable of scaling to hundreds of
    servers and petabytes of structured and unstructured
    data". :cite:`www-elasticsearch-hadoop` mentions that Elastic
    search can be used on big data by using the Elasticsearch-Hadoop
    (ES-Hadoop) connector. ES-Hadoop connector lets you index the
    Hadoop data into the Elastic Stack to take full advantage of the
    Elasticsearch engine and returns output through Kibana
    visualizations. :cite:`www-wikipedia-elasticsearch` A log parsing
    engine "Logstash" and analytics and visualization platform
    *Kibana* are also developed alongside Elasticsearch forming a
    single package.
    
69. Kibana

    Kibana is an open source data visualization plugin for
    Elasticsearch. :cite:`www-kibana-1` It provides visualization
    capabilities on top of the content indexed on an Elasticsearch
    cluster. Users can create bar, line and scatter plots, or pie
    charts and maps on top of large volumes of
    data. :cite:`www-kibana-2` The combination of Elasticsearch,
    Logstash, and Kibana (also known as ELK stack or Elastic stack) is
    available as products or service. Logstash provides an input
    stream to Elastic for storage and search, and Kibana accesses the
    data for visualizations such as dashboards. :cite:`www-kibana-3`
    Elasticsearch is a search engine based on
    Lucene. :cite:`www-kibana-4` It provides a distributed,
    multitenant-capable full-text search engine with an HTTP web
    interface and schema-free JSON documents. Kibana makes it easy to
    understand large volumes of data. Its simple, browser-based
    interface enables you to quickly create and share dynamic
    dashboards that display changes to Elasticsearch queries in real
    time. :cite:`www-kibana-5` :cite:`www-kibana-6`

70. Logstash

    Logstash is an open source data collection engine with real-time
    pipelining capabilities. Logstash can dynamically unify data from
    disparate sources and normalize the data into destinations of your
    choice. :cite:`www-logstash` Cleanse and democratize all your data
    for diverse advanced downstream analytics and visualization use
    cases.

    While Logstash originally drove innovation in log collection, its
    capabilities extend well beyond that use case. Any type of event
    can be enriched and transformed with a broad array of input,
    filter, and output plugins, with many native codecs further
    simplifying the ingestion process. Logstash accelerates your
    insights by harnessing a greater volume and variety of data.
	
71. Graylog

    Graylog is an open source log management tool that allows an
    organization to assemble, organize and analyze large amounts of
    data from its network activity. It collects and aggregates events
    from a group of sources and presents data in a streamlines,
    simplified interface where one can drill down to significant
    metrics, identify key relationships, generate powerful data
    visualizations and derive actionable insights
    :cite:`www-graylog-blog`.  Graylog allows us to centrally collect
    and manage log messages of an organization's complete
    infrastructure :cite:`www-graylog-optimization`. A user can
    perform search on terrabytes of log data to discover number of
    failed logins,find application errors across all servers or
    monitor the acivity of a suspicious user id.Graylog works on top
    of ElasticSearch and MongoDB to facilitate this high availability
    searching.  Graylog provides visualization through creation of
    dashboards that allows a user to build pre-defined views on his
    data to assemble all of his important data only a single click
    away :cite:`www-graylog-dashboards`. Any search result or metric
    shall be added as a widget on the dashboard to observe trends in
    one single location. These dashboards can also be shared with
    other users in the organization. Based on a user's recent search
    queries,graylog also allows you to distinguish data that are not
    searched upon very often and thus can be archived on cost
    effective storage drives. Users can also add certain trigger
    conditions that shall alert the system about performance issues,
    failed logins or exceptions in the flow of the application.
    
72. Splunk

    Splunk is a platform for big data analytics. It is a software
    product that enables you to search, analyze, and visualize the
    machine-generated data gathered from the websites, applications,
    sensors, devices, and so on, that comprise your IT infrastructure
    or business :cite:`www-splunk`. After defining the data source,
    Splunk indexes the data stream and parses it into a series of
    individual events that you can view and search. It provides
    distributed search and MapReduce linearly scales search and
    reporting. It uses a standard API to connect directly to
    applications and devices. It was developed in response to the
    demand for comprehensible and actionable data reporting for
    executives outside a company's IT department :cite:`www-splunk`.
	  
73. Tableau

    :cite:`www-tableau-tutorial` Tableau is a family of interactive
    data visualization products focused on business intelligence. The
    different products which tableau has built are: Tableau Desktop,
    for individual use; Tableau Server for collaboration in an
    organization; Tableau Online, for Business Intelligence in the
    Cloud; Tableau Reader, for reading files saved in Tableau Desktop;
    Tableau Public, for journalists or anyone to publish interactive
    data online.  :cite:`www-tableau-web` Tableau uses VizQL as a
    visual query language for translating drag-and-drop actions into
    data queries and later expressing the data visually. Tableau also
    benefits from an Advanced In-Memory Technology for handling large
    amounts of data.  The strengths of Tableau are mainly the ease of
    use and speed.  However, it has a number of limitations, which the
    most prominent are unfitness for broad business and technical
    user, being closed-source, no predictive analytical capabilities
    and no support for expanded analytics.

74. D3.js

    D3.js is a JavaScript library responsible for manipulating
    documents based on data. D3 helps in making data more interactive
    using HTML, SVG, and CSS. D3’s emphasis on web standards makes it
    framework independent utilizing the full capabilities of modern
    browsers, combining powerful visualization components and a
    data-driven approach to DOM manipulation :cite:`www-d3`.

    It assists in binding random data to a Document Object Model
    (DOM), followed by applying data-driven transformations to the
    document. It is very fast, supports large datasets and dynamic
    behaviours involving interaction and animation.

    
75. three.js

    Three.js is an API library with about 650 contributions till date
    , where users can create and display an animated 3D computer
    graphics in a web browser.It is written in javascript and uses
    WebGL, HTML5 or SVG. Users can animate HTML elements using CSS3 or
    even import models from 3D modelling apps
    :cite:`www-threejs-wiki`. In order to display anything using
    three.js we need three basic features, which are scene, camera and
    renderer. This will result in rendering the scene with a
    camera. In addition to these three features , we can add
    animation, lights (ambience,spot lights, shadows), objects (lines
    , ribbons , particles) , geometry etc :cite:`www-threejs-webpage`.
    
76. Potree

    Potree :cite:`www-potree` is a opensource tool powered by WebGL
    based viewer to visualize data from large point clouds. It started
    at the TU Wien, institute of Computer Graphics and Algorithms and
    currently begin continued under the Harvest4D project. Potree
    relies on reorganizing the point cloud data into an
    multi-resolution octree data structure which is time consuming. It
    efficiency can be improved by using techiques such as divide and
    conquer as disscused in a conference paper Taming the beast: Free
    and Open Source massive cloud point cloud web
    visualization :cite:`potree-paper-1`. It has also been widely used
    in works involving spatio-temporal data where the changes in
    geographical features are across time :cite:`potree-paper-2`.
    
77. DC.js

    According to :cite:`www-dcjs`: "DC.js is a javascript charting
    library with native crossfilter support, allowing exploration on
    large multi-dimensional datasets. It uses d3 to render charts in
    CSS-friendly SVG format. Charts rendered using dc.js are data
    driven and reactive and therefore provide instant feedback to user
    interaction." DC.js library can be used to perform data anlysis
    on both mobile devices and different browsers. Under the dc
    namespace the following chart classes are included: barChart,
    boxplot, bubbleChart, bubbleOverlay, compositeChart, dataCount,
    dataGrid, dataTable, geoChoroplethChart, heatMap,
    legend,lineChart, numberDisplay, pieChart, rowChart, scatterPlot,
    selectMenu and seriesChart.
      
78. TensorFlow

    TensorFlow is a platform that provides a software library for
    expressing and executing machine learning
    algorithms. :cite:`tensorflow-paper-2016` states TensorFlow has a
    flexible architecture allowing it to be executed with minimal
    change to many hetegeneous systems such as CPUs and GPUs of mobile
    devices, desktop machines, and servers. TensorFlow can "express a
    wide variety of algorithms, including training and inference
    algorithms for deep neural netowrk models, and it has been used
    for conducting research and for deploying machine learning systems
    into production across more than a dozen
    areas". :cite:`www-tensorflow` describes that TensorFlow utilizes
    data flow graphs in which the "nodes in the graph represent
    mathematical operations, while the graph edges represent the
    multidimensional data arrays (tensors) communicated between them."
    TensorFlow was developed by the Google Brain Team and has a
    reference implementation that was released on 2015-11-09 under the
    Apache 2.0 open source license.
    
79. CNTK

    The Microsoft Cognitive Toolkit - CNTK - is a unified
    deep-learning toolkit by Microsoft Research. It is in essence an
    implementation of Computational Network(CN) which supports both
    CPU and GPU. CNTK supports arbitrary valid computational networks
    and makes building DNNs, CNNs, RNNs, LSTMS, and other complicated
    networks as simple as describing the operations of the networks.
    The toolkit is implemented with efficiency in mind. It removes
    duplicate computations in both forward and backward passes, uses
    minimal memory needed and reduces memory reallocation by reusing
    them. It also speeds up the model training and evaluation by doing
    batch computation whenever possible :cite:`book-cntk` . It can be
    included as a library in your Python or C++ pro grams, or used as
    a standalone machine learning tool through its own model
    description language (BrainScript). :cite:`www-cntk` Latest
    Version:2017-02-10. V 2.0 Beta 11 Release


Application Hosting Frameworks
------------------------------

80. Google App Engine

    Google App Engine is a cloud computing platform to host your
    mobile or web applications on Google managed servers. Google App
    Engine provides automatic scaling for web applications, i.e it
    automatically allocates more resources to the application upon
    increase in the number of requests. It gives developers the
    freedom to focus on developing their code and not worry about the
    infrastructure. Google App Engine provides built-in services and
    APIs such as load balancing, automated security scanning,
    application logging, NoSQL datastores, memcache, and a user
    authentication API, that are a core part to most
    applications :cite:`www-appengine-google`.
     
    An App Engine platform can be run in either the Standard or the
    Flexible environment. Standard environment lays restrictions on
    the maximum number of resources an application can use and charges
    a user based on the instance hours used. The flexible environment
    as the name suggests provides higher flexibility in terms of
    resources and is charged based on the CPU and disk utilization.The
    App Engine requires developers to use only its supported languages
    and frameworks. Supported languages are Java, Python, Ruby, Scala,
    PHP, GO, Node.js and other JVM oriented languages. The App Engine
    datastore uses a SQL like syntax called the GQL (Google Query
    Language) which works with non-relational databases when compared
    to SQL :cite:`www-wiki-appengine`.
    
81. AppScale

    AppScale is an application hosting platform. This platform helps
    to deploy and scale the unmodified Google App Engine application,
    which run the application on any cloud infrastructure in public,
    private and on premise cluster. :cite:`www-appscale` AppScale
    provide rapid, API development platform that can run on any cloud
    infrastructure. The platform separates the app logic and its
    service part to have control over application deployment, data
    storage, resource use, backup and migration.  AppScale is based on
    Google’s App Engine APIs and has support for Python, Go, PHP and
    Java applications. It supports single and multimode deployment,
    which will help with large, dataset or CPU. AppScale allows to
    deploy app in thee main mode i.e. dev/test, production and
    customize deployment.  :cite:`www-appscale-deployment`

82. Red Hat OpenShift

    OpenShift was launched as a PaaS (Platform as a
    Service) by Red Hat in the Red Hat Summit, 2011 :cite:`www-paas-openshift`.
    It is a cloud application development and hosting platform that 
    envisages shifting of the developer's focus to development by 
    automating the management and scaling of applications 
    :cite:`www-developers-openshift`.  Thus, OpenShift :cite:`www-openshift` 
    enables us to write our applications in any one web development
    language (using any framework) and it itself takes up the task of
    running the application on the web.  This has its advantages and
    disadvantages - advantage being the developer doesn't have to
    worry about how the stuff works internally (as it is abstracted
    away) and the disadvantage being that he cannot control how it
    works, again because it is abstracted.

    OpenShift is powered by Origin, which is in turn built using 
    Docker container packaging and Kubernetes container cluster 
    :cite:`www-openshift-blog`.  Due to this, OpenShift offers a lot of
    options, including online, on-premise and open source project
    options.
    
83. Heroku

    Heroku :cite:`www-Heroku` is a platform as a service that is used
    for building, delivering monitoring and scaling applications. It
    lets you develop and deploy application quickly without thinking
    about irrelevant problems such as infrastructure. Heroku also
    provides a secure and scalable database as a service with number
    of developers’ tools like database followers, forking, data clips
    and automated health checks. It works by deploying to cedar stack
    :cite:`www-cedar`, an online runtime environment that supports
    apps buit in Java, Node.js, Scala, Clojure, Python and PHP. It
    uses Git for version controlling. It is also tightly intergrated
    with Salesforce, providing seamless and smooth Heroku and
    Salesforce data synchronization enabling companies to develop and
    design creative apps that uses both platforms.

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

    AWS Elastic Beanstalk is an orchestration service offered from
    Amazon Web Services which provides user with a platform for easy
    and quick deployment of their WebApps and services
    :cite:`www-amazon-elastic-beanstalk`. Amazon Elastic BeanStack
    automatically handles the deployment details of capacity
    provisioning by Amazon Cloud Watch, Elastic Load Balancing,
    Auto-scaling, and application health monitoring of the WebApps and
    service :cite:`amazon-elastic-beanstalk-book`. AWS Management
    Console allows the users to configure an automatic scaling
    mechanism of AWS Elastic Beanstalk. Elastic Load Balancing enables
    a load balancer, which automatically spreads the load across all
    running instances in an auto-scaling group based on metrics like
    request count and latency tracked by Amazon CloudWatch. Amazon
    CloudWatch tracks and stores per-instance metrics, including
    request count and latency, CPU, and RAM utilization. Elastic
    Beanstalk supports applications developed in Java, PHP, .NET,
    Node.js, Python, and Ruby as well as supports different container
    types for each language such as Apache Tomcat for Java
    applications, Apache HTTP Server for PHP applications Docker, GO
    and much more for specific languages where the container defines
    the infrastructure and software stack to be used for a given
    environment. "AWS Elastic Beanstalk runs on the Amazon Linux AMI
    and the Windows Server 2012 R2 AMI. Both AMIs are supported and
    maintained by Amazon Web Services and are designed to provide a
    stable, secure, and high-performance execution environment for
    Amazon EC2 Cloud computing":cite:`www-amazon-elastic-beanstalk`.

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

    It is an open source software with multi cloud application .It is
    a platform for running applications and services. It was
    originally developed by VMware and currently owned by Pivotal . It
    is written in Ruby and Go .It has a commercial version called
    Pivotal Cloud Foundry (PFC):cite:`www-cloudfoundry-book`. Cloud
    Foundry is available as a stand alone software package, we can
    also deploy it to Amazon AWS as well as host it on OpenStack
    server , HP’s Helion or VMware’s vSphere as given in the blog
    :cite:`www-cloudfoundry-blog` , it delivers quick application from
    development to deployment and is highly scalable. It has a DevOps
    friendly workflow.  Cloud Foundry changes the way application and
    services are deployed and reduces the develop to deployment cycle
    time.

88. Pivotal

    Pivotal Software, Inc. (Pivotal) is a software and services
    company. It offeres multiple consulting and technology services,
    which includes Pivotal Web Services, which is an agile application
    hosting service. It has a single step upload feature *cf push*,
    another feature called Buildpacks lets us push applications
    written for any language like Java, Grails, Play, Spring, Node.js,
    Ruby on Rails, Sinatra or Go. Pivotal Web Services also allows
    developers to connect to 3rd party databases, email services,
    monitoring and more from the Marketplace. It also offers
    performance monitoring, active health monitoring, unified log
    streaming, web console built for team-based agile development
    :cite:`pivotal-www`.

89. IBM BlueMix
90. (Ninefold)

    The Australian based cloud computing platform has shut down their
    services since January 30, 2016. Refer :cite:`www-ninefoldSite`

91. Jelastic

    Jelastic (acronym for Java Elastic) is an unlimited PaaS and
    Container based IaaS within a single platform that provides high
    availability of applications, automatic vertical and horizontal
    scaling via containerization to software development clients,
    enterprise businesses, DevOps, System Admins, Developers, OEMs and
    web hosting providers. :cite:`www-jelastic-2` Jelastic is a
    Platform-as-Infrastructure provider of Java and PHP hosting.  It
    has international hosting partners and data centers. The company
    can add memory, CPU and disk space to meet customer needs. The
    main competitors of Jelastic are Google App Engine, Amazon Elastic
    Beanstalk, Heroku, and Cloud Foundry.Jelastic is unique in that it
    does not have limitations or code change requirements, and it
    offers automated vertical scaling, application lifecycle
    management, and availability from multiple hosting providers
    around the world. :cite:`www-jelastic-1`

92. Stackato
    
    Hewlett Packard Enterprise or HPE Helion Stackato is a platform as
    a service(PaaS) cloud computing solution.  The platform
    facilitates deployment of the user’s application in the cloud and
    will function on top of an Infrastructure as a
    service(IaaS). :cite:`www-hpe` Multiple cloud development is
    supported across AWS, vSphere, and Helion Openstack.  The platform
    supports the following programming languages: native .NET support,
    java, Node.js, python, and ruby.  This flexibility is advantageous
    compared to early PaaS solutions which would force the customer
    into utilizing a single stack.  Additionally, this solution has
    the capacity to support private, public and hybrid clouds.
    :cite:`www-virt` This capability user has to not have to make
    choices of flexibility over security of sensitive data when
    choosing a cloud computing platform.
 
    
93. appfog

    According to :cite:`wee`, "AppFog is a platform as a service (PaaS)
    provider." Platform as a service provides a platform for the
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

    Cloudbees provides Platform as a Service (PaaS) solution, which is
    a cloud service for Java applications
    :cite:`www-cloudbees-wiki`. It is used to build, run and manage
    the web applications. It was created in 2010 by Jenkins. It has a
    continuous delivery platform for DevOps, and adds a
    enterprise-grade functionality with an expert level
    support. Cloudbees is better than the traditional Java platform as
    it requires no provision of the nodes, clusters, load balancers
    and databases. In cloudbees the environment is constantly managed
    and monitored where a metering and scale updating is done on a
    real time basis. The platform ships with verified security and
    enhancements assuring less risk for sharing sensitive
    information. It simplies the task of getting the platform accessed
    by every user using the feature *Jenkins Sprawl*
    :cite:`www-cloudbees-webpage`.

95. Engine Yard :cite:`www-engineyard`

    A deployment platform with fully managed services that combines
    high-end clustering resources to run Ruby and Rails applications
    in the cloud is offered by Engine Yard. It is designed as a
    platform-as-a-Service for Web application developers using Ruby on
    Rails, PHP and Node.js who requires the advantages of cloud
    computing. Amazon cloud is the platform where the Engine Yard
    perform its operations and accomplishes application stack for its
    users. Amazon allows as many as eight regions to Engine Yard to
    deploy its CPU instances in varying capacities such as normal,
    high memory and high CPU. According to customer requirements
    multiple software components are configured and processed when an
    instance is started in Engine Yard.
    
    Engine Yard builds its version on Gentoo Linux and has
    non-proprietary approach to its stack. The stack includes HAProxy
    load balancer, Ngnix and Rack Web servers, Passenger and Unicorn
    app servers, as well as MySQL and PostgreSQL relational databases
    in addition to Ruby, PHP, and Node.js The credibility of Engine
    Yard rests with orchestration and management as developers have
    option of performing functions in Amazon cloud. Standard
    operations management procedures are performed once the systems
    are configured and deployed. Key operations tasks such as
    performing backups, managing snapshots, managing clusters,
    administering databases and load balancing are taken care by
    Engine Yard.
    
    Engine Yard users are empowered as they have more control over
    virtual machine instances. These instances are dedicated instances
    and are not shared with other users. As the instances are
    independent every user can exercise greater control over instances
    without interferences with other users.

96. (CloudControl)

    No Longer active as of Feb. 2016 :cite:`www-wiki`

97. dotCloud :cite:`www-dotCloud`

    dotCloud services were shutdown on February 29,2016.
    

98. Dokku
99. OSGi
100. HUBzero
     
     HUBzero is a collaborative framework which allows creation of
     dynamic websites for scientific research as well as educational
     activities.  HUBzero lets scientific researchers work together
     online to develop simulation and modeling tools.  These tools can
     help you connect with powerful Grid computing resources as well
     as rendering farms.:cite:`hubzerowebsite` Thus allowing other
     researchers to access the resulting tools online using a normal
     web browser and launch simulation runs on the Grid infrastructure
     without having to download or compile any code. It is a unique
     framework with simulation and social networking
     capabilities.:cite:`hubzeropaper2010`

101. OODT
     
     The Apache Object Oriented Data Technology (OODT) is an open
     source data management system framework. OODT was originally
     developed at NASA Jet Propulsion Laboratory to support capturing,
     processing and sharing of data for NASA's scientific
     archives. OODT focuses on two canonical use cases: Big Data
     processing and on Information integration. It facilitates the
     integration of highly distributed and heterogeneous data
     intensive systems enabling the integration of different,
     distributed software systems, metadata and data. OODT is written
     in the Java, and through its REST API used in other languages
     including Python. :cite:`www-oodt2`
     
102. Agave

     Agave is an open source, application hosting framework and
     provides a platform-as-a-service solution for hybrid
     computing :cite:`agave-paper`. It provides everything ranging
     from authentication and authorization to computational, data and
     collaborative services. Agave manages end to end lifecycle of an
     application’s execution.  Agave provides an execution platform,
     data management platform, or an application platform through
     which users can execute applications, perform operations on their
     data or simple build their web and mobile
     applications :cite:`www-agaveapi-features`.

     Agave’s API’s provide a catalog with existing technologies and
     hence no additional appliances, servers or other software needs
     to be installed. To deploy an application from the catalog, the
     user needs to host it on a storage system registered with Agave,
     and submit to agave, a JSON file that shall contain the path to
     the executable file, the input parameters, and specify the
     desired output location. Agave shall read the JSON file,
     formalize the parameters, execute the user program and dump the
     output to the requested destination :cite:`agave-paper`.

103. Atmosphere

     Atmosphere is developed by CyVerse (previously named as iPlant
     Collaborative).  It is a cloud-computing platform. It allows one
     to launch his own "isolated virtual machine (VM) image
     :cite:`www-at1`.  It does not require any machine
     specification. It can be run on any device
     (tablet/desktop/laptop) and any machine(Linux/Windows/Max/Unix).
     User should have a CyVerse account and be granted permission to
     access to Atmosphere before he can begin using Atmosphere. No
     subscription is needed.  Atmosphere is designed to execute
     data-intense bioinformatics tasks that may include
     a)Infrastructure as a Service (IaaS) with advanced APIs;
     b)Platform as a Service (PaaS), and c)Software as a Service
     (SaaS).  On Atmosphere one has several images of virtual machine
     and user can launch any image or instance according to his
     requirements.  The images launched by users can be shared among
     different members as and when required :cite:`www-at2`.


High level Programming
----------------------

104. Kite

     Kite is a programming language designed to minimize the required
     experience level of the programmer.  It aims to allow quick
     development and running time and low CPU and memory usage. Kite
     was designed with lightweight systems in mind.  On OS X Leopard,
     the main Kite library is only 88KB, with each package in the
     standard library weighing in at 13-30KB. The main design
     philosophy is minimalism — only include the minimum necessary,
     while giving developers the power to write anything that they can
     write in other languages. Kite combines both object oriented and
     functional paradigms in the language syntax.  One special feature
     is its use of the pipe character (|) to indicate function calls,
     as opposed to the period (.) or arrow (->) in other languages.
     Properties are still de-referenced using the period
     :cite:`kite-devtopics`. Kite also offers a digital assistant for
     programmers. Kite offers a product which sits as a sidebar in
     code editor and enables programmers to search for opensource
     codes to implement in their codes. It even provides relavant
     examples/syntax and also tries to spot errors in the programs
     :cite:`kite-wired`.
	   
105. Hive
     
     The reason behind development of Hive is making it easier for end
     users to use Hadoop. Map reduce programs were required to be
     developed by users for simple to complex tasks. It lacked
     expressiveness like query language. So, it was a time consuming
     and difficult task for end users to use Hadoop. For solving this
     problem Hive was built in January 2007 and open sourced in
     August2008.  Hive is an open source data warehousing solution
     which is built on top of Hadoop. It structures data into
     understandable and conventional database terms like tables,
     columns, rows and partitions. It supports HiveQL queries which
     have structure like SQL queries. HiveQL queries are compiled to
     map reduce jobs which are then executed by Hadoop.  Hive also
     contains Metastore which includes schemas and statistics which is
     useful in query compilation, optimization and data exploration
     :cite:`www-hive`

106. HCatalog
107. Tajo

     Apache Tajo :cite:`www-apache-tajo` is a big data relational and
     distributed data warehouse system for Apache's Hadoop
     framework. It uses the Hadoop Distributed File System (HDFS) as a
     storage layer and has its own query execution engine instead of
     the MapReduce framework. Tajo is designed to provide low-latency
     and scalable ad-hoc queries, online aggregation, and ETL
     (extraction-transformation-loading process) on large-data sets
     which are stored on HDFS (Hadoop Distributed File System) and on
     other data sources. :cite:`www-tutorialspoint-tajo` Apart from HDFS,
     it also supports other storage formats as Amazon S3, Apache
     HBase, Elasticsearch etc. It provides distributed SQL query
     processing engine and even has query optimization techniques and
     provides interactive anaysis on large-data sets. Tajo is
     compatible with ANSI/ISO SQL standard, JDBC standard. Tajo can
     also store data from various file formats such as CSV,
     JSON,RCFile, SequenceFile, ORC and Parquet. It provides a SQL
     shell which allows users to submit the SQL queries. It also
     offers user defined functions to work with it which can be
     created in python. A Tajo cluster has one master node and a
     number of worker nodes. :cite:`www-tutorialspoint-tajo` The master
     node is responsible for performing the query planning and
     maintaining a coordination among the worker nodes. It does this
     by dividing a query in small task which are assigned to the
     workers who have a local query engine for executing the queries
     assigned to them.
     

108. Shark

     Data Scientists when working on huge data sets try to extract
     meaning and interpret the data to enhance insight about the
     various patterns, opportunities, and possibilities that the
     dataset has to offer :cite:`shark-paper-2012`. At a traditional
     EDW (Enterprise Data Warehouse), a simple data manipulation can
     be performed using SQL queries but we have to rely on other
     systems to apply the machine learning algorithms on these data
     sets. Apache Shark is a distributed query engine developed by the
     open source community whose goal is to provide a unified system
     for easy data manipulation using SQL and pushing sophisticated
     analysis towards the data.

     Shark is a data Warehouse system built on top of Apache Spark
     which does the parallel data execution and is also capable of
     deep data analysis using the Resilient Distributed Datasets(RDD)
     memory abstraction which unifies the SQL query processing engine
     with analytical algorithms :cite:`shark-paper-2012`.B ased on
     this common abstraction, it allows running two query in the same
     set of workers and share intermediate data. Since RDDs are
     designed to scale horizontally, it is easy to add or remove nodes
     to accommodate more data or faster query processing. Thus, it can
     be scaled to the large number of nodes in a fault-tolerant manner

     "Shark is built on Hive Codebase and it has the ability to
     execute HIVE QL queries up to 100 times faster than Hive without
     making any change in the existing queries"
     :cite:`shark-paper-2012`. Shark can run both on the Standalone
     Mode and Cluster-Mode. Shark can answer the queries 40X faster
     than Apache Hive and can run machine learning algorithms 25X
     faster than MapReduce programs in Apache Hadoop on large data
     sets :cite:`shark-paper-2012`.Thus, this new data analysis system
     performs query processing and complex analytics (iterative
     Machine learning) at scale and efficiently recovers from the
     failures.

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

     Cloudera Impala is Cloudera's open source massively parallel
     processing (MPP) SQL query engine for data stored in a computer
     cluster running Apache Hadoop :cite:`www-impala-cloudera`. It
     allows users to execute low latency SQL queries for data stored
     in HDFS and HBase, without any movement or transformation of
     data. The Apache Hive provides a powerful query mechanism for
     hadoop users, but the query respponse time are not acceptable due
     to Hive's reliance on MapReduce. Impala technology by Cloudera
     has its MPP query engine written in C++ replacing the Java engine
     prooves to improve the interactive Hadoop queries and interactive
     query response time for hadoop users :cite:`www-impala-dummies`
     . Impala is faster than Hive also because it executes the SQL
     queries natively without translating them into Hadoop MapReduce
     jobs, thus taking less time. Impala uses HiveQL as programming
     interface and also the Impala's Query Exec Engines are co-located
     with the HDFS data nodes, so that the data nodes and processing
     tasks are co-located, following the haddops paradigm
     :cite:`www-impala-dummies`.  Impala can aslo use Hbase as a data
     source. Thus, Impala can be considered as an extension to the
     Apache Hadoop, providing a better performance alternative to
     Hive-on-top-of-MapReduce model.

     Hive and other frameworks built on MapReduce are best suited for
     long running batch jobs, such as those involving batch processing
     of Extract, Transform, and Load (ETL) type jobs
     :cite:`www-impala-cloudera`.  The important applications of
     Impala are when the data is to be partially analyzed or when the
     same kind of query is to be processed several times from the
     dataset. When the data is to be partially analyzed, Impala uses
     parquet as the file format, which is developed by Twitter and
     Cloudera and it stores data in vertical manner
     :cite:`www-impala-beginner`. When Parquet queries the dataset it
     only reads the coloumn split part files rather than reading the
     entire dataset as compared to Hive.
     
111. MRQL

     MapReduce Query Language (MRQL, pronounced miracle) "is a query
     processing and optimization system for large-scale, distributed
     data analysis" :cite:`www-apachemrql`. MRQL provides a SQL
     like language for use on Apache Hadoop, Hama, Spark, and Flink.
     MRQL allows users to perform complex data analysis using only SQL
     like queries, which are translated by MRQL to efficient Java
     code. MRQL can evaluate queries in Map-Reduce (using Hadoop), Bulk
     Synchronous Parallel (using Hama), Spark, and Flink modes
     :cite:`www-apachemrql`.

     MRQL was created in 2011 by Leaonids
     Fegaras :cite:`www-mrqlhadoop` and is currently in the Apache
     Incubator.  All projects accepted by the Apache Software
     Foundation (ASF) undergo an incubation period until a review
     indicates that the project meets the standards of other ASF
     projects :cite:`www-apacheincubator`.

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
    
     HadoopDB is a hybrid of parallel database and MapReduce
     technologies. It approaches parallel databases in performance and
     efficiency, yet still yields the scalability, fault tolerance,
     and flexibility of MapReduce systems. It is a free and open
     source parallel DBMS. The basic idea behind it is to give Hadoop
     access to multiple single-node DBMS servers (eg. PostgreSQL or
     MySQL) deployed across the cluster. It pushes as much as possible
     data processing into the database engine by issuing SQL queries
     which results in resembling a shared-nothing cluster of
     machines. :cite:`www-hadoopdb`

     HadoopDB is more scalable than currently available parallel
     database systems and DBMS/MapReduce hybrid systems. It has been
     demonstrated on clusters with 100 nodes and should scale as long
     as Hadoop scales, while achieving superior performance on
     structured data analysis workloads.
     
114. PolyBase

     "PolyBase is a technology that accesses and combines both non-relational
     and relational data, all from within SQL Server. It allows you to run 
     queries on external data in Hadoop or Azure Blob storage acts 
     mediator between SQL and non SQL data store it makes the analysis 
     of the relation data and other data that is non structure to 
     tables (Hadoop)."`:cite:www-polybase` Unless there is a way to 
     transfer data between the data stores it is always difficult to do so. 
     PolyBase bridges this gap by operating on data that is external 
     to SQL server. It don’t require additional software, querying to 
     external can be done with same syntax as querying a database table. 
     This happens transparently behind the scene, no knowledge of Hadoop
     or Azure is required.

     It can query data store in Hadoop using T-SQL, polybase also makes 
     it easy to access the Azure blob data using T-SQL. There is no 
     need for a separate ETL or import tool while importing data 
     from Hadoop, "Azure blob storage or Azure Data Lake into relational 
     tables. It leverages Microsoft’s Columnstore technology and analysis 
     capabilities while importing"`:cite:www-polybase`. It also archives 
     data into Hadoop Azure blob and data lake store in cost effective way. 

     Push computation to Hadoop. The query optimizer makes a cost-based 
     decision to push computation to Hadoop and while doing so will 
     improve query performance. It uses statistics on external tables 
     to make the cost-based decision. Pushing computation creates 
     MapReduce jobs and leverages Hadoop's distributed computational 
     resources. Scale compute resources. SQL Server PolyBase scale-out 
     groups can be used to improve query performance. This enables parallel 
     data transfer between SQL Server instances and Hadoop nodes, 
     and it adds compute resources for operating on the external data.


115. Pivotal HD/Hawq

     Pivotal HDB is the Apache Hadoop native SQL database powered by
     Apache HAWQ :cite:`www-apache-hqwq` for data science and machine
     learning workloads. It can be used to gain deeper and actionable
     insights into data with out the need from moving data to another
     platform to perfrom advanced analytics. Few important problems
     that Pivot HDB address are as follows Quickly unlock business
     insights with exceptional performance, Integrate SQL BI tools
     with confidence and Iterate advanced analytics and machine
     learning in database support. Pivotal HDB comes with an elastic
     SQL query engine which combines MPP-based analytical performance,
     roboust ANSI SQL compliance and integrated Apache MADlib for
     machine learning :cite:`www-pivotalhdb`.
     
116. Presto

     .. include:: techs/presto.rst

117. Google Dremel
 
     Dremel is a scalable, interactive ad-hoc query system for
     analysis of read-only nested data. By combining multi-level
     execution trees and columnar data layout, Google Dremel is
     capable of running aggregation queries over trillion-row tables
     in seconds. :cite:`paper-dremel` With Dremel, you can write a
     declarative SQL-like query against data stored in a read-only
     columnar format efficiently for analysis or data exploration.
     It's also possible to write queries that analyze billions of
     rows, terabytes of data, and trillions of records in
     seconds. Dremel can be use for a variety of jobs including
     analyzing web-crawled documents, detecting e-mail spam, working
     through application crash reports.

118. Google BigQuery


     Google BigQuery :cite:`www-bigquery` is an enterprise data
     warehouse used for large scale data
     analytics. :cite:`www-bigquery-documentation` A user can store
     and query massive datasets by storing the data in BigQuery and
     querying the database using fast SQL queries using the processing
     power of Google's infrastructure. In Googe BigQuery a user can
     control access to both the project and the data based on the his
     business needs which gives the ability to others to view and even
     query the data. :cite:`www-bigquery` BigQuery can scale the
     database from GigaBytes to PetaBytes. BigQuery can be accessed
     using a Web UI or a command-line tool or even by making calls to
     the BigQuery REST API using a variety of client libraries such as
     Java, .NET pr python. BigQuery can also be accessed using a
     variety of third party tool. BigQuery is fully managed to get
     started on its own, so there is no need to deploy any resources
     such as disks and virtual machines.

     Projects in BigQuery :cite:`www-bigquery-documentation` are
     top-level containers in Google Cloud Platform. They contain the
     BigQuery Data. Each project is referenced by a name and
     unique ID. Tables contain the data in BigQuery. Each table has a
     schema that describes field names, types, and other
     information. Datasets enable to organise and control access to
     the tables. Every table must belong to a dataset. A BigQuery data
     can be shared with others by defining roles and setting
     permissions for organizations, projects, and datasets, but not on
     the tables within them. BigQuery stores data in the
     :cite:`www-bigquery-columnar-storage` Capacitor columnar data
     format, and offers the standard database concepts of tables,
     partitions, columns, and rows.

     
119. Amazon Redshift
     
     Amazon Redshift is a fully managed, petabyte-scale data werehouse
     service in the cloud. Redshift service manages all of the workof
     setting up, operating and scalling a data werehouse. AWS Redshift
     can perform these tasks including provisioning capacity,
     monitoring and backing up the cluster, and applying patches as
     well as upgrades to the Redshift's engine :cite:`www-redshift`.
     Redshift is built on thet top of technology from the Massive
     Paraller Processing (MPP) data-werehouse company ParAccel which
     based on PostgresSQL 8.0.2 to PostgresSQL 9.x with capabilty to
     handle analytics workloads on large- scale dataset stored by a
     column-oriented DBMS principle :cite:`www-wiki-red`.

120. Drill

     Apache Drill :cite:`www-ApacheDrill` is an open source framework
     that provides schema free SQL query engine for distributed 
     large-scale datasets. Drill has an extensible architecture at 
     its different layers. It does not require any centralized 
     metadata and does not have any requirement for schema 
     specification. Drill is highly useful for short and interactive
     ad-hoc queries on very large scale data sets. It is scalable to
     several thousands of nodes. Drill is also capable to query 
     nested data in various formats like JSON and Parquet. It can 
     query large amount of data at very high speed. It is also  
     capable of performing discovery of dynamic schema. 
     A service called ‘Drillbit’  is at the core of Apache Drill 
     responsible for accepting requests from the client, processing
     the required queries, and returning all the results to the client.
     Drill is primarily focused on non-relational datastores, 
     including Hadoop and NoSQL

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
     :cite:`pike05sawzall`

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
     language itself".  :cite:`pike05sawzall`

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
     
     Google Cloud DataFlow :cite:`www-cloud-google1` is a unified
     programming model that manages the deployment, maintenance and
     optimization of data processes such as batch processing, ETL
     etc. It creates a pipeline of tasks and dynamically allocates
     resources thereby maintaining high efficiency and low
     latency. According to :cite:`www-cloud-google1`, these
     capabilities make it suitable for solving challenging big data
     problems. Also, google DataFlow overcomes the performance issues
     faced by Hadoops Mapreduce while building pipelines. As stated in
     :cite:`www-dataconomy` the performance of MapReduce started
     deteriorating while facing multiple petabytes of data whereas
     Google Cloud Dataflow is apparently better at handling enormous
     datasets.  :cite:`www-cloud-google1` Additionally Google Dataflow
     can be integrated with Cloud Storage, Cloud Pub/Sub, Cloud
     Datastore, Cloud Bigtable, and BigQuery. The unified programming
     ability is another noteworthy feature which uses Apache Beam SDKs
     to support powerful operations like windowing and allows
     correctness control to be applied to batch and stream data
     processes.

     
125. Summingbird
     
     According to :cite:'summingbirdgit', "Summingbird is
     a library that lets you write MapReduce programs that look like
     native Scala or Java collection transformations and execute them
     on a number of well-known distributed MapReduce platforms,
     including Storm and Scalding."  Summingbird is open-source and is
     a domain-specific Scala implemented language
     :cite:'boykin2014summingbird'. It combines online and batch
     MapReduce computations into one framework
     :cite:'boykin2014summingbird'. It utilizes the platforms Hadoop
     for batch and Storm for online process execution
     :cite:'boykin2014summingbird'. The open-source Hadoop
     implementation of MapReduce is a tool which those responsible for
     data management use to handle problems related to big data
     :cite:'boykin2014summingbird'. Summingbird uses an algebraic
     structure called a commutative semigroup to perform aggregations
     of both batch and online processes
     :cite:'boykin2014summingbird'. A commutative semigroup is a
     particular type of semigroup "where the associated binary
     operation is also commutative" :cite:'boykin2014summingbird'.
     The types of data that Summingbird takes as inputs are streams
     and snapshots :cite:'boykin2014summingbird'. The types of data
     Summingbird jobs generate are called stores and sinks
     :cite:'boykin2014summingbird'. Stores are "an abstract model of a
     key-value store" while sinks are unaggregated tuples from a
     producer :cite:'boykin2014summingbird'. Summingbird aims to
     simplify the process of both batch and online analytics by
     exploiting "the formal properties of algebraic structures" to
     integrate the various modes of distributed processing
     :cite:'boykin2014summingbird'.
	   
126. Lumberyard
     
     It is powerful and full-featured enough to develop triple-A,
     current-gen console games and is deeply integrated with AWS and
     Twitch(an online steaming service)
     :cite:`gamasutra`. Lumberyard's core engine technology is based
     on Crytek's CryEngine :cite:`hands`. The goal is "creating
     experiences that embrace the notion of a player, broadcaster, and
     viewer all joining together":cite:`gamasutra`. Monetization for
     Lumberyard will come strictly through the use of Amazon Web
     Services' cloud computing. If you use the engine for your game,
     you're permitted to roll your own server tech, but if you're
     using a third-party provider, it has to be Amazon :cite:`what`.

Streams
----------------------------------------------------------------------

127. Storm

     Apache Storm is an open source distributed computing framework for
     analyzing big data in real time. :cite:`storm-paper-IJCTT` refers
     storm as the Hadoop of real time data. Storm operates by reading real
     time input data from one end and passes it through a sequence of
     processing units delivering output at the other end. The basic element
     of Storm is called topology. A topology consists of many other
     elements interconnected in a sequential fashion. Storm allows us to
     define and submit topologies written in any programming language.

     Once under execution, a storm topology runs indefinitely unless killed
     explicitly. The key elements in a topology are the spout and the
     bolt. A spout is a source of input which can read data from various
     datasources and passes it to a bolt. A bolt is the actual processing
     unit that processes data and produces a new output stream. An output
     stream from a bolt can be given as an input to another
     bolt :cite:`www-storm-home-concepts`.
     
128. S4


     S4 :cite:`www-s4` is a distributed, scalable, fault-tolerant,
     pluggable platform that allows programmers to easily develop
     applications for processing continuous unbounded streams of
     data. It is built on similar concept of key-value pairs like the
     MapReduce. The core platform is written in
     Java. :cite:`www-s4-overview` S4 provides a runtime distributed
     platform that handles communication, scheduling and distribution
     across containers. The containers are called S4 nodes. The data
     is executed and processed on these S4 nodes. These S4 nodes are
     then deployed on S4 clusters. The user develops applications and
     deploys them on S4 clusters for its processing. The applications
     are built as a graph of Processing Elements (PEs) and Stream that
     interconnects the PEs. All PEs communicate asynchronously by
     sending events on streams. Events are dispatched to nodes
     according to their key in the program. :cite:`www-s4` All nodes
     are symmetric with no centralized service and no single point of
     failure. Additionally there is no limit on the number of nodes
     that can be supported.  :cite:`www-wiki-s4` In S4, both the
     platform and the applications are built by dependency injection,
     and configured through independent modules.

     
129. Samza

     Apache Samza is an open-source near-realtime, asynchronous
     computational framework for stream processing developed by the
     Apache Software Foundation in Scala and Java. :cite:`www-samza-3`
     Apache Samza is a distributed stream processing framework. It
     uses Apache Kafka for messaging, and Apache Hadoop YARN to
     provide fault tolerance, processor isolation, security, and
     resource management. Samza processes streams. A stream is
     composed of immutable messages of a similar type or
     category. Messages can be appended to a stream or read from a
     stream.  Samza supports pluggable systems that implement the
     stream abstraction: in Kafka a stream is a topic, in a database
     we might read a stream by consuming updates from a table, in
     Hadoop we might tail a directory of files in HDFS. Samza is a
     stream processing framework. Samza provides a very simple
     callback-based *process message* API comparable to MapReduce.
     Samza manages snapshotting and restoration of a stream
     processor’s state.  Samza is built to handle large amounts of
     state (many gigabytes per partition). :cite:`www-samza-1`
     Whenever a machine in the cluster fails, Samza works with YARN to
     transparently migrate your tasks to another machine. Samza uses
     Kafka to guarantee that messages are processed in the order they
     were written to a partition, and that no messages are ever lost.
     Samza is partitioned and distributed at every level. Kafka
     provides ordered, partitioned, replayable, fault-tolerant
     streams. YARN provides a distributed environment for Samza
     containers to run in. Samza works with Apache YARN, which
     supports Hadoop’s security model, and resource isolation through
     Linux CGroups :cite:`www-samza-4` :cite:`www-samza-3`.

130. Granules

     Granules in used for execution or processing of data streams in
     distributed environment.  When applications are running
     concurrently on multiple computational resources, granules manage
     their parallel execution.  The MapReduce implementation in
     Granules is responsible for providing better performance.It has
     the capability of expressing computations like graphs.
     Computations can be scheduled based on periodicity or other
     activity.  Computations can be developed in C, C++, Java, Python,
     C#, R It also provides support for extending basic Map reduce
     framework.  Its application domains include hand writing
     recognition, bio informatics and computer brain interface
     :cite:`www-granules`.
131. Neptune

132. Google MillWheel

     MillWheel is a framework for building low-latency data-processing
     applications. Users specify a directed computation graph and
     application code for individual nodes, and the system manages
     persistent state and the continuous flow of records, all within
     the envelope of the framework’s fault-tolerance guarantees. Other
     streaming systems do not provide this combination of fault
     tolerance, versatility, and scalability. MillWHeel allows for
     complex streaming systems to be created without distributed
     systems expertise. MillWheel’s programming model provides a
     notion of logical time, making it simple to write time-based
     aggregations. MillWheel was designed from the outset with fault
     tolerance and scalability in mind. In practice, we find that
     MillWheel’s unique combination of scalability, fault tolerance,
     and a versatile programming model :cite:`millwheel-paper`.
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
     
     LinkedIn is a social networking website for Business and employment
     :cite:`www-linkedinwiki`. LinkedIn has more than 400 million
     user profiles (as per 10 March2016 news), and increasing
     at a rate of 2new member every second :cite:`www-linkedinbigdata`.
     LinkedIn provides different products like:

     - People You May Know
     - Skill Endorsements
     - Jobs You May Be Interested In
     - News Feed Updates

     Such products are based on big data. To achieve such big data
     tasks, LinkedIn has its ecosystem consist of Oracle, Hadoop, Pig,
     Hive, Azkaban (Workflow), Avro Data, Zookeeper, Aster Data,
     Data In- Apache Kafka, Data Out- Apache Kafka and Voldemort
     :cite:`www-linkedinbigdata`. LinkedIn uses Hadoop and Aster Data
     as an analytics layer :cite:`www-linkedinquora`. LinkedIn
     partitioned the user’s data into separate DB’s stored it in XML
     format. Voldemort is a key lookup system used to store the
     analytically-derived data for the products like "People You
     May Know". Voldemort stores the data in key-value form
     :cite:`www-linkedinquora`. LinkedIn has exposed REST
     API to get the user data :cite:`www-linkedindevelopers`.

135. Twitter Heron

     Heron is a real-time analytics platform that was developed at
     Twitter for distributed streaming processing. Heron was
     introduced at SIGMOD 2015 to overcome the shortcomings of Twitter
     Storm as the scale and diversity of Twitter data increased. As
     mentioned in :cite:`www-TwitterHeronOpen` The primary advantages
     of Heron were: API compatible with Storm: Back compatibility with
     Twitter Storm reduced migration time. Task-Isolation: Every task
     runs in process-level isolation, making it easy to debug/
     profile. Use of main stream languages: C++, Java, Python for
     efficiency, maintainability, and easier community
     adoption. Support for backpressure: dynamically adjusts the rate
     of data flow in a topology during run-time, to ensure data
     accuracy. Batching of tuples: Amortizing the cost of transferring
     tuples. Efficiency: Reduce resource consumption by 2-5x and Heron
     latency is 5-15x lower than Storm’s latency. The architecture of
     Heron (as shown in :cite:`www-TwitterHeron`)uses the Storm API to
     submit topologies to a scheduler. The scheduler runs each
     topology as a job consisting of several containers. The
     containers run the topology master, stream manager, metrics
     manager and Heron instances. These containers are managed by the
     scheduler depending on resource availability.
     
136. Databus
137. Facebook Puma/Ptail/Scribe/ODS
     
     The real time data Processing at Facebook is carried out using
     the technologies like Scribe, Ptail, Puma, and ODS. While
     designing the system, facebook primarily focused on the five key
     decisions that the system should incorporate which were Ease of
     Use, Performance, Fault-tolerance, Scalability, and
     Correctness. "The real time data analytics ecosystem at facebook
     is designed to handle hundreds of Gigabytes of data per second
     via hundreds of data pipelines and this system handles over
     200,000 events per second with a maximum latency of 30 seconds"
     :cite:`www-facebook`. Facebook focused on the Seconds of latency
     while designing the system and not milliseconds as seconds are
     fast enough to for all the use case that needs to be supported,
     and it allowed facebook to use persistent message bus for data
     transport and this also made the system more fault tolerant and
     scalable :cite:`www-facebook`. The large infrastructure of
     facebook comprises of hundreds of systems distributed across
     multiple data centers that needs a continiuous monitoring to
     track their health and performance which is done by Operational
     Data Store(ODS) :cite:`facebook-paper-2016`. ODS comprises of a
     time series database (TSDB), which is a query service, and a
     detection and alerting system. ODS’s TSDB is built atop the HBase
     storage system. Time series data from services running on
     Facebook hosts is collected by the ODS write service and written
     to HBase.

     When the data is generated by the user from their devices, an
     AJAX request is fired to facebook, and these requests are then
     written to a log file using Scribe (distributed data transport
     system), this messaging system collects, aggregates, and delivers
     high volume of log data with few seconds of latency and high
     throughput. Scribe stores the data in the HDFS (Hadoop
     Distributed File System) in a tailing fashion, where the new
     events are stored in log files and the files are tailed below the
     current events. The events are then written into the storage
     HBase on distributed machines. This makes the data available for
     both batch and real-time processing. Ptail is an internal tool
     built to aggregate data from multiple Scribe stores. It then
     tails the log files and pulls data out for processing. Puma is a
     stream processing system which is the real-time
     aggregation/storage of data. Puma provides filtering and
     processing of Scribe streams (with a few seconds delay), usually
     Puma batches the storage per 1.5 seconds on average and when the
     last flush completes, then only a new batch starts to avoid the
     contention issues, which makes it fairly real time.
     
138. Azure Stream Analytics

     Azure Stream Analytics is a platform that manages data streaming
     from devices, web sites, infrastructure systems, social media,
     internet of things analytics, and other sources usings real-time
     event processing engine. :cite:`www-azurestreamanalytics` Jobs
     are authored by "specifying the input source of the streaming
     data, the output sink for the results of your job, and a data
     tranformation expressed in a SQL-like language."  Some key
     capabilities and benefits include ease of use, scalability,
     reliability, repeatability, quick recovery, low cost, reference
     data use, user defined functions capability, and
     connectivity. :cite:`www-docs-microsoft` Available documentation
     to get started with Azure Stream
     Analytics. :cite:`www-github-azure` Azure Stream Analytics has a
     development project available on github.

     
139. Floe
140. Spark Streaming :cite:`www-apache-spark-stream`

     Spark Streaming is a library built on top of Spark Core which
     enables Spark to process real-time streaming data. The streaming
     jobs can be written similar to batch jobs in Spark, using either
     Java, Scala or Python. The input to Spark Streaming applications
     can be fed from multiple data sources such HDFS, Kafka, Flume,
     Twitter, ZeroMQ, or custom-defined sources. It also provides a
     basic abstraction called Discretized Streams or DStreams to
     represent the continuous data streams. Spark's API for
     manipulating these data streams is very similar to the Spark
     Core’s Resilient Distributed Dataset(RDD) API
     :cite:`www-apache-spark-RDD` which makes it easier for users to
     move between projects with stored and real-time data as the
     learning curve is short.  Spark Streaming is designed to provide
     fault-tolerance, throughput, and scalability. Examples of
     streaming data are messages being published to a queue for
     real-time flight status update or the log files for a production
     server.
     
141. Flink Streaming
142. DataTurbine

     Data Turbine :cite:`www-data-turbine` is open source engine that
     allows to stream data from various sources, process it and sink
     it to different destinations. The streaming sources can be labs,
     web cams and Java enabled cell phones. The sinks can be
     visualizations, interfaces and databases.  Data Turbine can be
     used to stream data formats like numbers, text, sound and video.

     :cite:`osdt-ecologicalsociety` explains that the Data Turbine
     middleware provides the cyber-infrastructure that integrates
     disparate elements of complex distributed real time
     application. Data Turbine acts as a middleware black box using
     which applications and devices can send and receive data. Data
     Turbine manages the management operations like memory and file
     management as well as book-keeping and reconnection logic.  Data
     Turbine also provides Android based controller which allows
     algorithms to run close to sensors.


Basic Programming model and runtime, SPMD, MapReduce
----------------------------------------------------

143. Hadoop

     Apache Hadoop is an open source framework written in Java that 
     utilizes distributed storage and the MapReduce programming model 
     for processing of big data. Hadoop utilizes commodity hardware to 
     build fault tolerant clusters.  Hadoop was developed based on 
     papers published by Google on the Google File System (2003) and 
     MapReduce (2004) :cite:`www-wikihadoop`.

     Hadoop consists of several modules: the Cluster, Storage, Hadoop 
     Distributed File System (HDFS) Federation, Yarn Infrastructure, 
     MapReduce Framework, and the Hadoop Common Package.  The Cluster 
     is comprised of multiple machines, otherwise referred to as nodes.  
     Storage is typically in the HDFS.  HDFS federation is the framework 
     responsible for this storage layer.  YARN Infrastructure provides 
     computational resources such as CPU and memory. The MapReduce layer 
     is responsible for implementing MapReduce :cite:`www-hadooparch2`.  
     The Hadoop Common Package which includes operating and file system 
     abstractions and JAR files needed to start Hadoop 
     :cite:`www-wikihadoop`. 


144. Spark :cite:`www-spark`

     Apache Spark which is an open source cluster computing framework
     has emerged as the next generation big data processing engine
     surpassing Hadoop MapReduce. "Spark engine is developed for
     in-memory processing as well a disk based processing. This system
     also provides large number of impressive high level tools such as
     machine learning tool M Lib, structured data processing, Spark
     SQL, graph processing took Graph X, stream processing engine
     called Spark Streaming, and Shark for fast interactive question
     device." The ability of spark to join datasets across various
     heterogeneous data sources is one of its prized
     attributes. Apache Spark is not the most suitable data analysis
     engine when it comes to processing (1) data streams where latency
     is the most crucial aspect and (2) when the available memory for
     processing is restricted. "When available memory is very limited,
     Apache Hadoop Map Reduce may help better, considering huge
     performance gap." In cases where latency is the most crucial
     aspect we can get better results using Apache Storm.
     
145. Twister

     Twister is a new software tool released by Indiana University,
     which is an extension to MapReduce architectures currently used
     in the academia and industry :cite:`www-twister1`. It supports
     faster execution of many data mining applications implemented as
     MapReduce programs. Applications that currently use Twister
     include: K-means clustering, Google's page rank, Breadth first
     graph search , Matrix multiplication, and Multidimensional
     scaling. Twister also builds on the SALSA team's work related to
     commercial MapReduce runtimes, including Microsoft Dryad software
     and open source Hadoop software. SALSA project work is funded in
     part by an award from Microsoft, Inc. The archite cture is based
     on pub/sub messaging that enables it to perform faster data
     transfers, minimizing the overhead of the runtime. Also, the
     support for long running processes improves the efficiency of the
     runtime for many iterative MapReduce
     computations. :cite:`www-twister2` :cite:`www-twister3`
     :cite:`paper-twister`.

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
     
     Apache Flink is an open-source stream processing framework for
     distributed, high-performing, always-available, and accurate data
     streaming applications. Apache Flink is used in big data application
     primarily involving analysis of data stored in Hadoop clusters. 
     It also supports a combination of in-memory and disk-based processing
     as well as handles both batch and stream processing jobs, with data
     streaming the default implementation and batch jobs running as 
     special-case versions of streaming application :cite:`www-flink`.


148. Reef

     REEF (Retainable Evaluator Execution Framework) :cite:`www-reef`
     is a scale-out computing fabric that eases the development of Big
     Data applications on top of resource managers such as Apache YARN
     and Mesos. It is a Big Data system that makes it easy to
     implement scalable, fault-tolerant runtime environments for a
     range of data processing models on top of resource managers. REEF
     provides capabilities to run multiple heterogeneous frameworks
     and workflows of those efficiently. REEF contains two libraries,
     Wake and Tang where Wake is an event-based-programming framework
     inspired by Rx and SEDA and Tang is a dependency injection
     framework inspired by Google Guice, but designed specifically for
     configuring distributed systems.

     
149. Disco

     a. Disco from discoproject.org represents an implementation of
     mapreduce for distributed computing that benefits end users by
     relieving them of the need to handle "difficult technicalities
     related to distribution such as communication protocols, load
     balancing, locking, job scheduling, and fault tolerance."
     :cite:`www-whatis-discoproject` Its designers wrote the software
     in Erlang, an inherently fault tolerant language. In addition,
     Disco’s creators chose Erlang because they believe it best meets
     the software’s need to handle "tens of thousands of tasks in
     parallel." :cite:`www-erlangprime-discoproject` Python was used
     for Disco’s libraries. Finally, Disco supports pipelines, "a
     linear sequence of stages, where the outputs of each stage are
     grouped into the input of the subsequent stage."
     :cite:`www-clarridge-discoproject` Its designers implemented
     Disco’s libraries in Python. Disco originated within Nokia
     Corp. to handle large data sets.  Since then it has proven itself
     reliable in production environments outside of
     Nokia. :cite:`www-nokia-discoproject`

     b. DISCO from the research group Service Engineering (SE),
     :cite:`www-discoabout-discoabstractionlayer` serves as "an
     abstraction layer for OpenStack‘s orchestration component [Heat]"
     SE based DISCO on its prior orchestration framework, Hurtle. The
     software sets up a computer cluster and deploys the user’s choice
     of distributed computing architecture onto the cluster based on
     setup inputs provided by the user. DISCO offers a command line
     interface via HTTP to directly access
     OpenStack. :cite:`www-discodescribed-discoabstractionlayer`

150. Hama

     Apache Hama is a framework for Big Data analytics which uses the
     Bulk Synchronous Parallel (BSP) computing model, which was
     established in 2012 as a Top-Level Project of The Apache Software
     Foundation.It provides not only pure BSP programming model but
     also vertex and neuron centric programming models, inspired by
     Google's Pregel and DistBelief :cite:`apache-hama`. It avoids the
     processing overhead of MapReduce approach such as sorting,
     shuffling, reducing the vertices etc. Hama provides a message
     passing interface and each superstep in BSP is faster than a full
     job execution in MApReduce framework, such as Hadoop
     :cite:`book-hama`.
     
151. Giraph

     Apache Giraph is an iterative graph processing system built for big
     data :cite:`www-giraph-apache`.It utilizes Hadoop Mapreduce
     technology for processing graphs :cite:`www-apache-giraph-wiki`
     Giraph was initially developed by Yahoo based on the paper
     published by Google on Pregel. :cite:`www-apache-giraph-pcworld`
     Facebook with some improvements on Giraph could analyze real world
     graphs up to a scale of a trillion.Giraph can directly interface
     with HDFS and Hive ( As it's developed in
     Java). :cite:`www-apache-giraph-fb`
   
152. Pregel
153. Pegasus

     See #4 above.

154. Ligra

     Ligra is a Light Weight Graph Processing Framework for the graph
     manipulation and analysis in shared memory system. It is
     particularly suited for implementing on parallel graph traversal
     algorithms where only a subset of the vertices are processed in an
     iteration. The interface is lightweight as it supplies only a
     few functions. The Ligra framework has two very simple routines,
     one for mapping over edges and one for mapping over vertices.

     The implementations of several graph algorithms like BFS,
     breadth-first search, betweenness centrality, graph radii
     estimation, graph-connectivity, PageRank and Bellman-Ford
     single-source shortest paths efficient and scalable, and often
     achieve better running times than ones reported by other graph
     libraries/systems :cite:`ligra-paper-2013`.  Although the shared
     memory machines cannot be scaled to the same size as distributed
     memory clusters, but the current commodity single unit servers
     can easily fit graphs with well over a hundred billion edges in
     the shared memory systems that are large enough for any of the
     graphs reported in the paper :cite:`ligra-paper-2`.

155. GraphChi

     GraphChi is a disk-based system for computing
     efficiently on graphs with large number of edges.  It uses a
     well-known method to break large graphs into small parts, and
     executes data mining, graph mining, machine learning
     algorithms. GraphChi can process over one hundred thousand graph
     updates per second, while simultaneously performing
     computation :cite:`GraphChi`. GraphChi is a spin-off of the
     GraphLab. GraphChi brings web-scale graph computation, such as
     analysis of social networks, available to anyone with a modern
     laptop

     
156. Galois
     
     Galois system was built by intelligent software systems team at
     University of Texas, Austin. As explained in
     :cite:`www-galoisSite`, "Galois is a system that automatically
     executes 'Galoized' serial C++ or Java code in parallel on
     shared-memory machines. It works by exploiting amorphous
     data-parallelism, which is present even in irregular codes that
     are organized around pointer-based data structures such as graphs
     and trees". By using Galois provided data structures programmers
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
     
     Graphs are commonly used data structures . However, developers
     may find it challenging to write correct and efficient
     programs. Furthermore, graph processing is further complicated by
     irregularities of graph structures. Medusa enables the developers
     to write sequential C/C++ code. According to :cite:`paper_medusa`
     it provides a set of APIs which embraces a runtime system to
     automatically execute those APIs in parallel. A number of
     optimization techniques are implemented to improvise the
     efficiency of graph processing. The experimental results provided
     in the paper :cite:`paper_medusa` demonstrate that (1) Medusa
     greatly simplifies implementation of GPGPU programs for graph
     processing, with many fewer lines of source code written by
     developers; (2) The optimization techniques significantly improve
     the performance of the runtime system, making its performance
     comparable with or better than manually tuned GPU graph
     operations. :cite:`www-medusa` Medusa has proved to be a powerful
     framework for networked digital audio and video
     framework. :cite:`www-medusa` By exploiting the APIs it takes a
     modular approach to construct complex graph systems. 

158. MapGraph
159. Totem

     Totem is a project to overcome the current challenges in graph 
     algorithms.  The project is research the Networked Systems
     Laboratory (NetSysLab) The issue resides in the scale of real 
     world graphs and the inability to process them on platforms
     other than a supercomputer.  Totem is based on a bulk synchronous 
     parallel(BSP) model that can enable hybrid CPU/GPU systems to process 
     graph based applications in a cost effective manner. 
     :cite:`www-netsyslab`

Inter process communication Collectives
---------------------------------------

160. point-to-point
161. (a) publish-subscribe: MPI

     see http://www.slideshare.net/Foxsden/high-performance-processing-of-streaming-data
     
161. (b) publish-subscribe: Big Data

     Publish/Subscribe (Pub/Sub) :cite:`thesis-pub-sub` is a
     communication paradigm in which subscribers register their
     interest as a pattern of events or topics and then asynchronously
     receive events matching their interest. On the other hand,
     publishers generate events that are delivered to subscribers with
     matching interests.  In Pub/sub systems, publishers and
     subscribers need not know each other. Pub/sub technology is
     widely used for a loosely coupled interaction between disparate
     publishing data-sources and numerous subscribing data-sinks. The
     two most widely used pub/sub schemes are - Topic-Based
     Publish/Subscribe (TBPS) and Content-Based Publish/Subscribe
     (CBPS) :cite:`paper-pub-sub`.
      
     Big Data analytics architecture are being built on top of a
     publish/subscribe service stratum, serving as the communication
     facility used to exchange data among the involved components
     :cite:`paper-pub-sub-bigdata`. Such a publish/subscribe service
     stratum brilliantly solves several interoperability issues due to
     the heterogeneity of the data to be handled in typical Big Data
     scenarios.

     Pub/Sub systems are being widely deployed in Centralized
     datacenters, P2P environments, RSS feed notifications, financial
     data dissemination, business process management, Social
     interaction message notifications- Facebook, Twitter, Spotify,
     etc.

162. HPX-5

     Based on :cite:`www-hpx-5`, High Performance ParallelX (HPX-5)
     is an open source, distributed model that provides opportunity
     for operations to run unmodified on one-to-many nodes. The
     dynamic nature of the model accommodates effective "computing
     resource management and task scheduling". It is portable and
     performance-oriented. HPX-5 was developed by IU Center for
     Research in Extreme Scale Technologies (CREST). Concurrency is
     provided by lightweight control object (LCO) synchronization and
     asynchronous remote procedure calls. ParallelX component allows
     for termination detection and supplies per-process
     collectives. It "addresses the challenges of starvation, latency,
     overhead, waiting, energy and reliability". Finally, it supports
     OpenCL to use distributed GPU and coprocessors. HPX-5 could be
     compiled on various OS platforms , however it was only tested on
     several Linux and Darwin (10.11) platforms. Required
     configurations and environments could be accessed via
     :cite:`www-hpx-5-user-guide`.
	 
	 
163. Argo BEAST HPX-5 BEAST PULSAR

     Search on the internet was not successsful.
     
164. Harp

     Harp :cite:`www-harp` is a simple, easy to maintain, low risk and
     easy to scale static web server that also serves Jade, Markdown,
     EJS, Less, Stylus, Sass, and CoffeeScript as HTML, CSS, and
     JavaScript without any configuration and requires low cognitive
     overhead. It supports the beloved layout/partial paradigm and it
     has flexible metadata and global objects for traversing the file
     system and injecting custom data into templates. It acts like a
     lightweight web server that was powerful enough for me to abandon
     web frameworks for dead simple front-end publishing. Harp can
     also compile your project down to static assets for hosting
     behind any valid HTTP server.
     
165. Netty

     Netty :cite:`www-netty` "is an asynchronous event-driven network
     application framework for rapid development of maintainable high
     performance protocol servers & clients". Netty :cite:`netty-book`
     "is more than a collection of interfaces and classes; it also
     defines an architectural model and a rich set of design
     patterns". It is protocol agnostic, supports both connection
     oriented protocols using TCP and connection less protocols built
     using UDP. Netty offers performance superior to standard Java NIO
     API thanks to optimized resource management, pooling and reuse
     and low memory copying.
     
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

     Apache ActiveMQ is a powerful open source messaging and
     Integration Patterns server :cite:`www-activeMQ`. It is a message
     oriented middleware(MOM) for the Apache Software Foundation that
     provides high availability, reliability, performance, scalability
     and security for enterprise messaging :cite:`ActiveMQ-book`. The
     goal of ActiveMQ is to provide standard-based, message-oriented
     application integration across as many languages and platforms as
     possible. ActiveMQ implements the JMS spec and offers dozens of
     additional features and value on top of this
     specifications. ActiveMQ is used in many scenarios such as
     heterogeneous application integration, as a replacement for RPC
     and to loosen the coupling between applications.
     
168. RabbitMQ

     RabbitMQ is a message broker :cite:`www-rabbitmq` which allows
     services to exchange messages in a fault tolerant manner. It
     provides variety of features which "enables software applications
     to connect and scale". Features are: reliability, flexible
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
        as follows "messages are published to exchanges, which are
        often compared to post offices or mailboxes. Exchanges then
        distribute message copies to queues using rules called
        bindings. Then AMQP brokers either deliver messages to
        consumers subscribed to queues, or consumers fetch/pull
        messages from queues on demand"

169. NaradaBrokering

     NaradaBrokering :cite:`www-narada`, is a content distribution
     infrastructure for voluminous data streams. The substrate places
     no limits on the size, rate and scope of the information
     encapsulated within these streams or on the number of entities
     within the system. The smallest unit of this substrate called as
     broker, intelligently process and route messages, while working
     with multiple underlying communication protocols. The major
     capabilities of NaradaBrokering consists of providing a message
     oriented middleware (MoM) which facilitates communications
     between entities (which includes clients, resources, services and
     proxies thereto) through the exchange of messages and providing a
     notification framework by efficiently routing messages from the
     originators to only the registered consumers of the message in
     question :cite:`paper-nb-sustrate`. Also, it provides salient
     stream oriented features such as their Secure end-to-end
     delivery, Robust disseminations, jitter reductions.

     NaradaBrokering incorporates support for several communication
     protocol such as TCP, UDP, Multicast, HTTP, SSL, IPSec and
     Parallel TCP as well as supports enterprise messaging standards
     such as the Java Message Service, and a slew of Web Service
     specifications such as SOAP, WS-Eventing, WS-Reliable Messaging
     and WS-Reliability :cite:`www-narada-features`.

     
170. QPid
171. Kafka

     Apache Kafka is a streaming platform, which works based on
     publish-subscribe messaging system and supports distributed
     environment.
      
     *Kafka lets you publish and subscribe to the messages.* Kafka
     maintains message feeds based on ‘topic’. A topic is a category
     or feed name to which records are published. Kafka’s Connector
     APIs are used to publish the messages to one or more topics,
     whereas, Consumer APIs are used to subscribe to the topics.

     *Kafka lets you process the stream of data at real time.* Kafka’s
     stream processor takes continual stream of data from input
     topics, processes the data in real time and produces streams of
     data to output topics. Kafka’s Streams API are used for data
     transformation.

     *Kafka lets you store the stream of data in distributed
     clusters.* Kafka acts as a storage system for incoming data
     stream. As Kafka is a distributed system, data streams are
     partitioned and replicated across nodes.

     Thus, a combination of messaging, storage and processing data
     stream makes Kafka a ‘streaming platform’. It can be used for
     building data pipelines where data is transferred between systems
     or applications. Kafka can also be used by applications that
     transform real time incoming data. :cite:'www-kafka'

172. Kestrel
     
     Kestrel is a distributed message queue, with added features and
     bulletproofing, as well as the scalability offered by actors and
     the Java virtual machine. It supports multiple protocols:
     memcache: the memcache protocol; thrift: Apache Thrift-based RPC;
     text: a simple text-based protocol. Each queue is strictly
     ordered following the FIFO (first in, first out) principle. To
     keep up with performance items are cached in system
     memory. Kestrel is more durable as queues are stored in memory
     for speed, but logged into a journal on disk so that servers can
     be shutdown or moved without losing any data. When kestrel starts
     up, it scans the journal folder and creates queues based on any
     journal files it finds there, to restore state to the way it was
     when it last shutdown (or was killed or died).

     Kestrel uses a pull-based data aggregator system that convey data
     without prior definition on its destination. So the destination
     can be defined later on either storage system, like HDFS or
     NoSQL, or processing system, like storm and sppark
     streaming. Each server handles a set of reliable, ordered message
     queues. When you put a cluster of these servers together, with no
     cross communication, and pick a server at random whenever you do
     a set or get, you end up with a reliable, loosely ordered message
     queue :cite:`git-kestrel`.

173. JMS

     JMS (Java Messaging Service) is a java oriented messaging
     standard that defines a set of interfaces and semantics which
     allows applications to send, receive, create, and read messages.
     It allows the communication between different components of a
     distributed application to be loosely coupled, reliable, and
     asynchronous :cite:`www-jms-wiki`. JMS overcomes the drawbacks of
     RMI (Remote Method Invocation) where the sender needs to know the
     method signature of the remote object to invoke it and RPC(Remote
     Procedure Call), which is tightly coupled i.e it cannot function
     unless the sender has important information about the receiver.

     JMS establishes a standard that provides loosely coupled
     communication i.e the sender and receiver need not be present at
     the same time or know anything about each other before initiating
     the communication.  JMS provides two communication domains.A
     point-to-point messaging domain where there is one producer and
     one consumer. On generating message, a producer simple pushes the
     message to a message queue which is known to the consumer. The
     other communication domain is publish/subscribe model, where one
     message can have multiple receivers :cite:`www-jms-oracle-docs`.

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

     It is basically a framework for management of a system where the
     systems undergo an organized coordination resulting in an
     automated deployment of systems which creates an orderly workflow
     or a parallel wise job execution. It doesn’t rely on central
     inventories such as SSH and uses tools such as Middleware :cite:
     `www-marionette-webpage`. This gives an advantage of delivering a
     very scalable and quick execution environment.  Mcollective gives
     us a huge advantage of working with a large number of servers ,
     it uses publish/subscribe middleware for communicating with many
     hosts at once in a parallel manner. Mcollective allows us to
     interact with a cluster of servers at the same time, it allows us
     to use a simple command line to call remote agents and there
     isn’t a centralized inventory. Mcollective uses a broadcast
     paradigm to distribute the requests , where all the servers
     receives the request at the same time which are also attached
     with a filter. The servers which match the filter will act on
     these requests.
     
178. Public Cloud: Amazon SNS

     Amazon SNS is an Inter process communication service which gives
     the user simple, end-to-end push messaging service allowing them
     to send messages, alerts, or notifications. According to
     :cite:`www-sns-webpage`, it can be used to send a directed message
     intended for an entity or to broadcast messages to list of
     selected entities. It is an easy to use and cost effective
     mechanism to send push messages. Amazon SNS is compatible to send
     push notifications to iOS, Windows, Fire OS and Android OS
     devices.

     According to :cite:`www-sns-blog` SNS system architecture consists 
     of four elements: (1) Topics, (2) Owners, (3) Publishers, and
     (4) Subscribers. Topics are events or access points that identifies
     the subject of the event and can be accessed by an unique
     identifier(URI). Owners create topics and control all access to
     the topic and define the corressponding permission for each
     topic. Subscribers are clients (applications, end-users,
     servers, or other devices) that want to receive messages or
     notifications on specific topics of interest to them.Publishers
     send messages to topics. SNS matches the topic with the list of
     subscribers interested in the topic, and delivers the message to
     them.

     According to :cite:`www-sns-faq`, Amazon SNS follows pay as per
     usage. In general it is $0.50 per 1 million Amazon SNS
     Requests.Amazon SNS supports notifications over multiple
     transport protocols such as HTTP/HTTPS, Email/Email-JSON,
     SQS(Message queue) and SMS.Amazon SNS can be used with other AWS
     services such as Amazon SQS, Amazon EC2 and Amazon S3.

179. Lambda

     AWS Lambda is a product from amazon which facilitates serverless
     computing :cite:`www-awslambda`.AWS Lambda allows for running the
     code without the need for provisioning or managing servers, all
     server management is taken care by AWS.The code to be run on AWS
     Lambda is called a server function which can be written in
     Node.js,Python,Java,C#.Each Lambda function is to be stateless
     and any persistent data needs are to be handled through storage
     devices.AWS Lambda function can be setup using the AWS Lambda
     console where one can setup the function code and specify the
     event that triggers the functional call.AWS Lamda service
     supports multiple event sources as identified in
     :cite:`www-awslambdaevent`.AWS Lambda is designed to use
     replication and redundancy to provide for high availability both
     for the service itself and the function it runs.AWS Lambda
     automatically scales your application by running the code in
     response to each trigger. The code runs in parallel and processes
     each trigger individually, scaling precisely with the size of the
     workload.Billing for AWS Lambda is based on the number of times
     the code executes and in 100 ms increments of the duration of the
     processing.

180. Google Pub Sub

     Google Pub/Sub provides an asynchronous messaging facility which 
     assists the communication between independent applications 
     :cite:`www-google-pub-sub`. It works in real time and helps
     keep the two interacting systems independent. It is the same
     technology used by many of the Google apps like GMail, Ads,
     etc. and so integration with them becomes very
     easy.  Some of the typical features it provides are: (1) Push 
     and Pull - Google Pub/Sub integrates quickly and easily with 
     the systems hosted on the Google Cloud Platform thereby supporting 
     one-to-many, one-to-one and many-to-many communication, using 
     the push and pull requests. (2) Scalability - It provides high 
     scalability and availability even under heavy load without any 
     degradation of latency. This is done by using a global and highly 
     scalable design. (3) Encryption - It provides security by encryption of
     the stored data as well as that in transit. Other than these
     important features, it provides some others as well, like the
     usage of RESTful APIs, end-to-end acknowledgement, replicated
     storage, etc :cite:`www-google-pub-sub-features`.
     
181. Azure Queues

     Azure Queues storage is a Microsoft Azure service, providing inter
     -process communication by message passing
     :cite:`silberschatz1998operating`.  A sender sends the message
     and a client receives and processes them.  The messages are
     stored in a queue which can contain millions of messages, up to
     the total capacity limit of a storage account
     :cite:`www-azurequeue-web`.  Each message can be up to 64 KB in
     size. These messages can then be accessed from anywhere in the
     world via authenticated calls using HTTP or HTTPS. Similar to the
     other message queue services, Azure Queues enables decoupling of
     the components :cite:`www-tutorialspoint`. It runs in an
     asynchronous environment where messages can be sent among the
     different components of an application. Thus, it provides an
     efficient solution for managing workflows and tasks. The messages
     can remain in the queue up to 7 days, and afterwards, they will
     be deleted automatically.

182. Event Hubs

     Azure Event Hubs is a hyper-scale telemetry ingestion service. It
     collects, transforms, and stores millions of events. As a
     distributed streaming platform, it offers low latency and
     configurable time retention enabling one to ingress massive
     amounts of telemetry into the cloud and read the data from
     multiple applications using publish-subscribe
     semantics. :cite:`www-eventhubs` It is a highly scalable data
     streaming platform. Data sent to an Event Hub can be transformed
     and stored using any real-time analytics provider or
     batching/storage adapters. With the ability to provide
     publish-subscribe capabilities , Event Hubs serves as the "on
     ramp" for Big Data.

In-memory databases/caches
--------------------------


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

     Memcached is a free and open-source, high performance,
     distributed memory object caching system. :cite:`www-memcached`
     Although, generic in nature,it is intended for se in speeding up
     dynamic web applications by reducing the database load.

     It can be thought of as a short term memory for your
     applications.  Memcached is an in-memory key-value store for
     small chunks of arbitrary data from the results of database
     calls, API calls and page rendering. Its API is available in most
     of the popular languages. In simple terms, it allows you to take
     memory from parts of your system where you have more memory than
     you need and allocate it to parts of your system where you have
     less memory than you need.
     
185. Redis

     Redis (Remote Dictionary Server) is an open source ,in-memory,
     key-value database which is commonly referred as a data structure
     server. "It is called a data structure server and not simply a
     key-value store because Redis implements data structure which
     allows keys to contain binary safe strings, hashes, sets, and
     sortedsets as well as lists" :cite:`redis-book-2011`.  Redis's
     better performance, easy to use and implement, and atomic
     manipulation of data structures lends itself to solving problems
     that are difficult to solve or perform poorly when implemented
     with traditional relational databases. "Salivator
     Sanfilippo (Creator of open-source database Redis) makes a strong
     case that Redis does not need to replace the existing database
     but is an excellent addition to an enterprise for new
     functionalities or to solve sometimes intractable problems."
     :cite:`redis-book-2016`

     A widely used use pattern for Redis is an in-memory cache for
     web-applications and the other being the use of pattern for REDIS
     for metric storage of such quantitative data such as the web page
     usage and user behavior on gamer leaderboards where using a bit
     operations on strings, Redis very efficiently stores binary
     information on a particular characteristics
     :cite:`redis-book-2016`.The other popular Redis use pattern is a
     communication layer between different systems through a
     publish/subscribe (pub/sub for short), where one can post the message
     to one or more channels that can be acted upon by other systems
     that are subscribed to or listening to that channel for incoming
     messages. The Companies using REDIS includes Twitter to store the
     timelines of all the user , Pinterest stores the user follower
     graph, Github, popular web frameworks like Node.js
     , Django, Ruby-on-Rails etc.

186. LMDB (key value)

     LMDB (Lighting memory-mapped Database) is a high performance
     embedded transactional database in form of a key-value store
     :cite:`www-keyvalue`. LMDB is designed around virtual memory
     facilities found in modern operating systems, multi-version
     concurrency control (MVCC) and single-level store (SLS)
     concepts. LMDB stores arbitrary key/data pairs as byte arrays,
     provides a range-based search capability, supports multiple data
     items for a single key and has a special mode for appending
     records at the end of the database (MDB_APPEND) which
     significantly increases its write performance compared to other
     similar databases.

     LMDB is not a relational database :cite:`www-relationaldb` and
     strictly uses key-value store. Key-value databases allows one
     write at a time, the difference that LMDB highlights is that
     write transactions do not block readers nor do readers block
     writes. Also, it does allow multiple applications on the same
     system to open and use the store simultaneously which helps in
     scaling up performance :cite:`www-lmdb`.

187. Hazelcast

     Hazelcast is a java based, in memory data grid
     :cite:`www-wikihazel`.  It is open source software, released
     under the Apache 2.0 License :cite:`www-githubhazel`. Hazelcast
     enables predictable scaling for applications by providing in
     memory access to data.  Hazelcast uses a grid to distribute data
     evenly across a cluster. Clusters allow processing and storage to
     scale horizontally. Hazelcast can run locally, in the cloud, in
     virtual machines, or in Docker containers. Hazelcast can be
     utilized for a wide variety of applications. It has APIs for many
     programing languages including Python, Java, Scala, C++, .NET and
     Node.js and supports any binary languages through an Open Binary
     Client Protocol :cite:`www-wikihazel`.

188. Ehcache

     EHCACHE is an open-source Java-based cache. It supports
     distributed caching and could scale to hundred of caches. It
     comes with REST APIs and could be integrated with popular
     frameworks like Hibernate :cite:`www-ehcache-features`. It offers
     storage tires such that less frequently data could be moved to
     slower tires :cite:`www-ehcache-documentation`. It's XA compliant
     and supports two- phase commit and recovery for
     transactions. It's developed and maintained by Terracotta and is
     available under Apache 2.0 license.  It conforms to Java caching
     standard JSR 107.

189. Infinispan

     Infinispan is a highly available, extremely scalable key/value data
     store and data grid platform. The design perspective of
     infinispan is exposing a distributed,highly concurrent data
     structure to make the most use of modern multi-core as well as
     multi-processor architectures. It is mostly used as a distributed
     cache, but also can be used as a object database or NoSQL
     key/value store :cite:`infinispan.org`.

     Infinispan is mostly used as a cache store. It is predomininantly
     used for applications that are clustered, and requires a cache
     coherency for data consistency. Infinispan is written in java and
     is open source. It is fully transactional. Infinispan is used to
     add clusterability as well as high availability to frameworks.
     Infinispan has many use-cases,they are: 1) it can be used as a
     distributed cache 2)Storage for temporal data, like web sessions,
     3)Cross-JVM communication, 4)Shared storage, 5)In-memory data
     processing and analytics and 6)MapReduce Implementstion in the
     In-Memory Data Grid. It is also used in research and academia as
     a framework for distribution execution and
     storage :cite:`infinispan_wikipedia`.
     
190. VoltDB

     VoltDB is an in-memory database. It is an ACID-compliant RDBMS
     which uses a shared nothing architecture to achieve database
     parallelism. It includes both enterprise and community
     editions. VoltDB is a scale-out NewSQL relational database that
     supports SQL access from within pre-compiled Java stored
     procedures.  VoltDB relies on horizontal partitioning down to the
     individual hardware thread to scale, k-safety (synchronous
     replication) to provide high availability, and a combination of
     continuous snapshots and command logging for durability (crash
     recovery) :cite:`www-voltdb`. The in-memory, scale-out
     architecture couples the speed of traditional streaming solutions
     with the consistency of an operational database. This gives a
     simplified technology stack that delivers low-latency response
     times (1ms) and hundreds of thousands of transactions per
     second. VoltDB allows users to ingest data, analyze data, and act
     on data in milliseconds, allowing users to create per-person,
     real-time experiences :cite:`www-voltdb`.

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
-------------------------

192. Hibernate

     Hibernate is an open source project which provides object
     relational persistence framework for applications in Java. It is
     an Object relational mapping library (ORM) which provides the
     framework for mapping object oriented model to relational
     database. It provides a query language, a caching layer and Java
     Management Extensions (JMX) support. Databases supported by
     Hibernate includes DB2, Oracle, MySQL, PostgreSQL.To provide
     persistence services, Hibernate uses database and configuration
     data. For using hibernate, firstly a java class is created which
     represents table in the database. Then columns in database are
     mapped to the instance variables of created Java class. Hibernate
     can perform database operations like select, insert, delete and
     update records in table by automatically creating
     query. Connection management and transaction management are
     provided by hibernate.  Hibernate saves development and debugging
     time in comparison to JDBC.  But it is slower at runtime as it
     generates many SQL statements at runtime. It is database
     independent. For batch processing it is advisable to use JDBC
     over Hibernate :cite:`www-hibernate`

193. OpenJPA

     According to :cite:`www-openjpa`, Apache OpenJPA is a Java
     persistence project developed by The Apache Software Foundation that
     can either be used as Plain old Java Object (POJO) or could be used in
     any Java EE compliant containers.It provides object relational mapping
     which effectively simplifies the storing of relational dependencies
     among objects in databases. :cite:`www-openjpa-wiki` mentions that
     Kodo, an implementation of Java Data Objects acted as a precursor to
     the development of OpenJPA. In 2006, BEA Systems donated the majority
     of the source code of Kodo to The Apache Software Foundation under the
     name OpenJPA. Being a POJO, OPenJPA can be used without needing to
     extend prespecified classes, implementing predefined interfaces and
     inclusion of annotations. OPenJPA can be used in cases where the focus
     of the project is majorly on business logic and has no dependencies on
     enterprise frameworks.OPenJPA can be implemented across multiple
     operating systems, on account of its function of cross platform
     support. It is written in Java and a most recent stable release came
     out in April 20, 2016 under the version 2.4.1 with Apache License 2.0.

194. EclipseLink

     EclipseLink is an open source persistence Services project from Eclipse
     foundation. It is a framework which provide developers to
     interact with data services including database and web services,
     Object XML mapping etc. :cite:`www-eclipselink`. This is the project
     which was developed out of Oracle's Toplink product. The main
     difference is EclipseLink does not have some key enterprise
     feature. Eclipselink support a number of persistence standard
     model like JPA, JAXB, JCA and Service Data Object. Like Toplink,
     the ORM (Object relational model) is the technique to convert
     incompatible type system in Object Oriented programming
     language. It is a framework for storing java object into
     relational database.
     
195. DataNucleus

     DataNucleus (available under Apache 2 open source license) is a
     data management framework in Java. Formerly known as 'Java
     Persistent Objects' (JPOX) this was relaunched in 2008 as
     'DataNucleus'. According to :cite:`www-DataNucleusWiki`
     DataNucleus Access Platform is a fully compliant implementation
     of the Java Persistent API (JPA) and Java Data Objects (JDO)
     specifications. It provides persistence and retrieval of data to
     a number of datastores using a number of APIs, with a number of
     query languages. In addition to object-relational mapping (ORM)
     it can also map and manage data from sources other than RDBMS
     (PostgreSQL, MySQL, Oracle, SQLServer, DB2, H2 etc.) such as
     Map-based (Cassandra, HBase), Graph-based (Neo4j), Documents
     (XLS, OOXML, XML, ODF), Web-based (Amazon S3, Google Storage,
     JSON), Doc-based (MongoDB) and Others (NeoDatis, LDAP). It
     supports the JPA (Uses JPQL Query language), JDO (Uses JDOQL
     Query language) and REST APIs :cite:`www-DataNucleus`.DataNucleus
     products are built from a sequence of plugins where each of it is
     an OSGi bundle and can be used in an OSGi environment. Google App
     Engine uses DataNucleus as the Java persistence layer
     :cite:`www-DataNucleusPerformance`.	   
	   
196. ODBC/JDBC

     Open Database Connectivity (ODBC) is an open standard application
     programming interface (API) for accessing database management
     systems (DBMS) :cite:`www-odbc`. ODBC was developed by the SQL
     Access Group and released in September, 1992. Microsoft Windows
     was the first to provide an ODBC product. Later the versions for
     UNIX, OS/2, and Macintosh platforms were developed. ODBC is
     independent of the programming language, database system and
     platform.

     Java Database Connectivity (JDBC) is a API developed specific to
     the Java programming language. JDBC was released as part of Java
     Development Kit (JDK) 1.1 on February 19, 1997 by Sun
     Microsystems :cite:`www-jdbc`. The ‘java.sql’ and ‘javax.sql’
     packages contain the JDBC classes. JDBC is more suitable for
     object oriented databases. JDBC can be used for ODBC compliant
     databases by using a JDBC-to-ODBC bridge.
     
Extraction Tools
----------------

197. UIMA

     Unstructured Information Management applications (UIMA) provides
     a framework for content analytics. It searches unstructured data
     to retrieve specific targets for the user. For example, when a
     text document is given as input to the system, it identifies
     targets such as persons, places, objects and even
     associations. According to , :cite:`www-wiki-uima` theUIMA
     architecture can be thought of as four dimensions: 1. Specifies
     component interfaces in analytics pipeline.  2. Describes a set
     of Design patterns. 3. Suggests two data representations: an
     in-memory representation of annotations for high-performance
     analytics and an XML representation of annotations for
     integration with remote web services. 4. Suggests development
     roles allowing tools to be used by users with diverse skills.

     UIMA uses different, possibly mixed, approaches which include
     Natural Language Processing, Machine Learning, IR. UIMA supports
     multimodal analytics :cite:`www-uima-slideshare` which enables
     the system to process the resource fro various points of
     view. UIMA is used in several software projects such as the IBM
     Research's Watson uses UIMA for analyzing unstructured data and
     Clinical Text Analysis and Knowledge Extraction System (Apache
     cTAKES) which is a UIMA-based system for information extraction
     from medical records.
     
381. Tika

     "The Apache Tika toolkit detects and extracts metadata and text
     from over a thousand different file types (such as PPT, XLS, and
     PDF). All of these file types can be parsed through a single
     interface, making Tika useful for search engine indexing, content
     analysis, translation, and much more. :cite:`www-tika`"


SQL(NewSQL)
-----------

198. Oracle

     Oracle database is an object-relational database management system by 
     Oracle. Following are some of the key features of Oracle :cite:`www-oracle`
     1. ANSI SQL Compliance
     2. Multi-version read consistency
     3. Procedural extensions: PL/SQL and Java.
     Apart from above they are performance related features, including but not 
     limited to: indexes, in-memory, partitioning, optimization. 
     As of today the latest release of Oracle is :cite:`www-oracle`
     Oracle Database 12c Release 1: 12.1 (Patch set as of June 2013 )


199. DB2

     DB2 is a Relational DataBase Management System (RDBMS). Though
     initially introduced in 1983 by IBM to run exclusively on its MVS
     (Multiple Virtual Storage) mainframe platform, it was later
     extended to other operating systems like UNIX, Windows and
     Linux. It is used to store, analyze and retrieve the data and is
     extended with the support of Object-Oriented features and
     non-relational structures with XML :cite:`www-DB2Intro`. DB2
     server editions include: Advanced Enterprise Server Edition and
     Enterprise Server Edition (AESE / ESE) designed for mid-size to
     large-size business organizations, Workgroup Server Edition (WSE)
     designed for Workgroup or mid-size business organizations,
     Express -C provides the capabilities of DB2 at no charge and can
     run on any physical or virtual systems, Express Edition designed
     for entry level and mid-size business organizations, Enterprise
     Developer Edition offers single application developer useful to
     design, build and prototype the applications for deployment on
     the IBM server. DB2 has APIs for REXX, PL/I, COBOL, RPG, FORTRAN,
     C++, C, Delphi, .NET CLI, Java, Python, Perl, PHP, Ruby, and many
     other programming languages. DB2 also supports integration into
     the Eclipse and Visual Studio integrated development environments
     :cite:`www-DB2Wiki`.

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

     In the book :cite:`book-sqlserver`, the technical architecture of
     SQL Server in OLTP(online transaction processing), hybrid cloud
     and business intelligence modes is explained in detail.



201. SQLite

     SQLite is a severless SQL database engine whose source code
     resides in the public domain :cite:'sqliteabout'. SQLite
     databases, including tables, indices, and views, reside on a
     single file on the disk :cite:'sqliteabout'. It has a compact
     library, often taking up less than KiB of space, depending on the
     particular configuration :cite:'sqliteabout'. Performance is the
     tradeoff with the smaller size, i.e. performance usually runs
     faster when given more memory :cite:'sqliteabout'. SQLite
     transactions comply with the ACID (Atomicity, Consistency,
     Isolation, Durability) :cite:'acid' properties
     :cite:'sqliteabout'. SQLite does not require administration or
     configuration :cite:'sqliteover'. There are some limitations
     associated with SQLite, such as the inability to perform Right
     Outer Joins, read-only views, and access permissions (other than
     those that are associated with regular file acces permissions)
     :cite:'sqliteover' SQLite does not compare directly with
     clien/server databases such as MySQL as they are both trying to
     solve different problems :cite:'sqlitewhentouse'. While database
     engines such as MySQL aim to provide a shared database, with
     different access permissions to different
     individuals/applications, SQLite has the goal of being a local
     repository of data for applications :cite:'sqlitewhentouse' While
     SQLite is not appropriate for every situation, there certainly
     exists situations where it can prove to be a prudent choice for
     data management needs :cite:'sqlitewhentouse'.
     
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

     PostgreSQL is an open-source relational database management
     system (DBMS).  It runs on all the major operating systems like
     Linux, Mac OSX, Windows and UNIX.  It supports the ACID
     (Atomicity, Consistency, Isolation and Durability) properties of
     a conventional DBMS.  It supports the standard SQL:2008 data
     types like INTEGER, NUMERIC, etc. besides providing native
     interafaces for languages such as C++, C, Java and .Net
     :cite:`www-postgreSQL-about`.

     With the release of its latest version 9.5, it has included new
     features like the UPSERT capability, Row Level security and
     multiple features to support Big Data.  These new features rolled
     out in the latest version make PostgreSQL a very strong contender
     for modern use.  UPSERT feature has predominantly been released
     for the application developers in order to help them simplify
     their web application and software development.  UPSERT is
     basically a shorthand of "Insert, on conflict update".  Row Level
     Security (RLS), as the name suggests, enables the database
     administrators to control which particular rows could be updated
     by the users.  This helps in ensuring that the users do not
     inadvertently update rows which they are not meant to.  Features
     such as BRIN indexing, Faster sorts, CUBE, ROLLUP and GROUPING
     SETS, Foreign Data Wrappers and TABLESAMPLE were added as a part
     of the new Big Data features.  Under BRIN indexing (Block Range
     Indexing), PostgreSQL supports creating small but powerful
     indexes for large tables.  Using a new algorithm called as
     "abbreviated keys", PostgreSQL can sort NUMERIC data very
     quickly.  The CUBE, ROLLUP and GROUPING clauses enable the users
     to use just a single query to create myriad reports at different
     levels of summarization.  Using the concept of Foreign Data
     Wrappers (FDWs), PostgreSQL can be used for querying Big Data
     systems like Cassandra and Hadoop.  The TABLESAMPLE clause allows
     quick statistical sample generation of huge tables without any
     need to sort them :cite:`www-postgreSQL-features`.

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

     SciDB is an open source DBMS based on multi-dimensional array data model
     and runs on Linux platform. :cite:`ercimnews` The data store is optimized
     for mathematical operations such as linear algebra and statistical
     analysis. The data can be distributed across multiple nodes in a cluster. 

     The dimensions of the data can be either standard integers or user-defined
     types. Ragged arrays are also supported. The data is accessed through AQL,
     a SQL like language designed specifically for array operations. It
     supports operations such as to filter and join arrays and aggregation over
     the cell values. It has few similarities to Postgres in terms of
     user-defined scalar functions and storage manager. Old values of data are
     updated instead of being deleted to retain different versions of a cell.
     The arrays are divided into chunks and partitioned across the nodes in the
     cluster, with provision of caching some of them in the main memory. 

207. Rasdaman

     Rasdaman is an specialized database management system which adds
     capabilities for storage and retrival of massive
     multi-dimensional array, such as sensors,image, and statistics
     data. :cite:`www-rasdaman-wiki` It is written in C++
     language. For example, it can serve 1-D measurement data, 2-D
     satellite data, 3-D x/y/t image series and x/y/z exploration
     data, 4-D ocean and climate data, and much more.

     :cite:`www-rasdaman-official`: Rasdaman servers provides
     functionality from geo service up to complex analytics which are
     related to spatio-temporal raster data.It also integrates
     smoothly with R, OpenLayers, NASA WorldWind etc. via APIs
     calls. It is massively used in the domains like earth, space,
     and social science related fields.
     
208. Apache Derby

     :cite:`www-apachederby`: Apache Derby is java based relational
     database system. Apache Derby has JDBC driver which can be used
     by Java based applications. Apache derby is part of the Apache DB
     subproject and licensed under Apache version 2.0.

     :cite:`www-apachederbycharter`: Derby Embedded Database Engine is
     the database engine with JDBC and SQL as programming APIs.
     Client/Server functionality is achieved by Derby network server,
     it allows connection through TCP/IP using DRDA protocol. ij,
     database utility makes it possible for SQL scripts to be run on
     JDBC database. The dblook utility is the schema extraction
     tool. The sysinfo utility is used for displaying version of Java
     environment and Derby.

     There are two deployement options for Apache Derby , embedded and
     Derby network server option. In embedded framework, Derby is
     started and stopped by the single user java application without
     any adiministration required. In the case of Derby network server
     configuration, Derby is started by multi user java application
     over TCP/IP. Since Apache Derby is written in Java, it runs on
     any certified JVM(Java Virtual Machine). :cite:`www-derbymanual`:
      
209. Pivotal Greenplum

     Pivotal Greenplum is a commercial fully featured data
     warehouse. It is powered by Greenplum Database an open source
     initiative." It is powered by advanced cost-based query optimizer
     thereby delivering high analytical query performance on large
     data volumes". Pivotal Greenplum is uniquely focused on big data
     analytics :cite:`pivotal.io`.

     The system consists of a master node, standy master node and
     segment nodes. The master node consists of the catalog
     information whereas the data resides on the segment nodes.  The
     segment nodes runs on one or more segments which are modified
     PostgreSQL databases and are assigned a content identifier. The
     data is distributed among these segment nodes. The segment node
     also supports bult loading and unloading. The master node parses,
     optimizes an SQL query and dispatch it to all segment
     nodes. Therefore, it provides powerful and rapid analytics on
     petabyte scale data volumes :cite:`pivotal_wikipedia`.
     
210. Google Cloud SQL
     
     Google Cloud SQL is a fully managed data base as service
     developed by Google where google manages the backup,patching and
     replication of the databases etc
     :cite:`www-cloud-sql-google`. Cloud SQL database aims at
     developers to focus on app development leaving database
     adminstitation to a minimum. This can be understood as 'My SQL
     on Cloud' as most of the features from MySQL 5.7 are directly
     supported in Cloud SQL. The service is offered with 'Pay per
     use' providing the flexibility and 'better performance per
     dollar'.  Cloud SQL is scalable up to 16 processor cores and
     more than 100GB of RAM. :cite:`www-cloud-sql-google-faq`
      
211. Azure SQL
212. Amazon RDS

     According to Amazon Web Services, Amazon Relation Database
     Service (Amazon RDS) is a web service which makes it easy to
     setup, operate and scale relational databases in the cloud. As
     mentioned in :cite:`www-AmazonRDS` It allows to create and use
     MySQL, Oracle, SQL Server, and PostgreSQL databases in the
     cloud. Thus, codes, applications and tools used with existing
     databases can be used with Amazon RDS. The basic components of
     Amazon(As listed in :cite:`www-AmazonRDSComponents`) RDS include:
     DB Instances: DB instance is an isolated database environment in
     the cloud. Regions and availability zones: Region is a data
     center location which contains Availability Zones. Availability
     Zone is isolated from failures in other Availability
     Zones. Security groups: controls access to DB instance by
     allowing access to IP address ranges or Amazon EC2 instances that
     is specified. DB parameter groups: manage configuration of DB
     engine by specifying engine configuration values that are applied
     to one or more DB instances of the same instance type. DB option
     groups: Simplifies data management through Oracle Application
     Express (APEX), SQL Server Transparent Data Encryption, and MySQL
     memcached support.

     
213. Google F1

     F1 is a distributed relational database system built at Google to
     support the AdWords business. It is a hybrid database that
     combines high availability, the scalability of NoSQL systems like
     Bigtable, and the consistency and usability of traditional SQL
     databases. F1 is built on Spanner, which provides synchronous
     cross-datacenter replication and strong consistency
     :cite:`paper-F1`.
     
     F1 features include a strictly enforced schema, a powerful
     parallel SQL query engine, general transactions, change tracking
     and notification, and indexing, and is built on top of a
     highly-distributed storage system that scales on standard
     hardware in Google data centers. The store is dynamically sharded
     and is able to handle data center outages without data loss
     :cite:`paper-RDBMS` . The synchronous cross-datacenter
     replication and strong consistency results in higher commit
     latency which can be overcome using hierarchical schema model
     with structured data types and through smart application design.
     

214. IBM dashDB

     IBM dashDB is a data warehousing service hosted in cloud ,
     This aims at integrating the data from various sources into a
     cloud data base. Since the data base is hosted in cloud it
     would have the benifits of a cloud like scalability and less
     maintainance. This data base can be configured as 'transaction
     based' or 'Analytics based' depending on the work load
     :cite:`www-ibm-dash-db.com` .This is available through ibm blue mix
     cloud platform.

     dash DB has build in analytics based on IBM Netezza Analytics
     in the PureData System for Analytics. Because of the build in
     analytics and support of
     in memory optimization promises better performance efficieny.
     This can be run alone as a standalone or can be connected to
     variousBI or analytic tools. :cite:`www-ibm-analytics.com`
       
215. N1QL
216. BlinkDB
217. Spark SQL

     Spark SQL is Apache Spark's module for working with structured
     data. Spark SQL is a new module that integrates relational
     processing with Spark's functional programming API
     :cite:`www-spark-sql`. It is used to seamlessly mix SQL queries
     with Spark programs. Spark SQL lets you query structured data
     inside Spark programs, using either SQL or a familiar DataFrame
     API.  it offers much tighter integration between relational and
     procedural processing, through a declarative DataFrame API that
     integrates with procedural Spark code.  Spark SQL reuses the Hive
     frontend and metastore, giving you full compatibility with
     existing Hive data, queries, and UDFs by installing it alongside
     Hive. Spark SQL includes a cost-based optimizer, columnar storage
     and code generation to make queries fast
     :cite:`www-spark-sql-2`. At the same time, it scales to thousands
     of nodes and multi hour queries using the Spark engine, which
     provides full mid-query fault tolerance.

NoSQL
-----

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
     
     Solandra is a highly scalable real-time search engine built on
     Apache Solr and Apache Cassandra. Solandra simplifies maintaining
     a large scale search engine, something that more and more
     applications need. At its core, Solandra is a tight integration
     of Solr and Cassandra, meaning within a single JVM both Solr and
     Cassandra are running, and documents are stored and disributed
     using Cassandra's data model. :cite:`github-solandra`

     Solandra supports most out-of-the-box Solr functionality (search,
     faceting, highlights), multi-master (read/write to any node). It
     features replication, sharing, caching, and compaction managed
     by Cassandra. :cite:`github-solandra2`
	  
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

     Riak is a set of scalable distributed NoSQL databases developed
     by Basho Technologies. Riak KV is a key-value :cite:`www-riak-kv`
     database with time-to-live feature so that older data is deleted
     automatically.  It can be queried through secondary indexes,
     search via Apache Solr, and MapReduce. Riak TS is designed for
     time-series data. It co- locates related data on the same
     physical cluster for faster access :cite:`www-riak-ts`. Riak S2
     is designed to store large objects like media files and software
     binaries :cite:`www-riak-s2`. The databases are available in both
     open source and commercial versions with multicluster replication
     provided only in later. REST APIs are available for these
     databases.

223. ZHT

     According to :cite:`datasys`, "ZHT is a zero-hop distributed hash
     table." Distributed hash tables effectively break a hash table up
     and assign different nodes responsibility for managing different
     pieces of the larger hash table. :cite:`wiley` To retrieve a
     value in a distributed hash table, one needs to find the node
     that is responsible for the managing the key value pair of
     interest. :cite:`wiley` In general, every node that is a part of
     the distributed hash table has a reference to the closest two
     nodes in the node list. :cite:`wiley` In a ZHT, however, every
     node contains information concerning the location of every other
     node. :cite:`Li` Through this approach, ZHT aims to provide "high
     availability, good fault tolerance, high throughput, and low
     latencies, at extreme scales of millions of nodes." :cite:`Li`
     Some of the defining characteristics of ZHT are that it is
     light-weight, allows nodes to join and leave dynamically, and
     utilizes replication to obtain fault tolerance among
     others. :cite:`Li`
     
224. Berkeley DB

     Berkeley DB is a family of open source, NoSQL key-value database
     libraries.  :cite:`www-bdb-wiki` It provides a simple
     function-call API for data access and management over a number of
     programming languages, including C, C++, Java, Perl, Tcl, Python,
     and PHP. Berkeley DB is embedded because it links directly into
     the application and runs in the same address space as the
     application. :cite:`www-bdb-stanford` As a result, no
     inter-process communication, either over the network or between
     processes on the same machine, is required for database
     operations. It is also extremely portable and scalable, it can
     manage databases up to 256 terabytes in size.
     
     :cite:`www-bdb` For data management, Berkeley DB offers advanced
     services, such as concurrency for many users, ACID transactions,
     and recovery.
     
     Berkeley DB is used in a wide variety of products and a large
     number of projects, including gateways from Cisco, Web
     applications at Amazon.com and open-source projects such as
     Apache and Linux.

225. Kyoto/Tokyo Cabinet

     Tokyo Cabinet :cite:`www-tokyo-cabinet` and Kyoto Cabinet
     :cite:`www-kyoto-cabinet` are libraries of routines for managing
     a database. The database normally is a simple data file
     containing records having a key value pair structure. Every key
     and value is serial bytes with variable length. Both binary data
     and character string can be used as a key and a value. There is
     no concept of data tables nor data types like RDBMS or
     DBMS. Records are organized in hash table, B+ tree, or
     fixed-length array.Tokyo and Kyoto cabinets both are developed as
     a successor of GDBM and QDBM which are library routines for
     managing database as well. Tokyo Cabinet is written in the C
     language, and is provided as API of C, Perl, Ruby, Java, and
     Lua. Tokyo Cabinet is available on platforms which have API
     conforming to C99 and POSIX. Whereas Kyoto Cabinet is written in
     the C++ language, and is provided as API of C++, C, Java, Python,
     Ruby, Perl, and Lua. Kyoto Cabinet is available on platforms
     which have API conforming to C++03 with the TR1 library
     extensions. Both are free software licenced under GNU (General
     Public Licence). :cite:`www-tokyo-cabinet` actually mentions that
     Kyoto Cabinet is more powerful and has convenient library
     structure than Tokyo and recommends people to use Kyoto. Since
     they use key-value pair concept, you can store a record with a
     key and a value, delete a record using the key and even retrive a
     record using the key. Both have smaller size of database file,
     faster processing speed and provide effective backup procedures.

     
226. Tycoon

     Tycoon/ Kyoto Tycoon :cite:`www-fallabs-tycoon` is a lightweight
     database server developed by FLL labs and is a distributed
     Key-value store :cite:`www-cloufare-tycoon`. It is very useful in
     handling cache data persistent data of various
     applications. Kyoto Tycoon is also a package of network interface
     to the DBM called Kyoto Cabinet :cite:`www-fallabs-kyoto` which
     contains a library of routines for managing a database. Tycoon is
     composed of a sever process that manger multiple databases. This
     renders high concurrency enabling it to handle more than 10
     thousand connections at the same time.
     
227. Tyrant

     Tyrant provides network interfaces to the database management
     system called Tokyo Cabinet. Tyrant is also called as Tokyo
     Tyrant. Tyrant is implemented in C and it provides APIs for Perl,
     Ruby and C. Tyrant provides high performance and concurrent
     access to Tokyo Cabinet. The blog :cite:`www-tyrant-blog` 
     explains the results of performance experiments between Tyrant and 
     Memcached + MySQL.

     Tyrant was written and maintained by FAL Labs
     :cite:`www-tyrant-fal-labs`.  However, according to FAL Labs,
     their latest product :cite:`www-kyoto-tycoon` Kyoto Tycoon is
     more powerful and convenient server than Tokyo Tyrant.


228. MongoDB

     MongoDB is a NoSQL database which uses collections and documents
     to store data as opposed to the relational database where data is
     stored in tables and rows. In MongoDB a collection is a container
     for documents, whereas a document contains key-value pairs for
     storing data. As MongoDB is a NoSQL database, it supports dynamic
     schema design allowing documents to have different fields. The
     database uses a document storage and data interchange format
     called BSON, which provides a binary representation of JSON-like
     documents.

     MongoDB provides high data availability by way of replication and
     sharding. High cost involved in data replication can be reduced
     by horizontal data scaling by way of shards where data is
     scattered across multiple servers. It reduces query cost as the
     query load is distributed across servers. This means that both
     read and write performance can be increased by adding more shards
     to a cluster. Which document resides on which shard is determined
     by the shard key of each collection.

     As far as data backup and restore is concerned the default
     MongoDB storage engines natively support backup of complete
     data. For incremental backups one can use MongoRocks that is a
     third party tool developed by Facebook.

229. Espresso

     Espresso :cite:`www-Linkedin-Espresso` is a document-oriented
     distributed data serving platform that plays an important role in
     LinkedIn's central data pipeline. It currently powers
     approximately 30 LinkedIn applications including Member Profile,
     InMail, etc and also hosts some of its most important member
     data. Espresso provides a heirarchical data model in which the
     databases and table schema are defined in JSON.Some of the key
     component of Espresso include : 1)Router: which is a stateless
     HTTP Proxy and also acts as a entry point for all client requests
     in Espresso. The Router uses local cached routing table to manage
     the partition among all the storage nodes within the
     cluster. 2)Storage Node: are the building blocks of the storage
     and each one of them hosts a set of partition. 3) Helix: is
     responsible for cluster management in Espresso. 4) Databus: are
     responsible for capturing change to transport source transactions
     in commit order.

     All the above mentioned components together enable Espresso to achieve 
     real-time secondary indexing, on-the-fly schema evolution and also a 
     timeline consistent change capture stream.

230. CouchDB
     
     The Apache Software Foundation makes CouchDB available as an
     option for those seeking an open-source, NoSQL, document-oriented
     database. CouchDB, or cluster of unreliable commodity hardware
     database, :cite:`www-exploringcdb-couchdb` stores data as a
     JSON-formatted document.  Documents can consist of a variety of
     field types, e.g., text, booleans or lists, as well as metadata
     used by the software.  :cite:`www-techoverview-couchdb` CouchDB
     does not limit the number of fields per document, and it does not
     require any two documents to consist of matching or even similar
     fields.  That is, the document has structure, but the structure
     can vary by document.  CouchDB coordinates cluster activities
     using the master-master mode by default, which means it does not
     have any one in charge of the cluster.  However, a cluster can be
     set up to write all data to single node, which is then replicated
     across the cluster.  Either way, the system can only offer
     eventual consistency.  :cite:`www-cdb-vs-cbs-couchdb` CouchDB
     serves as the basis of Couchbase, Inc's Couchbase Server.

231. Couchbase Server

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
     Erlang.  In actuality, it is written in "Erlang using components
     of OTP alongside some C/C++" :cite:`www-erlangcentral-cbs`, It
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
     
     Cloudant is based on both Apache-backed CouchDB project and the
     open source BigCouch project. IBM Cloudant is an open source
     non-relational, distributed database service as service (DBaaS)
     that provides integrated data management, search and analytics 
     engine designed for web applications. Cloudant's distributed
     service is used the same way as standalone CouchDB, with the
     added advantage of data being redundantly distributed over
     multiple machines :cite:`www-ibm-cloudant`.
   

233. Pivotal Gemfire :cite:`www-gemfire`
     
     A real-time, consistent access to data-intensive applications is
     provided by a open source, data management platform named Pivotal
     Gemfire. "GemFire pools memory, CPU, network resources, and
     optionally local disk across multiple processes to manage
     application objects and behavior". The main features of Gemfire
     are high scalability, continuous availability, shared nothing
     disk persistence, heterogeneous data sharing and parallelized
     application behavior on data stores to name a few.  In Gemfire,
     clients can subscribe to receive notifications to execute their
     task based on a specific change in data. This is achieved through
     the continuous querying feature which enables event-driven
     architecture. The shared nothing architecture of Gemfire suggests
     that each node is self-sufficient and independent, which means
     that if the disk or caches in one node fail the remaining nodes
     remaining untouched. Additionally, the support for multi-site
     configurations enable the user to scale horizontally between
     different distributed systems spread over a wide geographical
     network.
     
234. HBase

     Apache Hbase is a distributed column-oriented database
     which is built on top of HDFS (Hadoop Distributed File
     System).According to :cite:`www-hbase`, It is a open source,
     versioned, distributed, non-relational database modelled after
     Google’s Bigtable. Similar to Bigtable providing harnessing
     distributed file storage system offered by Google file system,
     Apache Hbase provides similar capabilities on top of Hadoop and
     HDFS. Moreover, Hbase supports random, real-time CRUD
     (Create/Read/Update/Delete) operations.

     Hbase is a type of NoSQL database and is classified as a key
     value store.In HBase, value is identied with a key where both of
     them are stored as byte arrays. Values are stored in the order of
     keys. HBase is a database system where the tables have no
     schema. Some of the companies that use HBase as their core
     program are Facebook, Twitter, Adobe, Netflix etc.

235. Google Bigtable

     Google Bigtable is a NoSQL database service, built upon several
     Google technologies, including Google File System, Chubby Lock
     Service, and SSTable :cite:`www-cloudbigtable`.  Designed for Big
     Data, Bigtable provides high performance and low latency and
     scales to hundreds of petabytes
     :cite:`www-cloudbigtable`. Bigtable powers many core Google
     products, such as Search, Analytics, Maps, Earth, Gmail, and
     YouTube. Bigtable also drives Google Cloud Datastore and
     influenced Spanner, a distributed NewSQL database also developed
     by Google :cite:`www-wikispanner` :cite:`www-wikibigtable`.
     Since May 6, 2015, Bigtable has been available to the public as
     Cloud Bigtable :cite:`www-wikibigtable`.

236. LevelDB

     LevelDB is a light-weight, single-purpose library for persistence
     with bindings to many platforms. :cite:`www-leveldb` It is a
     simple open source on-disk key/value data store built by Google,
     inspired by BigTable and is used in Google Chrome and many other
     products. It supports arbitrary byte arrays as both keys and
     values, singular get, put and delete operations, batched put and
     delete, bi-directional iterators and simple compression using the
     very fast Snappy algorithm. It is hosted on GitHub under the New
     BSD License and has been ported to a variety of Unix-based
     systems, Mac OS X, Windows, and Android. It is not an SQL
     database and does not support SQL queries. Also, it has no
     support for indexes. Applications use LevelDB as a library, as it
     does not provide a server or command-line interface.

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

     Apache Accumulo, a highly scalable structured store based on
     Google’s BigTable, is a sorted, distributed key/value store that
     provides robust, scalable data storage and retrieval. Accumulo is
     written in Java and operates over the Hadoop Distributed File
     System (HDFS), which is part of the popular Apache Hadoop
     project. Accumulo supports efficient storage and retrieval of
     structured data, including queries for ranges, and provides
     support for using Accumulo tables as input and output for
     MapReduce jobs.
     Accumulo features automatic load-balancing and
     partitioning, data compression and fine-grained security
     labels. Much of the work Accumulo does involves maintaining
     certain properties of the data, such as organization,
     availability, and integrity, across many commodity-class
     machines :cite:`apache-accumulo`.

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

     Rya is a "scalable system for storing and retrieving RDF data in
     a cluster of nodes." :cite:`Punnoose` RDF stands for Resource
     Description Framework. :cite:`Punnoose` RDF is a model that
     facilitates the exchange of data on a network. :cite:`w3` RDF
     utilizes a form commonly referred to as a triple, an object that
     consists of a subject, predicate, and object. :cite:`Punnoose`
     These triples are used to describe resources on the
     Internet. :cite:`Punnoose` Through new storage and querying
     techniques, Rya aims to make accessing RDF data fast and
     easy. :cite:`apacherya`
     
241. Sqrrl
242. Neo4J

     Neo4J :cite:`www-wiki-neo4j` is a popular ACID compliant graph
     database management system developed by Neo technology. In this
     database everything is stored as nodes or edges, both of which
     can be labeled. Labels help in narrowing and simplifying the
     search process through the database. :cite:`www-slideshare` It is
     a highly scalable software and can be distributed across multiple
     machines.  The graph query language that accompanies the software
     has traversal framework which makes it fast and
     powerful. :cite:`www-neo4j` The Neo4J is often used for
     clustering. It offers two feature clustering solutions: Causal
     Clustering and Highly available
     clustering. :cite:`www-neo4j-causal-cluster` Casual clustering
     focuses on safety, scalability and causal consistency in the
     graph. :cite:`www-neo4j-HA-cluster` The highly available cluster
     places importance to fault tolerance as each instance in the
     cluster has full copies of data in their local database.

     
243. graphdb

     A Graph Database is a database that uses graph structures for
     semantic queries with nodes, edges and properties to represent
     and store data.  :cite:`www-graphdb` The Graph is a concept which
     directly relates the data items in the store.  The data which is
     present in the store is linked together directly with the help of
     relationships. It can be retrieved with a single operation.
     Graph database allow simple and rapid retrieval of complex
     hierarchical structures that are difficult to model in relational
     systems.

     There are different underlying storage mechanisms used by graph
     databases.  Some graphdb depend on a relational engine and store
     the graph data in a table, while others use a key-value store or
     document-oriented database for storage. Thus, they are inherently
     caled as NoSQL structures.  Data retrieval in a graph database
     requires a different query language other than SQL. Some of the
     query languages used to retrieve data from a graph database are
     Gremlin, SPARQL, and Cypher.  Graph databases are based on graph
     theory. They employ the concepts of nodes, edges and properties.
     
244. Yarcdata

     Yarcdata is Cray subsidiary providing Analytics
     products, namely the Urika Agile Analytics Platform and Graph
     Engine. Cray’s Urika (Universal RDF Integration Knowledge
     Appliance) system :cite:`www-Urika-appliance` is a hardware
     platform designed specifically to provide high-speed
     graph-retrieval for relationship analytics. Urika is a massively
     parallel, multi-threaded, shared-memory computing device designed
     to store and retrieve massive graph datasets. The system can
     import and host massive heterogeneous graphs represented in the
     resource description framework (RDF) format and can retrieve
     descriptive graph patterns specified in a SPARQL query.

     Urika-GD :cite:`techspec-Urika-GD` is a big data appliance for
     graph analytics helps enterprises gain key insights by
     discovering relationships in big data. Its highly scalable,
     real-time graph analytics warehouse supports ad hoc queries,
     pattern-based searches, inferencing and deduction. The Urika-GD
     appliance complements an existing data warehouse or Hadoop®
     cluster by offloading graph workloads and interoperating within
     the existing analytics workflow

     Cray Graph Engine :cite:`paper-graph-data` is a semantic database
     using Resource Description Framework (RDF) triples to represent
     the data, SPARQL as the query language and extensions to support
     mathematical algorithms.

     The paper "Graph mining meets the semantic web"
     :cite:`paper-lee2015graph` outlines the implementation of graph
     mining algorithms using SPARQL.

245. AllegroGraph
     
     "AllegroGraph is a database technology that enables businesses to
     extract sophisticated decision insights and predictive analytics
     from their highly complex, distributed data that can’t be
     answered with conventional databases, i.e., it turns complex data
     into actionable business insights." :cite:`www-Allegro` It can be
     viewed as a closed source database that is used for storage and
     retrieval of data in the form of triples (triple is a data entity
     composed of subject-predicate-object like "Professor teaches
     students").  Information in a triplestore is retrieved using a
     query language. Query languages can be classified into database
     query languages or information retrieval query languages. The
     difference is that a database query language gives exact answers
     to exact questions, while an information retrieval query language
     finds documents containing requested information.  Triple
     format represents information in a machine-readable format.
     Every part of the triple is individually addressable via
     unique URLs — for example, the statement "Professor teaches
     students" might be represented in RDF(Resource Description
     Framework ) as  http://example.name#Professor12
     http://xmlns.com/foaf/0.1/teacheshttp:
     //example.name#students. Using this representation, semantic data
     can be queried.  :cite:`www-Allegrow`

246. Blazegraph

     Blazegraph is a graph database also supporting property graph, 
     capable of clustered deployment. A graph database is a NoSQL 
     database. It is based on a graph theory of nodes and edges where 
     each node represents an element such as user or business and each 
     edge represents relationship between two nodes. It is mainly used 
     for storing and analyzing data where maintaining interconnections 
     is essential. Data pertaining to social media is best example where 
     graph database can be used.

     Blazegraph’s main focus is large scale complex graph analytics and query. 
     The Blazegraph database runs on graphics processing units (GPU) to 
     speed graph traversals. :cite ‘paper-blzgraph’

     Lets now see how Blazegraph handles data. :cite ‘www-blzgraph’ 
     **Blazegraph data can be accessed** using REST APIs. 

     **Blazegraph supports** Apache TinkerPop, which is a graph
      computing framework.

     **For graph data mining,** Blazegraph implements GAS (Gather, Apply, 
     Scatter) model as a service.

247. Facebook Tao

     In the paper published in USENIX annual technical conference,
     Facebook Inc describes TAO (The Association and Objects) as :cite
     ‘book-tao’ a geographically distributed data store that provides
     timely access to the social graph for Facebook’s demanding
     workload using a fixed set of queries. It is deployed at Facebook
     for many data types that fit its model. The system runs on
     thousands of machines, is widely distributed, and provides access
     to many petabytes of data. TAO represents social data items as
     Objects (user) and relationship between them as Associations
     (liked by, friend of).  TAO cleanly separates the caching tiers
     from the persistent data store allowing each of them to be scaled
     independently. To any user of the system it presents a single
     unified API that makes the entire system appear like 1 giant
     graph database. :cite:'www-tao'.

248. Titan:db

     Titan:db :cite:`www-Titan` is a distributed graph database that
     can support of thousands of concurrent users interacting with a
     single massive graph database that is distributed over the
     clusters. It is open source with liberal Apache 2 license.  Its
     main components are storage backend, search backend, and
     TinkerPop graph stack. Titan provides support for various 
     storage backends and also linear scalability for a growing data
     and user base. It inherits features such as ‘Gremlin’ query
     language and ‘Rexter’ graph server from TinkerPop
     :cite:`www-TinkerPop`.  For huge graphs, Titan uses a component
     called Titan-hadoop which compiles Gremlin queries to Hadoop
     MapReduce jobs and runs them on the clusters. Titan is basically
     optimal for smaller graphs.

249. Jena

     Jena is an open source Java Framework provided by Apache for
     semantic web applications. (:cite:`www-w3-jena`) It provides a
     programmatic environment for RDF, RDFS and OWL, SPARQL, GRDDL,
     and includes a rule-based inference engine. Semantic web data
     differs from conventional web applications in that it supports a
     web of data instead of the classic web of documents format. The
     presence of a rule based inference engine enable Jena to perform
     a reasoning based on OWL and RDFS ontologies.
     :cite:`www-trimc-nlp-blogspot` ` The architecture of Jena
     contains three layers : Graph layer, model layer and Ontology
     layer. The graph layer forms the base for the architecture. It
     does not have an extensive RDF implementation and serves more as
     a Service provider Interface. According to
     :cite:`www-trimc-nlp-blogspot` It provides classes/methods that
     could be further extended. The model layer extends the graph
     layer and provides objects of type ‘resource’ instead of ‘node’
     to work with.  The ontology layer enables one to work with
     triples.

250. Sesame

     Sesame is framework which can be used for the analysis of RDF
     (Resource Description Framework) data.  Resource Description
     Framework (RDF) :cite:`www-RDF` is a model that facilitates the
     interchange of data on the Web.  Using RFD enables us to merge
     data even if the underlying schemas differ.  Sesame has now 
     officially been integrated into RDF4J Eclipse project :cite:`www-sesame`.  
     Sesame takes in the natively written code as the input and then 
     performs a series of transformations, generating kernels for
     various platforms.  In order to achieve this, it makes use of the
     feature identifier, impact predictor, source-to-source translator 
     and the auto-tuner :cite:`sesame-paper-2013`.  The
     feature identifier is concerned with the extraction and detection
     of the architectural features that are important for application
     performance.  The impact predictor determines the performance
     impact of the core features extracted above.  A source-to-source
     translator transforms the input code into a parametrized one;
     while the auto-tuner helps find the optimal solution for the
     processor.
     
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

     Amazon explains DynamoDB as :cite:'www.dyndb' a fast and flexible 
     NoSQL database service for all applications that need consistent, 
     single-digit millisecond latency at any scale. It is a fully managed 
     cloud database and supports both document and key-value store models. 
     Its flexible data model and reliable performance make it a great fit 
     for mobile, web, gaming, ad tech, IoT, and many other applications. 
     DynamoDB can be easily integrated with big-data processing tools like 
     Hadoop. It can also be integrated with AWS Lambda, an event driven platform, 
     which enables creating applications that can automatically react to data 
     changes. At present there are certain limits to DynamoDB. Amazon has listed 
     all the limits in a web page titled ‘`Limits in DynamoDB <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html>`_
’

253. Google DataStore

     Google Cloud Datastore is a NoSQL document database built for
     automatic scaling, high performance, and ease of application
     development :cite:`www-google-datastore`. Though Cloud Datastore
     interface has many of the features similar to traditional
     databases,but as a NoSQL database, it differs from the SQL in the
     way as it describes relationships between various data
     objects. It also provides a number of features that relational
     databases are not optimally suited to provide, including
     high-performance at a very large scale and high-reliability. The
     Google Cloud DataStore can have different kinds of properties for
     the same kind of entities, unlike the Relational Database where
     they are represented in rows. For example, the difference between
     entities can have the properties with the same name but having
     different values. The flexible schema maps naturally to
     object-oriented and scripting languages.

     Non-relational databases have become popular recently, especially
     for web applications that require high-scalability and
     performance with high-availability. Non-relational databases such
     as Cloud DataStore let developers to choose an optimal balance
     between strong consistency and eventual consistency for each
     application. This allows developers to combine the benefits of
     both the database structures :cite:`www-google-datastore-2`.
     Datastore is designed to automatically scale to very large data
     sets, allowing applications to maintain high performance as they
     receive more traffic. Datastore also provides a number of
     features that relational databases are not optimally suited to
     provide, including high-performance at a very large scale and
     high-reliability :cite:`www-google-datastore`.

File management
---------------

254. iRODS

     The Integrated Rule-Oriented Data System (iRODS) is open source
     data management software. iRODS is released as a production-level
     distribution aimed at deployment in mission critical
     environments. It virtualizes data storage resources, so users can
     take control of their data, regardless of where and on what
     device the data is stored. The development infrastructure
     supports exhaustive testing on supported platforms. The plugin
     architecture supports microservices, storage systems,
     authentication, networking, databases, rule engines, and an
     extensible API :cite:`irods-www`.  iRODS implements data
     virtualization, allowing access to distributed storage assets
     under a unified namespace, and freeing organizations from getting
     locked in to single-vendor storage solutions. iRODS enables data
     discovery using a metadata catalog that describes every file,
     every directory, and every storage resource in the iRODS
     Zone. iRODS automates data workflows, with a rule engine that
     permits any action to be initiated by any trigger on any server
     or client in the Zone. iRODS enables secure collaboration, so
     users only need to log in to their home Zone to access data
     hosted on a remote Zone. :cite:`github-irods-www`


255. NetCDF

     NetCDF is a set of software libraries and self-describing,
     machine-indepen dent data formats that support the creation,
     access, and sharing of array oriented scientific data. NetCDF was
     developed and is maintained at Unidata , part of the University
     Corporation for Atmospheric Research (UCAR) Commun ity Programs
     (UCP). Unidata is funded primarily by the National Science F
     oundation :cite:`paper-netCDF` :cite:`www-netcdf` . The purpose
     of the Netwo rk Common Data Form(netCDF) interface is to support
     the creation, efficient access, and sharing of data in a form
     that is self-describing, portable, co mpact, extendible, and
     archivable Version 3 of netCDF is widely used in atmospheric and
     ocean sciences due to its simplicity. NetCDF version 4 has been
     designed to address limitations of netCDF version 3 while
     preserving useful forms of compatibility with existing
     application software and data archives :cite:`paper-netCDF`.
     NetCDF consists of: a) A conceptual data model b) A set of binary
     data formats c) A set of APIs for C/Fortran/Java

256. CDF

     Common Data Format :cite:`www-cdf` is a conceptual data
     abstraction for storing, manipulating, and accessing
     multidimensional data sets. CDF differs from traditional physical
     file formats by defining form and function as opposed to a
     specification of the bits and bytes in an actual physical format.
 
     CDF's integrated dataset is composed by following two categories
     :(a)Data Objects - scalars, vectors, and n-dimensional
     arrays.(b)Metadata - set of attributes describing the CDF in
     global terms or specifically for a single variable
     :cite:`user-guide-cdf`.

     The self-describing property (metadata) allows CDF to be a
     generic, data-independent format that can store data from a wide
     variety of disciplines. Hence, the application developer remains
     insulated from the actual physical file format for reasons of
     conceptual simplicity, device independence, and future
     expandability.CDF data sets are portable on any of the
     CDF-supported platforms and accessible with CDF applications or
     layered tools. To ensure the data integrity in a CDF file,
     checksum method using MD5 algorithm is employed
     :cite:`www-digitalpreserve`.

     Compared to HDF format :cite:`www-wiki-hdf`, CDF permitted
     cross-linking data from different instruments and spacecraft in
     ISTP with one development effort. CDF is widely supported by
     commercial and open source data analysis/visualization software
     such as IDL, MATLAB, and IBM’s Data Explorer (XP).

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
     magzines. Vatican Library :cite:`www-fits-vatican-library` used FITS 
     for long term preservation of their book, manuscripts and other
     collection. Matlab, a language used for technical computing
     supports fits :cite:`www-fits-matlab`. The 2011 paper
     :cite:`paper-fits-2011` explains how to perform
     processing of astronomical images on Hadoop using FITS. 

260. RCFile

     RCFile (Record Columnar File) :cite:`www-rcfile-wiki` is a big
     data placement data structure that supports fast data loading and
     query processing coupled with efficient storage space utilization
     and adaptive to dynamic workload environments. It is designed for
     data warehousing systems that uses map-reduce. The data is stored
     as a flat file comprising of binary key/value pairs. The rows are
     partitioned first and then the columns are partitioned in each
     row and the respective meta-data for each row is stored in the
     key part for that row and the values comprises of the data part
     of the row. Storing the data in this format enables RCFile to
     accomplish fast loading and query processing.A shell utility is
     available for reading RCFile data and metadata
     :cite:`www-rcfile-cat`. According to :cite:`he2011rcfile`, RCFile has
     been chosen in Facebook data warehouse system as the default
     option. It has also been adopted by Hive and Pig, the two most
     widely used data analysis systems developed in Facebook and
     Yahoo!

261. ORC

     ORC files were created as part of the initiative to massively
     speed up Apache Hive and improve the storage efficiency of data
     stored in Apache Hadoop. ORC is a self-describing type-aware
     columnar file format designed for Hadoop workloads. It is
     optimized for large streaming reads, but with integrated support
     for finding required rows quickly. Storing data in a columnar
     format lets the reader read, decompress, and process only the
     values that are required for the current query. Because ORC files
     are type-aware, the writer chooses the most appropriate encoding
     for the type and builds an internal index as the file is
     written.ORC files are divided in to stripes that are roughly 64MB
     by default. The stripes in a file are independent of each other
     and form the natural unit of distributed work. Within each
     stripe, the columns are separated from each other so the reader
     can read just the columns that are required :cite:`www-orc-docs`.

     
262. Parquet

     Apache parquet is the column Oriented data store for Apache
     Hadoop ecosystem and available in any data processing framework,
     data model or programming language :cite:`www-parquet`. It
     stores data such that the values in each column are physically
     stored in contiguous memory locations. As it has the columnar
     storage, it provides efficient data compression and encoding
     schemes which saves storage space as the queries that fetch
     specific column values need not read the entire row data and thus
     improving performance.It can be implemented using the Apache
     Thrift framework which increases its flexibility to work with a
     number of programming languages like C++, Java, Python, PHP, etc.
     

Data Transport
--------------

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

     According to :cite:`www-ftp-wiki` FTP is an acronym for File Transfer
     Protocol. It is network protocol standard used for transferring
     files between two computer systems or between a client and a
     server. It is part of the Application layer of the Internet
     Protocol Suite and works along with HTTP/SSH. It follows a
     client-server model architecture. Secure systems asks the client
     to authenticate themselves using a Username and Password
     registered with the server to access the files via FTP. The
     specification for FTP was first written by Abhay Bhushan
     :cite:`www-rfc114` in 1971 and is termed as RFC114. The current
     specification, RFC959 in use was written in 1985. Several other
     versions of the specification are available which provides
     firewall friendly FTP access, additional security extensions,
     support for IPV6 and passive mode file access respectively. FTP
     can be used in command line in most of the operating systems to
     transfer files. There are FTP clients such as WinSCP, FileZilla
     etc. which provides a graphical user interface to the clients to
     authenticate themselves (sign on) and access the files from the
     server.
     
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
     log data :cite:`apache-flume`. Flume was created to allow you to
     flow data from a source into your Hadoop® environment.  In Flume,
     the entities you work with are called sources, decorators, and
     sinks. A source can be any data source, and Flume has many
     predefined source adapters. A sink is the target of a specific
     operation. A decorator is an operation on the stream that can
     transform the stream in some manner, which could be to compress
     or uncompress data, modify data by adding or removing pieces of
     information, and more :cite:`ibm-flume`.

269. Sqoop
     
     Apache Sqoop is a tool to transfer large amounts of data between
     Apache Hadoop and sql databases :cite:`www-sqoop`. The name is a
     Portmanteau of SQL + Hadoop. It is a command line interface
     application which supports incremental loads of complete tables,
     free form (custom) SQL Queries and allows the use of saved and
     scheduled jobs to import latest updates made since the last
     import. The imports can also be used to populate tables in Hive
     or Hbase. Sqoop has the option of export, which allows data to be
     transferred from Hadoop into a relational database. Sqoop is
     supported in many different business integration suits like
     Informatica Big Data Management, Pentaho Data Integration,
     Microsoft BI Suite and Couchbase :cite:`sqoop-wiki`.

270. Pivotal GPLOAD/GPFDIST

     Greenplum Database :cite:`book-greenplum-gollapudi2013` is a
     shared nothing, massively parallel processing solution built to
     support next generation data warehousing and Big Data analytics
     processing. In its new distribution under Pivotal, Greenplum
     Database is called Pivotal(Greenplum) Database.

     gpfdist :cite:`www-gpfdist` is Greenplum's parallel file
     distribution program. It is used by readable external tables and
     gpload to serve external table files to all Greenplum Database
     segments in parallel. It is used by writable external tables to
     accept output streams from Greenplum Database segments in
     parallel and write them out to a file.

     gpload :cite:`book-greenplum-gollapudi2013` is data loading
     utility is used to load data into Greenplum's external table in
     parallel.

     Google has an invention :cite:`patent-google-gpf` relating to
     integrating map-reduce processing techniques into a distributed
     relational database. An embodiment of the invention is
     implemented by Greenplum as gpfdist.

Cluster Resource Management
---------------------------

271. Mesos

     Apache Mesos :cite:`www-mesos` abstracts CPU, memory,
     storage, and other compute resources away from machines (physical
     or virtual), enabling fault-tolerant and elastic distributed
     systems to easily be built and run effectively. The Mesos kernel
     runs on every machine and provides applications (e.g., Hadoop,
     Spark, Kafka, Elasticsearch) with API’s for resource management
     and scheduling across entire datacenter and cloud environments.

     The resource scheduler of Mesos supports a generalization of
     max-min fairness :cite:`paper-mesos-Abu-Dbai-2016`, termed Dominant
     Resource Fairness (DRF) :cite:`paper-mesos-ghodsi2011dominant`
     scheduling discipline, which allows to harmonize execution of
     heterogeneous workloads (in terms of resource demand) by
     maximizing the share of any resource allocated to a specific
     framework.
     
     Mesos uses containers for resource isolation between
     processes. In the context of Mesos, the two most important
     resource-isolation methods to know about are the control groups
     (cgroups) built into the Linux kernel,and Docker. The difference
     between using hyper-V, Docker containers, cgroup is described in
     detail in the book "Mesos in action" :cite:`book-mesos-Ignazio-2016`


272. Yarn

     Yarn (Yet Another Resource Negotiator) is Apache Hadoop’s cluster
     management project :cite:`www-cloudera` . It’s a resource
     management technology which make a pace between, the way
     applications use Hadoop system resources & node manager
     agents. Yarn, "split up the functionalities of resource
     management and job scheduling/monitoring". The NodeManager watch
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

     Helix is a data management system getting developed by IBM which
     helps the users to do explitory analysis of the data received
     from various sources following different formats. This system
     would help orgnaize the data by providing links between data
     collected across various sources dispite of the knowledge of the
     data sources schemas.It also aims at providing  the data really
     required for the user by extracting the important information
     from the data. This would plan to target the issue by
     mainataining the "knowledge base of schemas" and
     "context-dependent dynamic linkage", The system can get the
     schema details either from the  knowledge base being maintained
     or can even get the schema from the data being received. As the
     number of users for helix increases the linkages gets stronger
     and would provide better data
     quality. :cite:`www-ibm-helix-paper`
      
274. Llama

     Llama stands for leveraging learning to automatically manage
     algorithms. There has been a phenomenal improvement in algorithm
     portfolio and selection approaches. The main drawback of them is
     that their implementation is specific to a problem domain and
     customized which leads to the difficulty of exploring new
     techniques for certain problem domains. Llama has been developed
     to provide an extensible toolkit which can initiate exploration
     of a variety of portfolio techniques over a wide range of problem
     domains. It is modular and implemented as an R package. It
     leverages the extensive library of machine learning algorithms
     and techniques in R :cite:`lla1`. Llama can be regarded as a
     framework which provides the prerequisites for initiating
     automatic portfolio selectors. It provides a set of methods for
     combining several trivial approaches of portfolio selection into
     sophisticated techniques. The primary reason behind the
     introduction of Llama was to help the researchers working in
     algorithm selection, algorithm portfolios, etc. and can be just
     used as a tool for designing the systems :cite:`lla1`.
     
275. Google Omega
276. Facebook Corona

     Corona is a new scheduling framework developed by facebook which
     separates the cluster resource management from job coordination.
     Facebook, employed the MapReduce implementation from Apache
     Hadoop since 2011 for job scheduling. The scheduling MapReduce
     framework has its limitations with the scalability as when the
     number of jobs at facebook grew in the next few years. Another
     limitation of Hadoop was it was a pull-based scheduling model as
     the task tracker have to provide a heartbeat to the job tracker to
     indicate that it is running which associated with a pre-defined
     delay, that was problematic for small jobs 
     :cite:`www-facebook-corona`. Hadoop MapReduce is also constrained
     by its static slot-based resource management model where a
     MapReduce cluster is divided into a fixed number of map and
     reduce slots based on a static configurations so the slots are
     not utilized completely anytime the cluster workload does not fit
     the static configuration.

     Corona improves over the Hadoop MapReduce by introducing a
     cluster manager whose only purpose is to track the nodes in the
     cluster and the amount free resources
     :cite:`www-facebook-corona`. A dedicated job tracker is created
     for each job and can run either in the same process as the
     client (for small jobs) or as a separate process in the cluster
     (for large jobs). The other difference is that it uses a
     push-based scheduling whose implementation does not involve a
     periodic heartbeat and thus scheduling latency is minimized. The
     cluster manager also implements a fair-share scheduling as it has
     access to the full snapshot of the cluster for making the
     scheduling decisions. Corona is used as an integral part of the
     Facebook's data infrastructure and is helping power big data
     analytics for teams across the company.
     
277. Celery

     "Celery is an asynchronous task queue/job queue based on
     distributed message passing.  The focus of celery is mostly on
     real-time operation, but it equally scheduling.  In celery there
     are execution units, called tasks, are executed concurrently on a
     single or more worker servers using multiprocessing, Eventlet,or
     gevent.  Tasks can execute asynchronously (in the background) or
     synchronously (wait until ready).  Celery is easy to integrate
     with web framework. Celery is written in python whereas the
     protocol can be implemented in any language":cite:`celery`.Celery
     is a simple, flexible, and reliable distributed system to process
     vast amounts of messages,while providing operations with the
     tools required to maintain such a system":cite:`celerydocs`

     
278. HTCondor

    
     HTCondor is a specialized workload management system for
     compute-intensive jobs.  HTCondor provides various features like
     a)job queuing mechanism, b)scheduling policy, c)resource
     monitoring, d)priority scheme and e)resource management just as
     other full-featured batch systems.  "Users submit their serial or
     parallel jobs to HTCondor,HTCondor places them into a queue,
     chooses when and where to run the jobs based upon a policy,
     carefully monitors their progress, and ultimately informs the
     user upon completion".  HTCondor can be used to manage a cluster
     of dedicated compute nodes. HTCondor uses unique mechanisms to
     harness wasted CPU power from idle deskto workstations.  "The
     ClassAd mechanism in HTCondor provides an extremely flexible and
     expressive framework for matching resource requests (jobs) with
     resource offers (machines).  Jobs can easily state both job
     requirements and job preferences".  "HTCondor incorporates many
     of the emerging Grid and Cloud-based computing methodologies and
     protocols":cite:`htcondor`

     
279. SGE

     According to :cite:`www-sge-wiki`, Sun Grid Engine (SGE) renamed
     to Oracle Grid Engine (OGE) is a grid computing cluster software
     system. Grid Engine is a high performance computing cluster used
     for managing job queueing in distributed and parallel
     environment. It can accept, schedule, dispatch and manage the
     execution of single, parallel user jobs in a remote or
     distributed manner. It also manages the resource allocation to
     those jobs. The resources can be anything like processors,
     storage, RAM and licenses for softwares. The latest stable
     release of OGE is termed as 6.2u8 which came out in October
     1,2012.

     OGE supports a vast array of features like: Topology-aware
     scheduling and thread binding, advanced fault tolerance
     mechanisms for job scheduling, web interface based status
     reporting and ability to use different scheduling
     algorithms,etc. OGE runs on several platforms including AIX, BSD,
     Linux, Solaris, OS X, Tru64, Windows, etc. It is under delpoyment
     phasae for IBM's 64-bit operating system z/OS. Standard Grid
     cluster comprises of one master host and many execution
     hosts. There is a option of creating shadow master hosts which
     would take the master's place incase of a system crash. Notable
     deployments of OGE include: TSUBAME supercomputer at the Tokyo
     Institute of Technology,Ranger at the Texas Advanced Computing
     Center (TACC) and San Diego Supercomputer Center (SDSC).

280. OpenPBS

     Portable Batch System (or simply PBS) is the name of computer
     software that performs job scheduling. Its primary task is to
     allocate computational tasks, i.e., batch jobs, among the
     available computing resources. It is often used in conjunction
     with UNIX cluster environments :cite:`openpbs-wiki`. OpenPBS is
     the original open source version of PBS. There are more
     commercialized versions of the same software. One of the key
     feature of OpenPBS is that it supports millions of cores with
     fast job dispatch and minimal latency. It meets unique site goals
     and SLAs by balancing job turnaround time and utilization with
     optimal job placement. OpenPBS also includes automatic fail-over
     architecture with no single point of failure – jobs are never
     lost, and jobs continue to run despite failures. It is built upon
     a Flexible Plugin Framework which simplifies administration with
     enhanced visibility and extensibility :cite:`openpbs-www`.

281. Moab

     Moab HPC Suite is a workload management and resource orchestration
     platform that automates the scheduling, managing, monitoring, and
     reporting of HPC workloads on massive scale. It uses multi-dimensional
     policies and advanced future modeling to optimize workload start and
     run times on diverse resources. It integrates and accelerates the
     workloads management across independent clusters by adding
     grid-optimized job submission. Moab's unique intelligent and
     predictive capabilities evaluate the impact of future orchestration
     decisions across diverse workload domains (HPC, HTC, Big Data, and
     Cloud VMs):cite:`www-moab`.

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

     :cite:`sotomayor2006globus` The Globus Toolkit is an open source
     toolkit organized as a collection of loosely coupled
     components. These components consist of services, programming
     libraries and development tools designed for building Grid-based
     applications. GT components fall into five broad domain areas:
     Security, Data Management, Execution Management, Information
     Services, and Common Runtime. :cite:`foster2006globus` These
     components enable a broader "Globus ecosystem" of tools and
     components that build on or interoperate with GT functionality to
     provide a wide range of useful application-level
     functions. www-about-globus :cite:`www-about-globus` Since 2000,
     companies like Fujitsu, IBM, NEC and Oracle have pursued Grid
     strategies based on the Globus Toolkit.

285. Pilot Jobs

     In pilot job, an application acquires a resource so that it can
     be delegated some work directly by the application; instead of
     requiring some job scheduler. The issue of using a job scheduler
     is that a waiting queue is required. Few examples of Pilot Jobs
     are the :cite:`pilot-job-falkon-paper-2007` Falkon lightweight
     framework and :cite:`pilot-job-htcaas-paper-2007` HTCaaS. Pilot
     jobs are typically associated with both Parallel computing as
     well as Distributed computing. Their main aim is to reduce the
     dependency on queues and the associated multiple wait times.

     Using pilot jobs enables us to have a multilevel technique for 
     the execution of various workloads. This is so because the jobs
     are typically acquired by a placeholder job and they 
     relayed to the workloads :cite:`www-pilot-job-paper-2016`.      

File systems
----------------------------------------------------------------------

286. HDFS
     
     Hadoop provides distributed file system framework that uses Map
     reduce (Distributed computation framework) for transformation and
     analyses of large dataset.  Its main work is to partition the
     data and other computational tasks to be performed on that data
     across several clusters.  HDFS is the component for distributed
     file system in Hadoop.An HDFS cluster primarily consists of a
     Name Node and Data Nodes. Name Node manages the file system
     metadata such as access permission, modification time, location
     of data and Data Nodes store the actual data.   When user
     applications or Hadoop frameworks request access to a file in
     HDFS, Name Node service responds with the Data Node locations for
     the respective individual data blocks that constitute the whole
     of the requested file:cite:`www-hdfs`.

287. Swift
288. Haystack

     Haystack is an open source project working with data from
     internet of Things, aim to standardise the semantic data model
     generated from smart devices, homes, factories etc.  It include
     automation, control, energy, HVAC, lighting and other
     environmental systems.  :cite:`www-project-haystack`
     
     Building block of Project haystack is on TagModel tagging of
     metadata stored in key/value pair applied to entity such id, dis,
     sites, geoAddr, tz. Structure the primary structure of haystack
     is based on three entities, Site location of single unit, equip
     physical or logical piece of equipment within site, point sensor,
     actuator or setpoint value for equip, it also includes weather
     outside weather condition. TimeZone time series data is most
     important factor it is foundation for sensor and operational
     data. Captured data not always associated with measurable unit,
     however it provides facility to associate the data points.
     Commonly Supported units like Misc, Area, Currency, Energy,
     Power, Temperature, Temperature differential, Time, Volumetric
     Flow. The data often represented in 2D tabular form for tagged
     entities. It supports the query language for filtering over the
     data, data exposed through REST API in JSON format.

289. f4
     
     As the amount of data Facebook stores continues to increase, the
     need for quick access and efficient storage of data continues to
     rise.  Facebook stores a class of data in Binary Large OBjects
     (BLOBs), which can be created once, read many times, never
     modified, and sometimes deleted. Haystack, Facebook’s traditional
     BLOB storage system is becoming increasingly inefficient. The
     storage efficiency is measured in the
     effective-replication-factor of BLOBs.

     f4 BLOB storage system provides an effective-replication-factor
     lower than that of Haystack. f4 is simple, modular, scalable, and
     fault tolerant. f4 currently stores over 65PBs of logical BLOBs,
     with a reduced effective-replication-factor from 3.6 to either
     2.8 or 2.1 :cite:`paper-f4`.

     
290. Cinder
      
     "Cinder is a block storage service for Openstack"
     :cite:`wiki-Cinder`. Openstack Compute uses ephemeral disks
     meaning that they exist only for the life of the Openstack
     instance i.e. when the instance is terminated the disks
     disappear. Block storage system is a type of persistent storage
     that can be used to persist data beyond the life of the
     instance. Cinder provides users with access to persistent
     block-level storage devices. It is designed such that users can
     create block storage devices on demand and attach them to any
     running instances of OpenStack Compute :cite:`book-Cinder`. This
     is achieved through the use of either a reference
     implementation(LVM) or plugin drivers for other storage. Cinder
     virtualizes the management of block storage devices and provides
     end users with a self-service API to request and consume those
     resources without requiring any knowledge of where their storage
     is actually deployed or on what type of device
     :cite:`wiki-Cinder`.
     
291. Ceph

     Ceph is open-source storage platform providing highly scalable
     object, block as well as file-based storage. Ceph is a unified,
     distributed storage system designed for excellent performance,
     reliability and scalability :cite:`www-ceph`. Ceph Storage
     clusters are designed to run using an algorithm called CRUSH
     (Controlled Replication Under Scalable Hashing) which replicates
     and re-balance data within the cluster dynamically to ensure even
     data distribution across cluster and quick data retrieval without
     any centralized bottlenecks.
 
     Ceph’s foundation is the Reliable Autonomic Distributed Object
     Store (RADOS) :cite:`www-cepharch`, which provides applications
     with object, block, and file system storage in a single unified
     storage cluster—making Ceph flexible, highly reliable and easy to
     manage. Ceph decouples data and metadata operations by
     eliminating file allocation tables and replacing them with
     generating functions which allows RADOS to leverage intelligent
     OSDs to manage data replication, failure detection and recovery,
     low-level disk allocation, scheduling, and data migration without
     encumbering any central server(s) :cite:`paper-Ceph`.
 
     The Ceph Filesystem :cite:`www-cephfs` is a POSIX-compliant
     filesystem that uses a Ceph Storage Cluster to store its
     data. Ceph’s dynamic subtree partitioning is a uniquely scalable
     approach, offering both efficiency and the ability to adapt to
     varying workloads. Ceph Object Storage supports two compatible
     interfaces: Amazon S3 and Openstack Swift.

292. FUSE

     FUSE (Filesystem in Userspace) :cite:`www-fuse` "is an interface
     for userspace programs to export a filesystem to the Linux
     kernel". The FUSE project consists of two components: the fuse
     kernel module and the libfuse userspace library. libfuse provides
     the reference implementation for communicating with the FUSE
     kernel module.The code for FUSE itself is in the kernel, but the
     filesystem is in userspace.  As per the 2006 paper
     :cite:`fuse-paper-hptfs` on HPTFS which has been built on top of
     FUSE. It mounts a tape as normal file system based data storage
     and provides file system interfaces directly to the application.
     Another implementation of FUSE FS is CloudBB
     :cite:`fuse-paper-CloudBB`. Unlike conventional filesystems
     CloudBB creates an on-demand two-level hierarchical storage
     system and caches popular files to accelerate I/O performance. On
     evaluating performance of real data-intensive HPC applications in
     Amazon EC2/S3, results show CloudBB improves performance by up to
     28.7 times while reducing cost by up to 94.7% compared to the
     ones without CloudBB.

     Some more implementation examples of FUSE are - mp3fs (A VFS to
     convert FLAC files to MP3 files instantly), Copy-FUSE(To access
     cloud storage on Copy.com), mtpfs(To mount MTP devices) etc.

293. Gluster
294. Lustre

     The Lustre file system :cite:`www-lustre` is an open-source,
     parallel file system that supports many requirements of
     leadership class HPC simulation environments and Enterprise
     environments worldwide. Because Lustre file systems have high
     performance capabilities and open licensing, it is often used in
     supercomputers.Lustre file systems are scalable and can be part
     of multiple computer clusters with tens of thousands of client
     nodes, tens of petabytes of storage on hundreds of servers, and
     more than a terabyte per second of aggregate I/O
     throughput. Lustre file systems a popular choice for businesses
     with large data centers, including those in industries such as
     meteorology, simulation, oil and gas, life science, rich media,
     and finance. Lustre provides a POSIX compliant interface and many
     of the largest and most powerful supercomputers on Earth today
     are powered by the Lustre file system.
     
295. GPFS

     IBM General Parallel File System (GPFS) was rebranded to IBM 
     Spectrum Scale on February 17, 2015 :cite:`www-wikigpfs`.
     See 380.

380. IBM Spectrum Scale

     General Parallel File System (GPFS) was rebranded as IBM Spectrum 
     Scale on February 17, 2015 :cite:`www-wikigpfs`.

     Spectrum Scale is a clustered file system, developed by IBM,
     designed for high performance. It "provides concurrent high-speed
     file access to applications executing on multiple nodes of
     clusters" :cite:`www-wikigpfs` and can be deployed in either
     shared-nothing or shared disk modes. Spectrum Scale is available
     on AIX, Linux, Windows Server, and IBM System Cluster 1350
     :cite:`www-wikigpfs`.  Due to its focus on performance and
     scalability, Spectrum Scale has been utilized in compute
     clusters, big data and analytics - including support for Hadoop
     Distributed File System (HDFS), backups and restores, and private
     clouds :cite:`www-spectrumscale`.

296. GFFS

     The Global Federated File System (GFFS) :cite:`www-gffs` is a
     computing technology that allows linking of data from Windows,
     Mac OS X, Linux, AFS, and Lustre file systems into a global
     namespace, making them available to multiple systems. It is a
     federated, secure, standardized, scalable, and transparent
     mechanism to access and share resources across organizational
     boundaries It is useful when, for data resources, boundaries do
     not require application modification and do not disrupt existing
     data access patterns. It uses FUSE to handle access control and
     allows research collaborators on remote systems to access a
     shared file system. Existing applications can access resources
     anywhere in the GFFS without modification. It helps in rapid
     development of code, which can then be exported via GFFS and
     implemented in-place on a given computational resource or Science
     Gateway.
     
297. Public Cloud: Amazon S3

     Amazon Simple Storage Service (Amazon S3) :cite:`www-amazon-s3` is
     storage object which provides a simple web service interface to
     store and retrieve any amount of data from anywhere on the
     web. With Amazon S3, users can store as much data as they want
     and can scale it up and down based on the requirements.For
     developers Amazon S3 provides full REST API's and SDK's which can
     be integrated with third-party technologies. Amazon S3 is also
     deeply integrated with other AWS services to make it easier to
     build solutions that use a range of AWS services which include
     Amazon CloudFront, Amazon CloudWatch, Amazon Kinesis, Amazon RDS,
     Amazon Glacier etc. Amazon S3 provides auotmatic encryption of
     data once the data is uploaded in the cloud. Amazon S3 uses the
     concept of Buckets and Objects for storing data wherein Buckets
     are used to store objects. Amazon S3 services can be used using
     the Amazon Console Management. :cite:`www-amazon-s3-docs` The steps
     for using the Amazon S3 are as follows: (1) Sign up for Amazon S3
     (2) After sign up, create a Bucket in your account, (3) Create
     and object which might be an file or folder, and (4) Perform
     operations on the object which is stored in the cloud.

	
298. Azure Blob

     Azure Blob storage is a service that stores unstructured data in
     the cloud as objects/blobs. Blob storage can store any type of
     text or binary data, such as a document, media file, or
     application installer :cite:`www-azure-3` Blob storage is also
     referred to as object storage. The word ‘Blob’ expands to Binary
     Large OBject. There are three types of blobs in the service offe-
     red by Windows Azure namely block, append and page
     blobs. :cite:`www-azure-2`
     1. Block blobs are collection of individual blocks with unique
     block ID.  The block blobs allow the users to upload large amount
     of data.
     2. Append blobs are optimized blocks that helps in making the
     operations efficient.
     3. Page blobs are compilation of pages. They allow random read
     and write operations. While creating a blob, if the type is not
     specified they are set to block type by default. All the blobs
     must be inside a container in your storage.  Azure Blob storage
     is a service for storing large amounts of unstructured object
     data, such as text or binary data, that can be accessed from
     anywhere in the world via HTTP or HTTPS. You can use Blob storage
     to expose data publicly to the world, or to store application
     data privately. Common uses of Blob storage include serving
     images or documents directly to a browser, storing files for
     distributed access, streaming video and audio, storing data for
     backup and restore, disaster recovery, and archiving and storing
     data for analysis by an on-premises or Azure-hosted service.
     Azure Storage is massively scalable and elastic with an
     auto-partitioning system that automatically load-balances your
     data. Blob storage is a specialized storage account for storing
     your unstructured data as blobs (objects) in Azure Storage. Blob
     storage is similar to existing general-purpose storage accounts
     and shares all the great durability, availability, scalability,
     and performance features. Blob storage has two types of access
     tiers that can be specified, hot access tier, which will be
     accessed more frequently, and a cool access tier, which will be
     less frequently accessed. There are many reasons why you should
     consider using BLOB storage. Perhaps you want to share files with
     clients, or off-load some of the static content from your web
     servers to reduce the load on them. :cite:`www-azure-3`

299. Google Cloud Storage

     Google Cloud Storage is the cloud enabled storage offered by
     Google. :cite:`www-google-cloud-storage` It is unified object
     storage. To have high availability and performance among
     different regions in the geo-redundant storage offering. If you
     want high availability and redundancy with a single region one
     can go for "Regional" storage. Nearline and Coldline’ are the
     different archival storage techniques. "Nearline" storage
     offering is for the archived data which the user access less than
     once a month . "Coldline’ storage is the storage which is used
     for the data which is touched less than once a year.

     All the data in Google Cloud storage belongs inside a project. A
     project will contains different buckets. Each bucket has
     different objects. We need to make sure that the name of the
     bucket is unique across all Google cloud name space . And the
     name of the objects should unique in a bucket.


Interoperability
----------------

300. Libvirt

     Libvirt is an open source API to manage hardware virtualization
     developed by Red Hat.  It is a standard C library but has
     accessibility from other languages such as Python, Perl, Java and
     others. :cite:`www-libvirt` Multiple virtual machine
     monitors(VMM) or hypervisors are supported such as KVM,QEMU, Xen,
     Virtuozzo, VMWare ESX, LXC, and BHyve.  It can be divided into
     five categories such as hypervisor connection, domain, network,
     storage volume and pool.  :cite:`www-ibm` It is accessible by
     many operating systems such as Linux, FreeBSD, Mac OS, and
     Windows OS.
     
301. Libcloud

     :cite::`www-libcloudwiki` Libcloud is a python library that
     allows to interact with several popular cloud service
     providers. It is primarily designed to ease development of
     software products that work with one or more cloud services
     supported by Libcloud. It provides a unified API to interact with
     these different cloud services. Current API includes methods for
     list, reboot, create, destroy, list images and list
     sizes. :cite::`www-libclouddoc` lists Libcloud key component APIs
     Compute, Storage, Load Balancers, DNS, Container and
     Backup. Compute API allows users to manage cloud servers. Storage
     API allows users to manage cloud object storage and also provides
     CDN management functionality. Load balancer, DNS and Backup API’s
     allows users to manage their respective functionalities, as
     services, and related products of different cloud service
     providers. Container API allows users to deploy containers on to
     container virtualization platforms. Libcloud supports Python 2,
     Python 3 and PyPy.
     
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
     management for the development of "interoperable tools"
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
     system requirements. It is often denoted as "resource
     templates" or "flavours"   :cite:`drescher-parak-wallom-2015`.

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

     The Storage Networking Industry Association (SNIA)
     :cite:`www-sniawebsite` is a non-profit organization formed by
     various companies, suppliers and consumers of data storage and
     network products. SNIA defines various standards to ensure the
     quality and interoperability of various storage systems. One of
     the standards defined by SNIA to for providers and users of cloud
     is Cloud Data Management Interface (CDMI). According latest issue
     of CDMI :cite:`cdmi-manual`, "CDMI International Standard is
     intended for application developers who are implementing or using
     cloud storage. It documents how to access cloud storage and to
     manage the data stored there." It defines functional interface
     for applications that will use cloud for various functionalities
     like create, retrieve, update and delete data elements from the
     cloud. These interface could be used to manage containers along
     with the data. The interface could be used by administrative and
     management applications as well. Also, the CDMI specification
     uses RESTful principles in the interface design. All the
     standards issued on CDMI can be found on SNIA web page
     :cite:`www-cdmiwebsite`.
     
306. Whirr
     
     Apache Whirr is a set of libraries for running cloud services,
     which provides a cloud-neutral way to run services
     :cite:`www-ApacheWhirr`. This is achieved by using cloud-neutral
     provisioning and storage libraries such as jclouds and
     libcloud. Whirr's API should be built on top these libraries and
     is not exposed to the users. It is also a common service API, in
     which the details of its working are, particular to the service.
     Whirr provides smart defaults for services by which any properly
     configured system can run quickly, while still being able to
     override settings as needed. Whirr can also be used as a command
     line tool for deploying clusters. It uses low level API libraries
     to work with providers which was mentioned in the
     :cite:`www-slideshare-ApacheWhirr`.

     
307. Saga

     SAGA(Simple API for Grid Applications) provides an abstraction
     layer to make it easier for applications to utilize and exploit
     infra effectively. With infrastructure being changed continuously
     its becoming difficult for most applications to utilize the
     advances in hardware. SAGA API provides a high level abstraction
     of the most common Grid functions so as to be independent of the
     diverse and dynamic Grid environments :cite:`saga-paper`. This
     shall address the problem of applications developers developing
     an application tailored to a specific set of infrastructure.
     SAGA allows computer scientists to write their applications at
     high level just once and not to worry about low level hardware
     changes. SAGA provides this high level interface which has the
     underlying mechanisms and adapters to make the appropriate calls
     in an intelligent fashion so that it can work on any underlying
     grid system. "SAGA was built to provide a standardized, common
     interface across various grid middleware systems and their
     versions" :cite:`www-saga-ogf-document`.

     As SAGA is to be implemented on different types of middleware it
     does not specify a single security model but provides hooks to
     interfaces of various security models. The SAGA API provides a
     set of packages to implement its objectivity : SAGA supports data
     management, resource discovery, asynchronous notification, event
     generation, event delivery etc. It does so by providing set of
     functional packages namely SAGA file package, replica package,
     stream package, RPC package, etc. SAGA provides interoperability
     by allowing the same application code to run on multiple grids
     and also communicate with applications running on
     others :cite:`saga-paper`.

308. Genesis

DevOps
------

309. Docker (Machine, Swarm)

     Docker is an open-source container-based technology. A container
     allows a developer to package up an application and all its part
     including the stack it runs on, dependencies it is associated
     with and everything the application requires to run within an
     isolated environment. Docker separates Application from the
     underlying Operating System in a similar way as Virtual Machines
     separates the Operating System from the underlying
     hardware. Dockerizing an application is lightweight in comparison
     with running the application on the Virtual Machine as all the
     containers share the same underlying kernel, the Host OS should
     be same as the container OS (eliminating guest OS) and an average
     machine cannot have more than few VMs running o them.

     Docker Machine is a tool that lets you install Docker Engine on
     virtual hosts, and manage the hosts with docker-machine commands
     :cite:`docker-book`. You can use Machine to create Docker hosts
     on your local Mac or Windows machine, on your company network, in
     your data center, or on cloud providers like AWS or Digital
     Ocean. For Docker 1.12 or higher swarm mode is integrated with
     the Docker Engine, but on the older versions with Machine's swarm
     option, user can configure a swarm cluster. Docker Swarm provides
     native clustering capabilities to turn a group of Docker engines
     into a single, virtual Docker Engine. "With these pooled
     resources user can scale out your application as if it were
     running on a single, huge computer" :cite:`www-docker`. Docker
     Swarm can be scaled up to 1000 Nodes or up to 50,000 containers
     
310. Puppet

     Puppet is an open source software configuration management
     tool :cite:`www-puppet-wiki-puppet`.This aims at automatic
     configuration of the software
     applications and infrastructure. This configuration is done
     using the easy to use languge.
     Puppet works on major linux distributions and also on
     microsoft windows ,
     it is also cross-platform application making it easy to manage
     and portable. :cite:`www-puppet-puppet-site`

     Puppet works with a client server model. All the clients (
     nodes)  which needs to be managed will have 'Puppet Agent'
     installed and 'Puppet Master' contains the configuration for
     different hosts this demon process rund on master server. The
     connection between 'Puppet Master' and 'Puppet agent' will be
     established using thesecured SSL connection. The configiration
     at client will be validated as per the set up in Puppet master
     at a predefined interval. If configration at client is not
     matching with the master puppet agent fetches the equired
     changes from master. :cite:`www-puppet-slashroot`

     Puppet is developed by Puppet Labs
     using ruby language and released as GNU General Public License
     (GPL) until version 2.7.0 and the Apache License 2.0 after
     that. :cite:`www-puppet-wiki-puppet`
	
311. Chef

     Chef is a configuration management tool. It is implemented in
     Ruby and Erlang. Chef can be used to configure and maintain
     servers on-premise as well as cloud platforms like Amazon EC2,
     Google Cloud Platform and Open Stack. The book
     :cite:`chef-book` explains the use of concept called 'recipes' in
     Chef to manage server applications and utilities such as database
     servers like MySQL, or HTTP servers like Apache HTPP and systems
     like Apache Hadoop.

     Chef is available in open source version and it also has
     commercial products for the companies which need it
     :cite:`www-chef-commercial`

312. Ansible

     Ansible is an IT automation tool that automates cloud
     provisioning, configuration management, and application
     deployment. :cite:`www-ansible` Once Ansible gets installed on a
     control node, which is an agentless architecture, it connects to
     a managed node through the default OpenSSH connection
     type. :cite:`www-ansible-wikipedia`

     As with most configuration management softwares, Ansible
     distinguishes two types of servers: controlling machines and
     nodes. First, there is a single controlling machine which is
     where orchestration begins. Nodes are managed by a controlling
     machine over SSH. The controlling machine describes the location
     of nodes through its inventory.

     Ansible manages machines in an agent-less manner. Ansible is
     decentralized, if needed, Ansible can easily connect with
     Kerberos, LDAP, and other centralized authentication management
     systems.

313. SaltStack

     SaltStack (also Salt) platform is a Python-based open-source
     configuration management software and remote execution engine,
     which makes systems and configuration management software for the
     orchestration and automation of CloudOps, ITOps and DevOps at
     scale :cite:`www-saltstack`. SaltStack is used to manage all the
     data center things including any cloud, infrastructure,
     virtualization, application stack, software or code. Salt is
     built on two major concepts, which are clearly mentioned in
     :cite:`SaltStack-book` as remote execution and configuration
     management. In the remote execution system, Salt leverages Python
     to accomplish complex tasks with single-function calls. The
     configuration management system in Salt, called States, builds
     upon the remote execution foundation to create repeatable,
     enforceable configuration for the minions (connects to the master
     and treats the master as the source)
     
314. Boto

     The latest version of Boto is Boto3 :cite:`www-boto`.
     Boto3 is the Amazon Web Services (AWS) Development Kit (SDK) for
     Python :cite:`www-boto-github`. It enables the
     Python developers to make use of services like Amazon S3
     and Amazon EC2 :cite:`www-boto-amazon-python-sdk`.  It provides
     object oriented APIs along with low-level direct service 
     :cite:`www-boto3-documentation`.  It provides simple in-built functions 
     and interfaces to work with Amazon S3 and EC2.

     Boto3 has two distinct levels of APIs - client and resource 
     :cite:`www-boto-amazon-python-sdk`. One-to-one mappings to underlying 
     HTTP API is provided by the client APIs. Resource APIs provide resource
     objects and collections to perform various actions by accessing
     the attributes.  Boto3 also comes with 'waiters'. Waiters are
     used for polling status changes in AWS, automatically. Boto3 has
     these waiters for both the APIs
     - client as well as resource. 
     
315. Cobbler

     Cobbler is a Linux provisioning system that facilitates and
     automates the network based system installation of multiple computer
     operating systems from a central point using services such as DHCP,
     TFTP and DNS :cite:`www-cobbler`.It is a nifty piece of code that
     assemble s all the usual
     setup bits required for a large network installation like TFTP, DNS,
     PXE installation trees. and automates the process[1].It can be
     configured for PXE, reinstallations and virtualized guests using Xen,
     KVM or VMware.  Cobbler interacts with the koan program for
     re-installation and virtualization support.  Cobbler builds the
     Kickstart mechanism and offers installation profiles that can be
     applied to one or many machines.  Cobbler has features to dynamically
     change the information contained in a kickstart template (definition),
     either by passing variables called ksmeta or by using so-called
     snippets.

316. Xcat

     xCAT is defined as extreme cloud/cluster administration
     toolkit. Tnd his open source software was developed by IBM and 
     utilized on clusters based on either linux or a version of UNIX 
     called AIX. With this service administrator is enabled with 
     a number of capabilities including parallel system management, 
     provision OS usage on virtual machines, and manage all systems 
     remotely. :cite:`www-xcat` xCAT works with various cluster types 
     such as high performance computing, horizontal scaling web farms, 
     administrative, and operating systems. :cite:`www-03ibm`
     
317. Razor

     Razor is a hardware provisioning application, developed by Puppet
     Labs and EMC. Razor was introduced as open, pluggable, and
     programmable since most of the provisioning tools that existed
     were vendor-specific, monolithic, and closed. According to
     :cite:`www-RazorWiki` it can deploy both bare-metal and virtual
     systems. During boot the Razor client automatically discovers the
     inventory of the server hardware – CPUs, disk, memory, etc.,
     feeds this to the Razor server in real-time and the latest state
     of every server is updated. It maintains a set of rules to
     dynamically match the appropriate operating system images with
     server capabilities as expressed in metadata. User-created policy
     rules are referred to choose the preconfigured model to be
     applied to a new node. The node follows the model's directions,
     giving feedback to Razor as it completes various steps as
     specified in :cite:`www-RazorPuppet`. Models can include steps
     for handoff to a DevOps system or to any other system capable of
     controlling the node.
     
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

     Openstack Heat, a template deployment service was the project
     launched by Openstack, a cloud operating system similar to AWS
     Cloud Formation. :cite:`www-heat-blog-introduction` states - Heat
     is an orchestration service which allows us to define resources
     over the cloud and connections amongst them using a simple text
     file called referred as a ‘template’. "A Heat template describes
     the infrastructure for a cloud application in a text file that is
     readable and writable by humans, and can be checked into version
     control" :cite:`www-heat-wiki`.

     Once the execution enviroment has been setup and a user wants to
     modify the architecture of resources in the future, a user needs
     to simply change the template and check it in. Heat shall make
     the necessary changes. Heat provides 2 types of template -
     HOT(Heat Orchestration Template) and CFN (AWS Cloud Formation
     Template). The HOT can be defined as YAML and is not compatible
     with AWS. The CFN is expressed as JSON and follows the syntax of
     AWS Cloud Formation and thus is AWS compatible. Further, heat
     provides an additional @parameters section in its template which
     can be used to parameterize resources to make the template
     generic.

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

     :cite:`www-rockscluster` Rocks provides open cluster distribution
     solution is buid targetting the scientist with less cluster
     experience to ease the process of deployment,managing,upgrading
     and scaling high performance parallel computing cluster.  It was
     initially build on linux however the latest version Rocks 6.2
     Sidewinder is also available on CentOS.Rocks can help create a
     cluster in few days with default configuration and software
     packages.  Rocks distribution package comes with high-performance
     distributed and parallel computing tools.It is used by NASA, the
     NSA , IBM Austin Research LAB, US Navy and many other institution
     for their projects.

324. Cisco Intelligent Automation for Cloud

     Cisco Intelligent automation for cloud desires to help different
     service providers and software professionals in delivering highly
     secure infrastructure as a service on demand. It provides a
     foundation for organizational transformation by expanding the
     uses of cloud technology beyond its infrastructure
     :cite:`cis1`. From a single self-service portal, it automates
     standard business processes and sophisticated data center which
     is beyond the provision of virtual machines. Cisco Intelligent
     automation for cloud is a unified cloud platform that can deliver
     any type of service across mixed environments :cite:`cis2`. This
     leads to an increase in cloud penetration across different
     business and IT holdings. Its services range from underlying
     infrastructure to anything-as-a-service by allowing its users to
     evaluate, transform and deploy the IT and business services in a
     way they desire.

325. Ubuntu MaaS
326. Facebook Tupperware

     Facebook Tupperware is a system which provisions services by
     taking requirements from engineers and mapping them to actual
     hardware allocations using containers
     :cite:`www-FaceTup`.Facebook Tupperware simplifies the task of
     configuring and running services in production and allows
     engineers to focus on actual application logic.The tupperware
     system consists of a Scheduler , Agent process and a Server
     Databse.  The Scheduler consists of set of machines with one of
     them as master and the others in standby.The machines share state
     among them.The Agent process runs on each and every machine and
     manages all the tasks and co-ordinates with the Scheduler.The
     Server database stores the details of resources available across
     machines which is used by the scheduler for scheduling jobs and
     tasks.Tupperware allows for sandboxing of the tasks which allows
     for isolation of the tasks.Initially isolation was implemented
     using chroots but now it is switched to Linux Containers(LXC)
     .The configuration for the container is done by a specific config
     file written in a dialect of python by the owner of the process.

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
     in each layer of AWS OpsWorks Stacks :cite:`www-awsopsworks`.

328. OpenStack Ironic

     Ironic :cite:`www-ironicwebsite` project is developed and
     supported by OpenStack. Ironic provisions bare metal machines
     instead of virtual machines and functions as hypervisor API that
     is developed using open source technologies like Preboot
     Execution Environment (PXE), Dynamic Host Configuration Protocol
     (DHCP), Network Bootstrap Program (NBP), Trivial File Transfer
     Protocol (TFTP) and Intelligent Platform Management Interface
     (IPMI). A properly configured Bare Metal service with the Compute
     and Network services, could provision both virtual and physical
     machines through the Compute service’s API. But, the number of
     instance actions are limited, due to physical servers and switch
     hardware. For example, live migration is not possible on a bare
     metal instance. The Ironic service has five key components. A
     RESTful API service, through which other components would
     interact with the bare metal servers, a Conductor service,
     various drivers, messaging queue and a database. Ironic could be
     integrated with other OpenStack projects like Identity
     (keystone), Compute (nova), Network (neutron), Image (glance) and
     Object (swift) services.
     
329. Google Kubernetes

     Google Kubernetes is a cluster management platform developed by
     Google. According to :cite:`www-kubernetesdoc` is an open source
     system for "automating deployment, scaling and management of
     containerized applications". It primarily manages clusters
     through containers as they decouple applications from the
     host operating system dependencies and allowing their quick and
     seamless deployment, maintenance and scaling.

     Kubernetes components are designed to extensible primarily
     through Kubernetes API. Kubernetes follows a master-slave
     architecture, according to :cite:`www-kuberneteswiki` Kubernetes
     Master controls and manages the clusters workload and
     communications of the system. Its main components are etcd, API
     server, scheduler and controller manager. The individual
     Kubernetes nodes are the workers where containers are
     deployed. The components of a node are Kubelet, Kube-proxy and
     cAdvisor. Kunernetes makes it easier to run application on public
     and private clouds. It is also said to be self-healing due to
     features like auto-restart and auto-scaling.
     
330. Buildstep
     
     Buildsteps is an open software developed under MIT license. 
     It is a base for Dockerfile and it activates Heroku-style 
     application. Heroku is a platform-as-service (PaaS) that 
     automates deployment of applications on the cloud. The 
     program is pushed to the PaaS using git push, and then 
     PaaS detects the programming language, builds, and runs 
     application on a cloud platform :cite:`plassnig15`.
     Buildstep takes two parameters: a tar file that contains 
     the application and a new application container name to 
     create a new container for this application. Build script 
     is dependent on buildpacks that are pre-requisites for 
     buildstep to run. The builder script runs inside the new 
     container.  The resulting build app can be run with Docker 
     using docker build -t your_app_name command.
     :cite:`github-buildstep`. 

331. Gitreceive

     Gitreceive is used to create an ssh+git user which can accept
     repository pushes right away and also triggers a hook
     script. Gitreceive is used to push code anywhere as well as
     extend your Git workflow. "Gitreceive dynamically creates bare
     repositories with a special pre-receive hook that triggers your
     own general gitreceive hook giving you easy access to the code
     that was pushed while still being able to send output back to the
     git user" Gitreceive can also be used to provide feedback to the
     user not only just to trigger code on git push.  Gitreceive can
     used for the following: "a)for putting a git push deploy
     interface in front of App Engine b)Run your company build/test
     system as a separate remote c)Integrate custom systems into your
     workflow d)Build your own Heroku e)Push code
     anywhere".:cite:`lindsay2016`
     
332. OpenTOSCA

     The Topology and Orchestration Specification for Cloud
     Applications,TOSCA is a new standard facilitating platform
     independent description of Cloud applications. OpenTOSCA is a
     runtime for TOSCA-based Cloud applications. The runtime enables
     fully automated plan-based deployment and management of
     applications defined in the OASIS TOSCA packaging format CSAR,
     Cloud Service ARchive.  The key tasks of OpenTOSCA, are to
     operate management operations, run plans, and manage state of the
     TOSCA :cite:`openTOSCA-paper`.
     
333. Winery

     Eclipse Winery :cite:`www-winery` is a "web-based environment to 
     graphically model [Topology and Orchestration Specification for 
     Cloud Applications] TOSCA topologies and plans managing these 
     topologies." Winery :cite:`winery-paper-2013` is a "tool 
     offering an HTML5-based environment for graph-based modeling of 
     application topologies and defining reusable component and 
     relationship types." This web-based :cite:`winery-paper-2013` 
     interface enables users to drag and drop icons to create 
     automated "provisioning, management, and termination of 
     applications in a portable and interoperable way." 
     Essentially, this web-based interface :cite:`winery-paper-2013` 
     allows users to create an application topology, which 
     "describes software and hardware components involved and 
     relationships between them" as well a management plan, which 
     "captures knowledge [regarding how] to deploy and manage an 
     application."

334. CloudML
                                                            
     CloudML a research project initiated by SINTEF in 2011
     :cite:`www-cloudml`. Cloud computing facilitates to shared
     and virtualized computer capabilities like storage, memory,
     CPU, GPU and networks, to user. There is multiple cloud provider,
     also the Iaas(Infrastructure-as-a-service) and
     Pass(Platform-as-a-service). To operate multiple cloud for
     applications, which requires multiple private, public, or hybrid
     clouds, limit the capability of each cloud solution.  Solution
     provided by such cloud will gets incompatible with others. So,
     to providing the solution which can compatible with multi-cloud
     platform is a tedious job. To achieve this CloudML provides a
     "domain-specific modelling language along with run time environment"
     :cite:`www-cloudml`.It provides the interoperability and provide
     vendor lock-in, also it provides the solution on specification of
     provisioning, deployment, and adaptation concerns of multi-cloud
     systems. At design time as well as runtime :cite:`www-cloudml`.
     CloudML provides two level of abstraction while developing model
     for multi-cloud application:

     - Cloud Provider-Independent Model (CPIM), this specifies the
       provisioning and deployment.
       
     - Cloud Provider-Specific Model (CPSM), which filters the
       provisioning and deployment of multiple cloud application,
       according to its cloud.

     This two abstract approach help CloudML to achieve the multi-cloud 
     application support :cite:`www-cloudmlwiki`.

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

     Terraform, developed by HashiCorp, is an infrastructure
     management tool, it has an open source platform as well as an
     enterprise version and uses infrastructure as a code to increase
     operator productivity. It’s latest release is Terraform 0.8
     According to the website :cite:`www-Terraform` it enables users
     to safely and predictably create, change and improve the
     production infrastructure and codifies APIs into declarative
     configuration files that can be shared amongst other users and
     can be treated as a code, edited, reviewed and versioned at the
     same time. The book :cite:`www-terraform-book` explains that it
     can manage the existing and popular service it provides as well
     as create customized in-house solutions. It builds an execution
     plan that describes what it can do next after it reaches a
     desired state to accomplish the goal state. It provides a
     declarative executive plan which is used for creating
     applications and implementing the infrastructures. Terraform is
     mainly used to manage cloud based and SaaS infrastructure, it
     also supports Docker and VMWare vSphere.
     
337. DevOpSlang
     
     DevOpSlang serves as means of collaboration and provides the
     foundation to automate deployment and operations of an
     application. Technically, it is a domain specific language based
     on JavaScript Object Notation (JSON). JSON Schema is used to
     define a formal schema for DevOpSlang and complete JSON Schema
     definition of DevOpSlang is publicly available on GitHub project
     DevOpSlang: http://github.com/jojow/devopslang Devopsfiles are
     the technical artifacts (Unix shell commands, Chef Scripts, etc.)
     rendered using DevOpSlang to implement operations.  Beside some
     meta data such as ’version’ and ’author’ Devopsfile defines
     operations like ’start’ consisting of a single or multiple
     actions which specifies the command to run the
     application. Similarly, a ’build’ operation can be defined to
     install the dependencies required to run the
     application. Different abstraction levels may be combined
     consistently such as a ’deploy’ operation consisting of actions
     on the level of Unix shell commands and actions using portable
     Chef cookbooks :cite:`DevOpSlang`.

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
---------------------------------------

339. Xen

     Xen is the only open-source bare-metal hypervisor based on
     microkernel design :cite:`www-xen-wikipedia`. The hypervisor runs
     at the highest privilege among all the processes on the
     host. It's responsibility is to manage CPU and memory and handle
     interrupts :cite:`www-xen-overview`. Virtual machines are
     deployed in the guest domain called DomU which has no access
     privilege to hardware. A special virtual machine is deployed in
     the control domain called Domain 0. It contains hardware drivers
     and the toolstack to control the VMs and is the first VM to be
     deployed. Xen supports both Paravirtualization and hardware
     assisted virtualization. The hypervisor itself has a very small
     footprint. It's being actively maintained by Linux Foundation
     under the trademark "XEN Project". Some of the features included
     in the latest releases include "Reboot-free Live Patching" (to
     enable application of security patches without rebooting the
     system) and KCONFIG support (compilation support to create a
     lighter version for requirements such as embedded systems)
     :cite:`www-xen-fl`.
          
340. KVM

     It is an acronym for Kernel-based Virtual Machine for the Linux
     Kernel that turns it into a hypervisor upon installation. It was
     originally developed by Qumranet in 2007 :cite:`www-KVM-wiki`. It
     has a kernel model and uses kernel as VMM. It only supports fully
     virtualized VMs. It is very active for Linux users due to it’s
     ease of use, it can be completely controlled by ourselves and
     there is an ease for migration from or to other platforms. It is
     built to run on a x86 machine on an Intel processor with
     virtualization technology extensions (VT-x) or an AMD-V. It
     supports 32 and 64 bit guests on a 64 bit host and hardware
     visualization features. The supported guest systems are Solaris ,
     Linux, Windows and BSD Unix :cite:`www-KVM-webpage`.

341. QEMU
     
     QEMU (Quick Emulator) is a generic open source hosted hypervisor
     :cite:`www-hypervisor` that performs hardware virtualization
     (virtualization of computers as complete hardware platform,
     certain logical abstraction of their componentry or only the
     certain functionality required to run various operating systems)
     :cite-`www-qemu` and also emulates CPUs through dynamic binary
     translations and provides a set of device models, enabling it to
     run a variety of unmodified guest operating systems.
     
     When used as an emulator, QEMU can run Operating Systems and
     programs made for one machine (ARM board) on a different machine
     (e.g. a personal computer) and achieve good performance by using
     dynamic translations.  When used as a virtualizer, QEMU achieves
     near native performance by executing the guest code directly on
     the host CPU. QEMU supports virtualization when executing under
     the Xen hypervisor or using KVM kernel module in Linux
     :cite:`www-qemuwiki`.

     Compared to other virtualization programs like VMWare and VirtualBox,
     QEMU does not provide a GUI interface to manage virtual machines nor
     does it provide a way to create persistent virtual machine with saved
     settings. All parameters to run virtual machine have to be specified
     on a command line at every launch. It’s worth noting that there are
     several GUI front-ends for QEMU like virt-manager and gnome-box.

342. Hyper-V
     
     Hyper-V is a native hypervisor which was first released alongside
     Windows Server 2008. It is available free of charge for all the
     Windows Server and some client operating systems since the
     release. Microsoft Hyper-V, is also codenamed as Viridian and
     formerly known as Windows Server Virtualization, is a native
     hypervisor. Xbox One also include Hyper-V, in which it would
     launch both Xbox OS and Windows 10. :cite:`www-hyper-v-wikipedia`

     Hyper-V is used to create virtual machines on x86-64 systems
     which are running Windows. Windows 8 onwards, Hyper-V supersedes
     Windows Virtual PC as the hardware virtualization component of
     the client editions of Windows NT. A server computer running
     Hyper-V can be configured to expose individual virtual machines
     to one or more networks.

343. VirtualBox
344. OpenVZ

     OpenVZ (Open Virtuozzo) is an operating system-level
     virtualization technology for Linux. It allows a physical server
     to run multiple isolated operating system instances, called
     containers, virtual private servers, or virtual environments
     (VEs). OpenVZ is similar to Solaris Containers and
     LXC. :cite:`www-openvz-3` While virtualization technologies like
     VMware and Xen provide full virtualization and can run multiple
     operating systems and different kernel versions, OpenVZ uses a
     single patched Linux kernel and therefore can run only Linux. All
     OpenVZ containers share the same archite- cture and kernel
     version. This can be a disadvantage in situations where guests
     require different kernel versions than that of the host. However,
     as it does not have the overhead of a true hypervisor, it is very
     fast and efficient. Memory allocation with OpenVZ is soft in that
     memory not used in one virtual environment can be used by others
     or for disk caching. :cite:`www-openvz-2` While old versions of
     OpenVZ used a common file system (where each virtual environment
     is just a directory of files that is isolated using chroot),
     current versions of OpenVZ allow each container to have its own
     file system.  OpenVZ has four main features, :cite:`www-openvz-1`
     1. OS virtualization: A container (CT) looks and behaves like a
     regular Linux system. It has standard startup scripts; software
     from vendors can run inside a container without OpenVZ-specific
     modifications or adjustment; A user can change any configuration
     file and install additional software; Containers are completely
     isolated from each other and are not bound to only one CPU and
     can use all available CPU power.
     2. Network virtualization: Each CT has its own IP address and CTs
     are isolated from the other CTs meaning containers are protected
     from each other in the way that makes traffic snooping
     impossible; Firewalling may be used inside a CT
     3. Resource management: All the CTs are use the same
     kernel. OpenVZ resource management consists of four main
     components: two-level disk quota, fair CPU scheduler, disk I/O
     scheduler, and user beancounters.
     4. Checkpointing and live migration: Checkpointing allows to
     migrate a container from one physical server to another without a
     need to shutdown/restart a container. This feature makes possible
     scenarios such as upgrading your server without any need to
     reboot it: if your database needs more memory or CPU resources,
     you just buy a newer better server and live migrate your
     container to it, then increase its limits.


345. LXC
     
     LXC (Linux Containers) is an operating-system-level
     virtualization method for running multiple isolated Linux systems
     (containers) on a control host using a single Linux kernel
     :cite:`www-wiki-lxc`. LXC are similar to the treditional virtual
     machines but instead of having seperate kernel process for the
     guest operating system being run, containers would share the
     kernal process with the host operating system. This is made
     possible with the implementation of namespaces and
     cgroups. :cite:`www-jpablo`

     Containers are light weighed ( As guest operating system
     loading and booting is eleminated ) and more customizable
     compared to VM technologies.The basis for docker developement
     is also LXC. :cite:`www-infoworld`. Linux containers would
     work on the major distributions of linux this would not work
     on Microsoft Windows.
	
346. Linux-Vserver

     Linux-VServers are used on web hosting services, pooling
     resources and containing any security
     breach. :cite:`www-linux-vserver-org` "Linux servers
     consist of three building blocks Hardware, Kernel and
     Applications" the purpose of kernel is to provide abstraction
     layer between hardware and application. Linux-Vserver provides
     VPS securely partitioning the resources on computer system in
     such a way that process cannot mount denial of service out of the
     partition.
     
     It utilises the power of Linux kernel and top of it with
     additional modification provides secure layer to each process
     (VPS) feel like it is running separate system.  By providing
     context separation, context capabilities, each partition called
     as security context, chroot barrier created on provate directory
     of each VPS to prevent unauthorized modification. Booting VPS in
     new secure context is just matter of booting server, context is
     so robust to boot many server simultaneously.
     
     The virtual servers shares same system calls, shares common file
     system, process within VS are queued to same scheduler that of
     host allowing guest process to run concurrently on SMP
     systems. No additional overhead of network virtualization.  These
     few advantages of Linux-VServer.

347. OpenStack
 
     OpenStack :cite:`www-OpenStack.org` is a free and open source cloud operating 
     system mostly deployed as infrastructure as a service(Iaas) that allows 
     us to control large pool of computers, storage, and networking resources.
     OpenStack is managed by OpenStack Foundation :cite:`www-OpenStack-Found`. 
     
     Just like cloud, OpenStack provides infrastructure which runs as platform 
     upon which end users can create applications. Key components of OpenStack 
     include: Nova: which is the primary computing engine, Swift: which is a 
     storage system for object and files, Neutron: which ensures effective 
     communication between each of the components of the OpenStack. Other   
     components include: Cinder, Horizon, Keystone, Glance, Ceilometer and 
     Heat. The main goal of Openstack is to allow business to build 
     Amazon-like cloud services in their own data centers.OpenStack is 
     licensed under the Apache 2.0 license :cite:`www-apache-license` 
	
348. OpenNebula

     According to OpenNebula webpage :cite:`www-opennebula-org` it
     provides simple but feature-rich and flexible solutions for the
     comprehensive management of virtualized data centers to enable
     private, public and hybrid laaS clouds. It is a cloud computing
     platform for managing heterogenous distributed data centers
     infrastructures. The OpenNebula toolkit includes features for
     management, scalability, security and accounting. It used in
     various sectors like hosting providers, telecom providers,
     telecom operators, IT service providers, supercomputing centers,
     research labs, and international research projects
     :cite:`www-opennebula-wiki`. More about OpenNebula can be found
     in the following paper that is published at ieee computer society
     :cite:`paper-opennebula`
     
349. Eucalyptus

     Eucalyptus is a Linux-based open source software framework for
     cloud computing that implements Infrastructure as a Service
     (IaaS). IaaS are systems that give users the ability to run and
     control entire virtual machine instances deployed across a
     variety physical resources :cite:`paper-eucalyptus`. Eucalyptus
     is an acronym for "Elastic Utility Computing Architecture for
     Linking Your Programs to Useful Systems."

     A Eucalyptus private cloud is deployed on an enterprise’s data
     center infrastructure and is accessed by users over the
     enterprise’s intranet. Sensitive data remains entirely secure
     from external interference behind the enterprise firewall
     :cite:`www-eucalyptus`.

     
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
     :cite:`nimbus-paper`, the use of Nimbus Phantom
     to deploy auto-scaling solution across multiple NSF FutureGrid
     clouds is explained. In this implementation Phantom was responsible 
     for deploying instances across multiple clouds and monitoring those
     instance.  Nimbus platform supports Nimbus, Open Stack, Amazon
     and several other clouds.

351. CloudStack

     Apache CloudStack is open source software designed to deploy and
     manage large networks of virtual machines, as a highly available,
     highly scalable Infrastructure as a Service (IaaS) cloud
     computing platform. It uses existing hypervisors such as KVM,
     VMware vSphere, and XenServer/XCP for virtualization. In addition
     to its own API, CloudStack also supports the Amazon Web Services
     (AWS) API and the Open Cloud Computing Interface from the Open
     Grid Forum. :cite:`www-cloudstack`

     ColudStack features like built-in high-availability for hosts
     and VMs, AJAX web GUI for management, AWS API compatibility,
     Hypervisor agnostic, snapshot management, usage metering, network
     management (VLAN's, security groups), virtual routers, firewalls,
     load balancers and multi-role support. :cite:`www-cloudstack-wikipedia`
	  
352. CoreOS
     
     :cite:`www-core` states that "CoreOS is a linux operating system
     used for clustered deployments." CoreOS allows applications to
     run on containers. CoreOS can be run on clouds, virtual or
     physical servers. CoreOS allows the ability for automatic software
     updates inorder to make sure containers in cluster are secure and
     reliable. It also makes managing large cluster environements
     easier. CoreOS provides open source tools like CoreOS Linux,
     etcd,rkt and flannel. CoreOS also has commercial products
     Kubernetes and CoreOS stack. In CoreOS linux service
     discovery is achieved by etcd, applications are run on Docker and
     process management is achieved by fleet.

353. rkt

     rkt is an container manager developed by CoreOS :cite:`www-CoreOS`
     designed for Linux clusters. It is an alternative for Docker 
     runtime and is designed for server environments with high 
     security and composibity requirement. It is the first 
     implementation of the open container standard called 
     "App Container" or "appc" specification but not the only one. 
     It is a standalone tool that lives outside of the core operating 
     system and can be used on variety of platforms such as Ubuntu,
     RHEL, CentOS, etc. rkt implements the facilities specified by 
     the App Container as a command line tool. It allows execution 
     of App Containers with pluggable isolation and also varying 
     degrees of protection. Unlike Docker, rkt runs containers as 
     un-priviliged users making it impossible for attackers to break 
     out of the containers and take control of the entire physical 
     server. rkt's primary interface comprises a single executable 
     allowing it easily integrate with existing init systems and 
     also advanced cluster environments. rkt is open source and is 
     written in the Go programming language :cite:`www-github/rkt`.

     
354. VMware ESXi

     VMware ESXi (formerly ESX) is an enterprise-class, type-1
     hypervisor developed by VMware for deploying and serving virtual
     computers :cite:`wiki-vmwareESXi`. The name ESX originated as an
     abbreviation of Elastic Sky X. ESXi installs directly onto your
     physical server enabling it to be partitioned into multiple
     logical servers referred to as virtual machines.  Management of
     VMware ESXi is done via APIs. This allows for an "agent-less"
     approach to hardware monitoring and system management. VMware
     also provides remote command lines, such as the vSphere Command
     Line Interface (vCLI) and PowerCLI, to provide command and
     scripting capabilities in a more controlled manner. These remote
     command line sets include a variety of commands for
     configuration, diagnostics and troubleshooting. For low-level
     diagnostics and the initial configuration, menu-driven and
     command line interfaces are available on the local console of the
     server :cite:`vmware-esxi`.
     
     
355. vSphere and vCloud

     vSphere was developed by VMware and is a cloud computing 
     virtualization platform. :cite:`www-vmware`  vSphere is not
     one piece of software but a suite of tools that contains software 
     such as vCenter, ESXi, vSphere client and a number of other 
     technologies.  ESXi server is a type 1 hypervisor on a physical 
     machine of which all virtual machines are installed.  
     The vSphere client then allows administrators to connect to 
     the ESXi and manage the virtual machines.  The vCenter server 
     is a virtual machine that is also installed on the 
     ESXi server which is used in environments when multiple ESXi 
     servers areexist.  Similarly, vCloud is also a suite of 
     applications but for establishing an infrastructure for a 
     private cloud. :cite:`www-mustbegeek`  The suite includes the 
     vsphere suite, but also contains site recovery management for 
     disaster recovery,  site networking and security.  Additionally, 
     a management suite that can give a visual of the infrastructure 
     to determine where potential issues might arise.
     
356. Amazon

     Amazon’s AWS (Amazon Web Services) is a provider of
     Infrastructure as a Service (IaaS) on cloud. It provides a broad
     set of infrastructure services, such as computing, data storage,
     networking and databases.  One can leverage AWS services by
     creating an account with AWS and then creating a virtual server,
     called as an instance, on the AWS cloud.  In this instance you
     can select the hard disk volume, number of CPUs and other
     hardware configuration based on your application needs.  You can
     also select operating system and other software required to run
     your application. AWS lets you select from the countless
     services.  Some of them are mentioned below:

     -  Amazon Elastic Computer Cloud (EC2)
     -  Amazon Simple Storage Service (Amazon S3)
     -  Amazon CloudFront
     -  Amazon Relational Database Service (Amazon RDS)
     -  Amazon SimpleDB
     -  Amazon Simple Notification Service (Amazon SNS)
     -  Amazon Simple Queue Service (Amazon SQS)
     -  Amazon Virtual Private Cloud (Amazon VPC)

     Amazon EC2 and Amazon S3 are the two core IaaS services, which
     are used by cloud application solution developers
     worldwide. :cite:'www-aws'

     **Improve: all of them need bibentries**
     
357. Azure
358. Google and other public Clouds

     A public cloud is a scenario where a provider provides services
     such as infrastructure or applications to the public over the
     internet. Google cloud generally refers to services such as cloud
     print, connect, messaging, storage and platform
     :cite:`goo1`. Google cloud print allows a print-aware application
     on a device, installed on a network, to provide prints to any
     printer on that network. Cloud connect allows an automatic
     storage and synchronization of Microsoft word documents,
     power-points and excel sheets to Google docs while preserving the
     Microsoft office formats. In certain cases, developers require
     important notifications to be sent to applications targeting
     android operating system. Google cloud messaging provides such
     services. Google cloud platform allows the developers to deploy
     their mobile, web and backend solutions on a highly scalable and
     reliable infrastructure :cite:`goo2`. It gives developers a
     privilege of using any programming language. Google cloud
     platform provides a wide range of products and services including
     networking, storage, machine learning, big data, authentication
     and security, resource management, etc. In general, public clouds
     provide services to different end users with the usage of the
     same shared infrastructure :cite:`goo3`. Windows Azure services
     platform, Amazon elastic compute cloud and Sun cloud are few
     examples of public clouds.
     
359. Networking: Google Cloud DNS

     Under the umbrella of google cloud platform, helps user to
     publish their domain using Google’s infrastructure. It is highly
     scalable, low latency, high availability DNS service residing on
     infrastructure same as google.
   
     It is build around projects a resource container, domain for
     access control, and billing configuration. Managed zones holds
     records for same DNS name. The resource record sets collection
     holds current state of the DNS that make up managed zones it is
     unmodifiable or cannot be modified easily and changes to record
     sets. It supports "A" address records, "AAAA" IPv6, "CAA"
     Certificate authority, "CNAME" canonical name, "MX" mail
     exchange, "NAPTR" naming authority pointer, "NS" Name server
     record, "SOA" start of authority, "SPF" Sender policy framework,
     "SRV" service locator, "TXT" text record.

360. Amazon Route 53

     Amazon Route 53 is a DNS (Domain Name System) service that gives
     developers and businesses a reliable way to route end users to
     Internet applications. The number 53 refers to TCP or UDP port
     53, where DNS server requests are addressed :cite:`www-ar53`.
     
     When using Route 53 as your DNS provider, in case of a recursion,
     the query of fetching an IP address (of a website or application)
     always goes to the closest server location to reduce query
     latency. The Route 53 server returns the IP address enabling the
     browser to load the website or application. Route 53 can also be
     used for registering domain names and arranging DNS "health
     checks" to monitor the server :cite:`www-amar53`.

Cross-Cutting Functions
-----------------------

Monitoring
^^^^^^^^^^

361. Ambari

     Apache Amabari is an open source platform that enables easy
     management and maintenance of Hadoop clusters, regardless of
     cluster size. Ambari has a simplified Web UI and robust REST API
     for automating and controlling cluster operations.
     :cite:`www-hortonworks-ambari` illustrates Ambari to provide key
     benefits including easy installation, configuration, and
     management with features such as Smart Configs and cluster
     recommendations and Ambari Blueprints, to provide repeatable and
     automated cluster creation. Ambari provides a centralized
     security setup that automates security capabilities of
     clusters. Ambari provides a holistic view for cluster monitoring
     and provides visualizations for operation
     metrics. :cite:`www-ambari` provides documentation about Ambari,
     including a quick start guide for installing a cluster with
     Ambari. :cite:`www-github-ambari` provides the project documents
     for ambari on github.
     
362. Ganglia

     Ganglia is a scalable distributed monitoring system for
     high-performance computing systems (clusters and grids). It is a
     BSD-licensed open-source project that grew out of the University
     of California, Berkeley Millennium Project which was initially
     funded in large part by the National Partnership for Advanced
     Computational Infrastructure (NPACI) and National Science
     Foundation RI Award EIA-9802069 :cite:`www-gms`.

     It relies on a multicast-based listen/announce protocol to
     monitor state within clusters. It uses a tree of point-to-point
     connections amongst representative cluster nodes to unite
     clusters and aggregate their state :cite:`www-gsoft`. It
     leverages technologies such as XML for data representation, XDR
     for compact, portable data transport, and RRDtool for data
     storage and visualization. The implementation is robust, has been
     ported to an extensive set of operating systems and processor
     architectures, and is currently in use on thousands of clusters
     around the world, handling clusters with 2000 nodes.
     
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
^^^^^^^^^^^^^^^^^^
365. InCommon

     The mission of InCommon is to "create and support a common trust
     framework for U.S. education and research.  This includes
     trustworthy shared management of access to on-line resources in
     support of education and research in the United
     States". :cite:`www-incommon` This mission ultimately is a
     simplification and an elimination of the need for multiple
     accounts across various websites that are at risk of data spills
     or misuse.  In the academic setting, this helps assist
     researchers to focus on their area of study, and enabling the
     cross collaboration which is happening on a globa scale.
     Currently any two and four year higher education institution that
     is accredited is eligble for joining InCommon.

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

     :cite:`www-keystone-wiki` Keystone is the identity service used
     by OpenStack for authentication (authN) and high-level
     authorization (authZ).  There are two authentication mechanisms
     in Keystone, UUID token, and PKI.  Universally unique identifier
     (UUID) is a 128-bit number used to identify information
     (user). Each application after each request of the client checks
     token validity online. PKI was introduced later and improved the
     security of Keystone :cite:`cui2015security`. In PKI, each token
     has its own digital signature that can be checked by any service
     and OpenStack application with no necessity to ask for Keystone
     database :cite:`www-cloudberrylab-kstn`.
 
     Thus, Keystone enables ensuring user’s identity with no need to
     transmit its password to applications. It has recently been
     rearchitected to allow for expansion to support proxying external
     services and AuthN/AuthZ mechanisms such as oAuth, SAML and
     openID in future versions :cite:`www-keystone`.

368. LDAP

     LDAP stands for Lightweight Directory Access Protocol. It is a software
     protocol for enabling anyone to locate organizations, individuals, and
     other resources such as files and devices in a network, whether on the
     Internet or on corporate internet.
     :cite:`www-ldap`

     LDAP is a "lightweight" (smaller amount of code) version of
     Directory Access Protocol (DAP), which is part of X.500, a
     standard for directory services in a network.  In a network, a
     directory tells you where in the network something is located. On
     TCP/IP networks (including the Internet), the domain name system
     (DNS) is the directory system used to relate the domain name to a
     specific network address (a unique location on the
     network). However, you may not know the domain name. LDAP allows
     you to search for an individual without knowing where they're
     located (although additional information will help with the
     search).An LDAP directory can be distributed among many
     servers. Each server can have a replicated version of the total
     directory that is synchronized periodically.  An LDAP server is
     called a Directory System Agent (DSA). An LDAP server that
     receives a request from a user takes responsibility for the
     request, passing it to other DSAs as necessary, but ensuring a
     single coordinated response for the user.

369. Sentry

     :cite:`www-sentry` "Apache Sentry is a granular, role-based authorization 
     module for Hadoop. Sentry provides the ability to control and enforce 
     precise levels of privileges on data for authenticated users and 
     applications on a Hadoop cluster. Sentry currently works out of the box 
     with Apache Hive, Hive Metastore/HCatalog, Apache Solr, Impala and HDFS 
     (limited to Hive table data). Sentry is designed to be a pluggable 
     authorization engine for Hadoop components. It allows the client to define 
     authorization rules to validate a user or application’s access requests 
     for Hadoop resources. Sentry is highly modular and can support authorization 
     for a wide variety of data models in Hadoop."

370. Sqrrl
371. OpenID 

     OpenID is an authentication protocol that allows users to log in
     to different websites, which are not related, using the same
     login credentials for each, i.e. without having to create
     separate id and password for all the websites. The login
     credentials used are of the existing account. The password is
     known only to the identity provider and nobody else which
     relieves the users’ concern about identity being known to an
     insecure website. :cite:`ope1` It provides a mechanism that makes
     the users control the information that can be shared among
     multiple websites. OpenID is being adopted all over the web. Most
     of the leading organizations including Microsoft, Facebook,
     Google, etc. are accepting the OpenIDs :cite:`ope2`. It is an
     open source and not owned by anyone. Anyone can use OpenID or be
     an OpenID provider and there is no need for an individual to be
     approved.

372. SAML OAuth

     As explained in :cite:`www-SAML`, Security Assertion Markup
     Language (SAML) is a secured XML based communication mechanism
     for communicating identities between organizations. The primary
     use case of SAML is Internet SSO. It eliminates the need to
     maintain multiple authentication credentials in multiple
     locations. This enhances security by elimination opportunities
     for identity theft/Phishing. It increases application access by
     eliminating barriers to usage. It reduces administration time and
     cost by excluding the effort to maintain duplicate credentials
     and helpdesk calls to reset forgotten passwords. Three entities
     of SAML are the users, Identity Provider (IdP-Organization that
     maintains a directory of users and an authentication mechanism)
     and Service Provider(SP-Hosts the application /service). User
     tries to access the application by clicking on a link or through
     an URL on the internet. The Federated identity software running
     in the IdP validates the user's identity and the user is then
     authenticated. A specifically formatted message is then
     communicated to the federated identity software running at SP. SP
     creates a session for the user in the target application and
     allows the user to get direct access once it receives the
     authorization message from a known identity provider.

Distributed Coordination
^^^^^^^^^^^^^^^^^^^^^^^^

373. Google Chubby

     Chubby Distributed lock service :cite:`www-chubby`
     is intended for use within a loosely-coupled distributed system
     consisting of moderately large numbers of small machines
     connected by a high-speed network. Asynchronous consensus is
     solved by the Paxos protocol. The implementation in Chubby is
     based on coarse grained lock server and a library that the client
     applications link against.  As per the 2016 paper
     :cite:`chubby-paper-2016`, an open-source implementation of the
     Google Chubby lock service was provided by the Apache ZooKeeper
     project. ZooKeeper used a Paxos-variant protocol Zab for solving
     the distributed consensus problem.  Google stack and Facebook
     stack both use versions of zookeeper.
     
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
^^^^^^^^^^^^^^^^^^^^^^^^^^

377. Avro

     Apache Avro is a data serialization system, which provides rich
     data structures, remote procedure call(RPC), a container file to
     store persistent data and simple integration with dynamic
     languages :cite:`www-Avro`.  Avro depends on schemas, which are
     defined with JSON. This facilitates implementation in other
     languages that have the JSON libraries.  The key advantages of
     Avro are schema evolution - Avro will handle the
     missing/extra/modified fields, dynamic typing - serialization and
     deserialization without code generation, untagged data - data
     encoding and faster data processing by allowing data to be
     written without overhead.
     
378. Thrift

     The Apache Thrift software framework, for scalable cross-language
     services development, combines a software stack with a code generation
     engine to build services that work efficiently and seamlessly between
     C++, Java, Python, PHP, Ruby, Erlang, Perl, Haskell, C#, Cocoa,
     JavaScript, Node.js, Smalltalk, OCaml and Delphi and other
     languages. :cite:`paper-thrift` It includes a complete stack for
     creating clients and servers. It includes a server infrastructure to
     tie the protocols and transports together. There are blocking,
     non-blocking, single and multithreaded servers available.  Thrift was
     originally developed at Facebook, it was open sourced in April 2007
     and entered the Apache Incubator in May, 2008. It became an Apache TLP
     in October, 2010. :cite:`www-thrift`
     
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

.. _new-techs:

New Technologies (To Be Integrated by the AIs)
----------------------------------------------

381. Snort

     :cite:`www-snort` Snort is a Network Intrusion Prevention System
     (NIPS) and Network Intrusion Detection System (NIDS). Snort's
     open source network-based intrusion detection system (NIDS) has
     the ability to perform real-time traffic analysis and packet
     logging on Internet Protocol (IP) networks. Snort performs
     protocol analysis, content searching and matching. These basic
     services have many purposes including application-aware triggered
     quality of service, to de-prioritize bulk traffic when
     latency-sensitive applications are in use.  The program can also
     be used to detect probes or attacks, including, but not limited
     to, operating system fingerprinting attempts, common gateway
     interface, buffer overflows, server message block probes, and
     stealth port scans.  Snort can be configured in three main modes:
     sniffer, packet logger, and network intrusion detection. In
     sniffer mode, the program will read network packets and display
     them on the console. In packet logger mode, the program will log
     packets to the disk. In intrusion detection mode, the program
     will monitor network traffic and analyze it against a rule set
     defined by the user. The program will then perform a specific
     action based on what has been identified.

382. Fiddler

     Fiddler is an HTTP debugging proxy server application. Fiddler
     captures HTTP and HTTPS traffic and logs it for the user to
     review by implementing man-in-the-middle interception using
     self-signed certificates. Fiddler can also be used to modify
     ("fiddle with") HTTP traffic for troubleshooting purposes as it
     is being sent or received.[5] By default, traffic from
     Microsoft's WinINET HTTP(S) stack is automatically directed to
     the proxy at runtime, but any browser or Web application (and
     most mobile devices) can be configured to route its traffic
     through Fiddler :cite:`www-fiddler`.

383. Zeppelin

     Apache Zeppelin :cite:`www-zeppelinwebsite` provides an
     interactive environment for big data data analytics on
     applications using distributed data processing systems like
     Hadoop and Spark. It supports various tasks like data ingestion,
     data discovery, data visualization, data analytics and
     collaboration. Apache Zeppelin provides built-in Apache Spark
     integration and is compatible with many languages/data-processing
     backends like Python, R, SQL, Cassandra and JDBC. It also
     supports adding new language backend. Zeppelin also lets users to
     collaborate by sharing their Notebooks, Paragraph and has option
     to broadcast any changes in realtime.

384. Open MPI 

     The Open MPI Project :cite:`www-open-mpi` is an open
     source Message Passing Interface implementation that is developed
     and maintained by a consortium of academic, research, and
     industry partners. Open MPI is therefore able to combine the
     expertise, technologies, and resources from all across the High
     Performance Computing community in order to build the best MPI
     library available. Open MPI offers advantages for system and
     software vendors, application developers and computer science
     researchers. Open MPI :cite:`open-mpi-paper-2004` provides
     functionality that has not previously been available in any
     single, production-quality MPI implementation, including support
     for all of MPI-2, multiple concurrent user threads, and multiple
     options for handling process and network failures.

385. Apache Tomcat

     Apache tomcat is an open source java servlet
     container. :cite:`www-tomcat-official` It is used in IT industry
     as a HTTP web server which listens to the requests made by web
     client and send reponses. The main components of tomcat are
     cataline, coyote and jasper. The most stable version of Apache
     Tomcat server is version 8.5.11. Apache tomcat is released under
     Apache License version 2. :cite:`www-tomcat-wiki` As it is cross
     platform, it can run in any platform or OS like Windows, UNIX,
     AIX or SOLARIS etc. It is basically an integral part of many java
     based web application.

386. Apache Beam       

     Apache Beam attempts to abstract away the need to write
     code for multiple data-oriented workflows, e.g., batch, interactive and
     streaming, as well as multiple big data tools, e.g., Storm, Spark and 
     Flink.  Instead, Beam attempts to automagically map a dataflow process 
     written in Java or Python to the target runtime environment via *runners*.
     As a result, switching a data processing routine from Spark to Flink only 
     requires changing the target runtime environment as opposed to re-writing 
     the entire process :cite:`www-infoworld-apachebeam` (perhaps in a 
     completely different language).  Google contributed its Dataflow SDK, the 
     Dataflow model and three runners :cite:`www-datanami-apachebeam` to the 
     Apache Software Foundation in the first half of 2016.  The ASF elevated
     Beam to a Top-Level project in January 2017.  Jean-Baptiste Onofre of 
     French tech company Talend, and a frequent Apache project contributor, 
     champions the project. :cite:`www-talend-apachebeam`  It should be grouped
     with the technologies in the *Interoperability* section.

387. Cloudability

     Cloudability is a financial management tool for analyzing and
     monitoring all cloud expenses across an organization. It can be
     used for cost monitoring, usage rightsizing, reserved instance
     planning, cost allocation, role-based visibility. It aggregates
     expenditures into reports, helps identify opportunities for
     reducing costs, offers budget alerts and recommendations via SMS
     and email, and provides APIs for connecting cloud billing and
     usage data to any business or financial
     system. :cite:`www-cloudability`



388. CUDA

     It is a parallel computing platform and application programming
     interface(API) model created by Nvidia. It allows software developers
     to use a CUDA-enabled graphics processing unit for general purpose
     processing. The CUDA platform is a software layer that gives direct
     access to the GPU's virtual instruction set and parallel computational
     elements, for the execution of compute kernels.  CUDA platform has
     advantages such as scattered reads i.e the code can read from
     arbitrary addresses in memory, unified virtual memory, unified memory,
     faster downloads and readbacks to and from the GPU and full support
     for integer and bitwise operations. :cite:`www-cuda-wikipedia`.  CUDA
     is used for accelerated rendering of 3D graphics, accelerated
     interconversion of video file formats, encryption, decryption and
     compression of files.  It is also usedd for distributed calculations,
     face recognition and distributed computing. :cite:`www-cuda-wikipedia`
	  

389. Blaze  

     Blaze library translates NumPy/Pandas-like syntax to data
     computing systems (e.g. database , in-memory,
     distributed-computing). This provides Python users with a
     familiar interface to query data in a variety of other data
     storage systems.  One Blaze query can work across data ranging
     from a CSV file to a distributed database.

     Blaze presents a pleasant and familiar interface regardless of
     what computational solution or database we use (e.g. Spark,
     Impala, SQL databases, No-SQL data-stores, raw-files). It
     mediates the users interaction with files, data structures, and
     databases, optimizing and translating the query as appropriate to
     provide a smooth and interactive session. It allows the data
     scientists and analyst to write their queries in a unified way
     that does not have to change because the data is stored in
     another format or a different data-store. :cite:`www-blaze`

389. CDAP

     CDAP :cite:`www-cdap` stands for Cask Data Application
     Platform. CDAP is an application development platform using which
     developers can build, deploy and monitor applications on Apache
     Hadoop. In a typical CDAP application, a developer can ingest
     data, store and manage datasets on Hadoop, perform batch mode
     data analysis, and develop web services to expose the data.  They
     can also schedule and monitor the execution of the
     application. This way, CDAP enables the developers to use single
     platform to develop the end to end application on Apache Hadoop.

     CDAP documentation :cite:`www-cdap-docs` explains the important
     CDAP concepts of CDAP Dataset, CDAP Application and CDAP
     Services. CDAP Datasets provide logical abstraction over the data
     stored in Hadoop. CDAP Applications provide containers to
     implement application business logic in open source processing
     frameworks like map reduce, Spark and real time flow. CDAP
     applications also provide standardize way to deploy and manage
     the apps. CDAP Services provide services for application
     management, metadata management, and streams management.  CDAP
     can be deployed on various Hadoop Platforms such as Apache
     Hadoop, Cloudera Hadoop, Hortonworks Hadoop and Amazon EMR.  CDAP
     sample apps :cite:`github-cdap-sample-apps` provide explain how
     to implement apps on CDAP platform.

389. Apache Arrow
     
     Apache arrow allows execution engines to utilize what is known as
     Single Input multiple data (SIMD).  :cite:`www-arrow` This SIMD
     is an operation that allows modern processors to take advantage
     of this engine.  Peformance is enhanced by grouping relevant data
     as close as possible in a column format.  Many programming
     languages are supported such a Java, C, C++, Python and it is
     anticipated that languages will be added as it grows.  It is
     still in early developemnt but has released a 0.1.0 build.

390. OpenRefine

     OpenRefine (formerly GoogleRefine) is an open source tool that is
     dedicated to cleaning messy data. With the help of this
     user-friendly tool you can explore huge data sets easily and
     quickly even if the data is a little unstructured. It allows you
     to load data, understand it, clean it up, reconcile it, and
     augment it with data coming from the web
     :cite:`www-openrefine`.It operates on rows of data which have
     cells under columns, which is very similar to relational database
     tables. One OpenRefine project is one table. The user can filter
     the rows to display using facets that define filtering
     criteria. most operations in OpenRefine are done on all visible
     rows: transformation of all cells in all rows under one column,
     creation of a new column based on existing column data, etc. All
     actions that were done on a dataset are stored in a project and
     can be replayed on another dataset. It has a huge community with
     lots of contributors meaning that the software is constantly
     getting better and better.

391. Apache OODT

     Apache Object Oriented Data Technology (OODT) :cite:`www-oodt` is
     a distributed data management technology that helps to integrate
     and archive your processes, your data, and its metadata. OODT
     allows to generate, process, manage and analyze distributed and
     heterogeneous data enabling integration of different, distributed
     software systems. Apache OODT uses structured XML-based capturing
     of the processing pipeline which is used to create, edit, manage
     and provision workflow and task execution. OODT is written in
     Java programming language and provides its own set of APIs for
     storing and processing data. :cite:`www-oodt-documentation` It
     provides three core services. A File Manager is responsible for
     tracking file locations, their metadata, and for transferring
     files from a staging area to controlled access storage. A
     Workflow Manager captures control flow and data flow for complex
     processes, and allows for reproducibility and the construction of
     scientific pipelines. A Resource Manager handles allocation of
     workflow tasks and other jobs to underlying resources, e.g.,
     Python jobs go to nodes with Python installed on them similarly
     jobs that require a large disk or CPU are properly sent to those
     nodes that fulfill those requirements. OODT is now supported with
     Apache Mesos and Grid Computing which can allow for creating of
     highly distributed, scalable data platforms that can process
     large amounts of data. OODT technology is used in NASA's Jet
     Propulsion Labatory.

389. Omid

     Omid is a "flexible, reliable, high performant and scalable ACID 
     transactional framework" :cite:`www-apacheomid` for NoSQL databases, 
     developed by Yahoo for HBase and contributed to the Apache 
     community  Most NoSQL databases, do not natively support ACID 
     transactions. Omid employs a lock free approach from concurrency 
     and can scale beyond 100,000 transactions per second. At Yahoo,
     millions of transactions per day are processed by Omid.
     :cite:`www-yahooomid`. 

     Omid is currently in the Apache Incubator.  All projects accepted 
     by the Apache Software Foundation (ASF) undergo an incubation 
     period until a review indicates that the project meets the 
     standards of other ASF projects :cite:`www-apacheincubator`

390. Askalon was developed at the University of Innsbruck :cite:`RMBDP-Book`.  
     It is application development as well as a runtime
     environment. It allows easy execution of distributed work flow
     applications in service oriented grids. It uses a Service
     Oriented Architecture. Also, for its Grid middleware it uses the
     Globus Toolkit. The work flow applications are developed using
     Abstract Grid Work flow Language (AGWL). The architecture has
     various components like the resource broker responsible for
     brokerage functions like management and reservation, information
     service for the discovery and organization of resources and data,
     metascheduler for mapping in the Grid, performance analysis for
     unification of performance monitoring and integration of the
     results and the Askalon scheduler.

     The Metascheduler is of special significance since it consists of
     two major components - the workflow converter and the scheduling
     engine. The former is responsible for conversion of traditional
     workflows into directed acyclic graphs (DAGs) while the later one is
     responsible for the scheduling of workflows for various specific
     tasks. It has a conventional pluggable architecture which allows easy
     integration of various services. By default, the Heterogeneous
     Earliest Finish Time (HEFT) is used as the primary scheduling
     algorithm.

391. Apache Ant

     Apache Ant is a Java library and command-line tool whose mission
     is to drive processes described in build files as targets and
     extension points dependent upon each other. The main known usage
     of Ant is the build of Java applications. Ant supplies a number
     of built-in tasks allowing to compile, assemble, test and run
     Java applications. Ant can also be used effectively to build non
     Java applications, for instance C or C++ applications. More
     generally, Ant can be used to pilot any type of process which can
     be described in terms of targets and tasks. Ant is written in
     Java. Users of Ant can develop their own "antlibs" containing Ant
     tasks and types, and are offered a large number of ready-made
     commercial or open-source "antlibs". Ant is extremely flexible
     and does not impose coding conventions or directory layouts to
     the Java projects which adopt it as a build tool. Software
     development projects looking for a solution combining build tool
     and dependency management can use Ant in combination with Apache
     Ivy. The Apache Ant project is part of the Apache Software
     Foundation :cite:`ant-www`.

392. LXD

     LXD is a  demon processes established to manage the
     containers. It can be understood as hypervisor for linux
     containers. It is implemented by exporting RESTful API for libxlc
     to the remote network or local unix
     socket. :cite:`www-lxd-thevarguy`. It implements the under
     previlized conatiners by default adding more security. It works
     with Image based work flow supports online snapshopping and live
     container migration. :cite:`www-lxd-lists-linux`.It was build
     with aim of providing VM like virtulization with container like
     performance. :cite:`www-lxd-ubuntu`

393. Wink

     Apache wink :cite:`www-apache-wink` provides a framework to
     develop and use RESTful web services. It implements using JAX-RS
     v1.1 specification. The project provides server module which
     integrates with all popular web servers and a client module which
     can used to write RESTful web services. This project will be
     integrated with Geronimo and other opensource REST projects to
     build a vendor neutral community. Currently IBM and HP have taken
     lead. IBM is writing a full JAX-RS implementation while HP is
     working on RESTful SDK for client and server components.  Portion
     of initial project was also taken from Apache CXF which uses
     other Apache components like commons-codec, commons-logging,
     Apache-Abdera. Apache wink will simply web services development
     using one single standard.

394. Apache Apex
     
     Apache Apex is "a YARN(Hadoop 2.0)-native platform that unifies
     cloud and batch processing" :cite:`www-apacheapexwiki`.This
     project was developed under Apache License 2.0 and was driven by
     Data Torrent. It can be used for processing both streams of data
     and static files making it more relevant in the context of
     present day internet and social media. It is aimed at leveraging
     the present Hadoop platform and reducing the learning curve for
     development of applications over it. It is aimed at It can used
     through a simple API. It enables reuse of code by not having to
     make drastic changes to the applications by providing
     interoperability with existing technology stack. It leverages the
     existing Hadoop platform investments.

     Apart from the Apex core component, it also has Apex Malhar which
     provides a library of connectors and logic functions. It provides
     connectors to existing file systems, message systems and relational,
     NoSQL and Hadoop databases, social media. It also provides a library
     of compute operators like Machine Learning, Stats and Math, Pattern
     Marching, Query and Scripting, Stream manipulators, Parsers and UI &
     Charting operators :cite:`www-apacheapexblog`.

     Apache Knox

     According to :cite:'knox', "the Apache Knox Gateway is a REST API
     Gateway for interacting with Apache Hadoop clusters." REST stands
     for Representational State Transfer and is web architectural
     style designed for distributed hypermedia systems and defines a
     set of constraints. :cite:'fielding' API Gateways manage concerns
     related to "Authentication, Transport Security, Load-balancing,
     Request Dispatching (including fault tolerance and service
     discovery), Depenency Resolution, Transport Transformations."
     :cite:'peyrott' Although every Apache Hadoop cluster has its own
     set of REST APIs, Knox will represent all of them as "a single
     cluster specific application context path." :cite:'knox' Knox
     protects Apache Hadoop clusters, by way of its gateway function,
     by aiding "the control, integration, monitoring and automation of
     critical administrative and analytical needs." :cite:'knox' Some
     Apache Hadoop Services that integrate with Knox are, "Ambari,
     WebHDFS (HDFS), Templeton (Hcatalog), Stargate (Hbase), Oozie,
     Hive/JDBC, Yarn RM, [and] Storm."  :cite:'knox' Apache Knox has a
     configuration driven method to aid in the addition of new routing
     services. :cite:'knox' This allows support for new and custom
     Apache Hadoop REST APIs to be added to the Knox gateway quickly
     and easily. :cite:'knox' This technology would be best placed
     under the interoperability category.

     Apache Apex

     The Apex platform is designed to process real-time events with
     streaming data natively in Hadoop. The platform handles
     application execution, dynamic scaling, state checkpointing and
     recovery, etc. This allows the users to focus on writing their
     application logic without mixing operational and functional
     concerns :cite:`apache-apex`. In the platform, building a
     streaming application is easy and intuitive.

     An application may consist of one or more operators each of which
     define some logical operation to be done on the tuples arriving
     at the operator. These operators are connected together to form
     streams. A streaming application is represented by a DAG that
     consists of operators and streams :cite:`apex-operators`. The
     Apex platform comes with support for web services and
     metrics. This enables ease of use and easy integration with
     current data pipeline components. DevOps teams can monitor data
     in action using existing systems and dashboards with minimal
     changes, thereby easily integrating with the current setup. With
     different connectors and the ease of adding more connectors, Apex
     easily integrates with an existing dataflow :cite:`apex-ease`.

395. Robot Operating System (ROS)

     The aptly-named *Robot Operating System*, or ROS, provides a
     framework for writing operating systems for robots.  ROS offers "a 
     collection of tools, libraries, and conventions [meant to] simplify the 
     task of creating complex and robust robot behavior across a wide variety 
     of robotic platforms" :cite:`www-ros-about`. ROS' designers, the Open 
     Source Robotics Foundation, hereinafter OSRF or the Foundation, attempt 
     to meet the aforementioned objective by implementing ROS as a modular 
     system.  That is, ROS offers a core set of features, such as 
     inter-process communication, that work with or without pre-existing, 
     self-contained components for other tasks.

     The OSRF designed ROS as a distributed, modular system.  The OSRF 
     maintains a subset of essential features for ROS, i.e., *ROS 
     core*, to provide an extensible platform for other roboticists.  The 
     Foundation also coordinates the maintenance and distribution of a vast 
     array of ROS add-ons, referred to as modules.  ROS' core consists of the 
     following components: a) communications infrastructure; b) robot-specific 
     features; and, c) tools.  The modules, analagous to packages in Linux 
     repositories or libraries in other software packages such as *R*, 
     provide solutions for numerous robot-related problems.  General 
     categories include a) drivers, such as sensor and actuator interfaces; b) 
     platforms, for steering and image processing, etc.; c) algorithms, for 
     task planning and obstacle avoidance; and, d) user interfaces, such as 
     tele-operation and sensor data display.:cite:`www-software-categories`


396. Apache Flex

     Apache Flex :cite:`www-flex` is an open source aplication
     framework for building and maintaining mobile and web
     applications that deploy consistently on multiple browsers,
     desktops and mobile devices. It was initially developed by
     Macromedia and then acquired by Adobe Systems. It was later
     donated to the Apache Software Foundation in 2011
     :cite:`blog-flex`. It can pull data from multiple back-end
     sources such as Java, Spring, PHP, Ruby, .NET, Adobe ColdFusion,
     and SAP and display it visually allowing users to drill down into
     the data for deeper insight and even change the data and have it
     automatically updated on the back end :cite:`wiki-flex`.

397. Apache Ranger
     Apache Ranger :cite:`www-apache-ranger` is open source software project
     designed to provide centralized security services to various components
     of Apache Hadoop. Apache Hadoop provides various mechanism to store,
     process and access the data. Each Apache tool has its own security
     mechanism. This increases administrative overhead and is also error
     prone.  Apache Ranger fills this gap to provide a central security and
     auditing mechanism for various Hadoop components
     :cite:`www-ranger-architecture`. Using Ranger, Hadoop administrators can
     perform security administration tasks using a central UI or Restful web
     services. He can define policies which enable users/user-groups to
     perform specific action using Hadoop components and tools. Ranger
     provides role based access control for datasets on Hadoop at column and
     row level.  The blog article :cite:`www-ranger-key-features` explains
     that the row level filtering and dynamic data masking are most important
     features of Apache Ranger. Ranger also provides centralized auditing of
     user acces and security related administrative actions.
     
398. Google Cloud Machine Learning
     
     Google Could Machine Leaning is a Googles cloud based managed
     system for building machine learning model, capable to work on any
     type and volume of data. User can create their own machine learning
     model using GoogleTensorFlow framework, which helps to use the
     range of Google products from Google Photos to Google Cloud Speech.
     We can build our machine learning model regardless the size, google
     will managed it infrastructure according to  requirement. User can
     immediately host the created model and start predicting on new data
     :cite:`www-googlecloudmachinelearning`.Cloud Machine Learning provides
     two important things:
     
     - Help user to train the machine learning model at large scale
       with the help of TensorFlow  training application.
	
     - User can host the trained model on cloud,  this will help
       to use the large and new data available on cloud, which help in
       creating good model.

     Google CloudML will help user to focus on model instead of hardware
     configuration and resource management :cite:`www-googlecloudoverview`.

399. Karajan

     Karajan is used to allow users to describe various workflows
     using XML :cite:`RMBDP-Book-1`.  It also uses a custom yet user
     friendly language called K.  The advantages of using XML and K is
     that we can use Directed Acyclic Graphs (DAGs) to describe
     hierarchical workflows.  Besides, it is also very easy to handle
     concurrency using trivial programming constructs like if/while
     orders.  It can also use tools such as Globus GRAM for parallel
     or distributed execution of various workflows.  From an
     architectural perspective, Karajan mainly consists of three
     components: Workflow engine, that monitors the execution and is
     responsible for the higher level interaction with higher level
     components like the Graphical User Interface Module (GUI) for the
     description of various workflows; Workflow service, that is used
     to allow the execution of various workflows using specific
     functionalities that can be accessed by the workflow engine using
     specific libraries; and the Checkpointing subsystem that monitors
     and checks the current state of the workflow.  Karajan is
     typically used as a scientific workflow scheduling technique for
     various Big Data platforms.

     The Karajan code, that can be obtained from Java CoG Kit CVS
     archive has two interfaces: the command line interface (CLI) and
     the GUI.  The CLI can be accessed via bin/karajan and provides a
     minimalist interface that is non-interactive and doesn't provide
     much feedback on the execution status.  As against this, the GUI
     can be accessed via bin/karajan-gui and provides an enriched
     interface that provides visual features to determine the
     execution status besides being interactive in real time
     :cite:`Karajan-interfaces`.

.. _techs-exercise:

Excercise
---------

TechList.1: In class you will be given an HID and you will be assigned
  a number of technologies that you need to research and create a
  summary as well as one or more relevant references to be added to the
  Web page. All technologies for TechList.1 are marked with a (1)
  behind the technology.  An example text is given for Nagios in this
  page.  Please create a pull request with your responses. You are
  responsible for making sure the request shows up and each commit is
  using gitchangelog in the commit message::

    new:usr: added paragraph about <PUTTECHHERE>

  You can create one or more pull requests for the technology and the
  references. We have created in the referens file a placeholder using
  your HID to simplify the management of the references while avoiding
  conflicts.  For the technologies you are responsible to invesitgate
  them and write an academic summary of the technology. Make sure to
  add your reference to refs.bib.  Many technologies may have
  additional references than the Web page. Please add the most
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
  Learn about plagiarism and how to avoid it.
  Many Web pages will conduct self advertisement while adding
  suspicious and subjective adjectives or phrases such as cheaper,
  superior, best, most important, with no equal, and others that you
  may not want to copy into your descriptions. Please focus on facts,
  not on what the author of the Web page claims.

TechList 1.d:
  Identify technologies from the `Apache Project
  <https://projects.apache.org/>`_ or other Big Data related Web pages
  and projects that are not yet listed here. Add them at the end of
  the Technologies page under the :ref:`New Technologies <new-techs>`
  section, together with a description and appropriate references just
  like you did for your list of technologies in TechList 1a-1c. As
  part of your paragraph, please suggest a section where you think is
  best to add the technologies. Once the new technologies have been
  submitted, the AIs will integrate them in the appropriate
  sections. Please, only add new techs to the last section, otherwise
  it will be easy to introduce conflicts in the file.

TechList.2:
  In this hopweork we provide you with additional technologies that
  you need to complete. They are marked with (2) in the :doc:`HID
  Assignment page <hids-techs>`.

TechList.3:   
  Identify technologies that are not listed here and add   them.
  Provide a description and a reference just as you did before. Before you
  add a technology, verify that it is not on the **new technologies** list
  already.  Duplicated entries will be merged.

Open Discussion:
  For useful information on how to correctly create BibTeX entries,
  see and contribute to :ref:`these open discussion threads Piazza
  <bibtex-discussions>`.

References
----------

.. bibliography:: technologies-tmp.bib
   :style: unsrt
   :cited:
   :labelprefix: tech4
