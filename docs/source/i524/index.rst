.. index:: i524
	   
I524 Big Data and Open Source Software Projects
===============================================

Class Material
--------------  
.. toctree::
   :maxdepth: 1

   calendar
   lectures
   technologies
   ../changelog
   
Overview
--------

This course studies software used in many commercial activities
related to Big Data. The backdrop for course contains more than 370
software subsystems illustrated in Figure 1.  We will describe the
software architecture represented by this collection and work towards
identifying best practices to deploy, access and interface with
them. Topics of this class will include:

.. sidebar:: Figure 1: Software Systems relevant for Big Data

   .. index:: I524 technology image
	   
   .. figure:: bigdata.png
      :width: 200px
      :align: center
      :alt: 370 Technologies
      :figclass: align-center

 
#. The cloud computing architecture underlying open source big data
   software and frameworks and contrast of them to high performance
   computing

#. The software architecture with its different layers covering broad
   functionality and rationale for each layer.

#. We will go through selected big data stack software from the list
   of more than 370

#. We will be identifying how we can create and replicate software
   environments based on software deployed and used on clouds while
   using Containers, OpenStack and Ansible playbooks.

#. Students will chose a number of open source members of the list
   each and create repeatable deployments as illustrated in class. 

#. The main activity of the course will be building a significant
   project using multiple subsystems combined with user code and
   data. Projects will be suggested or students can chose their own. A
   project report will summarize the work conducted.

#. Topics taught in this class will be very relevant for industry as
   you are not only exposed to big data, but you will also be
   practically exposed to DevOps and collaborative code development
   tools as part of your homework and project assignment.
   
Students of this class will need to conduct their project deployments
in python using ansible and enabling a software stack that is useful
for a big data analysis. While it is not necessary to know either
python or ansible to take the class it is important that you have
knowledge of a programming language so you can enhance your knowledge
on them throughout the class and succeed. You will be expected to have
a computer on which you have python 2.7.x installed.  You will be
using chameleon and possibly our local cloud. Optionally some projects
may use docker. 
 
Figure 2 illustrates that you can follow the components of the class
in a variety of ways and in parallel. For example, you do not have to
wait to start the project or to find out more about any of the
subsystems.

.. graphviz::

   digraph class {
      rankdir="LR";
      compound=true;
      node [shape=box,
            style=filled,
            fillcolor=ivory];

      subgraph cluster_prj {
		"Project Proposal" -> "Project Approval" ->
		"Project Update" -> "Final Project";
		label = "Project";
	}

      subgraph cluster_ppr {
		"Paper 1" -> "Paper 2" -> "Paper 3";
		label = "Technology Papers";
	}

	
      "start" [shape=circle,fillcolor=palegreen];
      "end" [shape=circle,fillcolor=khaki];
      "midterm" [shape=circle,fillcolor=salmon];
      
      "start" -> "Technology";
      "start" -> "Collaboration";
      "start" -> "Systems";
      "start" -> "Theory";
      "start" -> "Web" -> "Paper 1" [lhead=cluster_ppr];
      "Paper 3" -> "midterm" [ltail=cluster_ppr];
      "midterm" -> "end";
      "Theory" -> "Technology" -> "Project Proposal" [lhead=cluster_prj];
      "Collaboration" -> "Project Proposal" [lhead=cluster_prj];
      "Collaboration" -> "Paper 1" [lhead=cluster_ppr];
      "Collaboration" -> "Web";
      "Systems" -> "Project Proposal" [lhead=cluster_prj];
      "Theory" -> "Web";
      "Theory" -> "Paper 1" [lhead=cluster_ppr];
      "Project Update" -> "midterm" [ltail=cluster_prj];
      "Final Project" -> "end" [ltail=cluster_prj];
   }

**Figure 2:** Components of the Class  

