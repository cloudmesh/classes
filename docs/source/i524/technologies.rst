
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

   Apache ODE (Orchestration Director Engine) is an open source 
   implementation of the WS-BPEL 2.0 standard. WS- BPEL which stands for 
   Web Services Business Process Execution Language, is an executable 
   language for writing business processes with web services :cite:`www-bpel-wiki`. 
   It includes control structures like conditions or loops as well as 
   elements to invoke web services and receive messages from services. 
   ODE uses WSDL (Web Services Description Language) for interfacing 
   with web services :cite:`www-ode-wiki`. Naming a few of its features, 
   It supports two communication layers for interacting with the outside 
   world, one based on Axis2 (Web Services http transport) and another 
   one based on the JBI standard. It also supports both long and short 
   living process executions for orchestrating services for applications :cite:`www-ode-web`.

2. ActiveBPEL
3. Airavata
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
   interface.  In the :cite:`taverna-paper` paper, the formal syntax and 
   operational semantics of Taverna is explained.

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
    
    BioKepler is a Kepler module of scientific workflow components to
    execute a set of bioinformatics tools using distributed execution
    patterns :cite:`WWW-bioKepler`. It contains a specialized set of
    actors called “bioActors” for running bioinformatic tools,
    directors providing distributed data-parallel(DPP) execution on
    Big Data platforms such as Hadoop and Spark they are also
    configurable and reusable :cite:`WWW-bioKepler-Demos`. BioKepler
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
14. (Dryad)
15. Naiad
16. Oozie

    Oozie is a workflow manager and scheduler. Oozie is designed to scale in a 
    Hadoop cluster. Each job will be launched from a different datanode
    :cite:`paper-Oozie` :cite:`www-Oozie1` . 
    Oozie :cite:`www-Oozie2` is architected from the ground up for large-scale 
    Hadoop workflow. Scales to meet the demand, provides a multi-tenant service, 
    is secure to protect data and processing, and can be operated cost effective
    ly. As demand for workflow and the sophistication of applications increase, 
    it must continue to mature in these areas :cite:`paper-Oozie`.Is well integr
    ated with Hadoop security. Is the only workflow manager with built-in Hadoo
    p actions, making workflow development, maintenance and troubleshooting easi
    er. It’s UI makes it easier to drill down to specific errors in the data
    nodes. Proven to scale in some of the world’s largest clusters 
    :cite:`paper-Oozie`. Gets callbacks from MapReduce jobs so it knows when 
    they finish and whether they hang without expensive polling. Oozie Coordinat
    or allows triggering actions when files arrive at HDFS. Also supported by
    Hadoop vendors :cite:`paper-Oozie`.
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

    In :cite:`e-science-central-paper-2010`, it is explained 
    that e-Science Central is designed to address some of the 
    pitfalls within current Infrastructure as a Service (e.g. 
    Amazon EC2) and Platform as a Service (e.g. force.com) 
    services. For instance, in 
    :cite:`e-science-central-paper-2010`, the "majority of 
    potential scientific users, access to raw hardware is of 
    little use as they lack the skills and resources needed to 
    design, develop and maintain the robust, scalable 
    applications they require" and furthermore "current 
    platforms focus on services required for business 
    applications, rather than those needed for scientific 
    data storage and analysis." In 
    :cite:`www-e-science-central`, it is explained that 
    e-Science Central is a "cloud based platform for 
    data analysis" which is "portable and can be run on 
    Amazon AWS, Windows Azure or your own hardware." In 
    :cite:`e-science-central-paper-2010`, e-Science Central 
    is further described  as a platform, which "provides 
    both Software and Platform as a Service for scientific 
    data management, analysis and collaboration." This 
    collaborative platform is designed to be scalable while 
    also maintaining ease of use for scientists. In 
    :cite:`e-science-central-paper-2010`, "a project 
    consisting of chemical modeling by cancer researchers" 
    demonstrates how e-Science Central "allows scientists to 
    upload data, edit and run workflows, and share results in 
    the cloud." 

23. Azure Data Factory
    
    Azure data factory is a cloud based data integration service that
    can ingest data from various sources, transform/ process data and
    publish the result data to the data stores. A data management
    gateway enables access to data on SQL Databases
    :cite:`Azure_df`. The data processing is done by It works by
    creating pipelines to transform the raw data into a format that
    can be readily used by BI Tools or applications. The services
    comes with rich visualization aids that aid data analysis. Data
    Factory supports two types of activities: data movement activities
    and data transformation activities. Data Movement :cite:`Azure_ms`
    is a Copy Activity in Data Factory that copies data from a data
    source to a Data sink. Data Factory supports the following data
    stores. Data from any source can be written to any sink.  Data
    Transformation: Azure Data Factory supports the following
    transformation activities such as Map reduce, Hive transformations
    and Machine learning activities.  Data factory is a great tool to
    analyze web data, sensor data and geo-spatial data.

24. Google Cloud Dataflow
    
    Google Cloud Dataflow is a unified programming model and a managed
    service for developing and executing a wide variety of data processing
    patterns (pipelines). Dataflow includes SDKs for defining data
    processing workflows and a Cloud platform managed services to run
    those workflows on a Google cloud platform resources such as Compute
    Engine, BigQuery amongst others :cite:`WWW-Dataflow`. Dataflow
    pipelines can operate in both batch and streaming mode. The platform
    resources are provided on demand, allowing users to scale to meet
    their requirements, it’s also optimized to help balance lagging work
    dynamically.

    Being a cloud offering, Dataflow is designed to allow users to focus
    on devising proper analysis without worrying about the installation
    and maintaining :cite:`WWW-GoogleLiveStream` the underlying data
    piping and process infrastructure.
    
25. NiFi (NSA)

    :cite:`www-nifi` Defines NiFi as "An Easy to use, powerful and
    realiable system to process and distribute data".
    This tool aims
    at automated data flow from sources with different sizes ,
    formats and following diffent protocals to the centralized
    location or destination. :cite:`www-hortanworks`.
    
    This comes equipped with an easy use UI where the data flow
    can be conrolled with a drag and a drop.
    NiFi was initiatially developed by NSA ( called Niagarafiles )
    using the concepts of flowbased
    programming and latter submitted to Apachi Software
    foundation. :cite:`www-forbes`
    
26. Jitterbit
27. Talend
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

    :cite:`www-R` R, a GNU project, is a successor to S - a
    statistical programming language. It offers a range of
    capabilities – “programming language, high level graphics,
    interfaces to other languages and debugging”. "R is an integrated
    suite of software facilities for data manipulation, calculation
    and graphical display". The statistical and graphical techniques
    provided by R make it popular in the statistical community. The
    statistical techniques provided include linear and nonlinear
    modelling, classical statistical tests, time-series analysis,
    classification and clustering to name a few. :cite:`book-R` The
    number of packages available in R has made it popular for use in
    machine learning, visualization, and data operations tasks like
    data extraction, cleaning, loading, transformation, analysis,
    modeling and visualization. It's strength lies in analyzing data
    using its rich library but falls short when working with very
    large datasets.
    
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
42. PetSc
43. PLASMA MAGMA

    PLASMA is built to address the performance shortcomings of the LAPACK and
    ScaLAPACK libraries on multicore processors and multi-socket systems of
    multicore processors and their inability to efficiently utilize accelerators
    such as Graphics Processing Units (GPUs). Real arithmetic and complex
    arithmetic are supported in both single precision and double precision.
    PLASMA has been designed by restructuring the software to achieve much
    greater efficiency, where possible, on modern computers based on multicore
    processors. PLASMA does not support band matrices and does not solve
    eigenvalue and singular value problems. Also, PLASMA does not replace
    ScaLAPACK as software for distributed memory computers, since it only
    supports shared-memory machines. :cite:`paper-plasma-magma-1` :cite:`www-plasma-1`
    Recent activities of major chip manufacturers, such as Intel, AMD, IBM and
    NVIDIA, make it more evident than ever that future designs of
    microprocessors and large HPC systems will be hybrid/heterogeneous in
    nature, relying on the integration (in varying proportions) of two major
    types of components: :cite:`paper-plasma-magma-2` :cite:`paper-plasma-magma-3`
    1. Many-cores CPU technology, where the number of cores will continue to
    escalate because of the desire to pack more and more components on a chip
    while avoiding the power wall, instruction level parallelism wall, and the
    memory wall;
    2. Special purpose hardware and accelerators, especially Graphics Processing
    Units (GPUs), which are in commodity production, have outpaced standard CPUs
    in floating point performance in recent years, and have become as easy, if
    not easier to program than multicore CPUs.
    While the relative balance between these component types in future designs
    is not clear, and will likely to vary over time, there seems to be no doubt
    that future generations of computer systems, ranging from laptops to
    supercomputers, will consist of a composition of heterogeneous components.
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
    conversations :cite:`WWW-Translation`.
46. mlpy
    
    mlpy is an open source python library made for providing
    machine learning functionality.It is built on top of popular
    existing python libraries of NumPy, SciPy and GNU scientific
    libraries (GSL).It also makes extensive use of Cython
    language. These form the prerequisites for mlpy. :cite:`DBLP:journals/corr/abs-1202-6548`
    explains the significanceq of its components: NumPy, SciPy provide
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

