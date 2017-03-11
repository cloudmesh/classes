Project
=======

The main activity of the course will be building a significant project
using multiple subsystems combined with user code and data. Projects
will be suggested or students can chose their own. A project report
will summarize the work conducted.

Topics taught in this class will be very relevant for industry as you
are not only exposed to big data, but you will also be practically
exposed to DevOps and collaborative code development tools as part of
your homework and project assignment.

Project Selection and Approval
------------------------------

Each project must be approved by the TAs and the Professor. This is
done in an itterative process in which the students needs to first
provide a 2 page description of the project detailing the project and
its execution plan. This is a *snapshot* of a draft of the actual
report that will be handed in at the end. Thus, you do not have to
write in your proposal the words, we propose, or in this proposal. You
can directly write in this report ... You can actually write directly
the project report and leave sections out or put in TBD as text.
Important is that the abstract and the introduction is there, as well
as an execution plan (e.g. reminding you what you can do realistically
when).

Selected Project Ideas
----------------------
	   
Students can select from a number of project ideas. We will improve
and add additional ideas throughout the semester. Students can also
conduct their own projects. We recommend that you identify a project
idea by the end of the first month of the class. Example project
descriptions that you may want to take a look at include:

* :ref:`robotswarm`
* :ref:`dockerswarm`
* :ref:`kubernetes`
* :ref:`slurmcluster`
* :ref:`authordisambiguity_b`
* NIST Big Data Working group examples: Selected and approved use case from
  http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1500-3.pdf
* Selected examples from Fall I523:
  Some students may have created an example as part of I523. Not all
  examples created as part of this class qualify for a I524
  project. Please contact Gregor von Laszewski via Piazza to discuss
  suitability of your previous I523 project. If such a project is
  selected, approved and used it is expected it is significantly
  enhanced.
* Cloudmesh Enhancements:
  A number of projects could center around the enhancements of
  cloudmesh for the improvement of big data projects using virtual
  machines and containers. This includes:

  * Development of REST services for cloudmesh while using cloudmesh
    client
  * Development of benchmarking examples while using cloudmesh client
  * Development of a better Azure interface to additinal services
  * Development of a better AWS interfac to additinal services
  * Development of a Web interface while using django
  * SLURM integration to create virtual clusters on comet
  * Port cloudmesh client to Windows 10
  * Integrate docker into cloudmesh and demonstrate its use
  * Integrate kubernetes into cloudmesh and demonstrate its use
  * Expand the HPC capabilities of cloudmesh

Other Examples
--------------

Example projects can also include the following, but must include a benchmark

* deploy Apache Spark on top of Hadoop
* deploy Apache Pig on top of Hadoop
* deploy Apache Storm
* deploy Apache Flink
* deploy a Tensorflow cluster
* deploy a PostgreSQL cluster
* deploy a MongoDB cluster
* deploy a CouchDB cluster
* deploy a Memcached cluster
* deploy a MySQL cluster
* deploy a Redis cluster
* deploy a Mesos cluster
* deploy a Hadoop cluster
* deploy a docker swarm cluster
* deploy NIST Fingerprint Matching
* deploy NIST Human Detection and Face Detection
* deploy NIST Live Twitter Analysis
* deploy NIST Big Data Analytics for Healthcare Data and Health Informatics
* deploy NIST Data Warehousing and Data mining

    
Datasets
--------

Links Datasets that may inspire a project and benchmarking them are

* https://www.data.gov/
* https://github.com/caesar0301/awesome-public-datasets
* https://aws.amazon.com/public-data-sets/
* https://www.kaggle.com/datasets
* https://cloud.google.com/bigquery/public-data/github
* https://www.quora.com/Where-can-I-find-large-datasets-open-to-the-public

For NIST Projects:

* `NIST Special Database 27A [4GB] <http://www.nist.gov/itl/iad/ig/sd27a.cfm>`_
* `INRIA Person Dataset <http://pascal.inrialpes.fr/data/human/>`_
* `Healthcare data from CMS <https://www.cms.gov/Research-Statistics-Data-and-Systems/Downloadable-Public-Use-Files/Part-B-National-Summary-Data-File/Overview.html>`_
* `Uber Ride Sharing GPS Data <https://github.com/fivethirtyeight/uber-tlc-foil-response>`_
* `Census Data <http://www.census.gov/population/www/cen2010/glance/>`_


For previous I523 class participants
------------------------------------

If you have not yet done an ansible deployment as part of your I523
project you are allowed to continue it as part of this class. Please
note that the focus of I523 allowed you to not conduct a deployment
and a benchmark. I524 **requires** you to conduct a deployment with
ansible and cloudmesh client, as well as benchmarking the application
on a real cloud (e.g. chameleoncloud.org).

Is there a sample report?
-------------------------

Due to the variability of the project we also do not have a sample
report for a sucessfully conducted project. However the papers written
in class as well as the homework to develop an ansible deployment will
provide you with sufficient clarity how to be successful.


Project Deployments
-------------------
   
