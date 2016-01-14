.. _s-lesson-git:

Using Git and GitHub for collaboration
======================================================================

.. sidebar:: Page Contents

   .. contents::
      :local:


Overview
----------------------------------------------------------------------

This lesson show you how to submit and work on homework assignments
using git version control and the GitHub collaboration platform.
Assignments are to be worked on as part of the `GitHub FutureSystems
organization`_.

Upon completion of this lesson you will be able to use GitHub for
submitting assignments for your course.

In order to use GitHub you will need (detailed below):

* a GitHub account
* to form a group with other students
* a FutureSystems account (see `Getting a FutureSystems account`_)
* an SSH key

.. _GitHub FutureSystems organization: https://github.com/futuresystems
.. _Getting a FutureSystems account: http://cloudmesh.github.io/introduction_to_cloud_computing/accounts/details.html#quickstart

Getting a GitHub account
----------------------------------------------------------------------

Go to `GitHub <https://github.com>`_ and sign up for an account.

This prerequisite is satisfied if you are able to

* go to `https://github.com`
* sign in

.. note::
   Please use a Gmail account to create your GitHub account.
   You can find details on how to do so at
   https://accounts.google.com/signup

Form a Group and Identify a Project
----------------------------------------------------------------------

You need to form a group with other students and determine a project
to work on together.
If you have difficulty on deciding a project please contact the
instructors.
The instructors need to approve your project so please send them
a report detailing:

* the names and email address of group members
* a project title
* the goal of the project
* a list of all deliverable
* assignments of tasks to group members

This prerequisite is satisfied if you and other students have formed
a group.
.. and your instructor has approved the project.

Obtain a FutureSystems account
----------------------------------------------------------------------

As all your work will be completed on FutureSystems, you will need
a FutureSystems account in order to access and user resources.
Go to the `FutureSystems portal <https://portal.futuresystems.org>`_
and request an account if you do not yet have one.
Then, you must request to be added to the course FutureSystems project.
Finally, you must upload an SSH key.
Please see the `FutureSystems documentation`_ for details on requesting
an account.
If you have trouble uploading an SSH Key please first consult
documentation on `how to upload an SSH Key`_ before contact support.

.. _FutureSystems documentation: http://futuregrid.github.io/manual/account.html#create-a-portal-account
.. _how to upload an SSH Key: http://cloudmesh.github.io/introduction_to_cloud_computing/accounts/ssh.html#s-using-ssh

This prerequisite is satisfied if you are able to accomplish the following:

* log into https://portal.futuresystems.org
* go to the ``Portal Account`` tab
* the ``status`` row is all green in the account status section


Have an SSH key
----------------------------------------------------------------------

You will need an SSH key to use both GitHub and FutureSystems.
If you have followed the documentation for creating a FutureSystems
account you should have created an SSH key in the process.

The prerequisite is satisfied if:

* You can log onto ``india.futuresystems.org``

On **Mac OS X** you will have

* The ``~/.ssh/id_rsa`` and ``~/.ssh/id_rsa.pub`` files exists

On **Windows** using Putty:

* **In Preparation**

If you have not satisfied this section, please see the `documentation`_
for details on how to do so.

.. _documentation: http://cloudmesh.github.io/introduction_to_cloud_computing/accounts/ssh.html#s-using-ssh

Using git on india.futuresystems.org
----------------------------------------------------------------------

To use git on india.futuresystems.org, Try::

        module load git

