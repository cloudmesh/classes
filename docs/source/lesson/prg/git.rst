Git
===

Install
~~~~~~~

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

  $ git config --global user.name "Albert Zweistein"
  $ git config --global user.email albert.zweistein@gmail.com

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

