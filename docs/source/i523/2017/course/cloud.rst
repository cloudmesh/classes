
.. _S11:

Cloud Computing Technology for Big Data Applications & Analytics (will be updated)
----------------------------------------------------------------------------------

We describe the central role of Parallel computing in Clouds and Big
Data which is decomposed into lots of ''Little data'' running in
individual cores. Many examples are given and it is stressed that
issues in parallel computing are seen in day to day life for
communication, synchronization, load balancing and
decomposition. Cyberinfrastructure for e-moreorlessanything or
moreorlessanything-Informatics and the basics of cloud computing are
introduced. This includes virtualization and the important ''as a
Service'' components and we go through several different definitions
of cloud computing.

Gartner's Technology Landscape includes hype cycle and priority matrix
and covers clouds and Big Data. Two simple examples of the value of
clouds for enterprise applications are given with a review of
different views as to nature of Cloud Computing. This IaaS
(Infrastructure as a Service) discussion is followed by PaaS and SaaS
(Platform and Software as a Service). Features in Grid and cloud
computing and data are treated. We summarize the 21 layers and almost
300 software packages in the HPC-ABDS Software Stack explaining how
they are used.

Cloud (Data Center) Architectures with physical setup, Green Computing
issues and software models are discussed followed by the Cloud
Industry stakeholders with a 2014 Gartner analysis of Cloud computing
providers. This is followed by applications on the cloud including
data intensive problems, comparison with high performance computing,
science clouds and the Internet of Things. Remarks on Security, Fault
Tolerance and Synchronicity issues in cloud follow. We describe the
way users and data interact with a cloud system. The Big Data
Processing from an application perspective with commercial examples
including eBay concludes section after a discussion of data system
architectures.




Parallel Computing: Overview of Basic Principles with familiar Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


We describe the central role of Parallel computing in Clouds and Big
Data which is decomposed into lots of ''Little data'' running in
individual cores. Many examples are given and it is stressed that
issues in parallel computing are seen in day to day life for
communication, synchronization, load balancing and decomposition.

.. todo:: The slides or videos are going to be updated
          
Slides: https://iu.app.box.com/s/nau0rsr39kyej240s4yz


Decomposition 
"""""""""""""""

We describe why parallel computing is essential with Big Data
and distinguishes parallelism over users to that over the data in
problem. The general ideas behind data decomposition are given
followed by a few often whimsical examples dreamed up 30 years ago in
the early heady days of parallel computing. These include scientific
simulations, defense outside missile attack and computer chess. The
basic problem of parallel computing -- efficient coordination of
separate tasks processing different data parts -- is described with
MPI and MapReduce as two approaches. The challenges of data
decomposition in irregular problems is noted.

.. todo:: The slides or videos are going to be updated
          
Video 1: https://youtu.be/R-wHQW2YuRE

Video 2: https://youtu.be/iIi9wdvlwCM

Video 3: https://youtu.be/F0aeeLeTD9I



Parallel Computing in Society 
"""""""""""""""""""""""""""""""

This lesson from the past notes that one can view society as an
approach to parallel linkage of people. The largest example given is
that of the construction of a long wall such as that (Hadrian's wall)
between England and Scotland. Different approaches to parallelism are
given with formulae for the speed up and efficiency. The concepts of
grain size (size of problem tackled by an individual processor) and
coordination overhead are exemplified. This example also illustrates
Amdahl's law and the relation between data and processor topology. The
lesson concludes with other examples from nature including collections
of neurons (the brain) and ants.

.. todo:: The slides or videos are going to be updated
          
Video 1: https://youtu.be/8rtjoe8AeJw

Video 2: https://youtu.be/7sCgH_TTPGk


Parallel Processing for Hadrian's Wall
""""""""""""""""""""""""""""""""""""""

This lesson returns to Hadrian's wall and uses it to illustrate
advanced issues in parallel computing. First We describe the
basic SPMD -- Single Program Multiple Data -- model. Then irregular
but homogeneous and heterogeneous problems are discussed. Static and
dynamic load balancing is needed. Inner parallelism (as in vector
instruction or the multiple fingers of masons) and outer parallelism
(typical data parallelism) are demonstrated. Parallel I/O for
Hadrian's wall is followed by a slide summarizing this quaint
comparison between Big data parallelism and the construction of a
large wall.

.. todo:: The slides or videos are going to be updated
          
Video: https://youtu.be/ZD2AQ08cy8I


Resources
"""""""""

