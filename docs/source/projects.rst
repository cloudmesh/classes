.. _ref-project-guidelines:

Project Guidelines
===============================================================================

.. sidebar:: Page Contents

   .. contents::
      :local:

Important Dates
-------------------------------------------------------------------------------

* Project Proposal: March 18th
* Oral Presentation: Week 12 - April 1st, 2nd (Tentative)
* Progress Checkup: Week 14 - April 15th, 16th (Tentative)
* Final Submission: April 29th

.. note:: Those who can't make the presentation with a time conflict, schedule
        a meeting with Course Team.

Submission
-------------------------------------------------------------------------------

* IU GitHub: https://github.iu.edu/bdossp-sp16

Team Coordination
-------------------------------------------------------------------------------

Up to 3 members is recommended but individual is allowed.

.. adding empty line breaks

.. |br| raw:: html

  <br />
  <br />
  <br />
  <br />
  <br />
  <br />

Project Expectation (Grade)
-------------------------------------------------------------------------------

Final project counts as 60% of semester grade and 40% goes on assignments.

* 60% Final project
   - 10% Proposal
   - 10% Presentation
   - 30% Source code
   - 10% Report

Project Style
-------------------------------------------------------------------------------

 * Basic 
 * Bonus

You do not require strong background or programming skills with HPC or
Hadoop to complete a final project. We've noticed that, however, there are some
difficulties learning Linux systems, shells, or scripts and improving
programming skills with parallelization in general. You have two options, Basic
and Bonus, to start your project based on your capability on these.

Basic Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Basic project starts from existing projects and extends the scope of the
projects with minimal efforts on code developments.  For example, take existing
Hadoop benchmark tools and run them on hadoop clusters with different system
configurations to compare. Try to increase data nodes, master nodes or add
ZooKeeper with different settings and measure differences. Comparing
performance in different software versions, settings or configurations tells
you where focal points are to optimize or improve throughput of hadoop. Choose
a basic project if you are not conpetent with programming languages e.g. Java
or Python. Note that starting from existing projects doesn't mean that you can
simply search and download popular projects on the internet and execute. You
need to address new findings and include the original source of the projects
that you referenced in your final project and reports.

* Minimal code writing
* Start from existing projects

.. TeraSort, DFSIO, NNBench, or MRBench on a different system configurations 

Bonus Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are working on a bonus project, you are required to write code/scripts
to implement your idea in the final project. Installation and configuration
should be done by Ansible Playbooks. For example, take NIST Facial Recognition
software and run with Hadoop clusters. Change serial calculation to be executed
in parallel. Writing map and reduce functions may be necessary in Java, Python
or Scala. Write Ansible Playbooks to install and configure your software
packages within a few commands. If data analytics is the area that you are
interested, you may try to develop new techniques to improve performance or
implement parallel algorithms for complex face detection. Developing parallel
programs would be involved in most cases. There are other possibilities as
well. For instance, take hadoop-ansible-stacks which consists of basic
components of Hadoop and append new software tools by writing new playbooks in
roles and addons. You could add Hives or update Spark with the latest release
using parameters or definition in YAML. If you focus on managing systems and
software deployments, think about how to manage traffics by adding/removing
additional nodes or how to apply new patches on particular nodes. Bonus points
are given exceptional project results.

* Ansible is required
* Extensive code and scripts writing are welcome
* Using GitHub Issues is mandatory to communicate with AIs for your projects
* Bonus points

Project Choice
-------------------------------------------------------------------------------

* Deployment
* Benchmark (Performance Test)
* Parallelization
* Analytics
* Created Own (upon approval)

Deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Deployment project focuses on automated software deployments on multiple nodes
using automation tools/configuration managements such as Ansible, Chef, Puppet,
Salt or Juju. For example, you can work on deploying Hadoop clusters with 10
medium virtual instances or Sharded MongoDB clusters or filesystems e.g. NFS or
Gluster. **Ansible** is recommended and supported in the class.

Examples:

* Deployment Hadoop clusters
* Deployment cluster managers (e.g. Mesos)