48. PyBrain
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
51. Caffe

    Caffe is a deep learning framework made with three terms namely
    expression, speed and modularity :cite:`www-caffe`. Using Expressive
    architecture, switching between CPU and GPU by setting a single
    flag to train on a GPU machine then deploy to commodity cluster or
    mobile devices.Here the concept of configuration file will comes
    without hard coding the values . Switching between CPU and GPU can
    be done by setting a flag to train on a GPU machine then deploy to
    commodity clusters or mobile devices.

    It can process over 60 million images per day with a single NVIIA
    k40 GPU It is being used bu academic research projects, startup
    prototypes, and even large-scale industrial applications in vision,
    speech, and multimedia.
    
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
    development of machine learning(ML) algorithms. 
    Theano uses recent GPUs for higher speed.
    It is used to evaluate mathematical expressions and especially
    those mathematical expressions that include multi-dimensional arrays.
    Theano’s working is dependent on combining aspects of a computer algebra
    system and an optimizing compiler.
    This combination of computer algebra system with optimized compilation
    is highly beneficial for the tasks which involves complicated 
    mathematical expressions and that need to be evaluated repeatedly as
    evaluation speed is highly critical in such cases. 
    It can also be used to generate customized C code for number of
    mathematical operations. 
    For cases where many different expressions are there and each of them 
    is evaluated just once, Theano can minimize the amount of compilation
    and analyses overhead :cite:`www-theano`.
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
56. IBM Watson

    IBM Watson :cite:`www-ibmwatson-wiki` is a super computer built on
    cognitive technology that processes information like the way human
    brain does by understanding the data in a natural language as well
    as analyzing structured and unstructured data. It was initially
    developed as a question and answer tool more specifically to
    answer questions on the quiz show "Jeopardy" but now it has been
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
58. GraphLab

    GraphLab :cite:`www-graphlab` is a graph-based, distributed computation,
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

    GraphX is Apache Spark's API for graph and graph-parallel computation.
    :cite:`www-graphX`
	  
    GraphX provides:
    
    Flexibility: It seamlessly works with both graphs and collections. GraphX
    unifies ETL, exploratory analysis, and iterative graph computation within a
    single system. You can view the same data as both graphs and collections,
    transform and join graphs with RDDs efficiently, and write custom iterative
    graph algorithms using the Pregel API.
    
    Speed: Its performance is comparable to the fastest specialized graph
    processing systems while retaining Apache Spark's flexibility, fault
    tolerance, and ease of use.
    
    Algorithms: GraphX comes with a variety of algorithms such as PageRank,
    Connected Components, Label propagations, SVD++, Strongly connected
    components and Triangle Count.

    It combines the advantages of both data-parallel and graph-parallel systems
    by efficiently expressing graph computataion within the Spark data-parallel
    framework. :cite:`www-graphX1`

    It gets developed as a part of Apache Spark project. It thus gets tested and
    updated with each Spark release.
    
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
    "Kibana" are also developed alongside Elasticsearch forming a
    single package.
    
69. Kibana
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
72. Splunk
73. Tableau

    :cite:`www-tableau-tutorial` Tableau is a family of interactive data visualization products 
    focused on business intelligence. The different products which 
    tableau has built are: Tableau Desktop, for individual use; 
    Tableau Server for collaboration in an organization; Tableau 
    Online, for Business Intelligence in the Cloud; Tableau Reader, 
    for reading files saved in Tableau Desktop; Tableau Public, for 
    journalists or anyone to publish interactive data online.
    :cite:`www-tableau-web` Tableau uses VizQL as a  visual query language for translating 
    drag-and-drop actions into data queries and later expressing the 
    data visually. Tableau also benefits from an Advanced In-Memory 
    Technology for handling large amounts of data. 
    The strengths of Tableau are mainly the ease of use and speed. 
    However, it has a number of limitations, which the most prominent 
    are unfitness for broad business and technical user, being 
    closed-source, no predictive analytical capabilities and no support 
    for expanded analytics.

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

    The Microsoft Cognitive Toolkit - CNTK - is a unified deep-learning toolkit 
    by Microsoft Research. It is in essence an implementation of Computational 
    Network(CN) which supports both CPU and GPU. CNTK supports arbitrary valid 
    computational networks and makes building DNNs, CNNs, RNNs, LSTMS, and other 
    complicated networks as simple as describing the operations of the networks. 
    The toolkit is implemented with efficiency in mind. It removes duplicate 
    computations in both forward and backward passes, uses minimal memory needed 
    and reduces memory reallocation by reusing them. It also speeds up the model 
    training and evaluation by doing batch computation whenever possible 
    :cite:`book-cntk` . It can be included as a library in your Python or C++ pro
    grams, or used as a standalone machine learning tool through its own model  
    description language (BrainScript). :cite:`www-cntk`
    Latest Version:2017-02-10. V 2.0 Beta 11 Release


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

    :cite:`www-paas` OpenShift was launched as a PaaS (Platform as a
    Service) by Red Hat in the Red Hat Summit, 2011.
    :cite:`www-developers-openshift` It is a cloud application
    development and hosting platform that envisages shifting of the
    developer's focus to development by automating the management and
    scaling of applications.  Thus, :cite:`www-openshift` OpenShift
    enables us to write our applications in any one web development
    language (using any framework) and it itself takes up the task of
    running the application on the web.  This has its advantages and
    disadvantages - advantage being the developer doesn't have to
    worry about how the stuff works internally (as it is abstracted
    away) and the disadvantage being that he cannot control how it
    works, again because it is abstracted.

    :cite:`openshift-blog` OpenShift is powered by Origin, which is in
    turn built using Docker container packaging and Kubernetes container
    cluster.  Due to this, OpenShift offers a lot of options, including
    online, on-premise and open source project options.
    
83. Heroku

    Heroku :cite:`www-Heroku` is a platform as a service that is used 
    for building, delivering monitoring and scaling applications. It 
    lets you  develop and deploy application quickly without thinking
    about irrelevant problems such as infrastructure. Heroku also 
    provides a secure and scalable database as a service with number of 
    developers’ tools like database followers, forking, data clips and
    automated health checks. It works by deploying to cedar stack 
    :cite:`www-cedar`, an online runtime environment that supports apps 
    buit in Java, Node.js, Scala, Clojure, Python and PHP. It uses Git 
    for version controlling. It is also tightly intergrated with 
    Salesforce, providing seamless and smooth Heroku and Salesforce 
    data synchronization enabling companies to develop and design creative 
    apps that uses both platforms.

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

    Jelastic (acronym for Java Elastic) is an unlimited PaaS and Container based
    IaaS within a single platform that provides high availability of
    applications, automatic vertical and horizontal scaling via containerization
    to software development clients, enterprise businesses, DevOps, System
    Admins, Developers, OEMs and web hosting providers. :cite:`www-jelastic-2` 
    Jelastic is a Platform-as-Infrastructure provider of Java and PHP hosting. 
    It has international hosting partners and data centers. The company can add 
    memory, CPU and disk space to meet customer needs. The main competitors of 
    Jelastic are Google App Engine, Amazon Elastic Beanstalk, Heroku, and Cloud 
    Foundry.Jelastic is unique in that it does not have limitations or code 
    change requirements, and it offers automated vertical scaling, application
    lifecycle management, and availability from multiple hosting providers
    around the world. :cite:`www-jelastic-1`

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

    dotCloud services were shutdown on February 29,2016
    :cite:`www-dotCloud`

98. Dokku
99. OSGi
100. HUBzero
101. OODT
102. Agave

     Agave is an open source, application hosting framework and
     provides a platform-as-a-service solution for hybrid
     computing. :cite:`agave-paper` It provides everything ranging
     from authentication and authorization to computational, data and
     collaborative services. Agave manages end to end lifecycle of an
     application’s execution.  Agave provides an execution platform,
     data management platform, or an application platform through
     which users can execute applications, perform operations on their
     data or simple build their web and mobile
     applications. :cite:`www-agaveapi-features`

     Agave’s API’s provide a catalog with existing technologies and
     hence no additional appliances, servers or other software needs
     to be installed. To deploy an application from the catalog, the
     user needs to host it on a storage system registered with Agave,
     and submit to agave, a JSON file that shall contain the path to
     the executable file, the input parameters, and specify the
     desired output location. :cite:`agave-paper` Agave shall read the
     JSON file, formalize the parameters, execute the user program and
     dump the output to the requested destination.

103. Atmosphere

     Atmosphere is developed by CyVerse (previously named as iPlant
     Collaborative).
     It is a cloud-computing platform. It allows one to launch his own
     “isolated virtual machine (VM) image :cite:`www-at1`.
     It does not require any machine specification. It can be run on any device
     (tablet/desktop/laptop) and any machine(Linux/Windows/Max/Unix).
     User should have a CyVerse account and be granted permission to access to 
     Atmosphere before he can begin using Atmosphere. No subscription is needed.
     Atmosphere is designed to execute data-intense bioinformatics tasks that 
     may include a)Infrastructure as a Service (IaaS) with advanced APIs;
     b)Platform as a Service (PaaS), and c)Software as a Service (SaaS).
     On Atmosphere one has several images of virtual machine and user can launch
     any image or instance according to his requirements.
     The images launched by users can be shared among different members as and
     when required :cite:`www-at2`.