* Solving Problems in Concurrent Processors-Volume 1,
  with M. Johnson, G. Lyzenga, S. Otto, J. Salmon, D. Walker, Prentice
  Hall, March 1988.
* Parallel Computing Works!, with P. Messina, R. Williams, Morgan
  Kaufman (1994). http://www.netlib.org/utk/lsi/pcwLSI/text/
* The Sourcebook of Parallel Computing book edited by Jack Dongarra,
  Ian Foster, Geoffrey Fox, William Gropp, Ken Kennedy, Linda Torczon,
  and Andy White, Morgan Kaufmann, November 2002.
* Geoffrey Fox Computational Sciences and Parallelism to appear in
  Encyclopedia on Parallel Computing edited by David Padua and
  published by
  Springer. http://grids.ucs.indiana.edu/ptliupages/publications/SpringerEncyclopedia_Fox.pdf

Cloud Computing Technology Part I: Introduction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


We discuss Cyberinfrastructure for e-moreorlessanything or
moreorlessanything-Informatics and the basics of cloud computing. This
includes virtualization and the important 'as a Service' components
and we go through several different definitions of cloud
computing.Gartner's Technology Landscape includes hype cycle and
priority matrix and covers clouds and Big Data. The unit concludes
with two simple examples of the value of clouds for enterprise
applications. Gartner also has specific predictions for cloud
computing growth areas.


.. todo:: The slides or videos are going to be updated
          
Slides: https://iu.app.box.com/s/p3lztuu9kv240pdm66141or9b8p1uvzb


Cyberinfrastructure for E-MoreOrLessAnything
""""""""""""""""""""""""""""""""""""""""""""

This introduction describes Cyberinfrastructure or e-infrastructure
and its role in solving the electronic implementation of any problem
where e-moreorlessanything is another term for
moreorlessanything-Informatics and generalizes early discussion of
e-Science and e-Business.

.. todo:: The slides or videos are going to be updated
          
Video: https://youtu.be/gHz0cu195ZM



What is Cloud Computing: Introduction
"""""""""""""""""""""""""""""""""""""

Cloud Computing is introduced with an operational definition involving
virtualization and efficient large data centers that can rent
computers in an elastic fashion. The role of services is essential --
it underlies capabilities being offered in the cloud. The four basic
aaS's -- Software (SaaS), Platform (Paas), Infrastructure (IaaS) and
Network (NaaS) -- are introduced with Research aaS and other
capabilities (for example Sensors aaS are discussed later) being built
on top of these.

.. todo:: The slides or videos are going to be updated
          
Video: https://youtu.be/Od_mYXRs5As


What and Why is Cloud Computing: Several Other Views I
""""""""""""""""""""""""""""""""""""""""""""""""""""""

This lesson contains 5 slides with diverse comments on ''what is cloud
computing'' from the web.

.. todo:: The slides or videos are going to be updated
          
Video 1: https://youtu.be/5VeqMjXKU_Y

Video 2: https://youtu.be/J963LR0PS_g

Video 3: https://youtu.be/_ryLXUnOAzo


Gartner's Emerging Technology Landscape for Clouds and Big Data
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This lesson gives Gartner's projections around futures of cloud and
Big data. We start with a review of hype charts and then go into
detailed Gartner analyses of the Cloud and Big data areas. Big data
itself is at the top of the hype and by definition predictions of doom
are emerging. Before too much excitement sets in, note that spinach is
above clouds and Big data in Google trends.

.. todo:: The slides or videos are going to be updated
          
Video: https://youtu.be/N7aEtU1mUwc


