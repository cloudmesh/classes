.. _ref-github-iu:

IU GitHub Guidelines
===============================================================================

The course uses private repositories to make online assignment submissions. The
following instructions explain how to setup private repositories for the
course.

Overview
-------------------------------------------------------------------------------

The ``master`` private repository contains pointers of assignments and project
submissions for the course when semester ends. ``master`` repository provides
**READ** access only to all team members (students) and changes can be merged
by *pull request (PR)*. The project, or an assignment has the following
structure, for example::

      s16-i590-master/
      \-- administrative/      
         \-- syllabus.md
         \-- grading.md
         \-- policy.md
         \-- FAQ.md
         \-- Contact.md
      \-- projects/
         \-- <group A> /
            \-- README.md
         \-- <group B> /
         \-- <group ...> /
      \-- HW3/
         \-- <user A> /
         \-- <user B> /
         \-- <user ...> /

*groups* or *users* directories are pointers, in the form of git submodules,
to the team member (student) forked private repository.  When students are
ready to submit, they should fork/update, this repository, add their
submissions as a git submodule under *projects* or *HW3* and create a pull request. The
pull request should also include a short description, including any team
members if it is under projects, in the ``README.md`` file.

The ``template`` private repository for final projects or assignments
should be forked to contain actual code in the team member (student) forked
private repository. 

The structure of the template repository looks like, if it is for project::

   s16-i590-template-project/
   \-- README.md
   \-- SUBMITTING.md
   \-- doc/                
      \-- README.md
   \-- src/             
      \-- README.md
   \-- data/
      \-- README.md
   \-- COPYING
   \-- LICENSE

Each student should have READ access to this repo with instructions
on usage in the ``SUBMITTING.md`` file. They should fork the repo, and
make sure to update the ``doc/README.md`` for the
report/documentation/etc, any code/scripts go into `src`, and any
other artifacts, such as input/intermediate data files go into
`data`. The `src` and `data` directories should include any specific
details about the contents of those sub-directories. Additionally,
anything submitted is done so under an open source license (the
`LICENSE` file) eg Apache or GPL, etc, with copying instructions in
`COPYING`. On forking this repository, the students will need to
grant at least READ privileges to the instructors and AIs.

Instructions
-------------------------------------------------------------------------------

- Sign in with IU Account at https://github.iu.edu/
- Add a new/existing SSH Key at https://github.iu.edu/settings/ssh
- Find Course Organiization at
   https://github.iu.edu/orgs/BDOSSPSpring2016
- Fork the master repository: https://github.iu.edu/orgs/BDOSSPSpring2016/master.git
- Fork the template repository: https://github.iu.edu/orgs/BDOSSPSpring2016/template.git
- Work on the forked template repository in an individual account e.g.
   https://github.iu.edu/albert/template.git
- Commit and push to sync changes
- Move to the master repository
- Add a submodule to the forked master repository, e.g.
   git submodule add https://github.iu.edu/albert/template.git
- Commit and push to sync changes


Useful Links
-------------------------------------------------------------------------------

- `What is Fork? <https://help.github.com/articles/fork-a-repo/>`_
- `Git submodules <http://git-scm.com/book/en/v2/Git-Tools-Submodules>`_
- `Git pull requests <https://help.github.com/articles/using-pull-requests/>`_


