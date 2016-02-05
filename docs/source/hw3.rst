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
   * the registered key,
   * and ``hw3-$OS_USERNAME`` vm name
   * Assign a Floating IP address
* Install required software on a virtual instance
   * virtualenv
   * pip
   * ansible
   * python-dev

.. note:: The two terms, VM or virtual instance, are exchangeable in this
        context.

Submission on IU GitHub (github.iu.edu)
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

Challenging Tasks (Optional with bonus points)
-------------------------------------------------------------------------------

The following tasks are optional but strongly recommended to try.

'Hello Big Data' Flask
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Find a ``flask`` directory in your assignment repository. We provide
``hello.py`` python file and you can run the file in your VM but there are a few
requirements that we request::

   * Use virtualenv named 'bdossp-sp16' in your home directory
   * Open a web port to the Flask application to allow access from outside

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

Cloud Management API (challenge task, optional, bonus points)
-------------------------------------------------------------------------------

4. libcloud

