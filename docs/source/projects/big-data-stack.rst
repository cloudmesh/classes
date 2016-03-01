.. _ref-big-data-stacks:

big-data-stacks
===============================================================================

Description of possible projects
-------------------------------------------------------------------------------

Projects related to the hadoop stack consist of either extending the
functionality or using the current features.  This repository is intended to
define a simple, easily deployable, customizable, data analytics stack built on
hadoop.  Currently, deployment is done to a virtual cluster running on
OpenStack Kilo on FutureSystems.

Extending
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A non-exhaustive list of possible projects are currently listed `here
<https://github.com/futuresystems/big-data-stack/issues?q=is:issue+is:open+label:project>`_.
These include adding hbase, mahoot, storm, and others to the deployment
options.
The goal is for students to pick one or more of the projects listed here to
work on.  They can also propose a project by submitting an issue.

Steps required:

*       fork the big-data-stack repository
*       defining an ansible role for that addon
*       adding the role to the roles directory as a git submodule
*       define a playbook to deploy the role in the addons directory
*       submit a pull request to the unstable branch of the futuresystems
  repository

If the pull request is approved, then the ownership of the developed role will
need to be transferred to the futuresystems organization.

For example: adding mahout involves:

*       defining a repository called ansible-role-mahoot housing the ansible
        role code
*       adding this repo as a git submodule names roles/mahout
*       defining a playbook called addons/mahout.yml

Deployment should be accomplished using the following command::

        $ ansible-playbook play-hadoop.yml addons/mahout.yml

After which the user can ssh into the frontend node and use the software.

Using
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An alternative project involves using this hadoop stack to run some big data
analysis projects.  This could be as simple as the hadoop benchmarking
programs, or something more complex like twitter analysis, etc.

How to use issues
-------------------------------------------------------------------------------

Note that software addons are not limited to those currently listed as possible
projects under the github issues.  Students are free to propose alternative
projects, but they must do so by submitting an issue to the repository.  If it
is accepted, it will be added to the list of possible projects and assigned to
them

Requirements
-------------------------------------------------------------------------------

It is expected that students taking on projects to extend the hadoop stack are
familiar with distributed system, git, ansible, and installing and configuring
linux systems.  They are expected to work fairly autonomously under my
supervision.

