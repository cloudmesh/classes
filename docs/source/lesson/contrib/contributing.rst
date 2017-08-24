Contributing
============

Contributing content to this web page is easy. First, you have to fork
the repository while going to the link:

* https://github.com/cloudmesh/classes

And press the fork icon. Now you can clone or directly manipulate your
fork from the web browser. If you clone, you need to make sure you
clone from your fork.

We assume you use Python 3.6.1

Next, you can cd to the `classes` directory and make the
modifications. Check them locally with::

  pip install -r requirements.txt
  make html 
  make view

To change things you can simply edit files in the docs/source
directory. Commit the changes and push them into your local fork. Now
you can create on the web page for the classes a pull request.

If accepted the request will be merged and you will be credited via
your github account. Make sure you use git config to set your name and e-mail.


Please also make sure you do not confuse GitHub and gitlab. While this
web page is located in GitHub, your activities for the class are done
in gitlab.

Using GitHub
------------

These instructions assume that you are using Gitbash, not the GUI.

Open up Gitbash in your classes directory.

First you need to initialize your directory for use with Git.
	``git init``

Next you need to set your user name and email to get credit for your work.
	``git config --global user.name "Firstname Lastname``
	``git config --global user.email yourusername@iu.edu``

Next you need to pull the information down from your forked repository.
You'll need to enter your Github username and password when prompted.
	``git pull https://github.com/username/classes``

With all the files downloaded to your local directory, you can begin editing
the rst files with a plain text editor.

When you have changes to commit to the repository, you'll first have to set
the origin for the changes. You only need to do this the first time you commit
changes, so don't worry about this step every time you push your changes.
	``git remote add origin https://github.com/username/classes.git``

Now you're ready to add the files you changed.
	``git add -A``

Then commit the changes with a meaningful comment explaining what you did.
	``git commit -m "A message indicating what you changed"``

Finally you can push your changes up to Github.
	``git push -u origin master``
	
Once you've done that, open up a browser and go to your forked project on Github.
When you've verified that the changes are there, you can issue a pull request for
your work to be integrated into the original repository by clicking the "Pull Request"
field in the right hand corner beneath the topics.

Exercise
--------

Contrib.1:
   Identify a spelling error on the web page or another item
   to improve. Fork the Web page, fix the error and create a pull request.

Contrib.2:
   Identify a section that is not covered by this material, but could
   be useful. Add such a section and create a pull request so your
   contribution can be added. Work with others that review your
   section before submitting so we make sure no one else is working on
   this already. If they do we bring you in contact with them.

Contrib.3:
   How do you clone from your fork? What is the difference betweem
   your fork and the main repository? How do you identify it is your
   fork you clone from?
   
