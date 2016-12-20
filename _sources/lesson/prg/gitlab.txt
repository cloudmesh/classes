
Using GitLab
======================================================================

In case your course the use of `GitLab.com <https://gitlab.com/>`_
for your homework submissions this information will help you to get stated.

Once you have completed the entry survey you will be granted access to
a gitlab repository in which to develop your homework submissions. 

The repository organization is determined by the class and specific
instructions will be given to you. This may include::

  report
  proposal
  report
  code
  paper1
  paper2
  paper3
  bib

Important is that the the use of
**lower case** directories, for the main directories in the reporsitory

.. important:: Please use only **lowercase** characters in the directory
	       names and no special characters such as @ ; / _ and
	       spaces. In general we recommend that you avoid using
	       directoru names with capital letters spaces and _ in
	       them. This will simplify your documentation efforts and
	       make the URLs from git more readable. Also while on
	       some OS's the directories "MyDirectory" is different
	       from "mydirectory" gitlab considers it teh same. 
	       Furthermore our automated scripts that check your
	       submission are case sensitive. We only will read the
	       lower case directories. It is in your responsibility to
	       assure proper spelling.
	       


Getting an account
----------------------------------------------------------------------

Please go to gitlab and create an account. Use a nice account name that
only includes characters in [a-zA-Z0-9].

* http://gitlab.com

Getting a repository
--------------------

Once you submitted the account to us you will recieve within a week an
e-mail with your repository. It will be based on a Homework-ID (HID)
that will be assigned to you by us. The HID will be the name of the
directory in gitlab that you will be using to submit your homework.

Upload your public key
----------------------

Please upload your public key to the repository as documented in gitlab.


How to configure Git and Gitlab	for your computer
-------------------------------------------------

The proper way to use git is to install a client on your
computer. Once you have done so, make sure to configure git to use
your name and email address label your commits.::

   $ git config --global user.name "Albert Einstein"
   $ git config --global user.email albert@iu.edu

Do this on any computer you want to make direct checkins into gitlab.

.. warning::

   Make sure to substitute in your name and email address in the
   commands above.


You should also configure the push behavior to push only matching
branches. See the `git documentation
<https://git-scm.com/docs/git-config>`_ for more details on what this
means.::

   $ git config --global push.default matching

Using Web browsers to upload
----------------------------

Although we do not recommend using the Web browser to add or modify
files, it is possible. This means you could operate it without
installing anything.  This will work, but it is not very
convenient. To conduct your project efficiently you certainly wil want
to use the git command line inteface.

Using Git GUI tools
-------------------

There are many git GUI tools available that directly integrate into
your operating system finders, windows, ..., or PyCharm.
It is up to you to identify such tools and see if they are useful for
you. Most of the people we work with us git from the command line, even
if they use PyCharm or other tools that have build in git support.
We find the commandline tools sufficient.



Submission of homework
----------------------

You will have a HID given to you. Let us assume the id is::

   S17-DG-9999

When you log into gitlab, you will find a directory with that
name. Please substitute the HID that we gave above as an example with
your own. We refer to this ID as <HID> in these instructions.


.. note:: THis section will be updated
	  
	  Now you can go to your web browser and past the following
	  URL into it, where you replace the <HID> with your HID that
	  you can find in Canvas.::

	    https://gitlab.com/cloudmesh_spring2017/<HID>

	  For our example this would result in::

	    https://gitlab.com/cloudmesh_spring2017/S16-DG-9999

.. note: naturally if you try the S16-DG-9999 URL it will not work ;-)

You will be responsible to create the directory structure in git
following the guidelines of your class.


To submit the homework you need to first clone the repository (read
the git manual about what cloning means)::

   git clone https://gitlab.com/cloudmesh/fall2016/HID

Your homework for submission should be organized according to folders
in your clone repository. To submit a particular assignment, you must
first add it using::

  git add <name of the file you are adding>

Afterwards, commit it using::

  git commit -m "message describing your submission"

Then push it to your remote repository using::

  git push
 
If you want to modify your submission, you only need to::

  git commit -m "message relating to updated file"

afterwards::

  git push
  
If you lose any documents locally, you can retrieve them from your
 remote repository using::

  git pull

If you have any issues, please post your question in the folder
gitlab. Our TAs will answer them.

README.md
----------

You will have to create a README.md file in the top most directory of
your repository It serves the purpose of identifying your submission
for homework and information about yourself.

It is important to follow the format precisely. Any derivation from
this format will not allow us to see your homework as our automated
scripts will use the README.rst to detect them. Please also mind that
all filenames of all homework and the main directory must be
**lowercase** as explained above.

Naturally you **MUST** use the firstname and lastname that you used in
CANVAS so we can identify you in CANVAS properly. If you use an alias
that is not used in CANVAS we can naturally not identify you. Each
homework will have a single line in the readme. Once you have
completed a homework, please check it of with an [x]. There is no need
to ask us if your submisison was received, we will delete such request
and not answer them.  A program will inspect your submission and a
list will be produced with all submissions included. THis list will be
updated on regular baseis and published for the class. If we require
additional fields we will announce this and you will need to add
them. When we request to update the README.md is a must and can not be
delayed.

::

   - [ ] author: Firtsname, Lastname
   - [ ] hid: TBD
   - [ ] github: githubusername (if used for class)
   - [ ] gitlab: gitlabusername (if used for class)
   - [ ] report: report/report.pdf, not started, date of submission
   - [ ] paper1: paper1/paper.pdf, not stated, date of submission
   - [ ] paper2: paper2/paper.pdf, not stated, date of submission
   - [ ] paper3: paper2/paper.pdf, not stated, date of submission
   



Git Resources
----------------------------------------------------------------------

If you are unfamiliar with git you may find these resources useful:

- `Pro Git book <https://git-scm.com/book/en/v2>`_
- `Official tutorial <https://git-scm.com/docs/gittutorial>`_
- `Official documentation <https://git-scm.com/doc>`_
- `TutorialsPoint on git <http://www.tutorialspoint.com/git/>`_
- `Try git online <https://try.github.io>`_
- `GitHub resources for learning git
  <https://help.github.com/articles/good-resources-for-learning-git-and-github/>`_
  Note: this is for github and not for gitlab. However as it is for gt
  the only thing you have to do is replace hihub, for gitlab.
- `Atlassian tutorials for git <https://www.atlassian.com/git/tutorials/>`_  

Exercise
--------

Gitlab.1: Create a gitlab account

Gitlab.2: Create a README.md in your gitlab account with your information
