Github
======

Github is a code repository that allows the development of code in a
distributed fashion. There are many good tutorials about github.

Some of them can be found on the github Web page. An interactive
tutorial is for example available at

* https://try.github.io/

A more extensive list of tutorials can be found at

* https://help.github.com/articles/what-are-other-good-resources-for-learning-git-and-github

Video Lectures on Github
---------------------

The github foundation has a number of excellent videos about git. If
you are unfamiliar with git and you like to watch videos in addition
to reading the docuentation we recommend these videos

* https://www.youtube.com/user/GitHubGuides/videos


Below we introduce some heavily used concepts:

.. _upload_key_:

Upload Key
~~~~~~~~~~
Before you fork a repository, you need to upload a public key
in order to access your repository. See lesson :ref:`s-ssh-generate`
before you upload. Copy the contents of your ``.ssh/id_rsa.pub`` file
and add them to `you github keys
<https://github.com/settings/keys>`_.

*    https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/

.. _fork_repo_:

Fork
~~~~

Forking is the first step to contributing to projects on
GitHub. Forking allows you to copy a repository and work on it under
your own account. Next, creating a branch, making some changes, and
offering a pull request to the original repository, rounds out your
contribution to the open source project.

*    https://www.youtube.com/watch?v=5oJHRbqEofs

Rebase
~~~~~~

With Git Rebase allows you to integrate your code easily into a
branch. Rebase allows you to take all of the work on your branch and
relocate it to another point in your repository's history, encouraging
you to branch early and often without the fear of messy merges or
missing out on new development.

When you start editing your project, you diverge from the original
version. During your developing, the original version may be updated,
or other developers may have some of their branches implementing good
features that you would like to include in your current work. That is
when 'Rebase' becomes useful. When you 'Rebase' to certain points, could
be a newer Master or other custom branch, consider you graft all your
on-going work right to that point.

Rebase may fail, because some times it is impossible to achieve what we
just described (conflicts!). For example, you and the to-be-rebased
copy both edited some common text section. Once this happens, human
intervention would be the only solution.

* https://www.youtube.com/watch?v=SxzjZtJwOgo

.. _remote_:

Remote
~~~~~~
Collaborating with others involves managing these remote repositories
and pushing and pulling data to and from them when you need to share
work. Managing remote repositories includes knowing how to add remote
repositories, remove remotes that are no longer valid, manage various
remote branches and define them as being tracked or not, and more.

Though out this semester, you will typically work on two 'remote' repos.
One is the office class repo, and another is the repo you forked from
the class repo. The class repo is used as the centralized, authority
and final version of all student submissions. The repo under your own
Github account is for your personal storage. Only when you feel good
about your personal repo, you should let us know that you want us to
merge your repo into the class repo (by submitting a pull request as
illustrated right next.)

*    https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes

Pull Request
~~~~~~~~~~

Pull requests are a means of starting a conversation about a proposed
change back into a project. We'll be taking a look at the strength of
conversation, integration options for fuller information about a
change, and cleanup strategy for when a pull request is finished.

*  https://www.youtube.com/watch?v=d5wpJ5VimSU

Checkout
~~~~~~~~

Change where and what you're working on with the checkout
command. Whether we're switching branches, wanting to look at the
working tree at a specific commit in history, or discarding edits we
want to throw away, all of these can be done with the checkout
command.

* https://www.youtube.com/watch?v=HwrPhOp6-aM

Branch
~~~~~

Branches are an excellent way to not only work safely on features or
experiments, but they are also the key element in creating Pull
Requests on GitHub. Let's take a look at why we want branches, how to
create and delete branches, and how to switch branches in this
episode.

* https://www.youtube.com/watch?v=H5GJfcp3p4Q

Merge
~~~~~

Once you know branches, merging that work into master is the natural
next step. Find out how to merge branches, identify and clean up merge
conflicts or avoid conflicts until a later date. Lastly, we'll look at
combining the merged feature branch into a single commit and cleaning
up your feature branch after merges.

* https://www.youtube.com/watch?v=yyLiplDQtf0

GUI
~~~

Using Graphical User Interfaces can supplement your use of the command
line to get the best of both worlds. GitHub for Windows and GitHub for
Mac allow for switching to command line, ease of grabbing repositories
from GitHub, and participating in a particular pull request. We'll
also see the auto-updating functionality helps us stay up to date with
stable versions of Git on the command line.

* https://www.youtube.com/watch?v=BMYOs5jflGE


Windows
~~~~~~~~

This is a quick tour of GitHub for Windows. It offers GitHub newcomers
a brief overview of what this feature-loaded version control tool and
an equally powerful web application can do for developers, designers,
and managers using Windows in both the open source and commercial
software worlds.  More: http://windows.github.com

*   https://www.youtube.com/watch?v=YBbkvCrfDSo


Exercise
-------

Github.1:
  How do you set your favorite editor as a default with github config

Github.2:
  What is the difference between merge and rebase?

Github.3:
  Assume you have made a change in your local fork, however other
  users have since committed to the master branch, how can you make
  sure your commit works off from the latest information in the master
  branch?

Github.4:
  Find a spelling error in theo Web page or a contribution and create
  a pull request for it.
