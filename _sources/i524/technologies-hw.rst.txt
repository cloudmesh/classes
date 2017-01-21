.. _techlist-tips:

Requirements for the TechList Homework
=================================

1. Watch the video at https://www.youtube.com/watch?v=roi7vezNmfo

2. Create a fork into your local repo: e.g. Go to
   https://cloudmesh.github.io/classes/ and click on “Fork me on
   GitHub” to create a fork into your local repo
   
3. Go to your GitHub account and open the forked repository. 

        Click on “Clone or download” and “Open in Desktop” to download the file 
	directory on your local machine. Alternatively, you can find the files 
	in the browser, click on the pencil sign to “Edit this File”.
	You will update two files:
	
	#. add the paragraph about the technologies, go to classes/docs/source/i524/technologies.rst 
	#. your references, go to  /docs/source/refs.bib

        For the descriptions remove advertisement adjectives and 
	sentences from your description, and spellcheck. 

	For refrences it is important that every reference is required
	to have owner field. For example::

	  owner = {TA-sp17-0001}

        In case your entry is MISC the howpublished field refers to the
        method on how it is published. A urls are posted in its own
	field. For example::

	  howpublished = {Web Page}
	  url = {http://www.google.com}
	  
	
4. Do rebase or pull. 

5. To get credit for the assignment write your commit summary with your::

       new:usr: Meaningful summary of what you did

   For example for new contributions::

          new:usr: Added entry for Nagios in the technology list

   For example for changes contributions::

           chg:usr: Changed the entire paraagraph for Nagios in the technology list

   For example for fixed contributions::

           fix:usr: Changed spelling for Nagios in the technology list
	
6. Compile and commit if correct.

7. Review the changed files to make sure you only change the two
    files. If you have other changes create separate pull requests for
    them.
  
8. Finally, create a pull request (check if no new content conflict with yours)


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


Learning outcomes
-----------------

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