High level Programming
----------------------------------------------------------------------

104. Kite
105. Hive
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
     various patterns, oppurtunities and possiblities that the dataset
     has to offer. :cite: 'shark-paper-2012' At a traditional
     EDW(Enterprrise Data Warehouse) a simple data manipulation can be
     perfpormed using SQL queries but we have to rely on other systems
     to apply the machine learning on thoese data.Apache Shark is a
     distributed query engine developed by the open source community
     whoese goal is to provide a a unified system for easy data
     manipulation using SQL and pushing sophisticated analysis towards
     the data.

     :cite:'shark-paper-2012' Shark is a data Warehouse system built
     on top of Apache Spark which does the parallel data execution and
     is capable of deep data analysis using the Resilient Distributed
     Datasets(RDD) memory abstraction which unifies the SQL query
     processing engine with analytical algorithms based on this common
     abstraction allowing the two to run in the same set of workers
     and share intermediate data. Since RDDs are designed to scale
     horizontally, it is easy to add or remove nodes to accommodate
     more data or faster query processing thus it can be scaled to
     thoushands o nodes in a fault-toleranat manner

     :cite:'shark-paper-2012' "Shark is built on Hive Codebase and it
     has the ability to execute HIVE QL queries up to 100 times faster
     than Hive without making any change in the existing
     queries". Shark can run both on the StandAlone Mode and Cluster
     Mode.:cite:'shark-paper-2012' Shark can answer the queries 40X
     faster than Apache Hive and can machine learning programs 25X
     faster than MapReduce programmes. in Apache hadoop on large data
     sets.Thus, this new data analysis system performs query
     processing and complex analytics(iterative Machine learning) at
     scale and efficiently recovers form the failures midway

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
     
     Google Cloud DataFlow :cite:`data_flow1` is a unified programming
     model that manages the deployment, maintenance and optimization
     of data processes such as batch processing, ETL etc. It creates a
     pipeline of tasks and dynamically allocates resources thereby
     maintaining high efficiency and low latency. According to
     :cite:`data_flow1`, these capabilities make it suitable for
     solving challenging big data problems. Also, google DataFlow
     overcomes the performance issues faced by Hadoops Mapreduce while
     building pipelines. As stated in :cite:`dataconomy` the
     performance of MapReduce started deteriorating while facing
     multiplepetabytes of data whereas Google Cloud Dataflow is
     apparently better at handling enormous
     datasets. :cite:`data_flow1` Additionally Google Dataflow can be
     integrated with Cloud Storage, Cloud Pub/Sub, Cloud Datastore,
     Cloud Bigtable, and BigQuery. The unified programming ability is
     another noteworthy feature which uses Apache Beam SDKs to support
     powerful operations like windowing and allows correctness control
     to be applied to batch and stream  data processes.
     
125. Summingbird
126. Lumberyard

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
     bolt. :cite:`www-storm-home-concepts`
     
128. S4
129. Samza

     Apache Samza is an open-source near-realtime, asynchronous computational 
     framework for stream processing developed by the Apache Software 
     Foundation in Scala and Java. :cite:`www-samza-3`
     Apache Samza is a distributed stream processing framework. It uses Apache
     Kafka for messaging, and Apache Hadoop YARN to provide fault tolerance,
     processor isolation, security, and resource management. Samza processes
     streams. A stream is composed of immutable messages of a similar type or
     category. Messages can be appended to a stream or read from a stream.
     Samza supports pluggable systems that implement the stream abstraction:
     in Kafka a stream is a topic, in a database we might read a stream by
     consuming updates from a table, in Hadoop we might tail a directory of
     files in HDFS. Samza is a stream processing framework. Samza provides a
     very simple callback-based “process message” API comparable to MapReduce.
     Samza manages snapshotting and restoration of a stream processor’s state.
     Samza is built to handle large amounts of state (many gigabytes per
     partition). :cite:`www-samza-1` Whenever a machine in the cluster fails, 
     Samza works with YARN to transparently migrate your tasks to another      
     machine. Samza uses Kafka to guarantee that messages are processed in the  
     order they were written to a partition, and that no messages are ever lost. 
     Samza is partitioned and distributed at every level. Kafka provides  
     ordered, partitioned, replayable, fault-tolerant streams. YARN provides a 
     distributed environment for Samza containers to run in. Samza works with   
     Apache YARN, which supports Hadoop’s security model, and resource isolation 
     through Linux CGroups :cite:`www-samza-4` :cite:`www-samza-3`.

130. Granules

     Granules in used for execution or processing of data streams in 
     distributed environment.
     When applications are running concurrently on multiple computational 
     resources, granules manage their parallel execution.
     The MapReduce implementation in Granules is responsible for providing
     better performance.It has the capability of expressing computations like 
     graphs.
     Computations can be scheduled based on periodicity or other activity.
     Computations can be developed in C, C++, Java, Python, C#, R
     It also provides support for extending basic Map reduce framework.
     Its application domains include hand writing recognition, bio informatics
     and computer brain interface :cite:`www-granules`.
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

     Heron is a real-time analytics platform that was developed at
     Twitter for distributed streaming processing. Heron was
     introduced at SIGMOD 2015 to overcome the shortcomings of Twitter
     Storm as the scale and diversity of Twitter data increased. As
     mentioned in :cite:`TwitterHeronOpen` The primary advantages of
     Heron were: API compatible with Storm: Back compatibility with
     Twitter Storm reduced migration time. Task-Isolation: Every task
     runs in process-level isolation, making it easy to debug/
     profile. Use of main stream languages: C++, Java, Python for
     efficiency, maintainability, and easier community
     adoption. Support for backpressure: dynamically adjusts the rate
     of data flow in a topology during run-time, to ensure data
     accuracy. Batching of tuples: Amortizing the cost of transferring
     tuples. Efficiency: Reduce resource consumption by 2-5x and Heron
     latency is 5-15x lower than Storm’s latency. The architecture of
     Heron (as shown in :cite:`TwitterHeron`)uses the Storm API to
     submit topologies to a scheduler. The scheduler runs each
     topology as a job consisting of several containers. The
     containers run the topology master, stream manager, metrics
     manager and Heron instances. These containers are managed by the
     scheduler depending on resource availability.
     
136. Databus
137. Facebook Puma/Ptail/Scribe/ODS
     
     The real time data Processing at Fcabook is carried out using the
     technologies like Scibe,PTail, Puma and ODS. While designing the
     system, facebook primarily focused on the five key decissions
     that the system should incorporate and that included Ease of Use,
     Performance , Fault-tolerance , Scalability and
     Correctness.:cite: 'www-facebook' "The real time data analytics
     ecosystem at facebook is designed to handle hundreds of Gigabytes
     of data per second via hundreds of data pipelines and this system
     handles over 200,000 events per second with a maximum latency of
     30 seconds". :cite:'www-facebook'Fcabook focused on the Seconds
     of latency while designing the system and not milliseconds as
     seconds are fast enough to for all the use case that needs to be
     supported, and it allowed facebook to use persistent message bus
     for data transport and this made the system more fault toleranat
     and scalable. :cite:'facebook-paper-2017' The large
     infrastructure of facebook comprises of hundreds of systems
     distributed across multiple data centers that needs a continious
     monitoring to track their health and performance.Which is done by
     Operational Data Store(ODS).ODS comprises of a time series
     database (TSDB),which is a query service, and a detection and
     alerting system. ODS’s TSDB is built atop the HBase storage
     system.Time series data from services running on Facebook hosts
     is collected by the ODS write service and written to HBase.

     When the data is generated by the user from their devices, an
     AJAX request is fired to facebook,and these requests are then
     written to a log file using Scribe(distributed data transport
     system), this messaging system collect, aggregate and delivers
     high volume of log data with few seconds of latency and high
     throughput.Scribe stores the data in the HDFS(Hadoop Distributed
     File System) in a tailing fashion, where the new events are
     stored in log files and the files are tailed below the current
     events.The events are then written into the storage HBase on
     distributed machines. This makes the data avalible for both batch
     and real-time processing. Ptail is an internal tool built to
     aggregate data from multiple Scribe stores and It then tails the
     log files and pulls data out for processing. Puma is a stream
     processing system which is the real-time aggregation/storage of
     data. Puma provides filtering and processing of Scribe streams
     (with a few seconds delay), usually Puma batches the storage per
     1.5 seconds on average and when the last flush completes, then
     only a new batch starts to avoid the contention issues, which
     makes i fairly real time
     
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
140. Spark Streaming
141. Flink Streaming
142. DataTurbine


Basic Programming model and runtime, SPMD, MapReduce
----------------------------------------------------------------------

