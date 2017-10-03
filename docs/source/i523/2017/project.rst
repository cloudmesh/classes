Term Paper or Project
----------------------------------------------------------------------

You have a choice to write a term paper or do a software project. This
will constitute to **60%** of your class grade. You have plenty of
time to make this choice and if you find you struggle with programming
you may want to consider a term paper instead of a project.

In case you chose a project your maximum grade for the entire class
could be an A+. However, an A+ project must be truly outstanding and
include an exceptional project report. Such a project and report will
have the potential quality of being able to be published in a
conference.

In case you chose a Term Paper your maximum grade for the entire class
will be an A-.

Please note that a project includes also writing a project
report/paper. However the length is a bit lower than for a term paper.

Team
^^^^

Software projects and term papers can be conducted with one, two or
three class members.  We do not allow more than three members in a
project. It will be up to you to determine a team, but we recommend
that you chose wisely. Naturally if a team member does not contribute
to the project you need to address this early on. Please do not come
to us a week before the deadline is due and say a team member has not
contributed, this is far to late to do any adjustment to the team. It
is in your responsibility to manage the team.

Common Deleiverables
^^^^^^^^^^^^^^^^^^^^

Both Projects and Term paper have the following common deliverables

Work Breakdown:
    This is an appendix to the document that describes in detail who did what in
    the project. This section comes in a new page after the references. It does not
    count towards the page length of the document. It also includes explicit URLs to
    the the git history that documents the statistics to demonstrate not only one
    student has worked on the project. If you can not provide such a statistic or all
    checkins have been made by a single student, the project has shown that they have
    not properly used git. Thus points will be deducted from the project.
    Furthermore, if we detect that a student has not contributed to a project we may
    invite the student to give a detailed presentation of the project.

Bibliography:
    All bibliography has to be provided in a jabref/bibtex file. This
    is regardless if you use LaTeX or Word. Ther is **NO EXCEPTION**
    to this rule. PLease be advised doing references right takes some
    time so you want to do this early.  Please note that exports of
    Endnote or other bibliography management tools do not lead to
    properly formatted bibtex files, despite they claiming to do
    so. You will have to clean them up and we recommend to do it the
    other way around. Manage your bibliography with jabref, and if you
    like to use it import them to endnote or other tools. Naturally
    you may have to do some cleanup to. If you use LaTeX and jabref,
    you have naturally much less work to do. What you chose is up to
    you.

Report Format:
       All reports will be using the our common format. This format is
       not the same as the ACM format, so if you use systems such as
       overleaf or sharelatex, you need to upload it and use it
       there.

       The format for LaTeX and Word found here:

       * `report.zip <https://github.com/cloudmesh/classes/raw/master/docs/source/format/report.zip>`_

       * `report.tar.gz <https://github.com/cloudmesh/classes/raw/master/docs/source/format/report.tar.gz>`_
                 
There will be **NO EXCEPTION** to this format. In case you are in a
team, you can use either github while collaboratively developing the
LaTeX document or use MicrosoftOne Drive which allows collaborative
editing features. All bibliographical entries must be put into a
bibliography manager such as jabref, endnote, or Mendeley. This will
guarantee that you follow proper citation styles. You can use either
ACM or IEEE reference styles. Your final submission will include the
bibliography file as a separate document.

Documents that do not follow the ACM format and are not accompanied by
references managed with jabref or endnote or are not spell checked
will be returned without review.

More details about the format can be found at

* https://cloudmesh.github.io/classes/lesson/doc/report.html

Software Project
^^^^^^^^^^^^^^^^

Systems Usage
"""""""""""""

Projects may be executed on your local computer, a cloud or other
resources you may have access to. This may include:

* chameleoncloud.org
* furturesystems.org
* AWS (you will be responsible for charges)
* Azure (you will be responsible for charges)
* virtualbox if you have a powerful computer and like to prototype
* other clouds

Deliverables
""""""""""""

The following artifacts are part of the deliverables for a project

Code:
    You must deliver the **source code** in github. The code must be
    compilable and a TA may try to replicate to run your code. You
    MUST avoid lengthy install descriptions and everything must be
    installable from the command line. We will check submission. All
    team members must be responsible for one or all parts of the project.

    Code repositories are for code, if you have additional libraries
    that are needed you need to develop a script or use a DevOps
    framework to install such software. Thus zip files and .class, .o
    files are not permissible in the project. Each project must be
    reproducible with a simple script. An example is::

        git clone ....
        make install
        make run
        make view

    Which would use a simple make file to install, run, and view the
    results. Naturally you can use cmd5 (we teach this in class),
    ansible or shell scripts. It is not permissible to use GUI based
    DevOps preinstalled frameworks. Everything must be installable
    form the command line.

Data:
    If the data is small it can be added into a data directory in github. If you have
    larger data, it should be downloaded from the internet. IT is in your
    responsibility to develop a download program,

Project Report:
    A report must be produced while using the format discussed in the
    Report Format section. The following length is required:

    * 6 pages, one student in the project
    * 8 pages, two students in the project
    * 10 pages, three students in the project
    
License:
    All projects are developed under an open source license such as
    Apache 2.0 License, or similar. You will be required to add a
    LICENCE.txt file and if you use other software identify how it can be
    reused in your project. If your project uses different licenses,
    please add in a README.rst file which packages are used and which
    license these packages have.

Term Paper
^^^^^^^^^^

In case you chose the term paper, you or your team will pick a topic
relevant for the class. You will write a high quality scholarly paper
about this topic. The following artifacts are part of the deliverables
for a term paper. A report must be produced while using the format
discussed in the Report Format section. The following length is
required:

* 9 pages, one student in the project
* 12 pages, two student in the project
* 15 pages, three student in the project



Grading
----------------------------------------------------------------------

Grading for homework will be done within two weeks of the submission
on the due date. For homework that were submitted beyond the due date,
the grading will be done a month after the submission. A 10% grade
reduction will be given for residential students if the project is
late. Some homework can not be delivered late (which will be clearly
marked and 0 points will be given if late; these are mostly related to
setting up your account and communicating to us your account names.)

It is the student’s responsibility to upload submissions well ahead of
the deadline to avoid last minute problems with network connectivity,
browser crashes, cloud issues, etc. It is a very good idea to make
early submissions and then upload updates as the deadline approaches;
we will grade the last submission received before the deadline.

Note that paper and project will take a considerable amount of time
and doing proper time management is a must for this class. Avoid
starting your project late. Procrastination does not pay off. Late
Projects or term papers will receive a 10% grade reduction.

* 15% Paper 1
* 15% Paper 2
* 60% Term Paper or Project
* 10% Participation/Discussion

All other assignments are pass/fail assignments and are geared towards
you being able to explore rather than you being bound by small
assignments.



