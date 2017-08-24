Git
===


Why are you using github for submitting projects and papers?
------------------------------------------------------------

This class is about open source technology and we like that you benefit
from material others in the class are developing or have developed. All
assignments are openly submitted to the class github for everyone to
see. As part of the goal of this class is to develop reusable
deployments. Such reuse is only possible if the code is publicly
available and others can benefit from it.

The technology papers are made accessible so you can read other
technology papers and can get an introduction in technologies that you
may not yet know about. It also allows others to contribute to your
technology papers and improve them.



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

You will also need to decide if you want to push branches individually
or all branches at the same time. It will be up to you to make what
whill work for you best. To be on the safe side, you may want to set
up pushing only the current branch with::

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

How to solve merge conflict in Pull Request?
--------------------------------------------

Make sure you have upstream repo defined::

  $ git remote add upstream https://github.com/cloudmesh/classes

 

Backup all your changed files - just in case you need them while merging the changes back

 

Get latest from upstream::

  $ git rebase upstream/master

 

In this step, the conflicting file shows up (in my case it was refs.bib)::

  $ git status

should show the name of the conflicting file::

  $ git diff <file name>

should show the actual differences. In some cases, it is easy to
simply take latest version from upstream and reapply your changes. So
you can decide to checkout one version earlier of the specific file.


.. note::
   
   You can find the version number with::

     $ git log --oneline

   You can checkout a specific version with::

     $ git checkout <version number - e.g. ed13c06> <file name>


At this stage, the re-base should be complete. So, you need to commit
and push the changes to your fork::

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
automatically


Building cloudmesh/classes in local machine
-------------------------------------------

If you experience following errors, please follow the guideline
explained below. Make sure to do the following steps first::

  sudo apt-get install libssl-dev


Follow this link for more info

* http://cloudmesh.github.io/client/system.html#ubuntu-14-04-15-04


Pip will give the following error if you have not installed the library:


Pip installation error when installing requirements.::


  error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
    
Rolling back uninstall of cryptography
--------------------------------------
    Command "/usr/bin/python -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-1vi4of/cryptography/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-gNcw68-record/install-record.txt --single-version-externally-managed --compile" failed with error code 1 in /tmp/pip-build-1vi4of/cryptography/


Trying to build the source with this error::


  $ make
  cd docs; make html
  make[1]: Entering directory '/home/albefrt/Documents/github/cloudmesh/classes/docs'
  sphinx-build -b html -d build/doctrees source build/html
  Running Sphinx v1.5.2
  Extension error:
  Could not import extension sphinxcontrib.fulltoc (exception: No module named fulltoc)
  Makefile:54: recipe for target 'html' failed
  make[1]: *** [html] Error 1
  make[1]: Leaving directory '/home/sabyasachi/Documents/github/cloudmesh/classes/docs'
  Makefile:18: recipe for target 'doc' failed
  make: *** [doc] Error 2



How to sole Merge Conflict in a Pull Request?
---------------------------------------------

.. warning:: THis FAQ seems duplicated. Also you are allowed to point
	     to content where thsi is already explained with a
	     link. so you do not have to duplicate.
	     
Steps followed to solve merge conflict in pull request.

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
automatically


             