.. note:: You do not have to take I523 in order to take I524.
	  
          **For previous I523 class participants:** While I523 is a
          beginners class I524 is a more advanced class and we expect that
          you know python which you hopefully have learned as part of
          I523 while doing a software project. If not, make sure you
          learn it before you take this class or consider
          **significant** additional time needed to learn it for the
          class. 
 
          **Residential students need to enroll early** so we avoid the
	  situation like last year where we had many signing up, but
	  did not even show up to the first lecture. I have asked that
	  students from I523 have preference, but I am not sure if we
	  can enforce this. So enroll ASAP. Those that are on the
	  waiting list are recommended to show up in the first
	  class. It is likely that you can join as others drop.


.. index:: I524 meeting times
    
Meeting Times
-------------

The classes are published online. Residential students at Indiana
University will participate in a discussion taking place at the
following time:

* Monday 09:30am - 10:45am EST, I2 130

For the 100% online students see the office hours.

Online Meetings
---------------

For the zoom information please go to

https://iu.instructure.com/courses/1603897/assignments/syllabus

A doodle was used and all students that answered the doodle have times
that they specified. We covered 100% the time for the students through
the following schedule:

All times are in Eastern Standard Time.

+-----------------+------------------------------------+
| **Day of Week** | **Meetings**                       |
+-----------------+------------------------------------+
| Monday          | | 8-9am Office Hours               |
|                 | | 9:30-10:45am Residential Lecture |
|                 | | 6-7pm Office Hours               |
+-----------------+------------------------------------+
| Tuesday         | | 1-2pm Office Hours               |
|                 | | 4-5pm Office Hours               |
+-----------------+------------------------------------+
| Wednesday       | 6-7pm Office Hours                 |
+-----------------+------------------------------------+
| Thursday        | 6-7pm Office Hours (Gregor)        |
+-----------------+------------------------------------+
| Friday	  | 4-5pm Office Hours                 |
+-----------------+------------------------------------+
| Saturday        | 8-9pm Office Hours                 |
+-----------------+------------------------------------+
| Sunday	  | | 9-10am Office Hours              |
|                 | | 8-9pm Office Hours               |
+-----------------+------------------------------------+
    
Who can take the class?
-----------------------

* Although Undergrads can take this class it will be thaught as
  graduate class. Make sure you have enough time and fulfill the
  prerequisites such as knowing a programming language well. You need
  to have enough time to learn python if you do not know it.

* You can take I524 without taking I523, but you must be proficient
  in python. Overlap between I523 and I524 only relates to some
  introduction lectures and naturally lectures from the systems track
  such as github, report writing, introduction to python.

* Online students

* Residential students

Homework
--------

.. index:: I524 homework

Grading policies are listed in Table 1.

.. list-table:: Table 1: Grading
   :widths: 10 80
   :header-rows: 1

   * - Percent
     - Description                                               
   * - 10%
     - Class participation and contribution to Web pages.
   * - 30%
     - Three unique technology papers per student of the 370
       systems. Each paper as at least 2 pages per technology without
       references.
   * - 60%
     - Project code and report with at least 6 pages without
       references. Much shorter reports will be returned without
       review. Do not artificially inflate contents. 

* **Technology papers:** Technology papers must be non-overlapping in
  the entire class. As we have over 370 such technologies we should
  have enough for the entire class. If you see technologies missing,
  let us know and we see how to add them. Technology papers could be a
  survey of multiple technologies or an indepth analysis of a
  particular technology.
  
* **Technology paper groups:** Groups of up to three students can work
  also on the technology papers. However the workload is not reduced,
  you will produce 3 times the number of group members technology
  papers of unique technologies. However, you can have multiple
  coauthors for each paper (up to thre) that are part of your
  group. Please do not ask us how many technology papers you need to
  write if you are in a group. The rule is clearly specified. Example:
  Your group has 3 members, each of them has to procude 3 unique
  papers, thus you have to produce 9 unique technology papers for this
  group. If you have 2 members you have to produce 6, if you work
  alone you have to produce 3.

* **Technology deployment Homework:** Each student will
  develop as a preparation for the project a deployment of a
  technology. Points may depend on completeness, effort of the
  deployment. Technology deployments should as much as possible be non
  overlapping. In many cases you chose wisely such deployments may
  line up with your technology papers as you can add a section
  reporting on your achievement and experience with such
  deployments.
  