Students of this class will need to conduct their project deployments
in Python using ansible and enabling a software stack that is useful
for a big data analysis. You will be expected to have a computer on
which you have python 2.7.x installed. You will be using
chameleoncloud.org and possibly our local cloud. Optionally some
projects may use docker. If your project uses docker you can use
docker files, but you still need to show its running on 3 different
computers.
 
If your project uses neither, you have to make sure that you hand in a
software stack deployment done very well on some software related to
the 300+ software systems. You can pick what you want, but shuld not
be as simple as installing emacs or R. For example a sharded mongodb
or cansandra deployment, a distributed deployment of hadoop (some
students asked for this one despite that we had already one like
this. Based on student feedback we allow you to do that. and many
others, ask for approval however).


Technology deployment Homework
------------------------------

Some students may elect to chose as the homework to deploy a
technology with ansible, a technology that is actually used as part of
the project. This is naturally a very good way of minimizing your work
while building and expanding upon the technology homework you elect to
conduct. Points may depend on completeness, effort of the
deployment.Technology deployments should as much as possible be non
overlapping. In many cases you chose wisely such deployments may line
up with your technology papers as you can add a section reporting on
your achievement and experience with such deployments.

Group Work
----------

Groups of up to three students can work on a project but workload
increases with each student and a work break down must be provided.
More than three students are not allowed. If you work in a group you
will be asked to deploy a larger system or demonstrate deployability
on multiple clouds or container frameworks while benchmarking and
comparing them. A group project containing 2 or 3 team members should
not look like a project done by an individual. Please plan careful and
make sure all team members contribute.

As we get this question often: No we will not allow more than three
students to participate in a project. Please do not ask.

We monitor progress for grades
------------------------------

We monitor your progress in Github and you will get *Discussion*
points for this. Thus it is imperative you do **Frequent checkins**:
It is **important** to make frequent and often commits to the github
repository as the activities will be monitored and will be integrated
into the project grade. For example, if you elect to just check in
your project at the end of the semester while not using github, you
will miss points.

Time Management
---------------

Note that paper and project will take a considerable amount of time
and doing proper time management is a must for this class. Avoid
starting your project late. Procrastination does not pay off.
Too often we see a student starting their project in the week before
it is due. We can guarantee you this will be problematic.
To force you to think about your time management we require that your
report contains a section **Project Execution Plan**, that documents when you
approximately do what.

Focus on your project
---------------------

We will not accept any bonus projects or secondary projects as we want
that you focus on your class project. If you would have time to do a
second project, we recommend you add or integrate it in your actual
project spo you can achieve your best. One exccelent project is better
than two good projects.


Chance for publishing a paper
-----------------------------

If however you find that the work you do could lead to a publishable
paper, you could work together with the course instructor as coauthors
to conduct such an activity. However, this is going to be a
significant effort and you need to decide if you like to conduct
this. In such cases if the work is sufficient for publication
submission, an A+ for the class could be considered. It will be a lot
of work. The length of such a paper is typically 10-12 high quality
pages including figures and references. We may elect for the final
submission to use a different LaTeX style

Piazza
------

All project related discussions must be conducted in the **piazza** folder.


Grading
-------

Some students form the class asked for a precise grading
scheme. However, based on previous pobservation with other classes a
truly outstanding project will not really need a grading scheme.

However as we got asked we propose the following::

 ansible 30%
 benchmarking 30%
 paper 30%
 wow factor 10%

The *wow factor** is given if one of the three other components of
the project is impressively well done.
 