Benchmark
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Benchmark project focuses on testing system's performance by putting some
stresses on different spots. Filesystems, CPUs, or memories can be tested and
measured, if you think about hardware benchmark.  APIs, messaging queues, load
balancers or any applications can be tested and measured, if software is more
focused. Hibench, Big Data Benchmark, or built-in tools e.g. Terasort
are available for Hadoop benchmark.

Examples:

* Hibench
* Storm Benchmark
* Big Data Benchmark for Big Bench

Parallelization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parallelization project focuses on building efficient software stacks in
parallel including MPI and Hadoop clusters. For example, you may find writing
map and reduce functions is relatively easy e.g. WordCount, but applying it in
practice with large datasets isn't that simple. Think about how to load your
dataset into hadoop file systems or databases and run your jobs in a
distributed fashion.

Examples:

* Pig
* Spark

Analytics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Analytics project focuses on developing algorithms for different problems based
on datasets and topics that you chose in your project. You will be required
to develop algorithms for improving parallelism or performance in this project 
rather than developing new algorithm for face recognition, for example.

Examples:

* Faunus Graph analytics
* Ibis

Created Own
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can develop own project idea and make it as a class project upon approval.
Describe your thought, tools, and topics and make a clear statement of the
problems you identified in your project proposal.

Project Requirement
-------------------------------------------------------------------------------

* Installation/Configuration by Ansible playbook or relevant tools
* Reproducibility - runnable on Linux distribution
* Sample Dataset - up to 480GB per team
* 12 VM instances with m1.medium are given to the utmost each team
* Software Stacks similar to :ref:`ref-software-layers`

Project Copyright
-------------------------------------------------------------------------------

Your project deliverables may be introduced in the future classes or be shared
by others online after the end of semester.

Project Proposal
-------------------------------------------------------------------------------

Please submit your project proposal to IU GitHub. The submission format is in a
``proposal.rst`` RST file. `RST Quick Reference
<http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_ , `Online RST
Editor <http://rst.ninjs.org/>`_. A project proposal is typically 1-2 pages
long and should contain in the description section:

* the nature of the project and its context
* the technologies used
* any proprietary issues
* specific aims you intent to complete
* and a list of intended deliverables (atrifacts produced)

Project Proposal Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`ref-project-proposal`

Oral Presentation
-------------------------------------------------------------------------------

You are required to demonstrate your project during the presentation week. The
clear statement of problems are necessary with schedule, plan, role of team
members, resources to use.

* A student will use Adobe Connect to give a presentation which will be
  recorded.
* 3-5 minutes per team.
* Presentation can be substituted with written reports upon approval.
  1-2 page progress report(s) need to be included.

Presentation Guideline
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Demonstrate the following criteria:
   - team members (roles)
   - problem definition
   - list of technologies
   - list of development tools, languages
   - list of dataset and its availability
   - schedule
   - resources to use
* All presentations will be recorded.

Progress Checkup
-------------------------------------------------------------------------------

The following activities will be evaluated:

* Code development in a project repository
* Participation of team members
* Software installation
* Datasets preparation

List of Possible Projects (In Progress)
-------------------------------------------------------------------------------

We are currently working on this and any software and/or details are subject to
change without notice. This is reference only.

* Big Data Analytics Stack
   - Deployment project using Ansible Playbooks

.. _ref-software-layers:

.. list-table:: Software Layers
    :widths: 10 10 10 10
    :header-rows: 1

    * - Layer
      - Supported
      - In Progress
      - Optional
    * - Scheduling Layer
      - YARN
      - 
      - Mesos
    * - Database Layer
      - 
      - MongoDB, HBase, MySQL
      - CouchDB, PostgreSQL, Memcached, Redis
    * - Analytics Layer
      - Java
      - MLlib, Python
      - BLAS, LAPACK, Mahout, MLbase, R
    * - Data Processing Layer
      - Hadoop MapReduce, Spark, Pig
      - Storm, Flink
      - Tez, Hama, Hive

