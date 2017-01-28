=====
 Git
=====

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

It is important is that you always want to make sure that you want to use
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

In addition the tutorials from atlasian are a good source. However
remember that you may not use bitbucket as the repository, so ignore
those tutorials. We found the following useful

* What is git: https://www.atlassian.com/git/tutorials/what-is-git
* Installing git: https://www.atlassian.com/git/tutorials/install-git
* git config: https://www.atlassian.com/git/tutorials/setting-up-a-repository#git-config
* git clone: https://www.atlassian.com/git/tutorials/setting-up-a-repository#git-clone
* saving changes: https://www.atlassian.com/git/tutorials/saving-changes
* collaborating with git: https://www.atlassian.com/git/tutorials/syncing

How to use Git in this class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let us use the first homework 'TechList 1' as an example to illstrate
why and how we choose Git as a essential tool in this class.

In the 'Technologies' section on the class website, we will collaboratly
edit the web page contents. Each student shall add their paragraphs about
certain tech topics. This leads to a question: multiple authors are working
on a same document, whose version should be used as the final version? After
all, there can only be one version published online.

Git can largely (not completely) help use sort it out. And here is our Git
workflow:

1) In the class official repo, we start from an empty TechList file. Here is the
file we start from in our class repo: https://github.com/cloudmesh/classes/blob/master/docs/source/i524/technologies.rst

2) Each student is going to create a repository exactly the same as the official
repo. This step is called to 'fork' the repo. You do so by click the 'fork'
button on the top right corner of the page. Once done, you have your own copy of
the class repo.

3) You create this repo in your Github account. This means you still store
everything online remotely. Although, this version is totally under your acount.

4) To conveniently edit the files, you need a copy on your laptop. This is to
'clone' your personal repo to your local disk. Look at your Github repo and find
a green button saying 'clone or download'. Click this button and you will have a
pulldown menu where you should copy the URL. In your terminal/commandline, run
'git clone <the URL you just copied>'. This step copies the project to your own
disk for editing.

5) Your local copy is a 'live' version, since you are going to keep editing it.
Put your contents in the 'technologies.rst' file in the corresponding sections.

6) At any point during your editing, if you want to secure the changes you made
to the file, you can always 'commit'. Refer to the 'git commit' instruction.
Obviously, when you finish all the typing, a 'commit' operation must be performed.
Consider a 'commit' operation a fancy 'save' operation you may always do during
file editing. A major advantage is, 'commit' will keep a history of all the
versions you committed. All the committed texts will not be lost. This reduces a
lot of risks during long term, large scale development.

7) When you complete your work, it is the time to submit your homework back to the
graders. Do this in two steps. First, you have to 'push' your local disk copy to
the repo you created under your acount in step 4). Follow closely after this link
https://github.com/cloudmesh/classes#submitting-changes to get your local disk and
your personal remote a.k.a. the 'origin' synchronized. Second step is done via
your browser. At the very top of your repo web page, switch to the 'Pull requests'
tab, and submit a pull request to the class repo. This way, the instructor will get
notified and merge your repo into the class official repo. After this merge being
performed, all your contributions will be included into the public site.