143. Hadoop
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

     Twister is a new software tool released by Indiana University, which is an 
     extension to MapReduce architectures currently used in the academia and 
     industry :cite:`www-twister1`. It supports faster execution of many data mining applications 
     implemented as MapReduce programs. Applications that currently use Twister
     include: K-means clustering, Google's page rank, Breadth first graph search
     , Matrix multiplication, and Multidimensional scaling. Twister also builds 
     on the SALSA team's work related to commercial MapReduce runtimes, 
     including Microsoft Dryad software and open source Hadoop software. SALSA 
     project work is funded in part by an award from Microsoft, Inc. The archite
     cture is based on pub/sub messaging that enables it to perform faster data
     transfers, minimizing the overhead of the runtime. Also, the support for 
     long running processes improves the efficiency of the runtime for many     
     iterative MapReduce computations. :cite:`www-twister2` :cite:`www-twister3` 
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
152. Pregel
153. Pegasus
154. Ligra

    Ligra is a Light Weight Graph Processing Framework for the graph
    manipulation and analysis in shared memory system. It is
    particularly suited for implementing on parallel graph traversal
    algorithms where only a subset of the vertices are processed in an
    iteration The interface is lightweight in that it supplies only a
    few functions. The Ligra framework has two very simple routines,
    one for mapping over edges and one for mapping over vertices.

    :cite:'ligra-paper-2013 'The implementations of several graph
    algorithms like BFS, breadth-first search, betweenness centrality,
    graph radii estimation, graph-connectivity, PageRank and
    Bellman-Ford single-source shortest paths efficient and scalable,
    and often achieve better running times than ones reported by other
    graph libraries/systems

    :cite:'ligra-paper-2' Although the shared memory machines cannot
    be scaled to the same size as distributed memory clusters but the
    current commodity single unit servers can easily fit graphs with
    well over a hundred billion edges in the shared memory systems
    that is large enough for any of the graphs reported in the papers
    mentioned above.
     
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
     publish-subscribe messaging system and supports distributed environment.
      
     *Kafka lets you publish and subscribe to the messages.* Kafka maintains 
     message feeds based on ‘topic’. A topic is a category or feed name to 
     which records are published. Kafka’s Connector APIs are used to publish 
     the messages to one or more topics, whereas, Consumer APIs are used to 
     subscribe to the topics.

     *Kafka lets you process the stream of data at real time.* Kafka’s stream 
     processor takes continual stream of data from input topics, processes the 
     data in real time and produces streams of data to output topics. Kafka’s 
     Streams API are used for data transformation.

     *Kafka lets you store the stream of data in distributed clusters.* Kafka 
     acts as a storage system for incoming data stream. As Kafka is a distributed 
     system, data streams are partitioned and replicated across nodes.

     Thus, a combination of messaging, storage and processing data stream makes 
     Kafka a ‘streaming platform’. It can be used for building data pipelines 
     where data is transferred between systems or applications. Kafka can also be 
     used by applications that transform real time incoming data. :cite:'www-kafka'

172. Kestrel
173. JMS

     JMS (Java Messaging Service) is a java oriented messaging standard
     that defines a set of interfaces and semantics which allows
     applications to send, receive, create, and read messages.  It allows
     the communication between different components of a distributed
     application to be loosely coupled, reliable, and
     asynchronous. :cite:`www-jms-wiki` JMS overcomes the drawbacks of RMI
     (Remote Method Invocation) where the sender needs to know the method
     signature of the remote object to invoke it and RPC(Remote Procedure
     Call), which is tightly coupled i.e it cannot function unless the
     sender has important information about the receiver.

     JMS establishes a standard that provides loosely coupled communication
     i.e the sender and receiver need not be present at the same time or
     know anything about each other before initiating the communication.
     JMS provides two communication domains.A point-to-point messaging
     domain where there is one producer and one consumer. On generating
     message, a producer simple pushes the message to a message queue which
     is known to the consumer. The other communication domain is
     publish/subscribe model, where one message can have multiple
     receivers. :cite:`www-jms-oracle-docs`

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

     Amazon SNS is an Inter process communication service which gives
     the user simple, end-to-end push messaging service allowing them
     to send messages, alerts, or notifications. According to
     :cite:`www-sns`, it can be used to send a directed message
     intended for an entity or to broadcast messages to list of
     selected entities. It is an easy to use and cost effective
     mechanism to send push messages. Amazon SNS is compatible to send
     push notifications to iOS, Windows, Fire OS and Android OS
     devices.

     According to :cite:`sns-blog`,Topics are named groups of events or
     access points, each identifying a specific subject, content, or event
     type. Each topic has a unique identifier (URI) that identifies the SNS
     endpoint for publishing and subscribing.Owners create topics and
     control all access to the topic. The owner can define the permissions
     for all of the topics that they own.Subscribers are clients
     (applications, end-users, servers, or other devices) that want to
     receive notifications on specific topics of interest to
     them.Publishers send messages to topics. SNS matches the topic with
     the list of subscribers interested in the topic, and delivers the
     message to each and every one of them.

     According to :cite:`sns-faq`, Amazon SNS follows pay as per usage. In
     general it is $0.50 per 1 million Amazon SNS Requests.Amazon SNS
     supports notifications over multiple transport protocols such as
     HTTP/HTTPS, Email/Email-JSON, SQS(Message queue) and SMS.Amazon SNS
     can be used with other AWS services such as Amazon SQS, Amazon EC2 and
     Amazon S3.

179. Lambda
180. Google Pub Sub

     :cite:`www-google-pub-sub` Google Pub/Sub provides an asynchronous 
     messaging facility which assists the communication between independent 
     applications. It works in real time and helps keep the two interacting 
     systems independent. It is the same technology used by many of the 
     Google apps like GMail, Ads, etc. and so integration with them becomes 
     very easy. :cite:`www-google-pub-sub-features` Some of the typical 
     features it provides are: (1) Push and Pull - Google Pub/Sub integrates 
     quickly and easily with the systems hosted on the Google Cloud Platform 
     thereby supporting one-to-many, one-to-one and many-to-many 
     communication, using the push and pull requests. (2) Scalability - It 
     provides high scalability and availability even under heavy load without 
     any degradation of latency. This is done by using a global and highly 
     scalable design. (3) Encryption - It provides security by encryption of 
     the stored data as well as that in transit. Other than these important 
     features, it provides some others as well, like the usage of RESTful 
     APIs, end-to-end acknowledgement, replicated storage, etc. 
     
181. Azure Queues

     Azure Queues storage is a Microsoft Azure service, providing inter
     -process communication by message passing :cite:`silberschatz1998operating`. 
     A sender sends the message and a client receives and processes them. 
     The messages are stored in a queue which can contain millions of 
     messages, up to the total capacity limit of a storage account :cite:`www-azurequeue-web`.
     Each message can be up to 64 KB in size. These messages can then be 
     accessed from anywhere in the world via authenticated calls using HTTP or 
     HTTPS. Similar to the other message queue services, Azure Queues enables 
     decoupling of the components :cite:`www-tutorialspoint`. It runs in an 
     asynchronous environment where messages can be sent among the different 
     components of an application. Thus, it provides an efficient solution for 
     managing workflows and tasks. The messages can remain in the queue up to 7 
     days, and afterwards, they will be deleted automatically.

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

     Memcached is a free and open-source, high performance, distributed memory
     object caching system. :cite:`www-memcached` Although, generic in nature,it
     is intended for se in speeding up dynamic web applications by reducing
     the database load.

     It can be thought of as a short term memory for your applications.
     Memcached is an in-memory key-value store for small chunks of arbitrary
     data from the results of database calls, API calls and page rendering. Its
     API is available in most of the popular languages. In simple terms, it
     allows you to take memory from parts of your system where you have more
     memory than you need and allocate it to parts of your system where you
     have less memory than you need.
     
185. Redis

     Redis (Remote Dictionary Server) is an open source ,in-memory,
     key-value database which is commonly referred as a data structure
     server.  :cite:'redis-book-2011' "It is called a data structure
     server and not simply a key-value store because Redis implements
     datastructure which allows keys to contain binary safe strings
     ,hashes,sets and sortedsets, as well as lists" .Redis’s
     exceptional performance, simplicity to use and implement, and
     atomic manipulation of data structures lends itself to solving
     problems that are difficult or perform poorly when implemented
     with traditional relational databases.  :cite:'redis-book-2016'
     "Salivator Sanfilippo(Creator of open-sorce database Redis) makes
     a strong case that Redis does not need to replace the existing
     database but is an excellent addition to an enterprise for new
     functionalities or to solve sometimes intyractable problems."

     :cite:'redis-book-2016' A very popular use pattern for Redis is
     an in-memory cache for web-applications. The second popular use
     pattern for REDIS is for metric storage of such quantitative data
     such as web page usage and user behaviour on gamer leaderboards
     where using a bit operations on strings, Redis very efficently
     stores binary information on a particular characteristics.The
     third popular Redis use pattern is a communication layer between
     different systems through a publish/subscribe(pub/sub for short),
     where one can post message to one or more channels that can be
     acted upon by other systems that are subscribed to or listening
     to that channel for incoming message. The Comapnies using REDIS
     includes Twitter to store the timelines of all the user ,
     Pinterest stores the user follower graph, Github, popular web
     frameworks like Node.js ,Django,Ruby-on-Rails etc.

