
Disclosure
----------

This page may be updated througout Fall 2016, we recommend to review
this page weekly for changes.

About the Course
-----------------

http://openedx.scholargrid.org/courses/SoIC/INFO-I-523/Fall_2016/about

The Big Data Applications and Analytics course is an overview course in
Data Science and covers the applications and technologies (data
analytics and clouds) needed to process the application data. It is
organized around rallying cry: Use Clouds running Data Analytics
Collaboratively processing Big Data to solve problems in X-Informatics.

Course Numbers
--------------

This course is offered for Graduate and Undergraduate Students at
Indiana University and as pure online course. To Register, for
University credit please go to:

* http://registrar.indiana.edu/browser/soc4168/INFO/INFO-I523.shtml

.. todo:: Jerome. Put table of course numbers here with columns
   	  coursenumber, title, description. where description
   	  indicates what this is for.

Meeting Times and Office Hours
--------------------------------

The classes are published online. Residential students at Indiana
University will participate in a discussion taking place Fridays
09:30A-10:45A. For the 100% online students a time will be determined.


Office Hours
~~~~~~~~~~~~

.. todo:: Gregor. clenup this secion

Office hours will be held every week. These are live sessions that
will allow you to interact one-on-one or in groups with either an
instructor ow a TA. During these times, we can be reached via zoom at
the following URL.

.. todo:: Gregor. put link here

Office hours sessions may be recorded.

Special Sessions
~~~~~~~~~~~~~~~~

Special Online sections with Instructors:

Time: 26th September, 2016 @ 1 pm US Eastern Time (Time may change)

We will be using Zoom for online sessions with the following URL

.. todo:: Gregor. set zoom url for discussion URL for online session: TBD.


Calendar
---------

.. todo:: Prashanth. add a calendar here with when what takes place on a weekly basis

+------------+-------+------------------------------------------+
| Date       | Week  | Sessions | Descriptions                  |
+------------+-------+------------------------------------------+
| mm/dd/2016 | 1     | urls     | Introduction                  |
+------------+-------+------------------------------------------+

first day
last day
due data projects
due date papers

class calendar

date week lecture discussion date

put details here

Email
----------------------------------------------------------------------

..todo:: Gregor. cleanup

You can expect a reply from someone on the course staff within 24
hours; if you do not receive one, please re-send your email. If you
are writing with questions about the assignments or course material,
please ask on the Discussion Forums so that other students can benefit
from the discussion. For sensitive personal matters, feel free to
email the instructors directly (laszewski@gmail.com).

* https://groups.google.com/forum/#!forum/big-data-iu-fall-2016-help

  For general help to contact instructors and TAs. This mailinglist is
  shared with all TAs, Dr. von Laszewski, and Dr. Abduhl-Wahid

* https://groups.google.com/forum/#!forum/big-data-iu-fall-2016-announce

  Class announcements will be send here

* https://groups.google.com/forum/#!forum/bigdata-iu-fall-2016

  This is an open mailing list students, TAs, Dr. von Laszewski, and
  Dr. Abduhl-Wahi.

.. todo:: look at piazza as alternative

Getting Access and Systems Support
----------------------------------------------------------------------

For some cases you will need accee to a cloud. We recommend you
evaluate which cloud would be most appropriate for your project. This
includes:

* chameleoncloud.org
* furturesystems.org
* AWS (you will be responsible for charges)
* Azure (you will be responsible for charges)
* virtualbox if you have a powerful computer and like to prototype
* other clouds

Systems staff is available only during regular buisiness hours Mo-Fri 10am - 4pm.

We will have a Section in the class material about these resources.

.. todo:: Hyungro. add the link to the section and prepare this section.

You could also use the cloudmesh client software on Linux and OSX to
access multiple clouds in easy fashion. A Section will introduce this
software.



Term Paper or Project
----------------------------------------------------------------------

You have a choice to write a term paper or do a software project using
our cloud computing test bed.

In case of a software project, we encourage a group project with up to three members.

You can use the discusson TBD  to form project teams or just communicate
privately with other classmembers to formulate a team.

.. todo:: include a link to the dicussion for formulating projects.

The following artifacts are part of the deliverabels

.. todo:: Hyungro. include paper/report length requirement as RST table

