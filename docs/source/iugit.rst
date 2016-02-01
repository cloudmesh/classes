.. _ref-iu-github-for-assignments:

IU GitHub Guidelines for Assignments
===============================================================================

The course uses private IU GitHub repositories to collect online assignment 
submissions. The following instructions explain how to setup the private
repositories for the course projects.

Overview
-------------------------------------------------------------------------------

The ``template-assignments`` public repository contains assignment
descriptions and submission guidelines in each branch, for example, homework 3
is in the ``hw3`` branch. Each assignment is stayed in an individual branch. A
student creates a private repository in the course organization
**BDOSSPSpring2016** and make a ``pull`` request with the template repository.
Required files and directories are added in a student private repository and
they are ready to make changes and submit solutions. Note that the name of the
repository should be IU Username e.g. albert if you have IU email address like
albert@indiana.edu and should remain in private.

Instructions
-------------------------------------------------------------------------------

- Sign in with IU Account at https://github.iu.edu/
- Add a new/existing SSH Key at https://github.iu.edu/settings/ssh
- Find Course Organiization at
   https://github.iu.edu/orgs/BDOSSPSpring2016
- Create a private individual repository with IU Username:
  https://github.iu.edu/organizations/BDOSSPSpring2016/repositories/new
- Clone your private repository on your local machine, and **REPLACE** USERNAME
  with your real IU Username: ::

     git clone git@github.iu.edu:BDOSSPSpring2016/USERNAME.git

- Create a branch in your local that you'd like to work with, e.g. hw2 for homework 2::

     git branch hw2
     git checkout hw2

- Pull the template repository: https://github.iu.edu/orgs/BDOSSPSpring2016/template-assignments.git
  ::
    
     git pull git@github.iu.edu:BDOSSPSpring2016/template-assignments.git hw2

- Push your changes to remote once you completed tasks in assignments and
  committed your changes. : ::

     git push origin hw2

Useful Links
-------------------------------------------------------------------------------


