.. _techlist-tips:

========================================
Completing Techlist Assignments
========================================

Watch the video at https://www.youtube.com/watch?v=roi7vezNmfo

From the video you learn how to fork and create pull requests. We
encourage you to watch the video. It is on purpose long. We assume
thet you are running the commands in virtualenv


Prerequisites
=============

#. You have Ubuntu installed in Virtualbox. See lesson :doc:`../lesson/linux/ubuntu`.
#. You have prepared the Ubuntu VM as in lesson :doc:`./ubuntu-setup`
   and :ref:`r-i524-ubuntu-setup-devtools`.
#. You have a GitHub account.
#. You have configured git to identify as you as well as to use your
   preferred text editor. See lesson :doc:`../lesson/prg/github`.

   Specifically, you should **adapt** the following commands:

   ::

      $ git config --global user.name "Albert Zweistein"
      $ git config --global user.email "albert.zweistein@gmail.com"
      $ git config --global core.editor emacs

#. You have created an ssh key on Ubuntu. See lesson :ref:`s-ssh-generate`
   or `video
   <https://youtu.be/roi7vezNmfo?t=23m37s>`_.

   You should do something like this to generate an ssh key:

   ::

      $ ssh-keygen
      Generating public/private rsa key pair.
      Enter passphrase (empty for no passphrase):
      Enter same passphrase again:
      Your identification has been saved in test.
      Your public key has been saved in test.pub.
      The key fingerprint is:
      SHA256:koA9ZYkSlBBpkR/W0bfIxLmViwQWY1qKqjTzGdK+7vQ ubuntu@ubuntu-xenial
      The key's randomart image is:
      +---[RSA 2048]----+
      |o*=o.XO.. .      |
      |.o+=B+o* +       |
      |..++= + * o      |
      |. .. o * o       |
      |.= o  o S        |
      |o * o  .         |
      |.  =             |
      |  . o            |
      |  o+ E           |
      +----[SHA256]-----+

#. You have uploaded the **public** key to your github
   profile. See lesson :ref:`upload_key_` or `video
   <https://youtu.be/roi7vezNmfo?t=24m26s>`_.

   Specifically, copy the contents of your ``.ssh/id_rsa.pub`` file
   and add them to `you github keys
   <https://github.com/settings/keys>`_.

   To get the contents of the public key, use the ``cat`` command.
   Something like the following:

   ::

      $ cat .ssh/id_rsa.pub
      ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC+kwxuJ46kIq20odlqQ/sLl0YPkG3yVcXS+IwyWxDiaxOyB3ZqVJPsCF7OKqA9WpIHsdWxXNtU0hD/ulO2DsIJI73tTF+ITDfeMs7A7pzFPmHwTRKIAGzsiiZkj7W2hQK6DFUt/x4fjwJImG3YrNjcJ2//2aOW88Dsoq/+8Hxz3Wm5uDpmkcX5aFFmkFV6oyZoVznUZqpIlRQbgM9b+kXr7pvnYYDrGVVY86frLMrGNKKXE+DXUPLRqUGYmLQ+62xw4I6xXaF4+AyR4j4uTY91Fq1ybSALkxgKkqrZavZudkAzc50nSTTbmgCSwEaAWw0Bz6eX28r4IJclAI98Apcl ubuntu@ubuntu-xenial

   .. warning::

      Do not use the above public key. It will not work for you.

#. You have created a Python Virtual Environment and activated it. See lesson :ref:`Virtual_Environments`
   to learn what is Virtual Environment. And lesson :ref:`virtualenv_`
   to learn how to properly install and activate Virtualenv.

   To create a virtual env, use the ``virtualenv`` command.

   ::

      $ virtualenv ~/ENV
      Running virtualenv with interpreter /usr/bin/python2
      New python executable in /home/ubuntu/ENV/bin/python2
      Also creating executable in /home/ubuntu/ENV/bin/python
      Installing setuptools, pkg_resources, pip, wheel...done.

   To activate the virtual environment you created, use the the following command.

   ::

      $ source ~/ENV/bin/activate

   .. tip::

      Notice how the shell prompt ``(ENV)`` changed upon activation.

   .. important::

      As virtualenv stated, you **must** activate the virtual environment
      before it can be used.

   It's troublesome and forgettable to activate the virtual environment every time
   before it can be used. `Autoenv
   <https://github.com/kennethreitz/autoenv>`_ is the tool that can help
   you. See lesson :ref:`AutoENV_` to learn how to install and use Autoenv.

   To install Autoenv,

   ::

      $ pip install autoenv
      $ echo "source `which activate.sh`" >> ~/.bashrc

   To use Autoenv, add the virtual environment ``ENV`` you created with virtualenv
   into ``.env`` file within your project directory:

   ::

      $ echo "source ~/ENV/bin/activate" > yourproject/.env
      $ echo "echo 'whoa'" > yourproject/.env
      $ cd project
      whoa
      (ENV) $

   Your virtual environment should be automatically activated.

   .. tip::

      Notice how the shell prompt ``(ENV)`` changed upon activation.


