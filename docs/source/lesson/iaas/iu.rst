


IU SOIC machines
================

.. warning:: the current python version on these machines are outdated
	     and are not suitable for programming use.
	     However they can be used toe create LaTex documents.

Machine information from IU SOIC is published at this Web page:

* https://uisapp2.iu.edu/confluence-prd/pages/viewpage.action?pageId=114491559

It is important to vist this page to look at the Tips before you send
questions to us or the Help Desk.

If your computer is not powerful enough you probably can log into one
of these machines to do LaTeX and other software for classes. In case
of python you will have to make sure you have the right version. YOu
can send a Help message to the Help Desk.

* https://uisapp2.iu.edu/confluence-prd/pages/viewpage.action?pageId=90899794

If you find a solution the works for you let us know so we add it to
this page.




Burrow:
  burrow.soic.indiana.edu
  The Burrow systems are available to all SoIC faculty, staff, and
  students (both graduate and undergraduate students in CS or
  Informatics) as well as non-SoIC students who are taking CS or
  Informatics classes requiring use of these systems. Accounts are
  created automatically for all SoIC graduate students and for
  undergraduate students taking certain SoIC classes. If you are a
  faculty, staff, or undergraduate student in the CS or Informatics
  program and do not already have a Burrow account, you can request an
  account using the Help Desk. Note that account requests for non-SoIC
  students should come from the instructor of the class using these
  systems.

Sharks:
  sharks.soic.indiana.edu
  The Sharks systems are available to all SoIC faculty, staff, and
  graduate students (CS and Informatics). Access can also be granted to
  undergraduate and non-SoIC students and guests with sponsorship by a
  member of the SoIC faculty. Accounts are created automatically for all
  SoIC graduate students (CS and Informatics). Accounts for other users
  can be created by having the faculty sponsor make the account request
  using the Help Desk.


Login
-----

To login, please use::

  ssh albert@burrow.soic.indiana.edu

You will than see womething like this:

  The authenticity of host 'burrow.soic.indiana.edu (129.X.X.X)' can't be established.
  ECDSA key fingerprint is SHA256kjshlkjhxkljhaBKCJSDHFJKSHFKJhb.
  Are you sure you want to continue connecting (yes/no)? yes
  Warning: Permanently added 'burrow.soic.indiana.edu,129.X.X.X' (ECDSA) to the list of known hosts.
  albert@burrow.soic.indiana.edu's password: 

  *******************************************************************
  **   Indiana University School of Informatics and Computing      **
  **             ** For Authorized Use Only **                     **
  *******************************************************************
  **  For general SoIC computing information, please see:          **
  **      http://help.soic.indiana.edu/                            **
  **                                                               **
  **  To submit a problem report or question, please see:          **
  **      http://help.soic.indiana.edu/request                     **
  *******************************************************************


  [albert@silo ~]$ 

LaTeX
-----

when you prope for LaTeX you can see it is already installed::

  [albert@silo ~]$ which latex
  /usr/bin/latex
  [albert@silo ~]$ which pdflatex
  /usr/bin/pdflatex