186. LMDB (key value)

     LMDB (Lighting memory-mapped Database) is a high performance embedded
     transactional database in form of a key-value store
     :cite:`www-keyvalue`. LMDB is designed around
     virtual memory facilities found in modern operating
     systems, multi-version concurrency control (MVCC)
     and single-level store (SLS) concepts. LMDB stores
     arbitrary key/data pairs as byte arrays, provides a
     range-based search capability, supports multiple
     data items for a single key and has a special mode
     for appending records at the end of the database
     (MDB_APPEND) which significantly increases its write
     performance compared to other similar databases.

     LMDB is not a relational database :cite:`www-relationaldb` and
     strictly uses key-value store. Key-value databases
     allows one write at a time, the difference that LMDB
     highlights is that write transactions do not block
     readers nor do readers block writes. Also, it does
     allow multiple applications on the same system to
     open and use the store simultaneously which helps in
     scaling up performance :cite:`WWW-LMDB`.

187. Hazelcast

     Hazelcast is a java based, in memory data grid. :cite:`www-wikihazel` 
     It is open source software, released under the Apache 2.0 License. 
     :cite:`www-githubhazel` Hazelcast enables predictable scaling for 
     applications by providing in memory access to data. 
     :cite:`www-wikihazel` Hazelcast uses a grid to distribute data evenly 
     across a cluster. Clusters allow processing and storage to scale 
     horizontally. Hazelcast can run locally, in the cloud, in virtual 
     machines, or in Docker containers. :cite:`www-wikihazel`

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
     data management framework in Java. Formerly known as ‘Java
     Persistent Objects’ (JPOX) this was relaunched in 2008 as
     ‘DataNucleus’. According to :cite:`DataNucleusWiki` DataNucleus
     Access Platform is a fully compliant implementation of the Java
     Persistent API (JPA) and Java Data Objects (JDO)
     specifications. It provides persistence and retrieval of data to
     a number of datastores using a number of APIs, with a number of
     query languages. In addition to object-relational mapping (ORM)
     it can also map and manage data from sources other than RDBMS
     (PostgreSQL, MySQL, Oracle, SQLServer, DB2, H2 etc.) such as
     Map-based (Cassandra, HBase), Graph-based (Neo4j), Documents
     (XLS, OOXML, XML, ODF), Web-based (Amazon S3, Google Storage,
     JSON), Doc-based (MongoDB) and Others (NeoDatis, LDAP). It
     supports the JPA (Uses JPQL Query language), JDO (Uses JDOQL
     Query language) and REST APIs :cite:`DataNucleus`.DataNucleus
     products are built from a sequence of plugins where each of it is
     an OSGi bundle and can be used in an OSGi environment. Google App
     Engine uses DataNucleus as the Java persistence layer
     :cite:`DataNucleusPerformance`.
	   
196. ODBC/JDBC


Extraction Tools
----------------------------------------------------------------------

197. UIMA
     
     Unstructured Information Management applications (UIMA) provides
     a framework for content analytics. It searches unstructured data
     to retrieve specific targets for the user. For example, when a
     text document is given as input to the system, it identifies
     targets such as persons, places, objects and even
     associations. According to , :cite:`uima_wiki` theUIMA
     architecture can be thought of as four dimensions: 1. Specifies
     component interfaces in analytics pipeline.  2. Describes a set
     of Design patterns. 3. Suggests two data representations: an
     in-memory representation of annotations for high-performance
     analytics and an XML representation of annotations for
     integration with remote web services. 4. Suggests development
     roles allowing tools to be used by users with diverse skills.

     UIMA uses different, possibly mixed, approaches which include
     Natural Language Processing, Machine Learning, IR. UIMA supports
     multimodal analytics :cite:`uima_ss` which enables the system to
     process the resource fro various points of view. UIMA is used in
     several software projects such as the IBM Research's Watson uses
     UIMA for analyzing unstructured data and Clinical Text Analysis
     and Knowledge Extraction System (Apache cTAKES) which is a
     UIMA-based system for information extraction from medical
     records.

381. Tika

     "The Apache Tika toolkit detects and extracts metadata and text
     from over a thousand different file types (such as PPT, XLS, and
     PDF). All of these file types can be parsed through a single
     interface, making Tika useful for search engine indexing, content
     analysis, translation, and much more. :cite:`www-tika`"


SQL(NewSQL)
----------------------------------------------------------------------

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

     In the book :cite:`book-sqlserver`, the technical architecture of SQL Server in
     OLTP(online transaction processing), hybrid cloud and business
     intelligence modes is explained in detail.



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

     According to Amazon Web Services, Amazon Relation Database
     Service (Amazon RDS) is a web service which makes it easy to
     setup, operate and scale relational databases in the cloud. As
     mentioned in :cite:`AmazonRDS` It allows to create and use
     MySQL, Oracle, SQL Server, and PostgreSQL databases in the
     cloud. Thus, codes, applications and tools used with existing
     databases can be used with Amazon RDS. The basic components of
     Amazon(As listed in :cite:`AmazonRDSComponents`) RDS include: DB
     Instances: DB instance is an isolated database environment in the
     cloud. Regions and availability zones: Region is a data center
     location which contains Availability Zones. Availability Zone is
     isolated from failures in other Availability Zones. Security
     groups: controls access to DB instance by allowing access to IP
     address ranges or Amazon EC2 instances that is specified. DB
     parameter groups: manage configuration of DB engine by specifying
     engine configuration values that are applied to one or more DB
     instances of the same instance type. DB option groups: Simplifies
     data management through Oracle Application Express (APEX), SQL
     Server Transparent Data Encryption, and MySQL memcached support.

     
213. Google F1
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
     
     Solandra is a highly scalable real-time search engine built on
     Apache Solr and Apache Cassandra. Solandra simplifies maintaining
     a large scale search engine, something that more and more
     applications need. At its core, Solandra is a tight integration
     of Solr and Cassandra, meaning within a single JVM both Solr and
     Cassandra are running, and documents are stored and disributed
     using Cassandra's data model. :cite:`www-solandra`

     Solandra supports most out-of-the-box Solr functionality (search,
     faceting, highlights), multi-master (read/write to any node). It
     features replication, sharding, caching, and compaction managed
     by Cassandra. :cite:`www-solandra2`
	  
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

     Berkeley DB is a family of open source, NoSQL key-value database libraries. 
     :cite:`www-bdb-wiki` It provides a simple function-call API for data access 
     and management over a number of programming languages, including C, C++, 
     Java, Perl, Tcl, Python, and PHP. Berkeley DB is embedded because it links 
     directly into the application and runs in the same address space as the 
     application. :cite:`www-bdb-stanford` As a result, no inter-process 
     communication, either over the network or between processes on the same 
     machine, is required for database operations. It is also extremely portable 
     and scalable, it can manage databases up to 256 terabytes in size.
     
     :cite:`www-bdb` For data management, Berkeley DB offers advanced services, 
     such as concurrency for many users, ACID transactions, and recovery. 
     
     Berkeley DB is used in a wide variety of products and a large number of 
     projects, including gateways from Cisco, Web applications at Amazon.com 
     and open-source projects such as Apache and Linux.

225. Kyoto/Tokyo Cabinet

     Tokyo Cabinet :cite:`www-tokyo-cabinet` and Kyoto Cabinet
     :cite:`www-kyoto-cabinet` are libraries of routines for managing a
     database. The database normally is a simple data file containing
     records having a key value pair structure. Every key and value is
     serial bytes with variable length. Both binary data and character
     string can be used as a key and a value. There is no concept of
     data tables nor data types like RDBMS or DBMS. Records are
     organized in hash table, B+ tree, or fixed-length array.Tokyo and
     Kyoto cabinets both are developed as a successor of GDBM and QDBM
     which are library routines for managing database as well. Tokyo
     Cabinet is written in the C language, and is provided as API of
     C, Perl, Ruby, Java, and Lua. Tokyo Cabinet is available on
     platforms which have API conforming to C99 and POSIX. Whereas
     Kyoto Cabinet is written in the C++ language, and is provided as
     API of C++, C, Java, Python, Ruby, Perl, and Lua. Kyoto Cabinet
     is available on platforms which have API conforming to C++03 with
     the TR1 library extensions. Both are free software licenced under
     GNU (General Public Licence). :cite:`www-tokyo-cabinet` actually mentions
     that Kyoto Cabinet is more powerful and has convenient library
     structure than Tokyo and recommends people to use Kyoto. Since
     they use key-value pair concept, you can store a record with a
     key and a value, delete a record using the key and even retrive a
     record using the key. Both have smaller size of database file,
     faster processing speed and provide effective backup procedures.

     
