HW3: OpenStack Exercise
===============================================================================

Guidelines
-------------------------------------------------------------------------------

* Assignments must be completed individually.
* Discussion is allowed (e.g. via Slack) but the submission should be made by
  yourself. Acknowledge your helpers/collaborators name in the submission if
  you discussed or got help from anyone.
* Use an individual github repository. A repository in FutureSystems will be
  given later.

OpenStack Command Line Tool ``nova``
-------------------------------------------------------------------------------

OpenStack Kilo is ready to use (as of 02/04/2016) on FutureSystems and you will
have a virtual instance (server) using OpenStack Command Line Tool ``nova``, if
you complete all the tasks in this assignment. The tasks you need to complete
are:

* SSH into india.futuresystems.org and
   * enable ``nova`` command
* Register a SSH key on OpenStack
   * ``rsa`` type
   * with default key file names 
      - public: ``$HOME/.ssh/id_rsa.pub``
      - private: ``$HOME/.ssh/id_rsa``
   * passphrase enabled
* Start a single instance:
   * on ``fg491`` project
   * with a ``m1.small`` flavor,
   * a ``Ubuntu-15.10-64`` image,
   * the registered key above,
   * and ``hw3-$OS_USERNAME`` vm name
   * Assign a Floating IP address
* Install required software on a virtual instance
   * virtualenv
   * pip
   * ansible

.. warning:: Do not terminate your instance, if you completed and submitted
        hw3.

Test Program
-------------------------------------------------------------------------------

We provide ``hw3.py`` test file in your repository. Run this on
india.futuresystems.org, if you completed all tasks above. All available tests
should be passed without errors. How to run? simply run this on your ssh
terminal::

        python hw3.py

Completed all? You may see::

        ...........
        ----------------------------------------------------------------------
        Ran 11 tests in 1.646s

        OK

Find ``hw3-results.txt`` file after you ran ``hw3.py`` python program in your
current directory. Add this file in your IU GitHub repository.

Submission via IU GitHub (github.iu.edu)
-------------------------------------------------------------------------------

From now on, we will use IU GitHub to submit assignments on a private
repository. :ref:`IU GitHub Guidelines <ref-github-iu>`

1. Clone your private repository from the course organization.
   You IU Username is the name of your repository.

2. Create a ``hw3`` branch ::

   git branch hw3
   git checkout hw3

3. Run ``pull`` command to fetch and merge with the template repository::

   git pull git@github.iu.edu:BDOSSPSpring2016/assignments.git hw3

4. Merge the template::

   git commit -am "initial merge with the template"

5. Add ``hw3-results.txt`` to your repository::

   git add hw3-results.txt

5. Commit your changes

6. Sync with remote::

   git push origin hw3

Challenging Tasks (Optional)
-------------------------------------------------------------------------------

The following tasks are optional but strongly recommended to try. These are
related to **Python** packages and APIs (application program interface).
OpenStack ``nova`` is also extended to get more experience.

'Hello Big Data' Flask Web Framework
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Find a ``flask`` sub-directory in ``challange`` directory in your assignment
repository.  We provide ``hello.py`` python file and you can run the file in
your VM but there are a few requirements that we request::

   * Use virtualenv named 'bdossp-sp16' in your home directory
   * Open a web port to the Flask application to allow access from outside

.. note:: The two terms, VM or virtual instance, are exchangeable in this
        context.

1. What command(s) do you run to create and enable the virtualenv?
2. ``python hello.py`` may not work if you run only with standard python
   libraries. What command(s) do you run to resolve the issue? (hint. Flask is
   not a Python standard package)
3. If you ran the application successfully, you can see 'Hello Big Data'
   message on your web browser with the ``15000`` web port.  However, it is not
   accessible from outside e.g. http://IP_ADDRESS:15000.  It is because that
   there is no rule for the port in OpenStack Security Group. (We assume there
   is no firewall here). What ``nova`` command(s) do you need to create/add a
   security group for the port?
4. ``flask`` rule is provided in *fg491* project. What ``nova`` command(s) do
   you need to see current rule(s) in the security group and to apply it to
   your VM?

Write your solution in the name of ``flask-sol.txt`` text file after completing
the tasks above. 

Example view of your submission::

  1. albert
  2. ...
  3. ...
  9. http://... 

.. comment::

        Writing a script
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        Find a `hw3-script` directory in your assignment repository. We provide a template
        bash script named ``hw3-

        Cloud Management API (libcloud)
        -------------------------------------------------------------------------------


Useful links
-------------------------------------------------------------------------------

* Python lesson:
  http://bdossp-spring2016.readthedocs.org/en/latest/lesson/linux/python.html

* OpenStack Beginners:
  http://bdossp-spring2016.readthedocs.org/en/latest/lesson/iaas/openstack.html

* OpenStack QuickGuide:
  http://bdossp-spring2016.readthedocs.org/en/latest/lesson/quickstart_openstack.html

* OpenStack Operations Guide: 
  http://docs.openstack.org/openstack-ops/content/user_facing_operations.html