* **Project groups:** Groups of up to three students can work on a
  project but workload increases with each student and a work break
  down must be provided.  More than three students are not allowed. If
  you work in a group you will be asked to deploy a larger system or
  demonstrate deployability on multiple clouds or container frameworks
  while benchmarking and comparing them. A group project containing 2
  or 3 team members shoudl not look like a project done by an
  individual. Please plan careful and make sure all team members
  contribute.

* **Frequent checkins**: It is **important** to make frequent and
  often commits to the github repository as the activities will be
  monitored and will be integrated into the project grade.  Note that
  paper and project will take a considerable amount of time and doing
  proper time management is a must for this class. Avoid starting your
  project late. Procrastination does not pay off.
       
* **No bonus projects:** This class will not have any bonus projects
  or regrading requests. Instead you need to focus your time on the
  papers and the project assignments and homework.

* **Voluntary work:** You are welcome to conduct assignments and
  excerises you find on the class Web page on your own. However they
  are not graded or considered for extra credit.

* **Late homework**: Any late homework will be receiving a 10% grade
  reduction.  As this is a large class and the assignments are not
  standard multiple choice questions, grading will take a considerable
  time. Some homework can not be delivered late as they are related to
  establish communication with you. Such **deadline specific**
  homework will receive 0 points in case they are late. See course
  calendar. It is the student’s responsibility to upload submissions
  well ahead of the deadline to avoid last minute problems with
  network connectivity, browser crashes, cloud issues, etc.
  
* **Chance for publishing a paper:** If however you find that the work
  you do could lead to a publishable paper, you could work together
  with the course instructor as coauthors to conduct such an
  activity. However, this is going to be a significant effort and you
  need to decide if you like to conduct this. In such cases if the
  work is sufficient for publication submission, an A+ for the class
  could be considered. It will be a lot of work. The length of such a
  paper is typically 10-12 high quality pages including figures and
  references. We may elect for the final submission to use a different
  LaTeX style

  

.. _ref-i524-prerequisits:

Prerequisites
-------------

.. index:: I524 prerequisites


We expect you are familiar with:

* Linux and the Operating system on which you will focus your
  deployment.
  
* Note that Windows as OS will not be sufficient as Ansible
  is not supported on it. However you can use virtualbox or log onto
  one of the clouds to get access to an OS that supports ansible. So
  you can use your Windows computer if it is powerful enough.
  
* Python 2.7.x (we will not use python 3 for this class as it
  is not yet portable with all systems) Although python is considered
  to be a straight forward language to learn, students that have not
  done any programming my find it challanging. 
  
* Familaiarity with th Python eco system. The best way to install
  python on a computer is to use virtualenv, and pip (which we will
  teach you as part of the class).

* Familiarity with an editor such as emacs, vi, jedit, pyCharm,
  eclipse, or other that you can use to program in and write your
  reports.
  
If you are not familiar with these technologies, we expect that you
get to know them before or during class. This may pose additional time
commitment.

Open Source Publication of Homework
-----------------------------------

.. index:: I524 report format

As this class is about open source technologies, we will be using such
technologies to gather the homework submissions. We will not be using
CANVAS so we teach you these technologies that are often mandated in
industry. CANVAS is not.

As a consequence all technology papers from all students will be
available as a single big technical report. To achieve this all
reports must be written in the same format. This wil be LaTeX and all
refernces have to be provided a bibtex file while you use jabref.
Alternatively lyx.org can be used, if you prefer to edit
latex in *what you see is almost what you get* format. The use of
sharelatex or overleave or lyx.org is allowed.


.. index:: I524 piazza
	   
Piazza
------

All communication will be done via Piazza. We will not read e-mail
send to our university or private e-mails. All instructors are
following this rule. Any mail that is not send via Piazza will be
**not read** and **deleted**. This is also true for any mail send to
the inbox system in CANVAS. We found CANVAS a not scalable solution
for our class and will not use CANVAS for reaching out to you.   If you
need a different mechanism to communicate with us, please ask on Piazza
how to do that. Please note that private posts in piazza are shared
among all instructors and TAs.