226. Tycoon

     Tycoon/ Kyoto Tycoon :cite:`Tycoon_fl` is a lightweight database
     server developed by FLL labs and is a distributed Key-value store
     :cite:`Tycoon_cf`. It is very useful in handling cache data
     persistent data of various applications. Kyoto Tycoon is also a
     package of network interface to the DBM called Kyoto Cabinet
     :cite:`Tycoon_fl2` which contains a library of routines for
     managing a database. Tycoon is composed of a sever process that
     manger multiple databases. This renders high concurrency enabling
     it to handle more than 10 thousand connections at the same time.
     
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
     for documents, whereas a document contains key-value pairs for storing 
     data. As MongoDB is a NoSQL database, it supports dynamic schema design 
     allowing documents to have different fields. The database uses a document 
     storage and data interchange format called BSON, which provides a binary 
     representation of JSON-like documents.

     MongoDB provides high data availability by way of replication and 
     sharding. High cost involved in data replication can be reduced by 
     horizontal data 
     scaling by way of shards where data is scattered across multiple 
     servers. It reduces query cost as the query load is distributed 
     across servers. This means that both read and write performance 
     can be increased by adding more shards to a cluster. Which document 
     resides on which shard is determined by the shard key of each collection.

     As far as data backup and restore is concerned the default MongoDB 
     storage engines natively support backup of complete data. For incremental 
     backups one can use MongoRocks that is a third party tool developed by Facebook.

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
     
     According to :cite:`www-gemfire`, a real-time, consistent access
     to data-intensive applications is provided by a open source, data
     management platform named Pivotal Gemfire. "GemFire pools memory,
     CPU, network resources, and optionally local disk across multiple
     processes to manage application objects and behavior". The main
     features of Gemfire are high scalability, continuous
     availability, shared nothing disk persistence, heterogeneous data
     sharing and parallelized application behavior on data stores to
     name a few.  In Gemfire, clients can subscribe to receive
     notifications to execute their task based on a specific change in
     data. This is achieved through the continuous querying feature
     which enables event-driven architecture. The shared nothing
     architecture of Gemfire suggests that each node is
     self-sufficient and independent, which means that if the disk or
     caches in one node fail the remaining nodes remaining
     untouched. Additionally, the support for multi-site
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

     Hbase is a type of NoSQL database and is classified as a key value
     store.In HBase, value is identied with a key where both of them are
     stored as byte arrays. Values are stored in the order of keys. HBase
     is a database system where the tables have no schema. Some of the
     companies that use HBase as their core program are Facebook, Twitter,
     Adobe, Netflix etc.

235. Google Bigtable

     Google Bigtable is a NoSQL database service, built upon several Google
     technologies, including Google File System, Chubby Lock Service, and
     SSTable. :cite:`www-cloudbigtable`  Designed for Big Data, Bigtable 
     provides high performance and low latency and scales to hundreds of
     petabytes. :cite:`www-cloudbigtable` Bigtable powers many core
     Google products, such as Search, Analytics, Maps, Earth, Gmail,
     and YouTube. :cite:`www-wikibigtable` Since May 6, 2015, a
     version of Bigtable has been available to the public.  Bigtable
     also drives Google Cloud Datastore :cite:`www-wikibigtable` and
     Spanner, a distributed NewSQL database also developed by
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

     A Graph Database is a database that uses graph structures for semantic
     queries with nodes, edges and properties to represent and store data.
     :cite:`www-graphdb`
     The Graph is a concept which directly relates the data items in the store.
     The data which is present in the store is linked together directly with the
     help of relationships. It can be retrieved with a single operation.
     Graph database allow simple and rapid retrieval of complex hierarchical
     structures that are difficult to model in relational systems.

     There are different underlying storage mechanisms used by graph databases.
     Some graphdb depend on a relational engine and store the graph data in a
     table, while others use a key-value store or document-oriented database for
     storage. Thus, they are inherently caled as NoSQL structures.
     Data retrieval in a graph database requires a different query language
     other than SQL. Some of the query languages used to retrieve data from a
     graph database are Gremlin, SPARQL, and Cypher.
     Graph databases are based on graph theory. They employ the concepts of
     nodes, edges and properties.
     
244. Yarcdata
245. AllegroGraph
     
     “AllegroGraph is a database technology that enables businesses to 
     extract sophisticated decision insights and predictive analytics from 
     their highly complex, distributed data that can’t be answered with 
     conventional databases, i.e., it turns complex data into actionable 
     business insights.” :cite:`www-Allegro`
     It can be viewed as a closed source database that is used for storage
     and retrieval of data in the form of triples (triple is a data entity 
     composed of subject-predicate-object like “Professor teaches students”).
     Information in a triplestore is retrieved using a query language. Query 
     languages can be classified into database query languages or information
     retrieval query languages. The difference is that a database query language
     gives exact answers to exact questions, while an information retrieval 
     query language finds documents containing requested information. 
     Triple format represents information in a machine-readable format. 
     Every part of the triple is individually addressable via unique URLs — 
     for example, the statement “Professor teaches students” might be 
     represented in RDF(Resource Description Framework ) as 
     http://example.name#Professor12 http://xmlns.com/foaf/0.1/teacheshttp:
     //example.name#students. Using this representation, semantic data can 
     be queried.  :cite:`www-Allegrow`

246. Blazegraph
247. Facebook Tao

     In the paper published in USENIX annual technical conference, 
     Facebook Inc describes TAO (The Association and Objects) as 
     :cite ‘book-tao’ a geographically distributed data store that 
     provides timely access to the social graph for Facebook’s demanding 
     workload using a fixed set of queries. It is deployed at Facebook for 
     many data types that fit its model. The system runs on thousands of 
     machines, is widely distributed, and provides access to many petabytes 
     of data. TAO represents social data items as Objects (user) and 
     relationship between them as Associations (liked by, friend of). 
     TAO cleanly separates the caching tiers from the persistent data 
     store allowing each of them to be scaled independently. To any user 
     of the system it presents a single unified API that makes the entire 
     system appear like 1 giant graph database. :cite:'www-tao'.

248. Titan:db

     Titan:db :cite:`www-Titan` is a distributed graph database that 
     can support of thousands of concurrent users interacting with a
     single massive graph database that is distributed over the 
     clusters. It is open source with liberal Apache 2 license. 
     Its main components are storage backend, search backend, and 
     TinkerPop graph stack. Titan provides support for various 
     storage backends and also linear scalability for a growing data 
     and user base. It inherits features such as ‘Gremlin’ query 
     language  and ‘Rexter’ graph server from TinkerPop :cite:`www-TinkerPop`. 
     For huge graphs, Titan uses a component called Titan-hadoop which 
     compiles Gremlin queries to Hadoop MapReduce jobs and runs them 
     on the clusters. Titan is basically optimal for smaller graphs.

249. Jena

     Jena is an open source Java Framework provided by Apache for
     semantic web applications. (:cite:`jena_wiki`) It provides a
     programmatic environment for RDF, RDFS and OWL, SPARQL, GRDDL,
     and includes a rule-based inference engine. Semantic web data
     differs from conventional web applications in that it supports a
     web of data instead of the classic web of documents format. The
     presence of a rule based inference engine enable Jena to perform
     a reasoning based on OWL and RDFS ontologies.  :cite:`jena_blog`
     The architecture of Jena contains three layers : Graph layer,
     model layer and Ontology layer. The graph layer forms the base
     for the architecture. It does not have an extensive RDF
     implementation and serves more as a Service provider
     Interface. According to :cite:`jena_blog` It provides
     classes/methods that could be further extended. The model layer
     extends the graph layer and provides objects of type ‘resource’
     instead of ‘node’ to work with.  The ontology layer enables one
     to work with triples.

250. Sesame

     Sesame is framework which can be used for the analysis of RDF
     (Resource Description Framework) data.  Resource Description
     Framework (RDF) :cite:`www-RDF` is a model that facilitates the
     interchange of data on the Web.  Using RFD enables us to merge
     data even if the underlying schemas differ.  :cite:`www-sesame`
     Sesame has now officially been integrated into RDF4J Eclipse
     project.  Sesame takes in the natively written code as the input
     and then performs a series of transformations, generating kernels
     for various platforms.  :cite:`sesame-paper-2013` In order to
     achieve this, it makes use of the feature identifier, impact
     predictor, source-to-source translator and the auto-tuner.  The
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

File management
----------------------------------------------------------------------

254. iRODS
255. NetCDF

     NetCDF is a set of software libraries and self-describing, machine-indepen
     dent data formats that support the creation, access, and sharing of array
     oriented scientific data. NetCDF was developed and is maintained at Unidata
     , part of the University Corporation for Atmospheric Research (UCAR) Commun
     ity Programs (UCP). Unidata is funded primarily by the National Science F
     oundation :cite:`paper-netCDF` :cite:`www-netcdf` . The purpose of the Netwo
     rk Common Data Form(netCDF) interface is to support the creation, efficient
     access, and sharing of data in a form that is self-describing, portable, co
     mpact, extendible, and archivable Version 3 of netCDF is widely used in   
     atmospheric and ocean sciences due to its simplicity. NetCDF version 4 has 
     been designed to address limitations of netCDF version 3 while preserving 
     useful forms of compatibility with existing application software and data 
     archives :cite:`paper-netCDF`. 
     NetCDF consists of: a) A conceptual data model b) A set of binary data 
     formats c) A set of APIs for C/Fortran/Java 

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
     magzines. Vatican Library :cite:`www-fits-vatican-library` used FITS 
     for long term preservation of their book, manuscripts and other
     collection. Matlab, a language used for technical computing
     supports fits :cite:`www-fits-matlab`. The 2011 paper
     :cite:`paper-fits-2011` explains how to perform
     processing of astronomical images on Hadoop using FITS. 