You may consider to work on Big Data Analytics Stack using Ansible Playbooks.
The default configuration of the stack is YARN + HDFS + Java + Hadoop
MapReduce, Spark, and Pig. You can develop a new addon for one of the optional
software and attach to your stack. Find more details here
:ref:`ref-big-data-stacks`.

.. include:: projects/list_of_projects_2016sp.rst

* :ref:`ref-2015-fall-list-of-projects`

List of Datasets (In Progress)
-------------------------------------------------------------------------------

We are currently working on this and any software and/or details are subject to
change without notice. This is reference only.

* :ref:`ref-list-of-datasets-2015-fall`

.. note:: There is no direct support on datasets.
.. note:: Large datasets will be downloadable via NFS on india.futuresystems.org

List of Technologies (In Progress)
-------------------------------------------------------------------------------

We are currently working on this and any software and/or details are subject to
change without notice. This is reference only.

* `ABDS and HPC Technologies and Software Stacks <http://hpc-abds.org/kaleidoscope/>`_
* :ref:`ref-list-of-tech-2015-fall`
* :ref:`ref-list-of-tech-2015-spring`

.. note:: There is no direct support on Analytics software.

Details on Software Submission
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Code submission should be made at Github including a ``README`` file.

* Source code on Github: https://github.iu.edu/bdossp-sp16/

``README`` includes:

- Test instruction
- List of data source
- List of technologies used

Details on Final Report 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Final report concludes the work of your team and describes findings with its
results.  The following sections should be included:

* Description of your project
* Problem statement
* Purpose and objectives
* Results 
* Findings
* Implementation
* References
   - original source of code snippets
   - original source of datasets

   .. http://ipro.iit.edu/wp-content/uploads/ipro-final-report-guidelines.pdf

The final reports should sastify the following guidelines:

- 4 - 6 pages
- Time Roman 12 point -- spacing 1.1 in Microsoft Word
- Figures can be included 
- Proper citations must be included
- Material may be taken from other sources but that must amount to at most 25%
  of original work and must be cited
- The level should be similar to a publishable paper or technical report

Details on Grading Criteria
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Proposal 
   - Clear statement
   - Quality and Breath
   - Interest
* Code
   - Reproducibility
   - Executable (Most weighted)
   - Instruction of Installation
   - Instruction of Configuration
   - Datasets
   - Acknowledgements 
   - Gee whiz factor
* Report
   - Related Work
   - Completeness
   - Level of insight

.. comment::

        What We Expect (or NOT)
        -------------------------------------------------------------------------------



        Example Recommended
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        Example Avoided
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        -

FAQ
-------------------------------------------------------------------------------

Q. Use of FutureSytem is required?

A. No, it is not required. However, you need to provide instructions how to
install your software project in a single or multiple nodes.

Q. I need more time to complete code development, may I have an extension?

A. Extension would be approved upon request. Send an extension request email
message to the course email with a title ``[Project Extension]`` and an
expected completion date.

Q. Our team wants to change a topic or scope of a project after project
proposal or presentation, is it allowed?

A. Topic should be close to what you proposed earlier. Please contact Dr. Fox
or Course Email if you change a topic or a scope of your project significantly.
Also inform if you change team members. These changes would be approved upon
request.

Q. Report or survey type of final project is allowed?

A. No, software project is only allowed in this class.

Q. I found there is a similar project that I proposed, should I keep working
on my project?

A. Consult with Course Team to make differences in detail. You may be asked to
focus on specific area in order to avoid similarity.

Q. Can't make a oral presentation because I have a business trip (or a conference).

A. Schedule a meeting in Week 11 or Week 13 with Course Team.

Q. What does that mean there is no direct support on Datasets and Analytics software?

A. You can choose your dataset and analytics tool freely from many choices but
   the course team can't assist you to validate whether datasets or tools you chose
   are runnable in your software stacks. Downloading large dataset is supported though.

Questions & Support
-------------------------------------------------------------------------------

* Course Email: bdosspcoursehelp@googlegroups.com
* Google Hangout (voice & screen share): upon request

Useful Links
-------------------------------------------------------------------------------