A sample output looks like::

        [albert@i136 ~]$ module load git
        git version 2.2.1 loaded

        [albert@i136 ~]$ git
        usage: git [--version] [--help] [-C <path>] [-c name=value]
                   [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
                   [-p|--paginate|--no-pager] [--no-replace-objects] [--bare]
                   [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
                   <command> [<args>]
        ...


Upload your SSH key to GitHub
----------------------------------------------------------------------

Now that you have an SSH key you need to upload it to GitHub in order
to access your repository (once it is assigned).

To add this key to GitHub, first copy your public ssh key.
You can view the key by executing the following command::

 $ cat ~/.ssh/id_rsa.pub

You may see something like the following::

  ssh-rsa AAA....... lovelace@gmail.com

Copy this public key by selecting it and ``right-click -> Copy``.

.. important::
   This must be your **public** key.
   Make sure you get the contents of ``id_rsa.pub`` and not
   ``id_rsa``.

Next go to your `GitHub account SSH keys`_ and click ``Add SSH key``
on the top right.
You will need to provide a title and the key.
It is a good idea to use your name and course number in the title,
for example, Ada could use ``Ada Lovelace BUEX-V 594``.
Next paste the key into the ``Key`` field and click ``Add key``
at the bottom.

This section is successfully completed if your
`GitHub account SSH keys`_ lists the key you provided with the
title and a fingerprint such as::

 d8:c3:dd:c8:2f:98:11:ca:[...]

.. _GitHub account SSH keys: https://github.com/settings/ssh


Getting access to repository
----------------------------------------------------------------------

Send an email to Badi' Abdul-Wahid (by 4pm on a business day)
and include the following information:

* the first and last name of each group member
* the email address of each group member
* the GitHub username of each group member
* the course number registered for
.. * the project proposal approved by the instructor

Please adhere to the following template for this email::

  Subject: request FutureSystems GitHub project
  Body:
    <first name> <last name>, <email> <github username>
    <first name> <last name>, <email> <github username>
    ...
    <course number>
    
    <project proposal>

For example, if Ada Lovelace and Albert Einstein are working together
to develop a computer simulations of the theory of relativity, they
would send the following (truncated) email::

  Subject: request FutureSystems GitHub project
  Body:
    Ada Lovelace, adalovelace@gmail.com lovelace
    Albert Einstein, emc2@gmail.com albert
    SP15-BL-BUEX-V594-37186

    Development of a computer simulation of the Theory of General Relativity
    [...]

A repository will then be created for your group and you will be
emailed the link.


.. warning::
   Please adhere to this format as improper formatting
   may result in your email being caught by spam filters.

.. warning::
   All members of a group will have access to this
   repository and can make changes.
   This means that anybody in your group can modify the work of of
   everybody else in that group.

.. warning::
   This repository is publicly view-able.
   Any content is view-able by *THE ENTIRE WORLD* so please do not add any
   private information.

This prerequisite is satisfied if are able to

* go to `https://github.com/futuresystems`
* find your repository (for example: ``class-bigdata-technology-spring-2015-ABCDE``)
* you are in the ``students`` team

Configuring your Git Identity (``git config``)
----------------------------------------------------------------------

You will need to configure git in order to use it properly.
The following are required:

* your name
* your email address
* your SSH keys (``id_rsa`` and ``id_rsa.pub``)

.. note::
   In order for git to function properly you will need to repeat the
   configuration steps for each machine you use git on.

Ada would configure your name and email like so::

 $ git config --global user.name "Ada Lovelace"
 $ git config --global user.email lovelace@gmail.com

Additionally, you can configure an editor such as ``nano``,
``emacs``, or ``vi``.
Ada will use ``nano``::

 $ git config --global core.editor nano

Once you have done so you should have a ``~/.gitconfig`` file.
You can check that this file exists and that it contains the correct
information::

 $ cat ~/.gitconfig
 [core]
     editor = nano
 [user]
     name = Ada Lovelace
     email = lovelace@gmail.com


Initializing the Repository with ``git clone``
----------------------------------------------------------------------

Once you have access to a repository you should use it to work on
assignments.
You must do so from your FutureSystems account by logging into
``india.futuresystems.org`` with ssh.
For instance, if your account name on FutureSystems is ``albert``::

  ssh albert@india.futuresystems.org

Once you have your repository URL
(for example: ``git@github.com:futuresystems/class-bigdata-technology-spring-2015-ABCDE.git``)
you can download the repository like so::

  git clone git@github.com:futuresystems/class-bigdata-technology-spring-2015-ABCDE.git
  cd class-bigdata-technology-spring-2015-ABCDE

Using the Repository
----------------------------------------------------------------------

Now that you have an initialized repository you may use it for
your assignments.

This section describes how to create and modify documents using git
to track and share the changes among collaborators.
Upon completion you will know how to do the following:

* ``add``-ing files to git
* ``commit``-ing changes
* ``push``-ing changes
* ``pull``-ing changes
* resolving conflicts


Adding content to git (``git add``, ``git commit``, ``git status``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that you have a repository in your account on ``india`` let us
create some content and notify git that changes to this content needs
to be tracked.
Tracking content makes it easy to share changes among collaborators,
track precisely who made a change, what was changed, when something
changed, and why a change was made.

The commands we are using in this section are:

* ``git add``
* ``git commit``
* ``git status``

The concepts are:

* untracked content
* staging area
* tracked content
* what a **change** means in git terminology

First let us create a file called ``fist.txt`` and write some lines::

  $ nano fish.txt # open the file in the "nano" editor
  $ cat fish.txt  # after saving, show the contents of the file
  One fish
  Two fish
  Red fish
  Blue fish

At this stage the file exists but git is not tracking changes made.
If it were to be deleted then it is gone for good.

We can inspect the status of git using the ``git status`` command::

  $ git status
  On branch master

  Initial commit

  Untracked files:
    (use "git add <file>..." to include in what will be committed)

          fish.txt

  nothing added to commit but untracked files present (use "git add" to track)

There is a lot of information here but the key pertinent point is the
``Untracked files`` heading which lists all files that git sees but
whose changes are not being tracked.
There is also the helpful hint ``use "git add <file>..."`` indicating
a possible next step.
Let us do so::

  $ git add fish.txt
  On branch master

  Initial commit

  Changes to be committed:
    (use "git rm --cached <file>..." to unstage)

          new file:    fish.txt

In order to understand what ``git add`` does, we need to know the
difference between each of the three states that content may be in:

* untracked
* staging
* tracked

When the ``fish.txt`` file was created the content was *untracked*.
That is, any modifications to ``fish.txt`` will not be logged.
If it is deleted it cannot be recovered, it cannot be shared using
git, and we cannot extract the **who**, **what**, **when**, and **why**
metadata associated with a change.

By using ``git add`` content can be added to the staging area.
Multiple files can be staged.
Hypothetically, if two other files ``hello.txt`` and ``world.txt``
were to be created they could be staged::

  $ git status
  On branch master

  Initial commit

  Untracked files:
    (use "git add <file>..." to include in what will be committed)

        fish.txt
	hello.txt
	world.txt

  nothing added to commit but untracked files present (use "git add" to track)
  $ git add hello.txt
  $ git add hello.txt
  $ git status
  On branch master
  
  Initial commit
  
  Changes to be committed:
    (use "git rm --cached <file>..." to unstage)
  
          new file:   fish.txt
          new file:   hello.txt
          new file:   world.txt


By using the staging area multiple files can be committed to git as a
single **change**.
Meaning: a **change** is the addition, deletion, of modification of
content of one or more files.

At this point, ignoring the hypothetical ``hello.txt`` and ``world.txt``
files, we can now **commit** this change::

  $ git commit -m "added counting fish"

The ``git commit`` command recording everything in the **staging area**
as a single **change**.
When committing a change it is necessary to add a message describing
the change.
The change itself stores the **what** (what content changed), and
**when** (time and date of a change), but you must provide a
message that describes **why** a change was made.
This message is then stored with the change and can be viewed by
looking at the history of the repository.

You can now see for yourself that git no longer sees any untracked
content::

  $ git status
  On branch master
  nothing to commit, working directory clean


At this point you have used the ``git add``, ``git commit``, and
``git status`` commands and should know the difference between the
``untracked``, ``staging area``, and ``tracked`` states that content
may be in, and understand what is meant by a "change."


Viewing Repository History (``git show``, ``git log``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Recall that a git "change" refers to **who** made a change, **what**
what changed, **when** a change was made, and **why** a change was made.
Each change is added to the others so that you can view the entire
history, each change on top of its parent, of a repository.

Try it out using ``git show`` to view the contents of a commit::

 $ git show
 commit 05b162b8e7ffe5eb8dda8822a691244a26ff2c0e
 Author: Ada Lovelace <lovelace@gmail.com>
 Date:   Wed Feb 25 12:40:20 2015 -0500

     added counting fish

 diff --git a/fish.txt b/fish.txt
 new file mode 100644
 index 0000000..77a5fea
 --- /dev/null
 +++ b/fish.txt
 @@ -0,0 +1,4 @@
 +One fish
 +Two fish
 +Red fish
 +Blue fish


As you can see there is a lot of information here.
The pertinent points are:

* **who**: the author name and email address is provided
* **what**: you can see the exact change at the bottom
* **when**: the date of the commit is given
* **why**: the commit message you provide is given

Additionally, you can see an overview containing the commit author,
date, and message using ``git log`` to show the history.
In this case there has only been one commit so that is all that will
be shown.
However, please try this out again later after making further commits.

::

 $ git log
 commit 05b162b8e7ffe5eb8dda8822a691244a26ff2c0e
 Author: Ada Lovelace <lovelace@gmail.com>
 Date:   Wed Feb 25 12:40:20 2015 -0500

     added counting fish


Sharing your changes via GitHub (``git push``, ``git pull``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section describes how to share you changes using git and GitHub.
The commands covered are:

* ``git push``
* ``git pull``

By the end of this section you will understand the difference between
a **local** and **remote** repository and how to share changes made
locally via a remote repository.

Recall that earlier you initialized a repository using the ``git clone``
command.
Let us look in further detail at what this command does.

First, you logged into ``india@futuresystems.org``.
At this point, your git repository was not on ``india``.
By executing the ``git clone`` command you created a **local** copy on
``india`` of the **remote** repository hosted on the GitHub server.
At this point there are two repositories: **local**  and **remote**
(also known as ``origin``).
You can inspect this for yourself.::

 $ cd class-bigdata-technology-spring-2015-ABCDE
 $ git remote -v
 origin	git@github.com:futresystems/class-bigdata-technology-spring-2015-ABCDE.git (fetch)
 origin	git@github.com:futresystems/class-bigdata-technology-spring-2015-ABCDE.git (push)

Here, ``origin`` is the shorthand name referring the the location
of the **remote** repository that this **local** one was created
from.

.. important::
   This means that **ANY** changes added via ``git commit`` are only
   committed to the **local** repository.
   These changes are **NOT YET** present at the **remote** (``origin``).

In order to share your commits with the **remote** repository, you
must ``push`` them.
Like so::

 $ git push origin master

Let's break this down a bit.
The first part is ``git push``, meaning that we are telling git
to share our **local** changes with a **remote** repository.

Now let us examine the ``origin`` and ``master`` parts of the command.
Recall the output of ``git remote -v`` and ``git status`` after our
commit earlier.
The ``git remote`` command provides us with the name associated
with the **remote** repository, namely ``origin``.
From ``git status``, we get ``On branch master``.
A repository can have multiple branches with different names
such as (``release-2.0``, ``dev1.3``, etc).
This is beyond the scope of this lesson, but it suffices to say
that all our commits so far have been to the default branch which is
called ``master``.

Let us look at the command again::

 $ git push origin master

Translated into English, this says: "push the changes made to the current
branch to the master branch of the repository called ``origin``".
In other words, ``git push`` updates the **remote** repository with all
**local** changes.

At this point, the remote repository reflects the changes made by Ada.
Now, Albert had previously cloned the repository at the same time as
Ada, since they are working together.
Since he cloned it before Ada ``push``-ed her commits, his repository
is out of date.
However, Ada can now tell Albert that she made some change:
  Ada: Hi Albert. I pushed some changes to the repo.

  Albert: Thanks Ada. I'll pull them right away.

Albert can then do the following::

 $ cd class-bigdata-technology-spring-2015-ABCDE
 $ git pull origin master

Albert now has all the changes Ada made.

.. important::
   Only by using ``git push`` will your GitHub repository be updated.
   If you are trying to share your changes but your team-members cannot
   see them, make sure to ``git push origin remote``.



Concurrent Changes
----------------------------------------------------------------------

One feature of git is that is allows multiple people to work on the
same repository concurrently.

For instance, while Ada was adding the ``fish.txt`` file, Albert may
have been writing about eggs.
He would have cloned the repository, just like Ada, but added
``eggs.txt`` instead::

 $ nano eggs.txt
 $ cat eggs.txt
 Do you like green eggs and ham?
 I do not like them, Sam-I-am.

As Ada did, Albert would ``add`` and ``commit`` the change::

 $ git add eggs.txt
 $ git commit -m "added green eggs and ham"

Now, when he pulls the changes that Ada made he sees that both
``eggs.txt`` and ``fish.txt`` are present in his **local** repository::

 $ ls
 eggs.txt   fish.txt

He can share his changes with Ada in the same fashion:

  Albert: Hi Ada. I pushed my changes.

  Ada: Great. I'll pull them now.

Now, Ada does the ``pull``-ing and sees Albert's changes::

 $ git pull origin master
 $ ls
 eggs.txt   fish.txt



Resolving Conflicts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**In preparation**


Exercise
----------------------------------------------------------------------

The goal of this exercise is for you and your team to become familiar
with ``push``-ing and ``pull``-ing to and from your repository.

Each person should log into ``india@futuresystems.org`` and clone the
repository from GitHub.
Next, each person should create a file ``<portalname>.txt`` in which
they explain what the following commands do:

* ``git clone``
* ``git add``
* ``git commit``
* ``git push``
* ``git pull``

Additionally, this file should describe the difference between a
remote and local repository.

For example, Ada would create ``lovelace.txt`` and Albert ``emc2.txt``.

Finally, each person should synchronize their changes with everyone else
so that each team member has the other team member's file.
This synchronization should be done with git such that the GitHub
repository also has these changes.

Be aware that individual participation counts.
Each team member must contribute their file and this file must be
unique.
Please recall that git tracks **who** made a contribution and
exactly **what** that change was.