This needs also to be provided for Papers that are written in a team.



Report Format
---------------



All reports will be using the ACM pubform format. The Word template
can be found here:

* :download:`paper-report.docx <files/paper-report.docx>`

A LaTeX version can be found at

* https://www.acm.org/publications/proceedings-template

however you have to remove the copyright notice.

There will be **NO EXEPTION** to this format. In case you are in a
team, you can use either github while collaboratively developing the
LaTeX document or use MicrosoftOne Drive which allows collaborative
editing features. All bibliographical entries must be put into a
bibliography manager such as jabref, endnote, or Mendeley. This will
gurantee that you follow proper citation styles. You can use either
ACM or IEEE refernce styles. YOur final submission will include the
bibligraphy file as a separte document.

Documents that do not follow the ACM format and are not accomponied by
refrences managed with jabref or endnote will be returned without
review.

Report Checklist:

* [ ] Have you written the report in word or LaTeX in the specified
  format
* [ ] In case of LaTeX, have you removed the ACM copyright information
* [ ] Have you included the report in gitlab
* [ ] Have you specified tha names and e-mails of all team members in
  your report.
* [ ] have you included all images in native and PDF format in gitlab
  in the images folder
* [ ] have you added the bibligraphy file (such as endnote or bibtex
  file e.g. jabref) in a directory bib
* [ ] have you submitted an additional page that describes who did
  what in the project or report.


Code repositories Deliverables
------------------------------

Code repositories are for code, if you have additional libraries that are needed you need to develop a script or use a DeVOps framework to install such software. Thus zip files and .class, .o files are not permissable in the project. Ech project must be reproducable with a simple script. An example is

    git clone ....
    make install
    make run
    make view

Which would use a simple make file to install, run, and view the results. Naturally you can use ansible or shell scripts. It is not permissible to use GUI based DevOps preinstalled frameworks. Everything must be installable form the command line.


Office Hours
----------------------------------------------------------------------

Office hours will be held every week. These are live sessions that
will allow you to interact one-on-one or in groups with either an
instructor ow a TA. During these times, we can be reached via a ZOOM
link. Office hours are Tue, Thu 10-11am.


Requirements
------------

Python or Java experience (programming load is modest). Optionally: In
case you are interested in further development of cloudmesh for big
data strong Python or JavaScript experience is needed.

Prerequisites
----------------------------------------------------------------------

In case you elect a programming project we will assume that you are
familiar with the programming languages required as part of the
project you suggest. We will limit the languages to Python, Java, and
JavaScript.  If you do not know the required technologies, we will
expect you to learn it outside of class. For example, Python has a
reputation for being easy to learn, and those with strong programming
background in another general-purpose programming language (like
C/C++, Java, Ruby, etc.) can learn it within a few days. Please
consult the instructor if you have concerns about your programming
background. In addition, we may encounter math of various kinds,
including linear 1 algebra, probability theory, and basic calculus. We
students with limited math backgrounds may need to do additional
reading outside of class.

Learning Outcomes
-----------------

Students will gain broad understanding of Big Data application areas and
approaches used. This course is a good preparation for any student
likely to be involved with Big Data in their future.


Grading
----------------------------------------------------------------------

Grading for homeworks will be done within a week for submission on due
date. For homeworks that were submitted beyond the due date, the grading
will be done within 2-3 weeks after the submission. Some homework can
not be delivered late and a 10% grade reduction will be given. We will
be clearly mark such mandatory deadlines.

 It is the student’s responsibility to upload submissions well ahead
 of the deadline to avoid last minute problems with network
 connectivity, browser crashes, etc. It is a very good idea to make
 early submissions and then upload updates as the deadline approaches;
 we will grade the last submission received before the deadline.

Licensing
---------

All projects are developed under an open source license such as Apache
2.0 License, or similar. You will be required to add a License file
and if you use other software identify how it can be reused in your
project.

Academic Integrity Policy
----------------------------------------------------------------------

