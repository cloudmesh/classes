.. _ref-chalemelon:

..
  COMMENT

  This page is a copy of
  https://github.com/futuresystems/class-admin-tools/blob/master/chameleon/big-data-stack.org
  prepared by Badi

Chameleon Cloud
===============================================================================

Chameleon Cloud provides OpenStack Cloud with KVM or Baremetal for developing
with the Big Data Stack. https://www.chameleoncloud.org/ Chameleon Cloud
provides an environment for experimenting with cloud environments.  This class
does not support use of Chameleon cloud for any assignment or project work but
computing resources may be available upon request with limited access and
allocation.

  There are some differences between FutureSystems OpenStack and Chameleon
  OpenStack.

  - different login usernames (``cc`` for all instead of ``ubuntu``,
    ``centos``, etc) for the images
  - limited resource availability
  - resource usage is charged to a finite allocation (thus you need to
    terminate your instances if you do not use them).

Getting Access
-------------------------------------------------------------------------------

** Closed as of 08/02/2016 **

  1. Create an account on [[https://www.chameleoncloud.org/][Chameleon Cloud]]
  2. Send your Chameleon username to <course email>
     Note: the subject *MUST* be
     #+BEGIN_EXAMPLE
     Chameleon Cloud Access
     #+END_EXAMPLE
  3. We will then add you to the project for this course. *IMPORTANT*: you will
       not be able to use Chameleon until you are added. We will reply to your
       request with a confirmation email.

Setup Instructions
-------------------------------------------------------------------------------

  1. ssh into ``india.futuresystems.org``
  2. Go to the
       `Chameleon Cloud OpenStack Dashboard
       <https://openstack.tacc.chameleoncloud.org/dashboard/project/access_and_security/>`_
       and download the openrc file (check under the ``API Access`` tab)

  3. Upload the openrc file to the ``india`` node::
     $ scp CH-817724-openrc.sh $PORTALID@india.futuresystems.org:~
  4. Upload your india ssh key to your `profile on github.com
       <https://github.com/settings/ssh>`_::
     albert@i136 ~ $ cat ~/.ssh/id_rsa.pub
  5. Source the openrc file (*only* the chameleon openrc file)::
     albert@i136 ~ $ source ~/CH-817724-openrc.sh
  6. Load the OpenStack module (same as with kilo on india)::
     albert@i136 ~ $ module load openstack

  At this point you the nova commands will control Chameleon.

Big Data Stack
-------------------------------------------------------------------------------
  You can now follow the `Big Data Stack Readme
  <https://github.com/futuresystems/big-data-stack>`_ for starting and
  deploying your BDS

Notes
-------------------------------------------------------------------------------

``apt`` related errors

  You may occasionally get an error when one of the tasks calls to apt, either
  to update the cache or install packages.  This will likely manifest as a
  ``Failed to fetch`` with an ``Error 403 Forbidden`` error.  The root cause
  for this is not yet known, but it seems related to a network saturation
  issue.  Nonetheless, the workaround is simple: rerun the playbook that
  failed.  This may need to be repeated a few times, but this has been
  sufficient to resolve the issue when I encounter them.