260. RCFile

     RCFile (Record Columnar File) :cite:`www-rcfile` is a big
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
     :cite:`www-rcfile`. According to :cite:`he2011rcfile`, RCFile has
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

     According to :cite:`ftp-wiki` FTP is an acronym for File Transfer
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
     log data :cite:`apche-flume`. Flume was created to allow you to
     flow data from a source into your Hadoop® environment.  In Flume,
     the entities you work with are called sources, decorators, and
     sinks. A source can be any data source, and Flume has many
     predefined source adapters. A sink is the target of a specific
     operation. A decorator is an operation on the stream that can
     transform the stream in some manner, which could be to compress
     or uncompress data, modify data by adding or removing pieces of
     information, and more :cite:`ibm-flume`.

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

     In pilot job, an application acquires a resource so that it can
     be delegated some work directly by the application; instead of
     requiring some job scheduler. The issue of using a job scheduler
     is that a waiting queue is required. Few examples of Pilot Jobs
     are the :cite:`pilot-job-falkon-paper-2007` Falkon lightweight
     framework and :cite:`pilot-job-htcaas-paper-2007` HTCaaS. Pilot
     jobs are typically associated with both Parallel computing as
     well as Distributed computing. Their main aim is to reduce the
     dependency on queues and the associated multiple wait times.

     :cite:`www-pilot-job-paper-2016` Using pilot jobs enables us to have a 
     multilevel technique for the execution of various workloads. This is so 
     because the jobs are typically acquired by a placeholder job and they 
     relayed to the workloads.      

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
289. f4
290. Cinder
      
     "Cinder is a block storage service for Openstack"
     :cite:`wiki-Cinder`. According to :cite:`book-Cinder` Openstack
     Compute uses ephemeral disks meaning that they exist only for the
     life of the Openstack instance i.e. when the instance is
     terminated the disks disappear. Block storage system is a type of
     persistent storage that can be used to persist data beyond the
     life of the instance. Cinder provides users with access to
     persistent block-level storage devices. It is designed such that
     users can create block storage devices on demand and attach them
     to any running instances of OpenStack
     Compute. :cite:`wiki-Cinder` This is achieved through the use of
     either a reference implementation(LVM) or plugin drivers for
     other storage. Cinder virtualizes the management of block storage
     devices and provides end users with a self-service API to request
     and consume those resources without requiring any knowledge of
     where their storage is actually deployed or on what type of
     device.
     
291. Ceph
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
     Spectrum Scale on February 17, 2015.  :cite:`www-wikigpfs`
     See 380.

380. IBM Spectrum Scale

     General Parallel File System (GPFS) was rebranded as IBM Spectrum 
     Scale on February 17, 2015. :cite:`www-wikigpfs`

     Spectrum Scale is a clustered file system, developed by IBM, designed 
     for high performance. It "provides concurrent high-speed file access 
     to applications executing on multiple nodes of clusters" 
     :cite:`www-wikigpfs` and can be deployed in either shared-nothing 
     or shared disk modes. Spectrum Scale is available on AIX, Linux, 
     Windows Server, and IBM System Cluster 1350. :cite:`www-wikigpfs` 
     Due to its focus on performance and scalability, Spectrum Scale has 
     been utilized in compute clusters, big data and analytics (including 
     support for Hadoop Distributed File System (HDFS), backups and 
     restores, and private clouds. :cite:`www-spectrumscale`

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
     for using the Amazon S3 are as follows:
     1) Sign up for Amazon S3
     2) After sign up, create a Bucket in your account.
     3) Create an object which might be an file or folder.
     4) Perform operations on the object which is stored in the cloud.
	
	

	
298. Azure Blob

     Azure Blob storage is a service that stores unstructured data in the cloud
     as objects/blobs. Blob storage can store any type of text or binary data,
     such as a document, media file, or application installer :cite:`www-azure-3`
     Blob storage is also referred to as object storage. The word ‘Blob’ expands 
     to Binary Large OBject. There are three types of blobs in the service offe-
     red by Windows Azure namely block, append and page blobs. :cite:`www-azure-2`
     1. Block blobs are collection of individual blocks with unique block ID.
     The block blobs allow the users to upload large amount of data.
     2. Append blobs are optimized blocks that helps in making the operations
     efficient.
     3. Page blobs are compilation of pages. They allow random read and write
     operations. While creating a blob, if the type is not specified they are
     set to block type by default. All the blobs must be inside a container in
     your storage.
     Azure Blob storage is a service for storing large amounts of unstructured
     object data, such as text or binary data, that can be accessed from
     anywhere in the world via HTTP or HTTPS. You can use Blob storage to expose
     data publicly to the world, or to store application data privately. Common
     uses of Blob storage include serving images or documents directly to a
     browser, storing files for distributed access, streaming video and audio,
     storing data for backup and restore, disaster recovery, and archiving and
     storing data for analysis by an on-premises or Azure-hosted service.
     Azure Storage is massively scalable and elastic with an auto-partitioning
     system that automatically load-balances your data. Blob storage is a
     specialized storage account for storing your unstructured data as blobs
     (objects) in Azure Storage. Blob storage is similar to existing
     general-purpose storage accounts and shares all the great durability,
     availability, scalability, and performance features. Blob storage has two
     types of access tiers that can be specified, hot access tier, which will be
     accessed more frequently, and a cool access tier, which will be less
     frequently accessed. There are many reasons why you should consider using
     BLOB storage. Perhaps you want to share files with clients, or off-load
     some of the static content from your web servers to reduce the load on
     them. :cite:`www-azure-3`

299. Google Cloud Storage

     Google Cloud Storage is the cloud enabled storage offered by
     Google. :cite:`www-google-cloud-storage` It is unified object
     storage. To have high availability and performance among
     different regions in the geo-redundant storage offering. If you
     want high availability and redundancy with a single region one
     can go for “Regional” storage. Nearline and Coldline’ are the
     different archival storage techniques. “Nearline” storage
     offering is for the archived data which the user access less than
     once a month . “Coldline’ storage is the storage which is used
     for the data which is touched less than once a year.

     All the data in Google Cloud storage belongs inside a project. A
     project will contains different buckets. Each bucket has
     different objects. We need to make sure that the name of the
     bucket is unique across all Google cloud name space . And the
     name of the objects should unique in a bucket.


Interoperability
----------------------------------------------------------------------

300. Libvirt
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

     SAGA(Simple API for Grid Applications) provides an abstraction layer
     to make it easier for applications to utilize and exploit infra
     effectively. With infrastructure being changed continuously its
     becoming difficult for most applications to utilize the advances in
     hardware. SAGA API provides a high level abstraction of the most
     common Grid functions so as to be independent of the diverse and
     dynamic Grid environments. :cite:`saga-paper` This shall address the
     problem of applications developers developing an application tailored
     to a specific set of infrastructure.  SAGA allows computer scientists
     to write their applications at high level just once and not to worry
     about low level hardware changes. SAGA provides this high level
     interface which has the underlying mechanisms and adapters to make the
     appropriate calls in an intelligent fashion so that it can work on any
     underlying grid system. “SAGA was built to provide a standardized,
     common interface across various grid middleware systems and their
     versions.”  :cite:`www-saga-ogf-document`

     As SAGA is to be implemented on different types
     of middleware it does not specify a single security model but provides
     hooks to interfaces of various security models. The SAGA API provides
     a set of packages to implement its objectivity : SAGA supports data
     management, resource discovery, asynchronous notification, event
     generation, event delivery etc. It does so by providing set of
     functional packages namely SAGA file package, replica package, stream
     package, RPC package, etc. SAGA provides interoperability by allowing
     the same application code to run on multiple grids and also
     communicate with applications running on others. :cite:`saga-paper`

308. Genesis

DevOps
----------------------------------------------------------------------