Setup Your Clone
================

#. Create a fork into your local repo: e.g. Go to
   https://github.com/cloudmesh/classes/ and click on the "Fork"
   button on the top right corner.

   This will redirect you to your page. Ensure that the url has is
   something like the following::

     https://github.com/YOUR_GITHUB_USERNAME/classes

   .. important::

      Verify that the url contains your github username in place of ``YOUR_GITHUB_USERNAME``.

#. Ensure that you are on your forked repository on GitHub.

   Click on “Clone or download” (a green button on the top right) and copy the curl.
   It should look something like::

     git@github.com:YOUR_GITHUB_USERNAME/classes.git


#. On Ubuntu, use the ``git`` command to clone the repository using the above link:

   ::

      (ENV) $ git clone git@github.com:YOUR_GITHUB_USERNAME/classes.git
      Cloning into 'classes'...
      remote: Counting objects: 13012, done.
      remote: Compressing objects: 100% (918/918), done.
      remote: Total 13012 (delta 727), reused 0 (delta 0), pack-reused 12029
      Receiving objects: 100% (13012/13012), 32.73 MiB | 13.42 MiB/s, done.
      Resolving deltas: 100% (9109/9109), done.
      Checking connectivity... done.

#. Change directories into your clone:

   ::

      (ENV) $ cd classes

#. Add the upstream repository as ``upstream``:

   Verify that the ``origin`` points to your clone

   ::

      (ENV) $ git remote -v
      origin	git@github.com:YOUR_GITHUB_USERNAME/classes.git (fetch)
      origin	git@github.com:YOUR_GITHUB_USERNAME/classes.git (push)

   Next, add the upstream:

   ::

      (ENV) $ git remote add upstream git://github.com/cloudmesh/classes

   Verify that the changes are as expected

   ::

      (ENV) $ git remote -v
      origin	git@github.com:YOUR_GITHUB_USERNAME/classes.git (fetch)
      origin	git@github.com:YOUR_GITHUB_USERNAME/classes.git (push)
      upstream	git://github.com/cloudmesh/classes (fetch)
      upstream	git://github.com/cloudmesh/classes (push)


#. Install the dependencies for building the website:

   ::

      (ENV) $ pip install -r requirements.txt


Adding your Technology
======================