Simple Examples of use of Cloud Computing
"""""""""""""""""""""""""""""""""""""""""

This short lesson gives two examples of rather straightforward
commercial applications of cloud computing. One is server
consolidation for multiple Microsoft database applications and the
second is the benefits of scale comparing gmail to multiple smaller
installations. It ends with some fiscal comments.

.. todo:: The slides or videos are going to be updated
          
Video: https://youtu.be/VCctCP6BKEo


Value of Cloud Computing
""""""""""""""""""""""""

Some comments on fiscal value of cloud computing.

.. todo:: The slides or videos are going to be updated
          
Video: https://youtu.be/HM1dZCxdsaA



Resources
"""""""""

* http://www.slideshare.net/woorung/trend-and-future-of-cloud-computing
* http://www.slideshare.net/JensNimis/cloud-computing-tutorial-jens-nimis
* https://setandbma.wordpress.com/2012/08/10/hype-cycle-2012-emerging-technologies/
* http://insights.dice.com/2013/01/23/big-data-hype-is-imploding-gartner-analyst-2/
* http://research.microsoft.com/pubs/78813/AJ18_EN.pdf
* http://static.googleusercontent.com/media/www.google.com/en//green/pdfs/google-green-computing.pdf

Cloud Computing Technology Part II: Software and Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


We cover different views as to nature of architecture and
application for Cloud Computing. Then we discuss cloud software for
the cloud starting at virtual machine management (IaaS) and the broad
Platform (middleware) capabilities with examples from Amazon and
academic studies. We summarize the 21 layers and almost 300 software
packages in the HPC-ABDS Software Stack explaining how they are used.

.. todo:: The slides or videos are going to be updated

Slides: https://iu.app.box.com/s/k61o0ff1w6jkn5zmpaaiw02yth4v4alh


What is Cloud Computing
"""""""""""""""""""""""

This lesson gives some general remark of cloud systems from an
architecture and application perspective.

.. todo:: The slides or videos are going to be updated
          
Video: https://youtu.be/h3Rpb0Eyj1c


Introduction to Cloud Software Architecture: IaaS and PaaS I
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

We discuss cloud software for the cloud starting at virtual
machine management (IaaS) and the broad Platform (middleware)
capabilities with examples from Amazon and academic studies.

.. todo:: The slides or videos are going to be updated
          
Video: https://youtu.be/1AnyJYyh490


Introduction to Cloud Software Architecture: IaaS and PaaS II
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

We cover different views as to nature of architecture and
application for Cloud Computing. Then we discuss cloud software for
the cloud starting at virtual machine management (IaaS) and the broad
Platform (middleware) capabilities with examples from Amazon and
academic studies. We summarize the 21 layers and almost 300 software
packages in the HPC-ABDS Software Stack explaining how they are used.

.. todo:: The slides or videos are going to be updated
          
Video: https://youtu.be/hVpFAUHcAd4


Using the HPC-ABDS Software Stack
"""""""""""""""""""""""""""""""""

Using the HPC-ABDS Software Stack.

.. todo:: The slides or videos are going to be updated

Video: https://youtu.be/JuTQdRW78Pg


Resources
"""""""""

* http://www.slideshare.net/JensNimis/cloud-computing-tutorial-jens-nimis
* http://research.microsoft.com/en-us/people/barga/sc09_cloudcomp_tutorial.pdf
* http://research.microsoft.com/en-us/um/redmond/events/cloudfutures2012/tuesday/Keynote_OpportunitiesAndChallenges_Yousef_Khalidi.pdf
* http://cloudonomic.blogspot.com/2009/02/cloud-taxonomy-and-ontology.html

Cloud Computing Technology Part III: Architectures, Applications and Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


We start with a discussion of Cloud (Data Center)
Architectures with physical setup, Green Computing issues and software
models. We summarize a 2014 Gartner analysis of Cloud computing
providers. This is followed by applications on the cloud including
data intensive problems, comparison with high performance computing,
science clouds and the Internet of Things. Remarks on Security, Fault
Tolerance and Synchronicity issues in cloud follow.

.. todo:: The slides or videos are going to be updated
          
Slides: https://iu.app.box.com/s/0bn57opwe56t0rx4k18bswupfwj7culv


Cloud (Data Center) Architectures 
""""""""""""""""""""""""""""""""""

