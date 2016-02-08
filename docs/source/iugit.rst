.. _ref-iu-github-for-assignments:

IU GitHub Guidelines for Assignments
===============================================================================

The course uses private IU GitHub repositories to collect online assignment 
submissions. The following instructions explain how to setup the private
repositories for the course projects.

Overview
-------------------------------------------------------------------------------

The ``assignments`` public repository contains assignment
descriptions and submission guidelines in each branch, for example, homework 3
is in the ``hw3`` branch. Each assignment is stayed in an individual branch. A
student creates a private repository in the course organization
**bdossp-sp16** and make a ``pull`` request with the template repository.
Required files and directories are added in a student private repository and
they are ready to make changes and submit solutions. Note that the name of the
repository should be IU Username e.g. albert if you have IU email address like
albert @ indiana.edu and should remain in private.

Instructions
-------------------------------------------------------------------------------

- Sign in with IU Account at https://github.iu.edu/
- Add a new/existing SSH Key at https://github.iu.edu/settings/ssh
- Find Course Organiization at
   https://github.iu.edu/orgs/bdossp-sp16
- Find your private repository named as IU Username:
  https://github.iu.edu/organizations/bdossp-sp16/USERNAME
.. note:: Report to Course Team if you can't find your repository
- Clone your private repository on your home directory on india.futuresystems.org,
and **REPLACE** USERNAME with your real IU Username: ::

     git clone git@github.iu.edu:bdossp-sp16/USERNAME.git

- Create a branch in your local that you'd like to work with, e.g. hw3 for homework 3::

     git branch hw3
     git checkout hw3

- Pull the template repository: https://github.iu.edu/orgs/bdossp-sp16/assignments.git
  ::
    
     git pull git@github.iu.edu:bdossp-sp16/assignments.git hw3

- Push your changes to remote once you completed tasks in assignments and
  committed your changes. : ::

     git push -u origin hw3

Useful Links
-------------------------------------------------------------------------------

* IU GitHub: https://github.iu.edu
