HW2: Get Ready for FutureSystems
===============================================================================

Guidelines
-------------------------------------------------------------------------------

* Assignments must be completed individually.

Tasks
-------------------------------------------------------------------------------

Complete the following tasks. Place all answers in a file named HW2-$USERID.txt
and submit it via IU Canvas. (Replace $USERID with your email name at IU e.g.
HW2-albert.txt if your email address is albert@indiana.edu)

FutureSystems Access
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Sign Up portal.futuresystems.org, if not exist.
   Provide your portal ID in your submission.

2. Join a Class Project and provide a project number in your submission.

3. Generate a new SSH key and register on the portal.futuresystems.org.
   Provide your key fingerprint in your submission.

4. SSH into india.futuresystems.org with your registered key.
   Run the following command and attach the output messages (plain text) in your submission.
   (Most SSH client tools offer copy and paste option with a mouse from the screen)::

   finger $USER

GitHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

5. Sign up github.com with your SSH key.
   Provide your github.com ID in your submission.

6. Create a 'I590-Projects-BigData-Software' repository on your account. 
   Create 'hw2' branch.

7. This is a question for you to answer with appropriate git commands to
   satisfy the following descriptions.::

   Albert has some Python code files that he was developing on his local
   machine but he wanted to use github.com to trace changes and share his work
   with others. He already created a new repository named 'BigData' on his
   github account.  So he made a copy of the repository on his machine and
   there was nothing in the repo. He added a 'README.rst' file to describe his
   repository first. To make sure his description looks okay he pushed his
   update to github and opened a webpage to check.  When he get access to his
   repository on github.com via a web browser, he found that Contact Info was
   missing so he added the info in the `README.rst` file online using a web
   browser and the his description showed wih the new Contact Info. He returned
   to his local repository and updated his repository because he wanted to sync
   the changes that he made on github.com. His next task was adding
   `new_feature.py` and `bug.py` in a separate branch, not in master because he
   thought these two files are still in progress with different purposes. He
   simply created 'next' and 'error' branches in his current repository and
   added the two files accordingly.

List ``git`` commands that `Albert` used in his work above in your submission.

Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

8. Write a python program called fizzbuzz.py that accepts an integer n from the
   command line. Pass this integer to a function called fizzbuzz.
   The fizzbuzz function should then iterate from 1 to n. If the ith number is
   a multiple of two, print “fizz”, if a multiple of three print “buzz”, if a
   multiple of both print “fizzbuzz”, else print the value.

9. Create a 'hw2' branch on your github repository
   'I590-Projects-BigData-Software' and add fizzbuzz.py to the branch. Provide
   a clone URL for the branch in your submission.