Some remarks on what it takes to build (in software) a cloud ecosystem,
and why clouds are the data center of the future are followed by
pictures and discussions of several data centers from Microsoft
(mainly) and Google. The role of containers is stressed as part of
modular data centers that trade scalability for fault tolerance. Sizes
of cloud centers and supercomputers are discussed as is "green"
computing.

.. todo:: The slides or videos are going to be updated
          
Video 1: https://youtu.be/j0P32DmQjI8

Video 2: https://youtu.be/3HAGqz34AB4



Analysis of Major Cloud Providers
"""""""""""""""""""""""""""""""""

Gartner 2014 Analysis of leading cloud providers.

.. todo:: The slides or videos are going to be updated
          
https://youtu.be/Tu8hE1SeT28



Commercial Cloud Storage Trends
"""""""""""""""""""""""""""""""

Use of Dropbox, iCloud, Box etc.

.. todo:: The slides or videos are going to be updated
          
https://youtu.be/i5OI6R526kM



Cloud Applications I
""""""""""""""""""""

This short lesson discusses the need for security and issues in its
implementation. Clouds trade scalability for greater possibility of
faults but here clouds offer good support for recovery from faults. We
discuss both storage and program fault tolerance noting that parallel
computing is especially sensitive to faults as a fault in one task
will impact all other tasks in the parallel job.

.. todo:: The slides or videos are going to be updated
          
Video 1: https://youtu.be/nkeSOMTGbbo

Video 2: https://youtu.be/ORd3aBhc2Rc


Science Clouds
""""""""""""""

Science Applications and Internet of Things.

.. todo:: The slides or videos are going to be updated
          
https://youtu.be/2PDvpZluyvs



Security
""""""""

This short lesson discusses the need for security and issues in its
implementation.

.. todo:: The slides or videos are going to be updated
          
https://youtu.be/NojXG3fbrEo


Comments on Fault Tolerance and Synchronicity Constraints
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Clouds trade scalability for greater possibility of faults but here
clouds offer good support for recovery from faults. We discuss both
storage and program fault tolerance noting that parallel computing is
especially sensitive to faults as a fault in one task will impact all
other tasks in the parallel job.

.. todo:: The slides or videos are going to be updated
          
https://youtu.be/OMZiSiN7dlU



Resources
"""""""""

* http://www.slideshare.net/woorung/trend-and-future-of-cloud-computing
* http://www.eweek.com/c/a/Cloud-Computing/AWS-Innovation-Means-Cloud-Domination-307831
* CSTI General Assembly 2012, Washington, D.C., USA Technical Activities Coordinating Committee (TACC) Meeting, Data Management, Cloud Computing and the Long Tail of Science October 2012 Dennis Gannon.
* http://research.microsoft.com/en-us/um/redmond/events/cloudfutures2012/tuesday/Keynote_OpportunitiesAndChallenges_Yousef_Khalidi.pdf
* http://www.datacenterknowledge.com/archives/2011/05/10/uptime-institute-the-average-pue-is-1-8/
* https://loosebolts.wordpress.com/2008/12/02/our-vision-for-generation-4-modular-data-centers-one-way-of-getting-it-just-right/
* http://www.mediafire.com/file/zzqna34282frr2f/koomeydatacenterelectuse2011finalversion.pdf
* http://www.slideshare.net/JensNimis/cloud-computing-tutorial-jens-nimis
* http://www.slideshare.net/botchagalupe/introduction-to-clouds-cloud-camp-columbus
* http://www.venus-c.eu/Pages/Home.aspx
* Geoffrey Fox and Dennis Gannon Using Clouds for Technical Computing To be published in Proceedings of HPC 2012 Conference at Cetraro, Italy June 28 2012 http://grids.ucs.indiana.edu/ptliupages/publications/Clouds_Technical_Computing_FoxGannonv2.pdf
* https://berkeleydatascience.files.wordpress.com/2012/01/20120119berkeley.pdf
* Taming The Big Data Tidal Wave: Finding Opportunities in Huge Data Streams with Advanced Analytics, Bill Franks Wiley ISBN: 978-1-118-20878-6
* Anjul Bhambhri, VP of Big Data, IBM http://fisheritcenter.haas.berkeley.edu/Big_Data/index.html
* Conquering Big Data with the Oracle Information Model, Helen Sun, Oracle
* Hugh Williams VP Experience, Search & Platforms, eBay http://businessinnovation.berkeley.edu/fisher-cio-leadership-program/
* Dennis Gannon, Scientific Computing Environments, http://www.nitrd.gov/nitrdgroups/images/7/73/D_Gannon_2025_scientific_computing_environments.pdf
* http://research.microsoft.com/en-us/um/redmond/events/cloudfutures2012/tuesday/Keynote_OpportunitiesAndChallenges_Yousef_Khalidi.pdf
* http://www.datacenterknowledge.com/archives/2011/05/10/uptime-institute-the-average-pue-is-1-8/
* https://loosebolts.wordpress.com/2008/12/02/our-vision-for-generation-4-modular-data-centers-one-way-of-getting-it-just-right/
* http://www.mediafire.com/file/zzqna34282frr2f/koomeydatacenterelectuse2011finalversion.pdf
* http://searchcloudcomputing.techtarget.com/feature/Cloud-computing-experts-forecast-the-market-climate-in-2014
* http://www.slideshare.net/botchagalupe/introduction-to-clouds-cloud-camp-columbus
* http://www.slideshare.net/woorung/trend-and-future-of-cloud-computing
* http://www.venus-c.eu/Pages/Home.aspx
* http://www.kpcb.com/internet-trends