Be reminded that the benchmark must involve multiple vms
In case you work as team, the benchmark must include multiple clouds`


Tips
----

The following tips have been issued and especially apply to the
project:

* **Start the project in the first 4 weeks of the class**
  starting means reading thinking and potentially discussing with
  other students or TAs 
* Do not underestimating the time it takes to do the project.
* Do not forget to include benchmarks in your project.
* Unnecessarily struggling with LaTeX as you do not use an example we
  provide.
* Not having a computer that is up to date. Update your memory and
  have a SSD
* Ignoring obvious security rules and not integrating ssh form the
  start into your projects.
* Not posting passwords into git. For example git does
  **not** allow to **easily** completely delete files that contain secret
  information such as passwords. It takes significant effort to do
  that. Make sure you do add in git on individual files and never
  just a bulk add.
* Having your coleagues do the work for you
* Underestimating the **time** it takes to do deployments
* Not reading our piazza posts and repeating the same question over
  and over
* In case of questions ask.
  
  
  
Artifacts
---------

The following artifacts are part of the deliverables for a project

Code:
    You must deliver the code in github. The code must be compilable
    and a TA may try to replicate to run your code. You MUST avoid
    lengthy install descriptions and everything must be installable
    from the command line. We will check submission. All team members
    must be responsible for one part of the project.

Project Report:
    A report must be produced while using the format discussed in the
    Report Format section. The following length is required:

    * 4 pages, one student in the project
    * 6 pages, two students in the project
    * 8 pages, three students in the project

Work Breakdown:
    The report contains in an appendix a section that is
    only needed for team projects. Include in the section a short but
    sufficiently detailed work breakdown documenting what the team has
    done. Back it up with commit information from github. Such as how
    many commits and lines of code a team member has contributed. The
    section does not count towards the overall length of the paper.

    In addition the graders will check the history of checkins to
    verify each team member has used github to checkin their
    contributions frequently. E.g. if we find that one of the students
    has not checked in code or documentation in the same way at other
    teammates, it will be questioned. An oral exam may be scheduled to
    verify that the student has contributed to the project. In an oral
    exam the student must be familiar with **all** aspects of the
    project not just the part you contributed.

License:
    All projects are developed under an open source license such
    as Apache 2.0 License. You will be required to add a LICENCE.txt
    file and if you use other software identify how it can be reused
    in your project. If your project uses different licenses, please
    add in a README.md file which packages are used and which license
    these packages have while adding a licenses file.


Reproducability:
    The reproducability of your code is anticipated to be tested
    twice. It is tetes by another student or team, it is also tested
    by a TA. A report of the testing team is provided. Your team will
    also be responsible for executing as many tests as you have team
    members on other projects. A reproducability statement should be
    written with details about functionality, readbility, and report
    quality. This statement does not have to be written in latex but
    uses RST.

Requirements:
    * Use of cloud resources is mandatory, can be substituted by
      kubeernetes or docker swarm
    * Deployment must be done with ansible
    * A Makefile or a cmd file as discussed in class is needed to
      deploy the software, start the program, conduct a
      parameter study/benchmark
    * Report
    * Cloudmesh client is to be used to start the virtual
      cluster/multiple vms in order to avoid reinventing the wheel
    * Cloudmesh contains deployments for hadoop and spark. If these
      technologies are used, it has to be shown that if the student(s)
      elect to write a new ansible script for it that it is better
      than the once provided by cloudmesh. Proof is to be provided by
      reproducible benchmarks. If this can not be achieved the
      student(s) have to write an additional ansible script for a
      technologie listed in class or approved by the professor.
      
    

Report Format
-------------

All reports will be using the format specified in Section :ref:`reports`.

There will be **NO EXCEPTION** to this format. Documents not following
this format and are not professionally looking, will be returned
without review. The format is the same format that we use for the
technology papers. Some additional information is provided in the
technology paper template.


Github repositories
-------------------

Class homework repository: https://github.com/cloudmesh/sp17-i524



Code Repositories Deliverables
------------------------------

Code repositories are for code, if you have additional libraries or
data that are needed you need to develop a script or use a DevOps
framework to install such software. They **must** not be checked into
github. Thus zip files and .class, .o, precompiled python, .exe, core
dumps, and other such files files are not permissible in the
project. If we find such files you will get a 20% deduction in your
grade. Each project must be reproducible with a simple script. An
example is::

    git clone ....
    make install
    make run
    make view

Which would use a simple make file to install, run, and view the
results. Naturally you can use ansible or shell scripts. It is not
permissible to use GUI based DevOps preinstalled frameworks (such as
the one you may have installed in your company or as part of another
project). Everything must be installable form the command line.
In many cases it is better not to use shell scripts but actually use
the python CMD or even better the CMD5 tools as presented in class


Submission
----------

The project is submitted into github into your project directory. We
will refine this section, but the code must be submitted here. No
compiled code or data is accepted in this directory. We expect you
make weekly pull requests.

If you are working in a team, we will set up a "special project directory"
directory for you, so you need to announce teams on Piazza. A post
will be made to collect the team information.

Woring Alone
^^^^^^^^^^^^

A README.rst file needs to be included that contains the following
information (please be mindfull with the spaces, there is an empty
line between each field. Additional fields may need to be added as the
project proceeds::

  group: no

  project_url: url to the project directory
  
  title: Your Project Title in CamelCase

  author: Firstname Lastname

  HID: your HID

  piazza: your piazza id

  github: your github id

  repository: the link to the report folder

  proposal: report-proposal.pdf

  proposal_submission: mm/dd/2017 hh:mmam

  report: report.pdf

  report_submission: mm/dd/2017 hh:mmam
  
  status: short one line non breaking sentance about where you are (updated weekly)

  dataset_url: url of the dataset, do not store in repo

  deployment: short description of what you deploy

  abstract: a copy of the abstract, make sure to use proper
    indentation in RST format
  
  Bibtex Entry
  ------------

  @TechReport{Project_ID_or_HID-project,
    author = 	  {},
    title = 	  {},
    institution = {Indiana University},
    year = 	  {2017},
    type = 	  {Class Project Report},
    number = 	  {your HID or project id},
    address = 	  {Course I524, Spring 2017},
    month = 	  apr,
    url =         (url of the report.pdf}
  } 
     
  
  
Working in a team
^^^^^^^^^^^^^^^^^^

YOu will need to communicate via Piazza with the TAs that will set up
a repository for you. All github names of all team members will need
to be listed in that request.

Each author has to go to their HID repository and fill out the
README.rst while making sure the values ar set as follows::

  group: yes

  project_url: url to the project directory, that will be assigned to you

AFter the project directory is created, fill out the README.rst, just
as if you do it for a single user, but add in the Author field the
list of authors. Use a comma to separate authors. 

Please note that we create automatically a proceedings from the
README.rst from all students. If you have not filled out the
README.rst we will not be able to see your submission.
