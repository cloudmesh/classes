Git
===

This class uses open source technology and we like that you benefit
from material others in the class are developing or have
developed. All assignments are openly submitted to the class github
for everyone to see. As part of the goal of this class is to develop
reusable instructions, deployments, software, and examples. Such reuse
is only possible if the code is publicly available and others can
benefit from it. While using github.com we make sharing of information
possible so every one can benefit and achieve their best.

Install
-------

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

You will also need to decide if you want to push branches individually
or all branches at the same time. It will be up to you to make what
whill work for you best. We found that the following seems to work
best::

  git config --global push.default matching

More information about a first time setup is documented at::

* http://git-scm.com/book/en/Getting-Started-First-Time-Git-Setup

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

.. warning:: Please read the information on the screen when you set up 

             
Merge 
-----

As we are allowing contribution by the community, they are best
managed through a merge with our upstream repository so you can
update to the newest status before you issue a pul request.
	     
Make sure you have upstream repo defined::
  
  $ git remote add upstream https://github.com/cloudmesh/classes


Backup all your changed files - just in case you need them while merging the changes back

Get latest from upstream::

  $ git rebase upstream/master

In this step, the conflicting file shows up (in my case it was refs.bib)::

  $ git status

should show the name of the conflicting file::

  $ git diff <file name>

should show the actual differences. May be in some cases, It is easy
to simply take latest version from upstream and reapply your changes.

So you can decide to checkout one version earlier of the specific
file. At this stage, the re-base should be complete. So, you need to
commit and push the changes to your fork::

  $ git commit
  $ git rebase origin/master
  $ git push

 

Then reapply your changes to refs.bib - simply use the backedup
version and use the editor to redo the changes.

At this stage, only refs.bib is changed::

  $ git status

should show the changes only in refs.bib.
Commit this change using:: 

  $ git commit -a -m "new:usr: <message>"

 

And finally push the last commited change::

  $ git push

 

The changes in the file to resolve merge conflict automatically goes
to the original pull request and the pull request can be merged
automatically.

You still have to issue the pull request from the Github Web page so
it is registered with the upstream repository.


             