We take academic integrity very seriously. You are required to abide
by the Indiana University policy on academic integrity, as described
in the Code of Student Rights, Responsibilities, and Conduct, as well
as the Computer Science Statement on Academic Integrity
(http://www.soic.indiana.edu/doc/graduate/graduate-forms/Academic-Integrity-Guideline-FINAL-2015.pdf). It
is your responsibility to understand these policies. Briefly
summarized, the work you submit for course assignments, projects,
quizzes, and exams must be your own or that of your group, if
groupwork is permitted. You may use the ideas of others but you must
give proper credit. You may discuss assignments with other students
but you must acknowledge them in the refrence section according to
scholarly citation rules. Please also make sure that you know how to
not plagerise text from other sources while reviewing citation rules.

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



Instructors
------------


Gregor von Laszewski
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/gregor2.png

Gregor von Laszewski is an Assistant Director of Cloud Computing in the
DSC. He held a position at Argonne National Laboratory from Nov. 1996 – Aug.
2009 where he was last a scientist and a fellow of the Computation
Institute at University of Chicago. During the last two years of that
appointment he was on sabbatical and held a position as Associate
Professor and the Director of a Lab at Rochester Institute of Technology
focussing on Cyberinfrastructure. He received a Masters Degree in 1990
from the University of Bonn, Germany, and a Ph.D. in 1996 from Syracuse
University in computer science. He was involved in Grid computing since
the term was coined. He was the lead of the Java Commodity Grid Kit
(http://www.cogkit.org) which provides till today a basis for many Grid
related projects including the Globus toolkit. Current research
interests are in the areas of Cloud computing. He is leading the effort
to develop a simple IaaS client available at as OpenSource project at
http://cloudmesh.github.io/client/

His Web page is located at http://gregor.cyberaide.org. To contact him
please send mail to laszewski@gmail.com. For class related e-mail please use the
goouple group
https://groups.google.com/forum/#!forum/big-data-iu-fall-2016-help,
which is shared between all instructors and AIs.

In his freetime he teaches Lego Robotics to highschool students. In 2015
the team won the 1st prize in programming design in Indiana. If you like
to volunteer helping in this effort please contact him.

He offers also the opportunity to work with him on interesting
independent studies. Current topics include cloudmesh, big data
benchmarking, scientific impact of supercomputer and data centers.


Dr. Geoffrey Fox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/gcf.jpg

Fox received a Ph.D. in Theoretical Physics from Cambridge University
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


Badi Abduhl-Whadi
~~~~~~~~~~~~~~~~

.. todo:: add picture and paragraph

Teaching Assistants
-------------------

Hyungro Lee
~~~~~~~~~~~

.. image:: images/Hyungro.jpg


Hyungro Lee is a PhD candidate in Computer Science at Indiana University
working with Dr. Geoffrey C. Fox. Prior to beginning the PhD program,
Hyungro worked as a software engineer in the Cyworld Group (social
networking platform in South Korea) at SK Communications, developing
communications platforms including emails, texts and messaging at large
scale to support over 40 million users. From this work he developed an
interest in how distributed systems achieve scalability and high
availability along with managing resources efficiently. He is currently
working on the Futuresystems project to support Big Data Analysis
Software Stacks in Virtual Clusters. He was also working on the
FutureGrid project, an NSF funded significant new experimental computing
grid and cloud test-bed to the research community, together with user
supports. His research interests are parallel and distributed systems,
and cloud computing


Jerome Mitchell
~~~~~~~~~~~~~~~~~~~~~~

.. todo:: Jerome. add picture and paragraph 100x100px

Prashanth Balasubramani
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/Prashanth.jpg

Prashanth Balasubramani is an MS student in Computer Science at Indiana
University working with Gregor von Laszewski, Assistant Director of Cloud
Computing at DSC. He has been working under Professor Gregor and Dr.Geoffrey Fox
for the past year as an Associate Instructor for the course Big Data Analytics
and Applications during the Fall 2015 and Spring 2016 semesters. Before joining
Indiana University, he worked as a ETL developer for Capital One Banking firm
(Wipro Technologies, Bangalore) developing Hadoop MR and Spark jobs for real
time migration of Historical Data into virtual clusters on the Cloud. He is
currently working as an Teaching Assistant for the Big Data Applications and
Analytics course for the Fall 2016 semester. He is also working on NIST
benchmarking project for recording benchmarks on different cloud platforms
His research interests include Big Data applications, Cloud computing and
Data Warehousing.
