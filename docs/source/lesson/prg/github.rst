Github
======

Github is a code repository that allows the development of code in a
distributed fashion. There are many good tutorials about github.

Some of them can be found on the github Web page. An interactive
tutorial is for example available at

* https://try.github.io/

A more extensive list of tutorials can be found at 

* https://help.github.com/articles/what-are-other-good-resources-for-learning-git-and-github

Important is that you always want to make sure that you want to use
the `git config` command to initialize git for the first time you use
it. This will ensure that you use on all resources the same Name and
e-mail so that git history and log will show consistently your
checkins. If you do not do this, your checkins in git do not show
up in a consistent fashion as a single user. This is done with the
following commands::

  $ git config --global user.name "John Doe"
  $ git config --global user.email johndoe@example.com

You can set also the editor with::

  $ git config --global core.editor emacs

More information about a first time setup is documented at::

  $ http://git-scm.com/book/en/Getting-Started-First-Time-Git-Setup

To check your setup you can say::

  $ git config --list

  
Git Tutorials
----------

The github web page contains many useful information as well as good
tutorials as pointed out before:

   * https://help.github.com/articles/what-are-other-good-resources-for-learning-git-and-github

In addition the tutorials from atlasian are a good source. However
remember that you may not use bitbucket as the repository, so ignore
those tutorials. We found the following useful

* What is git: https://www.atlassian.com/git/tutorials/what-is-git
* Installing git: https://www.atlassian.com/git/tutorials/install-git
* git config: https://www.atlassian.com/git/tutorials/setting-up-a-repository#git-config
* git clone: https://www.atlassian.com/git/tutorials/setting-up-a-repository#git-clone
* saving changes:
  https://www.atlassian.com/git/tutorials/saving-changes
* collaborating with git: https://www.atlassian.com/git/tutorials/syncing


Video Lectures on GIthub
---------------------

The github foundation has a number of excelent videos about git. If
you are unfamiliar with git and you like to watch videos in addition
to reading the docuentation we recommend these videos

* https://www.youtube.com/user/GitHubGuides/videos

Install
~~~~~

Information on how to install git can be found at

* https://www.atlassian.com/git/tutorials/install-git

  
Config
~~~~~~

Once you've got Git installed, several bits of configuration will
enhance your experience with the tool and better tune it to your
operating system. Let us tell you about settings for your username and
email address, line endings, and color, along with the settings'
associated configuration scopes.

*   https://www.youtube.com/watch?v=ZChtKFLiaNw

Fork
~~~~

Forking is the first step to contributing to projects on
GitHub. Forking allows you to copy a repository and work on it under
your own account. Next, creating a branch, making some changes, and
offering a pull request to the original repository, rounds out your
contribution to the open source project.

* https://www.youtube.com/watch?v=5oJHRbqEofs

Pull Request
~~~~~~~~~~

Pull requests are a means of starting a conversation about a proposed
change back into a project. We'll be taking a look at the strength of
conversation, integration options for fuller information about a
change, and cleanup strategy for when a pull request is finished.

*  https://www.youtube.com/watch?v=d5wpJ5VimSU

Branch
~~~~~

Branches are an excellent way to not only work safely on features or
experiments, but they are also the key element in creating Pull
Requests on GitHub. Let's take a look at why we want branches, how to
create and delete branches, and how to switch branches in this
episode.

* https://www.youtube.com/watch?v=H5GJfcp3p4Q

Checkout
~~~~~~~~

Change where and what you're working on with the checkout
command. Whether we're switching branches, wanting to look at the
working tree at a specific commit in history, or discarding edits we
want to throw away, all of these can be done with the checkout
command.

* https://www.youtube.com/watch?v=HwrPhOp6-aM


Merge
~~~~~

Once you know branches, merging that work into master is the natural
next step. Find out how to merge branches, identify and clean up merge
conflicts or avoid conflicts until a later date. Lastly, we'll look at
combining the merged feature branch into a single commit and cleaning
up your feature branch after merges.

* https://www.youtube.com/watch?v=yyLiplDQtf0

Rebase
~~~~~~

With Git Rebase allows you to integrate your code easily into a
branch. Rebase allows you to take all of the work on your branch and
relocate it to another point in your repository's history, encouraging
you to branch early and often without the fear of messy merges or
missing out on new development.

* https://www.youtube.com/watch?v=SxzjZtJwOgo
  
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