#. Edit the following two files from within the ``classes`` directory:

   #. add the paragraph about the technologies in ``docs/source/i524/technologies.rst``
   #. your references, go to  ``docs/source/refs.bib``

      .. warning::

         Make sure to find your **HID** in ``refs.bib`` and make your
         changes under that line.  This will help prevent conflicts
         when merging later.

   For the descriptions remove advertisement adjectives and
   sentences from your description, and spellcheck.

   For references it is important that every reference is required
   to have owner field. For example::

     owner = {TA-sp17-0001}

   In case your entry is MISC the howpublished field refers to the
   method on how it is published. A urls are posted in its own
   field. For example::

     howpublished = {Web Page}
     url = {http://www.google.com}


#. After making your changing, you should compile the webpage using
   ``make``. You can then open the locally generated copy of the class
   website using ``make view``:

   ::

      (ENV) $ make
      (ENV) $ make view


#. Once you have verified that your changes have been integrated
   correctly, you should commit your changes:

   ::

      (ENV) $ git commit \
        -m "new:usr: Added YOUR_TECHNOLOGY to techlist" \
        docs/source/i524/technologies.rst \
        docs/source/refs.bib

   .. tip::

      Make sure to replace ``YOUR_TECHNOLOGY`` with the technology you
      just provided the description for.


      To get credit for the assignment write your commit summary with your::

        new:usr: Meaningful summary of what you did

      For example for new contributions::

        new:usr: Added entry for Nagios in the technology list

      For example for changes contributions::

        chg:usr: Changed the entire paraagraph for Nagios in the technology list

      For example for fixed contributions::

        fix:usr: Changed spelling for Nagios in the technology list


#. Rebase your changes on top of any changes to upstream

   Since you are working on your own independant copy of the
   ``classes`` repository, it will soon be out of date.  In order to
   stay up to date, you need to ``rebase`` your changes on top of the
   upstream master branch.

   .. tip::

      You should run the ``fetch`` and ``rebase`` very frequently.
      This will help reduce the frequency of conflicts.


   a. Fetch any changes that have been commited to ``upstream``:


      ::

         (ENV) $ git fetch upstream master

   b. Replay your commits on top of the upstream changes:

      ::

         (ENV) $ git rebase upstream/master


   c. If you should run into a merge conflict, you should abort the rebase:

      ::

         (ENV) $ git rebase --abort

      Next, make a copy of your changes:

      ::

         (ENV) $ cp docs/source/i524/technologies.rst my-technologies.rst
         (ENV) $ cp docs/source/refs.bib my-refs.bib

      You should then rerun the rebase, taking the upstream changes

      ::

         (ENV) $ git rebase -Xours upstream/master

      .. tip::

         Even though you pass the ``-Xours`` to git, it will
         automatically resolve the conflicts by using the upstream
         version. The ``-Xours`` is due to running the rebase from the
         perspective of the ``upstream`` version, rather than your
         modified version.

      At this point you should incorportate your changes that you
      saved in ``my-technologies.rst`` and ``my-refs.bib``. Go back to
      the previous step where you commit.

      .. warning::

         Do not commit your backup files. Remove them after rebasing
         successfully.


#. Review the changed files to make sure you only change the two
   files. If you have other changes create separate pull requests for
   them.

   .. tip::

      You can verify that your commits only include changes to the two
      files using the `diff` subcommand. You'll get something like the
      following:

      ::

         (ENV) $ git diff --stat origin/master
         docs/source/i524/technologies.rst | 10 ++++++++++
         docs/source/refs.bib              |  3 +++

#. You should now push your changes to your fork:

   ::

      (ENV) $ git push origin master

#. Finally, create a pull request by going to your fork on github.
   Underneath the green "Clone or download" button you should see a
   line that says ``Pull request``. Click ``Pull request`` and review
   your changes in the web browser. If you are satisfied, click the
   green "Create Pull Request".

   .. tip::

      Fill out the subject line in the same format you make your
      commits, e.g: ``new:usr: Added technology YOUR_TECHNOLOGY to
      techlist``.


..
   Tips
   ----

   1. Why do I not see that my changes are published on the Web page?

      Changes will take time to be reviewed and integrated into the Web

      page. Changes will be done in two steps. First, they will be merged
      into the branch I524. Later, your changes will be merged into the
      master branch. You will see your changes in the master branch.

   2. How do I know if I did it right?

      Check the https://github.com/cloudmesh/classes/pulls to see your
      pull request.
      When your changes were approved and merged with the master branch,
      your pull request will disappear.

   3. Create an upstrem synchronization

      First, make sure that git on your computer is configured properly. For example::

        $ git config --global user.name "Albert Zweistein"
        $ git config --global user.email albert.zweistein@gmail.com

      Fork this repository by clicking the "Fork" button on the top right
      of this page. You will be redirected to a new page. Verify that
      your github username is in the url. Eg:

      https://github.com/YOUR_GITHUB_USERNAME/classes
      Clone your forked repository::

        $ git clone git@github.com:YOUR_GITHUB_USERNAME/classes.git

      Add the upstream repository
      https://help.github.com/articles/configuring-a-remote-for-a-fork/ ::

        $ git remote add upstream https://github.com/cloudmesh/classes

      ..note:: You should frequently keep your fork up to date
               https://help.github.com/articles/syncing-a-fork/

      ::

         $ git fetch upstream
         $ git merge upstream/master

      You should also periodically push your changes to your fork::

         $ git push origin master


Learning outcomes
=================

1. CANVAS is not a tool used in open source development and
   industry. It has limitations in scalability and in structuring
   effective communication with large numbers of
   students/collaborators.

   Instead we use industry accepted github for homework submission. To
   showcase one way of collaborating with more than 70 collaborators
   we will use the class Web page to demonstrate how this can be
   achieved with forks and pull requests. The TAs are responsible for
   communication to you how to do this and are also organizing the
   merge of your pull requests into the Master Web page.

2. As you look over the list you get familiar with technologies of
   interest.

3. You will learn how not to plagiarize

4. You will learn how to create proper references for Web-pages while
   using academic bibliography management tools.
