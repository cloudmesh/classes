
Using GitLab
======================================================================

This course requires the use of `GitLab.com <https://gitlab.com/>`_
for your homework submissions.

Once you have completed the entry survey you will be granted access to
a git repository in which to develop your homework submissions. What
you submit to canvas will be a link to a folder or file in your gitlab
repository.

The repository should consist of a subfolder in the root directory for
each assignment, e.g. ``prg1``, ``prg2``, ``project``, for programming
assignment 1, programming assignment 2 and your project.

.. important::

   The above are just examples. The assignment prompts will indicate
   the exact name for each subdirectory.  It is imperative that you
   adhere to the name that will be specified else you may have points
   deducted.

.. important:: Please use only lowercase characters in the directory
	       names and no special charaters such as @ ; /


Getting an account
----------------------------------------------------------------------

Please go to gitlab and create an account. Use a nice accountname that
only includes characters in [a-zA-Z0-9].

* http://gitlab.com

In canvas a list is published that shows your Homework-ID (HID). The
HID will be the name of the directory in gitlab that you will be using
to submit your homework.

Upload your public key
----------------------

Please upload your public key to the repository.


How to configere Git and Gitlab	for your computer
-------------------------------------------------

The proper way to use git is to install it on your computer. Once you have done
so, make sure to configure git to use your name and email address
label your commits.::

   $ git config --global user.name "Albert Einstein"
   $ git config --global user.email albert@iu.edu


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

Although we do not recommend using this, it is possible to use the Web
browser to modify existing and to upload new files via the Web
browser. This means you could operate it without installing anything.
This will work, but it is not very convenient.

Using Git GUI tools
-------------------

There are many git GUI tools available that directly integrate into
your operating system finders, windows, ..., or PyCharm.
It is up to you to identify such tools and see if they are useful for
you. Most of the people we work with us git from the commandline, even
if they use PyCharm or ther tools that have build in git suport.



Git Resources
----------------------------------------------------------------------

If you are unfamiliar with git you may find these resources useful:

- `Pro Git book <https://git-scm.com/book/en/v2>`_
- `Official tutorial <https://git-scm.com/docs/gittutorial>`_
- `Official documentation <https://git-scm.com/doc>`_
- `TutorialsPoint on git <http://www.tutorialspoint.com/git/>`_
- `Try git online <https://try.github.io>`_
- `GitHub resources for learning git <https://help.github.com/articles/good-resources-for-learning-git-and-github/>`_
- `Atlassian tutorials for git <https://www.atlassian.com/git/tutorials/>`_

Submission of homework
----------------------

You will have a HID givven to you. Let us assume the id is::

   F16-DG-9999

When you log into gitlab, you will find a directory with that
name. Please substitute the HID that we gave above as an example with
your own. We refer to thi ID as <HID> in these instructions.

Now you can go to your web browser and past the following URL into it,
wher eyou replace the <HID> with your HID.::

  https://gitlab.com/cloudmesh_fall2016/<HID>

For our example this would result in::

 https://gitlab.com/cloudmesh_fall2016/F16-DG-9999

.. note: naturally if you try the F16-DG-9999 URL it will not work ;-)

You will find in the directory subdirectories for your homework. If
they are missing, please create them. You will see::

  prg1
  prg2
  prg3
  paper1
  paper2
  paper3
  bib1

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
  
*If you lose any documents locally, you can retrieve them from your remote repository using::

  git pull