To sign up in piazza please follow this link:

* https://piazza.com/iu/spring2017/i524

We have created a number of piazza folder to organize the posts int
topics.  Thes folders are:

help:
    Our help folder is just like a ticket system that is monitored by
    the TA's. Once you file a question here, a TA will attend to it,
    and work with you. Once the issue you had is resolved, the TA is
    marking it as resolved. If you need to reopen a help message,
    please mark it again as unresolved or post a follow up.

project:
    Questions related to projects are posted here.

logistics:
    Question regarding the logistics of the class are posted
    here. This includes questions about communication, meeting times,
    and other administrative activities.

papers:
    Questions regarding the paper are posted here.    

grading:
    Questions regarding grades are posted here.
    
clouds:
    Questions regarding cloud resources are posted here.
    
faq:
    Some questions will be transformed to FAQ's that we post here.
    Note also that we have an FAQ on the class Web page that you may
    want to visit. We try to move important FAQ's from Piazza into the
    Web page, so it is important that you check both.

meetings: Here we will post times for meetings with TA's and
    instructors that are not yet posted on the Web page as part of the
    regular meeting times. Class participants are allowed to attend
    any Zoom meeting that we annonce in this folder. For online
    students we will also determine a time for regulare meetings. The
    TAs are required to hold 10 hours of meeting times upon request
    with you. Please make use of this.

    
other:
    In case no folder matches for your question use other.

    
.. index:: I524 tips

Tips on how to achieve your best
--------------------------------

While teaching our classes we noticed the following tips to achieve
your best:

* Listening to the lectures
* **Set aside enough undisturbed time for the class**. Switch off
  facebook, twitter, or other distracting social media systems when
  focussing on the class.
* **Ask for help**. The TAs can schedule custom help office hours on
  appointment during reasonable times.
* Do not **Procrastinate**.
* Do not **take your other classes more serious**.
* **Start the project in the first 4 weeks of the class**
* Be aware that this class is not based on a text book and what this
  implies. 
* Do not overestimating the technical abilities.
* Do not underestimating the time it takes to do the project.
* Do not forget to include benchmarks in your project.
* Unnecessarily struggling with LaTeX as you do not use an example we
  provide.
* Trying to do things just on Windows which is typically more difficult
  than using Linux.
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
* Use Piazza to communicate and not CANVAS or e-mail.
* When you receive an e-mail from piazza, reply to it while clicking
  on the link instead of replying via e-mail directly. This is more
  reliable.

   
Submissions
-----------

Your papers and projects will be developed on GitHub and submitted
using :doc:`Pull Requests <../lesson/prg/pull_requests>`.  The process
is as follows:

#. fork the `sp17-i524 <https://github.com/cloudmesh/sp17-i524>`_ repository.
#. clone your fork and commit and push your changes.
#. submit a pull request to the master branch of the origin repository.

See the repository for details on the individual assignments. As it
will periodically be updated, make sure you are familiar with the
process of `Syncing a fork
<https://help.github.com/articles/syncing-a-fork/>`_.

Some things to keep in mind:

* space on github is limited, so do not add datasets to the
  repository. Any datasets you use should be publicly hosted and
  deployed as part of your project ansible deployment scripts.
* never add ssh private keys to the repository. This results in a
  security risk, possible point deductions, and lots of time and
  effort to fix.
* all work will be licensed under the Apache 2 open source license.
* all submissions and discussion will be visible to the world.

.. index:: I524 project ideas
	   
Selected Project Ideas
------------------------------
	   
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

  
  
Software Project
----------------

For a software project you have the choice of working indifidualy or
working in a team of up to three students. You can use the **search
teammate** folder to find and form groups:

* https://piazza.com/class/ix39m27czn5uw?cid=5

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

Work Breakdown: The report contains in an appendix a section that is
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

License: All projects are developed under an open source license such
    as Apache 2.0 License. You will be required to add a LICENCE.txt
    file and if you use other software identify how it can be reused
    in your project. If your project uses different licenses, please
    add in a README.md file which packages are used and which license
    these packages have while adding a licenses file.