Cloud Computing Technology Part IV: Data Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



We describe the way users and data interact with a cloud system. The
unit concludes with the treatment of data in the cloud from an
architecture perspective and Big Data Processing from an application
perspective with commercial examples including eBay.


.. todo:: The slides or videos are going to be updated
          
Slides: https://iu.app.box.com/s/ftfpybxm8jzjepzp409vgair1fttv3m1


The 10 Interaction scenarios (access patterns) I
""""""""""""""""""""""""""""""""""""""""""""""""

The next 3 lessons describe the way users and data interact with the
system.

.. todo:: The slides or videos are going to be updated
          
Video: https://youtu.be/vB4rCNri_P0



The 10 Interaction scenarios. Science Examples
""""""""""""""""""""""""""""""""""""""""""""""

This lesson describes the way users and data interact with the system
for some science examples.

.. todo:: The slides or videos are going to be updated
          
Video: https://youtu.be/cFX1PQpiSbk


Remaining general access patterns
"""""""""""""""""""""""""""""""""

This lesson describe the way users and data interact with the system
for the final set of examples.

.. todo:: The slides or videos are going to be updated
          
Video: https://youtu.be/-dtE9zXB-I0


Data in the Cloud
"""""""""""""""""

Databases, File systems, Object Stores and NOSQL are discussed and
compared. The way to build a modern data repository in the cloud is
introduced.

.. todo:: The slides or videos are going to be updated
          
          Video: https://youtu.be/HdtIOnk3qX4


Applications Processing Big Data
""""""""""""""""""""""""""""""""

This lesson collects remarks on Big data processing from several
sources: Berkeley, Teradata, IBM, Oracle and eBay with architectures
and application opportunities.

.. todo:: The slides or videos are going to be updated
          
          Video: https://youtu.be/d6A2m4GR-hw


Resources
"""""""""

* http://bigdatawg.nist.gov/_uploadfiles/M0311_v2_2965963213.pdf
* https://dzone.com/articles/hadoop-t-etl
* http://venublog.com/2013/07/16/hadoop-summit-2013-hive-authorization/
* https://indico.cern.ch/event/214784/session/5/contribution/410
* http://asd.gsfc.nasa.gov/archive/hubble/a_pdf/news/facts/FS14.pdf
* http://blogs.teradata.com/data-points/announcing-teradata-aster-big-analytics-appliance/
* http://wikibon.org/w/images/2/20/Cloud-BigData.png
* http://hortonworks.com/hadoop/yarn/
* https://berkeleydatascience.files.wordpress.com/2012/01/20120119berkeley.pdf
* http://fisheritcenter.haas.berkeley.edu/Big_Data/index.html


.. _S13:
