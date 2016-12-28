.. index:: i524
	   
I524 Big Data & Open Source Software Projects
=============================================

Class Material
--------------  
.. toctree::
   :maxdepth: 1

   calendar
   lectures
   technologies


.. graphviz::

   digraph class {
      rankdir="LR";
      node [shape=box,
            style=filled,
            fillcolor=lightgrey];
      "start" [shape=circle];
      "end" [shape=circle];      
      
      "start" -> "Technology";
      "start" -> "Theory" -> "end";
      "start" -> "Web" -> "Paper 1" -> "Paper 2" -> "Paper 3" -> "midterm" -> "end";
      "Theory" -> "Technology" -> "Project";
      "Theory" -> "Web";
      "Theory" -> "Paper 1";
      "Theory" -> "Paper 2";
      "Theory" -> "Paper 3";   
      "Project" -> "end";            
   }
   
Overview
--------

This course studies software used in many commercial activities to
related to Big Data. The backdrop for course relates to more than 300
software subsystems illustrated in Figure 1.

.. figure:: bigdata.png
    :width: 200px
    :align: center
    :alt: 300 Technologies
    :figclass: align-center

    **Figure 1:** Software Systems relevant for Big Data

We will describe the software architecture represented by this
collection and work towards identifying best practices to deploy,
access and interface with them. Topics of this class will include:
 
#. The cloud computing architecture underlying open source big data
   software and frameworks and contrast of them to high performance
   computing

#. The software architecture with its different layers covering broad
   functionality and rationale for each layer.

#. We will go through selected big data stack software from the list
   of more than 300

#. We will be identifying how we can create replicate software
   environments based on software deployed and used on clouds while
   using Containers, OpenStack and ansible playbooks.

#. Students will chose a number of open source members of the list
   each and create repeatable deployments as illustrated in class. 

#. The main activity of the course will be building a significant
   project using multiple subsystems combined with user code and
   data. Projects will be suggested or students can chose their own. A
   project report will summarize the work conducted.
 
Students of this class will need to conduct their project deployments
in python using ansible and enabling a software stack that is useful
for a big data analysis. While it is not necessary to know either
python or ansible to take the class it is important that you have
knowledge of a programming language so you can enhance your knowledge
on them throughout the class and succeed.
 
 
.. note:: For current I523 class participants: While I523 is a
          beginners class I524 is an advanced class and we expect that
          you know python which you hopefully have learned as part of
          I523. If not, make sure you learn it before you take this
          class. If not consider significant additional time needed to
          learn it for the class. You will be expected to have a
          computer on which you have python 2.7.x installed.  You will
          be using chameleon and possibly our local cloud. Optionally
          some projects may use docker. A significant amount of time
          will be spend to familiarize yourself with the technologies
          more so than in I523. You do not have to take I523 in order
          to take I524.
 
.. note:: Residential students need to enroll early so we avoid the
	  situation like last year where we had many signing up, but
	  did not even show up to the first lecture. I have asked that
	  students from I523 have preference, but I am not sure if we
	  can enforce this. So enroll ASAP. Those that are on the
	  waiting list are recommended to show up in the first
	  class. It is likely that you can join as others drop.

Special Example Projects
------------------------

Besides your own projects we have a number of example project
descriptions that you may want to take a look at:

* :ref:`robotswarm`
* :ref:`dockerswarm`
* :ref:`kubernetes`
* :ref:`slurmcluster`
* :ref:`authordisambuigity`
* :ref:`authordisambiguity_b`
  
NIST Big Data Working group examples:
  Any use case from
  http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1500-3.pdf

Selected examples from Fall I523:
   Some students may have created an example as part of I523. Not all
   examples created as part of this class qualify for a I524
   project. Please contact Gregor von Laszewski via Piazza to discuss
   suitability of your previous I523 project. If such a project is
   selected, approved and used it is expected it is significantly
   enhanced.

Cloudmesh Enhancements:
   A number of projects could center around the enhancements of
   cloudmesh for the improvement of big data projects using virtual
   machines and containers.

   
Who can take the class?
-----------------------

* Undergrads can take this class. Make sure you have enough time and
  fulfill the prerequisites such as knowing a programming language
  well and you have enough time to learn python.

* You could take I524 without taking I523, but you must be proficient
  in python and catch up with some of the material in I523 which makes
  the selection of a project easier.

* Online students

* Residential students

Homework
--------

Grading policies are listed in Table 1.

.. list-table:: Table 1: Grading
   :widths: 10 80
   :header-rows: 1

   * - Percent
     - Description                                               
   * - 10%
     - Discussions and contribution to Web pages                 
   * - 30%
     - Three unique technology papers per student of the 300
       systems. Each paper as at least 2 pages per technology without
       references.
   * - 60%
     - Project code and report with at least 6 pages without
       references. Much shorter reports will be returned without
       review. Do not artificially inflate contents. 

* **Project groups:** Groups of up to three students can work on a
  project but workload increases with each student and a work break
  down must be provided.  More than three students are not
  allowed. For a team you will be asked to deploy a larger system or
  demonstrate deployability on multiple clouds while benchmarking it.

* **Technology papers:** Technology papers must be non-overlapping in
  the entire class. If multiple students select the same technology,
  we will be drawing randomly which students does which technology. As
  we have over 300 such technologies we should have enough for the
  entire class. If you see technologies missing, let us know and we
  see how to add them.
  
* **Technology paper groups:** Groups of up to three students can work
  also on the technology papers. However the workload is not reduced,
  you will produce 3 times the number of group members technology
  papers of unique technologies. However, you could be having
  coauthors that are part of your group. Please do not ask us how many
  technology papers you need to write if you are in a group. The rule
  is clearly specified. Example: Your group has 3 members, each of
  them has to procude 3 unique papers, thus you have to produce 9
  unique technology papers for this group. If you have 2 members you
  have to produce 6, if you work alone you have to produce 3.

* **Technology deployment for your project:** Each student will
  develop as part of the project a deployment of a technology. Points
  may depend on effort and simplicity of the deployment.

* **Late homework**: Any late homework will be receiving a 10% grade
  reduction.  As this is a large class and the assignments are not
  standard multiple choice questions, grading will take a considerable
  time. Some homework can not be delivered late as they are related to
  establish communication with you. Such **deadline specific**
  homework will receive 0 points in case they are late. See course
  calendar. It is the student’s responsibility to upload submissions
  well ahead of the deadline to avoid last minute problems with
  network connectivity, browser crashes, cloud issues, etc.

* **Frequent checkins**: It is **important** to make frequent and
  often commits to the github repository as the activities will be
  monitored and will be integrated into the project grade.  Note that
  paper and project will take a considerable amount of time and doing
  proper time management is a must for this class. Avoid starting your
  project late. Procrastination does not pay off.
       
* **No bonus projects:** This class will not have any bonus projects
  or regrading requests. Instead you need to focus your time on the
  papers and the project assignments.

* **Voluntary work:** You are welcome to conduct assignments and
  excerises you find on the class Web page on your own. However they
  are not graded or considered for extra credit.

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

  
Prerequisites
------------

We expect you are familiar with:

* (easy) Linux or the Operating system on which you will focus your
  deployment.
  
* (moderate) Note that Windows as OS will not be sufficient as Ansible
  is not supported on it. However you can use virtualbox or log onto
  one of the clouds to get access to an OS that supports ansible.
  
* (easy) Python 2.7.x (we will not use python 3 for this class as it
  is not yet portable with all systems) (we consider learning python
  as easy, however some students found it challenging)
  
* (easy) pip

* (easy) virtualenv

* (easy) an editor (emacs, vi, jedit, pyCharm, eclipse, or other)
  
If you are not familiar with the technologies, we expect that you get
to know them during class. This may pose additional time commitment. 

Open Source Publication of Homework
-----------------------------------

As this class is about open source technologies, we will be using the
same to gather and distribute the homework submissions.
 
The results of all technology papers will be available as a single big
report. Due to the organization as a single report bound into a book
format of the technologies, all reports must be written in LaTeX and
jabref must be used to manage references. This class will therefore
not accept word, openoffice, and endnote. Alternatively lyx.org can be
used, if you prefer to edit latex in *what you see is almost what you
get* format. The use of sharelatex or overleave is allowed.


.. index:: I524 mistakes

Mistakes
--------

While teaching our classes we noticed the following mistakes students
often make:

* Overestimating the technical abilities
* Underestimating the time it takes to do the project
* Unnecessarily struggling with LaTeX as you do not use an example we
  provide
* Trying to do things on Windows Which is typically more difficult
  than using Linux
* Having a computer that is underpowered or outdated
* **Procrastinating**
* **Take other classes more serious**
* **Starting the project not in the first 4 weeks of the class**
* not listening to the lectures
* Ignoring security via ssh
* Posting passwords into git
* Being not aware that git does **not** allow to easily completely
  delete files that contain secret information such as passwords
* Assume your colleagues does the work, so you get lazy
* Underestimating the **time** it takes to do deployments
* Not reading our piazza posts and repeating the same question over
  and over
* Sending mail to instructors, which will be out of principal deleted
  and not read. Instead you should use piazza
* Not using Piazza to communicate and instead use CANVAS. We will
  be deleting all canvas posts after we have established you can post
  to piazza. Which will be the first week of class.



   
Piazza
------

All communication will be done via Piazza. We will not read any e-mail
send to our university or private e-mails. All instructors are
following this rule. Any mail that is not send via Piazza will be
**not read** and **deleted**. This is also true for any mail send to
the inbox system in CANVAS. We found CANVAS a not scalable solution
for our class and will not use CANVAS for reaching out to you.   If you
need a different mechanism to communicate with us, please ask on Piazza
how to do that.

To sign up in piazza please follow this link:

* https://piazza.com/iu/spring2017/i524


Piazza Folders
^^^^^^^^^^^^^^

Piazza folders allow us to organize some posts into topics. If we need
to introduce a new folder, please discuss and Gregor will approve and
create it if needed. We will not create folders for individual
projects or teams.

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
    
other:
    In case no folder matches for your question use other.

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

  
Meeting Times
-------------

The classes are published online. Residential students at Indiana
University will participate in a discussion taking place at the
following time:

* Fridays 09:30am - 10:45am EST, I2 130

For the 100% online students see the office hours.
   
Software Project
----------------

In case of a software project, we encourage a group project with up to
three members.  You can use the **search teammate** folder to find
and form groups:

* https://piazza.com/class/ix39m27czn5uw?cid=5

The following artifacts are part of the deliverables for a project

Code:
    You must deliver the code in gitlab. The code must be compilable
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
    This document is only needed for team projects. Include in the
    appendix a short but sufficiently detailed work breakdown
    documenting what the team has done. Back it up with commit
    information from github. 

    In addition the graders will go into github/lab, which provides a
    history of checkins to verify each team member has used github/lab to
    checkin their contributions frequently. E.g. if we find that one
    of the students has not checked in code or documentation at all,
    it will be questioned. An oral exam my be scheduled to verify that
    the student has contributed to the project.

License: All projects are developed under an open source license such
    as Apache 2.0 License. You will be required to add a LICENCE.txt
    file and if you use other software identify how it can be reused
    in your project. If your project uses different licenses, please
    add in a README.md file which packages are used and which license
    these packages have while adding a licenses file.

Additional links:
    * :ref:`projects`


Report Format
---------------

All reports will be using the format specified in Section :ref:`reports`.

There will be **NO EXCEPTION** to this format. Documents not following
this format and are not professionally looking, will be returned
without review.




Code Repositories Deliverables
------------------------------

Code repositories are for code, if you have additional libraries that
are needed you need to develop a script or use a DevOps framework to
install such software. Thus zip files and .class, .o files are not
permissible in the project. Each project must be reproducible with a
simple script. An example is::

    git clone ....
    make install
    make run
    make view

Which would use a simple make file to install, run, and view the
results. Naturally you can use ansible or shell scripts. It is not
permissible to use GUI based DevOps preinstalled
frameworks. Everything must be installable form the command line.
      


Online Meetings
---------------

    * **PC, Mac, Linux, iOS or Android:**
        * https://IU.zoom.us/j/534178131?pwd=nebOhW76Q54%3D
        * Password: To be posted in CANVAS
    * **Telephone**:
        * Dial: +1 646 558 8656 (US Toll) or +1 408 638 0968 (US Toll)
        * Meeting ID: 534 178 131 
        * International numbers available:
	  * https://IU.zoom.us/zoomconference?m=xAjpb6jx8gjnut6Q2SW5yPuC09ekuO7H 
    * **H.323/SIP room system**:
        * H.323: 162.255.37.11 (US West) or 162.255.36.11 (US East) 
        * Meeting ID: 534 178 131
        * Password: 520093
    * **SIP:** 534178131@zoomcrc.com
        * Password: 520093



Learning Outcomes
-----------------

Students will gain broad understanding of Big Data applications and
open source technologies supporting them. Students will have intense
programming experience in Pythin and ansible. Students will be able to
communicate their reserach in professional scientific reports.





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
* Nikolov, Dimitar (Teaching Assistant)


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



Links
-------

This page is conveniently managed with git. The location for the
changes can be found at

* https://cloudmesh.github.io/classes/

The repository is at

* https://github.com/cloudmesh/classes

Issues can be submitted at

* https://github.com/cloudmesh/classes/issues

Or better use piazza so you notify us in our discussion lists. If you
detect errors, you could also create a merge request at

* https://piazza.com/iu/i524

	  
	  
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