Additional links:
    * :ref:`projects`

Reproducability: The reproducability of your code will be tested
    twice. It is tetes by another student or team, it is also tested
    by a TA. A report of the testing team is provided. Your team will
    also be responsible for executing as many tests as you have team
    members on other projects. A reproducability statement should be
    written with details about functionality, readbility, and report
    quality. This statement does not have to be written in latex but
    uses RST.
      

Report Format
---------------

All reports will be using the format specified in Section :ref:`reports`.

There will be **NO EXCEPTION** to this format. Documents not following
this format and are not professionally looking, will be returned
without review.

Github repositories
--------------------

Class content repository: https://github.com/cloudmesh/classes

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
      


Learning Outcomes
-----------------

Students will

1. gain broad understanding of Big Data applications and open source
   technologies supporting them.

2. have intense programming experience in Python and ansible and DevOps.

3. use open source technologies to manage code in large groups of
   individuals.

4. be able to communicate reserach in professional scientific reports.


Outcome 1 is supported by a series of lectures around open source
technologies for big data.

Outcome 2 is supported by a significant software project that will
take up a considerable amount of time to plan and execute.

Outcome 1 and 4 is supported by writing 3 technology papers and a project
report that is shared with all students. Students can gain additional
insight from reading and reviewing other students contributions.

Outcome 3 is supported by using piazza and github as well as
contributiong to the class Web page with git pull requests.



Academic Integrity Policy
----------------------------------------------------------------------