309. Docker (Machine, Swarm)
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
     type. :cite:`www-ansible2`

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
314. Boto

     :cite:`www-boto` The latest version of Boto is Boto3. 
     :cite:`www-boto-github` Boto3 is the Amazon Web Services (AWS) Software 
     Development Kit (SDK) for Python. It enables the Python developers to 
     make use of services like Amazon S3 and Amazon EC2. 
     :cite:`www-boto3-documentation` It provides object oriented APIs along 
     with low-level direct service access. It provides simple in-built 
     functions and interfaces to work with Amazon S3 and EC2. 

     :cite:`www-boto-amazon-python-sdk` Boto3 has two distinct levels of APIs 
     - client and resource. One-to-one mappings to underlying HTTP API is 
     provided by the client APIs. Resource APIs provide resource objects and 
     collections to perform various actions by accessing the attributes. 
     Boto3 also comes with 'waiters'. Waiters are used for polling status 
     changes in AWS, automatically. Boto3 has these waiters for both the APIs 
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
317. Razor

     Razor is a hardware provisioning application, developed by Puppet
     Labs and EMC. Razor was introduced as open, pluggable, and
     programmable since most of the provisioning tools that existed
     were vendor-specific, monolithic, and closed. According to
     :cite:`RazorWiki` it can deploy both bare-metal and virtual
     systems. During boot the Razor client automatically discovers the
     inventory of the server hardware – CPUs, disk, memory, etc.,
     feeds this to the Razor server in real-time and the latest state
     of every server is updated. It maintains a set of rules to
     dynamically match the appropriate operating system images with
     server capabilities as expressed in metadata. User-created policy
     rules are referred to choose the preconfigured model to be
     applied to a new node. The node follows the model's directions,
     giving feedback to Razor as it completes various steps as
     specified in :cite:`RazorPuppet`. Models can include steps for
     handoff to a DevOps system or to any other system capable of
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
     control" :cite:`www-heat-wiki`

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
     in each layer of AWS OpsWorks Stacks. :cite:`www-awsopsworks`

328. OpenStack Ironic
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
     
     QEMU (Quick Emulator) is a generic open source hosted hypervisor
     :cite:`WWW-Hypervisor` that performs hardware virtualization
     (virtualization of computers as complete hardware platform,
     certain logical abstraction of their componentry or only the
     certain functionality required to run various operating systems)
     :cite:`WWW-QEMU` and also emulates CPUs through dynamic binary
     translations and provides a set of device models, enabling it to
     run a variety of unmodified guest operating systems.
     
     When used as an emulator, QEMU can run Operating Systems and programs
     made for one machine (ARM board) on a different machine (e.g. a
     personal computer) and achieve good performance by using dynamic
     translations.  When used as a virtualizer, QEMU achieves near native
     performance by executing the guest code directly on the host CPU. QEMU
     supports virtualization when executing under the Xen hypervisor or
     using KVM kernel module in Linux :cite:`WWW-QEMUWiki`.

     Compared to other virtualization programs like VMWare and VirtualBox,
     QEMU does not provide a GUI interface to manage virtual machines nor
     does it provide a way to create persistent virtual machine with saved
     settings. All parameters to run virtual machine have to be specified
     on a command line at every launch. It’s worth noting that there are
     several GUI front-ends for QEMU like virt-manager and gnome-box.

342. Hyper-V
343. VirtualBox
344. OpenVZ

     OpenVZ (Open Virtuozzo) is an operating system-level virtualization
     technology for Linux. It allows a physical server to run multiple isolated
     operating system instances, called containers, virtual private servers, or
     virtual environments (VEs). OpenVZ is similar to Solaris Containers and
     LXC. :cite:`www-openvz-3` While virtualization technologies like VMware and 
     Xen provide full virtualization and can run multiple operating systems and 
     different kernel versions, OpenVZ uses a single patched Linux kernel and 
     therefore can run only Linux. All OpenVZ containers share the same archite-
     cture and kernel version. This can be a disadvantage in situations where 
     guests require different kernel versions than that of the host. However, as
     it does not have the overhead of a true hypervisor, it is very fast and 
     efficient. Memory allocation with OpenVZ is soft in that memory not used in 
     one virtual environment can be used by others or for disk caching. :cite:`www-openvz-2`
     While old versions of OpenVZ used a common file system (where each virtual 
     environment is just a directory of files that is isolated using chroot), 
     current versions of OpenVZ allow each container to have its own file system. 
     OpenVZ has four main features, :cite:`www-openvz-1`
     1. OS virtualization: A container (CT) looks and behaves like a regular
     Linux system. It has standard startup scripts; software from vendors can
     run inside a container without OpenVZ-specific modifications or adjustment;
     A user can change any configuration file and install additional software;
     Containers are completely isolated from each other and are not bound to
     only one CPU and can use all available CPU power.
     2. Network virtualization: Each CT has its own IP address and CTs are
     isolated from the other CTs meaning containers are protected from each
     other in the way that makes traffic snooping impossible; Firewalling may
     be used inside a CT
     3. Resource management: All the CTs are use the same kernel. OpenVZ
     resource management consists of four main components: two-level disk quota,
     fair CPU scheduler, disk I/O scheduler, and user beancounters.
     4. Checkpointing and live migration: Checkpointing allows to migrate a
     container from one physical server to another without a need to
     shutdown/restart a container. This feature makes possible scenarios such as
     upgrading your server without any need to reboot it: if your database needs
     more memory or CPU resources, you just buy a newer better server and live
     migrate your container to it, then increase its limits.


345. LXC
     
     LXC (Linux Containers) is an operating-system-level
     virtualization method for running multiple isolated
     Linux systems (containers) on a control host using a single
     Linux kernel :cite:`www-wiki-lxc`. LXC are similar to the treditional virtual
     machines but instead of having seperate kernel process for the
     guest operating system being run, containers would share the
     kernal process with the host operating system. This is made
     possible with the implementation of namespaces and cgroups. :cite:`www-jpablo`

     Containers are light weighed ( As guest operating system
     loading and booting is eleminated ) and more customizable
     compared to VM technologies.The basis for docker developement
     is also LXC. :cite:`www-infoworld`. Linux containers would
     work on the major distributions of linux this would not work
     on Microsoft Windows.
	
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
     load balancers and multi-role support. :cite:`www-cloudstack2`
	  
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
     VMware ESXi is done via APIs. This allows for an “agent-less”
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
356. Amazon

     Amazon’s AWS (Amazon Web Services) is a provider of Infrastructure 
     as a Service (IaaS) on cloud. It provides a broad set of infrastructure 
     services, such as computing, data storage, networking and databases. 
     One can leverage AWS services by creating an account with AWS and then 
     creating a virtual server, called as an instance, on the AWS cloud. 
     In this instance you can select the hard disk volume, number of CPUs 
     and other hardware configuration based on your application needs. 
     You can also select operating system and other software required 
     to run your application. AWS lets you select from the countless services. 
     Some of them are mentioned below.

          -  Amazon Elastic Computer Cloud (EC2)

          -  Amazon Simple Storage Service (Amazon S3)

          -  Amazon CloudFront

          -  Amazon Relational Database Service (Amazon RDS)

          -  Amazon SimpleDB

          -  Amazon Simple Notification Service (Amazon SNS)

          -  Amazon Simple Queue Service (Amazon SQS)

          -  Amazon Virtual Private Cloud (Amazon VPC)

     Amazon EC2 and Amazon S3 are the two core IaaS services, which are 
     used by cloud application solution developers worldwide. :cite:'www-aws'

357. Azure
358. Google and other public Clouds
359. Networking: Google Cloud DNS
360. Amazon Route 53


Cross-Cutting Functions
----------------------------------------------------------------------

Monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

     :cite:`www-keystone-wiki` Keystone is the identity service used by 
     OpenStack for authentication (authN) and high-level authorization (authZ). 
     There are two authentication mechanisms in Keystone, UUID token, and PKI. 
     Universally unique identifier (UUID) is a 128-bit number used to identify 
     information (user). Each application after each request of the client 
     checks token validity online. PKI was introduced later and improved the 
     security of Keystone :cite:`cui2015security`. In PKI, each token has its 
     own digital signature that can be checked by any service and OpenStack 
     application with no necessity to ask for Keystone database :cite:`www-cloudberrylab-kstn`.
 
     Thus, Keystone enables ensuring user’s identity with no need to transmit 
     its password to applications. It has recently been rearchitected to allow 
     for expansion to support proxying external services and AuthN/AuthZ 
     mechanisms such as oAuth, SAML and openID in future versions :cite:`www-keystone`.

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

     As explained in :cite:`SAML`, Security Assertion Markup Language
     (SAML) is a secured XML based communication mechanism for
     communicating identities between organizations. The primary use
     case of SAML is Internet SSO. It eliminates the need to maintain
     multiple authentication credentials in multiple locations. This
     enhances security by elimination opportunities for identity
     theft/Phishing. It increases application access by eliminating
     barriers to usage. It reduces administration time and cost by
     excluding the effort to maintain duplicate credentials and
     helpdesk calls to reset forgotten passwords. Three entities of
     SAML are the users, Identity Provider (IdP-Organization that
     maintains a directory of users and an authentication mechanism)
     and Service Provider(SP-Hosts the application /service). User
     tries to access the application by clicking on a link or through
     an URL on the internet. The Federated identity software running
     in the IdP validates the user’s identity and the user is then
     authenticated. A specifically formatted message is then
     communicated to the federated identity software running at SP. SP
     creates a session for the user in the target application and
     allows the user to get direct access once it receives the
     authorization message from a known identity provider.

Distributed Coordination
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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




References
---------

.. bibliography:: ../refs.bib
   :style: unsrt
   :cited:
