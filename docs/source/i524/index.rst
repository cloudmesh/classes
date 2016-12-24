.. index:: i524
	   
I524 Big Data & Open Source Software Projects
=============================================

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

#. Students will chose one other open source member of Kaleidoscope
   each and deploy as illustrated in class.

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
 
 
.. note:: A note to current I523 class participants: While I523 is a
          beginners class I524 is an advanced class and we expect that
          you know python which you hopefully have learned as part of
          I523. If not, make sure you learn it before you take this
          class. If not consider significant additional time needed
          for that class. You will be expected to have a computer on
          which you have python installed.  You will be using
          chameleon and possibly our local cloud. Optionally some
          projects may use docker. A significant amount of time will
          be spend to familiarize yourself with the technologies more
          so than in I523.
 
.. note:: Residential students enroll early so we avoid the situation
	  like last year where we had many signing up, but did not
	  even show up to the first lecture. I have asked that
	  students from I523 have preference, but I am not sure if we
	  can enforce this. So enroll ASAP.

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

Grading pilicies are listed in Table 1.

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
       refences.
   * - 60%
     - Project code and report with at least 6 pages without
       references. Much shorter reports will be returned without
       review. Do not artifically inflate contents. 

  
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

* **No bonus projects:** This class will not have any bonus projects
  or regrading requests. Instead you need to focus your time on the
  papers and the project assignments.

* **Voluntary work:** You are welcome to conduct assignments and
  excerises you find on the class Web page on your own. However they
  are not graded or considered for extra credit.

* **Chance for publishing a paper:** If however you find that the work
  you do could lead to a publishable paper, you could work together
  with the course instructor as coauthors to conduct such an
  activity. However, this is goind to be a significant effort and you
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

Class Material
  
.. toctree::
   :maxdepth: 1

   calendar
   lectures
   technologies


   
Piazza
------

All communication will be done via Piazza. We will not read any e-mail
send to our university or private e-mails. All instructurs are
following this rule. Any mail that is not send via PIazza will be
**not read** and **deleted**. This is also true for any mail send to
the inbox system in CANVAS. We found CANVAS a not scalable solution
for our class and will not use CANVAS for reaching out to you.   If you
need a different mechnism to communicate with us, please ask on PIazza
how to do that.

To sign up in piazza please follow this link:

* https://piazza.com/iu/spring2017/i524

* https://piazza.com/class/ix39m27czn5uw

Piazza Folders
^^^^^^^^^^^^^^

Piazza folders allow us to organize some posts into topics. If we need
to introduce a new folder, please discuss and Gregor will approve and
create it if needed. We will not create folders for individual
projects or teams.

help:
    Our help folder is just like a ticket system that is monitored by
    the TA's. Once you file a question here, a TA will attend to it,
    and work with you. ONce the issue you had is resolved, the TA is
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
three members.  You can use the
`discussion forum in the folder project <https://piazza.com/class/irqfvh1ctrg2vt>`_
to form project teams or just communicate privately with other class
members to formulate a team. The following artifacts are part of the
deliverables for a project

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
    This document is only needed for team projects. A one page PDF
    document describing who did what. It includes pointers to
    the git history that documents the statistics that demonstrate not
    only one student has worked on the project.

    In addition the graders will go into gitlab, which provides a
    history of checkins to verify each team member has used gitlab to
    checkin their contributions frequently. E.g. if we find that one
    of the students has not checked in code or documentation at all,
    it will be questioned.

License:
    All projects are developed under an open source license such as
    Apache 2.0 License, or similar. You will be required to add a
    LICENCE.txt file and if you use other software identify how it can be
    reused in your project. If your project uses different licenses,
    please add in a README.rst file which packages are used and which
    license these packages have.

Additional links:
    * :ref:`projects`


Report Format
---------------

All reports will be using the format specified in Section reports_.

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