We take academic integrity very seriously. You are required to abide
by the Indiana University policy on academic integrity, as described
in the Code of Student Rights, Responsibilities, and Conduct, as well
as the Computer Science Statement on Academic Integrity
(http://www.soic.indiana.edu/doc/graduate/graduate-forms/Academic-Integrity-Guideline-FINAL-2015.pdf). It
is your responsibility to understand these policies. Briefly
summarized, the work you submit for course assignments, projects,
quizzes, and exams must be your own or that of your group, if group
work is permitted. You may use the ideas of others but you must give
proper credit. You may discuss assignments with other students but you
must acknowledge them in the reference section according to scholarly
citation rules. Please also make sure that you know how to not
plagiarize text from other sources while reviewing citation rules.

We will respond to acts of plagiarism and academic misconduct
according to university policy. Sanctions typically involve a grade of
0 for the assignment in question and/or a grade of F in the course. In
addition, University policy requires us to report the incident to the
Dean of Students, who may apply additional sanctions, including
expulsion from the university.

Students agree that by taking this course, papers and source code
submitted to us may be subject to textual similarity review, for
example by Turnitin.com. These submissions may be included as source
documents in reference databases for the purpose of detecting
plagiarism of such papers or codes.

It is not acceptable to use for pay services to conduct your project. 
Please be aware that we monitor such services and have TAs speaking
various languages and know about these services even in different
countries. Also do not just translate a report written by someone in a
different language and claim it to be your project.

Instructors
------------

The course presents lectures in online form given by the instructors
listed bellow. Many others have helped making this material available
and may not be listed here. For this class support is provided by

* Gregor von Laszewski (PhD)
* Badi' Abdul-Wahid (PhD)
* Jerome Mitchell (Teaching Assistant)
* Miao Zhang (Teaching Assistant)
* Tony Liu (Teaching Assistant)
* Vibhatha Abeykoon (Teaching Assistant)
* Dimitar Nikolov (Teaching Assistant)  


Dr. Gregor von Laszewski
^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /images/gregor2.png

Gregor von Laszewski is an Assistant Director of Cloud Computing in
the DSC. His is also an Adj. Assoc. Professor of the Intelligent
Systems Engineering Department at Indiana University. He held a
position at Argonne National Laboratory from Nov. 1996 – Aug.  2009
where he was last a scientist and a fellow of the Computation
Institute at University of Chicago. During the last two years of that
appointment he was on sabbatical and held a position as Associate
Professor and the Director of a Lab at Rochester Institute of
Technology focussing on Cyberinfrastructure. He received a Masters
Degree in 1990 from the University of Bonn, Germany, and a Ph.D. in
1996 from Syracuse University in computer science. He was involved in
Grid computing since the term was coined. He was the lead of the Java
Commodity Grid Kit (http://www.cogkit.org) which provides till today a
basis for many Grid related projects including the Globus
toolkit. Current research interests are in the areas of Cloud
computing. He is leading the effort to develop a simple IaaS client
available at as OpenSource project at
http://cloudmesh.github.io/client/

His Web page is located at http://gregor.cyberaide.org. To contact him
please send mail to laszewski@gmail.com. For class related e-mail
please use Piazza for this class.

In his free time he teaches Lego Robotics to high school students. In 2015
the team won the 2nd prize in programming design in Indiana. If you like
to volunteer helping in this effort please contact him.

He offers also the opportunity to work with him on interesting
independent studies. Current topics include but are not limited to

* cloudmesh
* big data for NIST
* big data benchmarking.
* scientific impact of supercomputer and data centers.
* STEM and other educational activities while using robotics or big data
   
Please contact me if you are interested in this.

Dr. Geoffrey C. Fox
^^^^^^^^^^^^^^^^^^^

.. image:: /images/gcf.jpg

Greoffrey C. Fox received a Ph.D. in Theoretical Physics from Cambridge University
and is now distinguished professor of Informatics and Computing, and
Physics at Indiana University where he is director of the Digital
Science Center, Chair of Department of Intelligent Systems Engineering
and Director of the Data Science program at the School of Informatics
and Computing.  He previously held positions at Caltech, Syracuse
University and Florida State University after being a postdoc at the
Institute of Advanced Study at Princeton, Lawrence Berkeley Laboratory
and Peterhouse College Cambridge. He has supervised the PhD of 68
students and published around 1200 papers in physics and computer
science with an index of 70 and over 26000 citations.  He currently
works in applying computer science from infrastructure to analytics in
Biology, Pathology, Sensor Clouds, Earthquake and Ice-sheet Science,
Image processing, Deep Learning, Manufacturing, Network Science and
Particle Physics. The infrastructure work is built around Software
Defined Systems on Clouds and Clusters. The analytics focuses on
scalable parallelism.

He is involved in several projects to enhance the capabilities of
Minority Serving Institutions. He has experience in online education
and its use in MOOCs for areas like Data and Computational Science. He
is a Fellow of APS (Physics) and ACM (Computing).


Dr. Badi' Abdul-Wahid
^^^^^^^^^^^^^^^^^^^^^

.. image:: /images/badi.png

Badi' received a Ph.D. in Computer Science at the University of Notre
Dame under Professor Jesus Izaguirre. The primary focus of his
graduate work was the development of scalable, fault-tolerant, elastic
distributed applications for running Molecular Dynamics simulations.

At Indiana University, Badi' works with the FutureSystems project
on a NIST-funded study whose goal is to understand patterns in the
development and usage of Big Data Analysis pipelines.


Teaching Assistants
-------------------

Jerome Mitchell
^^^^^^^^^^^^^^^

.. image:: /images/jerome.png

**Jerome Mitchell** is a Ph.D candidate in computer science at Indiana
University and is interested in coupling the fields of computer and
polar science. He has participated in the United State Antarctic
Program, (USAP), where he collaborated with a multidisciplinary team
of engineers and scientists to design a mobile robot for harsh polar
environments to autonomously collect ice sheet data, decrease the
human footprint of polar expeditions, and enhance measurement
precision. His current work include: using machine learning techniques
to help polar scientists identify bedrock and internal layers in radar
imagery. He has also been involved in facilitating workshops to
educate faculty and students on the importance of parallel and
distributed computing at minority-serving institutions.




Dimitar Nikolov
^^^^^^^^^^^^^^^
.. image:: /images/dimitar.png
	   
**Dimitar Nikolov** is a PhD student in the Computer Science program at
Indiana University since August 2008. His research interests include
online social networks, tagging systems and web mining. As part of his
PhD he conducts research with the NaN group, led by Professor Fil
Menczer. His thesis topic is TBD.


Vibhatha Abeykoon
^^^^^^^^^^^^^^^^^
.. image:: /images/vb.png
     
**Vibhatha Abeykoon** is a PhD student in the Intelligent Systems Engineering program at
Indiana University since August 2016. His research interests include
machine learning, singal processing, source seperation, deep learning, big data and distributed systems. As part of his
PhD he conducts research with Professor Geoffrey C. Fox and Assistant Professor Minje Kim. His thesis topic is TBD.


Miao Zhang
^^^^^^^^^^
.. image:: /images/miao100px.jpg
     
**Miao Zhang** PhD student working primarily on computer network related stuff.
Currently focuses on network performance monitoring and forecasting.

Tony Liu
^^^^^^^^
.. image:: /images/tony.png

**Tony Liu** is a PhD student in the Intelligent Systems Engineering program at Indiana University since August 2016. He received his Master degree in Computer Science program in May 2016 at IU. His research interests are high performance computing, computer systems and computer architecture. He used to work under Professor Thomas Sterling and Professor Andrew Lumsdaine from Center for Research in Extreme Scale Technology (CREST) on HPX-5 runtime system project. His currently works on benchmarking Intel Xeon Phi Knights Landing processor with Caffe under Professor Judy Qiu and Professor Lei Jiang.

Links
-------

This page is conveniently managed with git. The location for the
changes can be found at

* https://cloudmesh.github.io/classes/

The repository is at

* https://github.com/cloudmesh/classes

Issues can be submitted at

* https://github.com/cloudmesh/classes/issues

Or better use piazza so you notify us in our discussion lists.

* https://piazza.com/iu/i524

If you detect errors, you could also create a merge request at

* https://github.com/cloudmesh/classes


	  
Course Numbers
--------------

This course is offered for Graduate (and Undergraduate students with
permission) at Indiana University and as an online course. To
Register, for University credit please go to:

* http://registrar.indiana.edu/browser/soc4172/INFO/INFO-I524.shtml
* http://registrar.indiana.edu/browser/soc4172/ENGR/ENGR-E599.shtml


Please, select the course that is most suitable for your program:

.. code-block:: none
   
    INFO-I 524  BIG DATA SOFTWARE AND PROJECTS (3 CR)    Von Laszewski G          
             Above class open to graduates only
             Above class taught online
             Discussion (DIS)
          30672 RSTR     09:30A-10:45A   M      I2 130    Von Laszewski G          
             Above class meets with ENGR-E 599
    INFO-I 524  BIG DATA SOFTWARE AND PROJECTS (3 CR)
          30673 RSTR     ARR             ARR    ARR       Von Laszewski G          
             Above class open to graduates only
             This is a 100% online class taught by IU Bloomington. No
             on-campus class meetings are required. A distance education
             fee may apply; check your campus bursar website for more
             information

     ENGR-E 599  TOPICS IN INTELL SYS ENGINEER (3 CR)
           VT: BIG DATA SOFTWARE AND PROJECTS
              ***** RSTR     ARR             ARR    ARR       Von Laszewski G          
                 Discussion (DIS)
           VT: BIG DATA SOFTWARE AND PROJECTS
              33924 RSTR     09:30A-10:45A   M      I2 130    Von Laszewski G 
                 Above class meets with INFO-I 524



		 
Refernces
---------

http://hpc-abds.org/kaleidoscope/ 


Disclaimer
----------

It is normal that questions posed by the students in the
online and residential classes lead to improvements and clarifications
of the content published on the class Web pages. Hence you need to
revisit the page updates. Just as in other years we provide a
changelog. Changes will not lead to any requirements change to the class
but only improving the content. However, we have learned from previous
classes that additional homework may need to be added in case the
class participants need to grasp a concept better or simplify their
work.

We have two ways of providing content to the class:

a) we release content only on weekly basis

b) we release content even in draft form

We decided to do the later so you may have the ability to see what is
comming up. Please do not mistake this as a changing requirement. This
is an opportunity for you. You are not required to look at lectures or
assignments that are not yet released for this class.

