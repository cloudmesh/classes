.. _ref-github-for-project:

GitHub Guidelines for Projects
===============================================================================

The course uses FutureSystems GitHub repositories to collect online project
submissions. The following instructions explain how to setup the repositories
for the course projects.

Overview
-------------------------------------------------------------------------------

The ``master`` public repository contains pointers of project submissions for
the course when semester ends. ``master`` repository provides **READ** access
only to all team members (students) and changes can be merged by *pull request
(PR)*. The project has the following structure, for example::

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

*groups* directories are pointers, in the form of git submodules,
to the team member (student) forked individual repository.  When students are
ready to submit, they should fork/update, this repository, add their
submissions as a git submodule under *projects* and create a pull request. The
pull request should also include a short description, including any team
members if it is under projects, in the ``README.md`` file.

The ``template`` repository for final projects 
should be forked to contain actual code in the team member (student) forked
individual repository. 

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

- Find Course Organiization at
   https://github.com/orgs/futuresystems-courses/
- Fork the master repository: https://github.com/orgs/futuresystems-courses/s16-i590-master.git
- Fork the template repository: https://github.com/orgs/futuresystems-courses/s16-i590-template-project.git
- Work on the forked template repository in an individual account e.g.
   https://github.com/lee212/s16-i590-template-project.git
- Commit and push to sync changes
- Move to the master repository
- Add a submodule to the forked master repository, e.g.
   git submodule add https://github.com/lee212/s16-i590-template-project.git
- Commit and push to sync changes

Useful Links
-------------------------------------------------------------------------------

- `What is Fork? <https://help.github.com/articles/fork-a-repo/>`_
- `Git submodules <http://git-scm.com/book/en/v2/Git-Tools-Submodules>`_
- `Git pull requests <https://help.github.com/articles/using-pull-requests/>`_

