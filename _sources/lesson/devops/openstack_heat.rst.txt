.. _ref-class-lesson-devops-openstack-heat:

OpenStack Heat
======================================================================

Overview
----------------------------------------------------------------------

This lesson will introduce you to a very important topic of OpenStack Heat, a
software provisioning tool on a OpenStack platform.

.. tip:: Duration: 1 hour

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have knowledge of

* `OpenStack for Beginners <../iaas/openstack.html>`_

Description
----------------------------------------------------------------------

OpenStack Heat is an open source software to deploy services within OpenStack
clouds. Heat launches VM instances, installs cloud software and manages
required resources such as security groups or floating ip addresses within a
resource group, a stack. You just need to describe your cloud services and
resources in a Heat Template file, and OpenStack deploys your cloud services by
provisioning cloud infrastructure and installing/configuring software. Through
this lesson, you will learn how to write a Heat Template file and how to deploy
your cloud applications with a command line tool or a web interface. OpenStack
Heat Orchestration Template (HOT) is compatible with AWS CloudFormation
template format, there are some extensions of Heat Templates though. If you
have AWS templates, you can use them on OpenStack as well to start your cloud
services.

This lesson covers:

* Basics of OpenStack Heat
* Use of Heat Client Tool
* How to write Heat Template
* Example of deploying Hadoop Cluster with Heat

Let's start with the basics of OpenStack Heat.

Resource Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Heat creates a stack with a combination of resources. The following resource
types are the most common items to start or connect each other, we may see
often how they are deployed and interact.

* Nova Server (VM instance)
* Floating IP addresses
* Volumes (Storage)
* Security Groups
* Key Pair

There are 70 resource types in total. See more at:
http://docs.openstack.org/hot-reference/content/openstack-resource-types.html

These are OpenStack Heat Resource types which are identified with the ``OS::`` prefix.
For example, if you'd like to start a VM instance, use the ``OS::Nova::Server`` resource type.

There are also Amazon CloudFormation compatible resource types.

Resource Types (Amazon compatible)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These resource types are exchangeable between Amazon (AWS) and OpenStack. Let's
review a few types.

* ``AWS::EC2::Instance``: EC2 Instance <-> Nova Server 
* ``AWS::EC2::SecurityGroup``: EC2 Security Group <-> OpenStack Security Group
* ``AWS::EC2::Volume``: AWS Elastic Block Store volume <->  OpenStack Cinder
  Volume

Currently, 25 resource types are compatible with AWS, AWS supports 88 resource
types on Amazon Cloud though.

For more information, 

* find supported AWS resource types on OpenStack:
  http://docs.openstack.org/hot-reference/content/cloudformation-compatible-resource-types.html

* see a full list of  AWS resource types:
  http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html

Template in YAML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OpenStack Heat templates are written in a YAML file format which is easy to
read and write.  The following template is an example of a launching a VM
server with Ubuntu 14.04 image and 1 vCPU and 2GB memories (m1.small flavor).

::

        heat_template_version: 2013-05-23

        description: Simple template to deploy a single compute instance on FutureSystems

        resources:
          my_instance:
            type: OS::Nova::Server
            properties:
              key_name: albert-india-key
              image: futuresystems/ubuntu-14.04
              flavor: m1.small

Heat template starts with a ``heat_template_version`` key to indicate supported
features and resource types. The following values are supported:

* 2013-05-23: supports features until the Icehouse release.
* 2014-10-16: supports features until the Juno release.
* 2015-04-30: supports features until the Kilo release.

Use of OpenStack Heat on FutureSystems
-------------------------------------------------------------------------------

We start learning OpenStack Heat on india.futuresystems.org. You can use Heat
on FutureSystems via a web interface Horizon or a command line tool (Heat CLI).
On a Horizon dashboard, graphical resource topology is displayed and relations
of connected resources are also presented in a canvas. If you use command line
tools, various command options (which might not be visible on a web) and
debugging messages are available.

Horizon on FutureSystems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Horizon on FutureSystems is at:
https://openstack-j.india.futuresystems.org/horizon/project/

For more details of Horizon:
`OpenStack Web Dashboard (Horizon) <../iaas/openstack_horizon.html>`_

Heat Client Tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you'd like to use Heat Client Tool (heat CLI), you
simply run the following commands on india.futuresystems.org::

  module load openstack
  source $HOME/.cloudmesh/clouds/india/juno/openrc.sh

.. note:: If you run OpenStack Havana, try the following commands::
  
     module load openstack-havana;
     module load heatclient;
     source $HOME/.cloudmesh/clouds/india/havana/novarc;


``module load openstack`` enables Heat CLI on your shell.

Stack List
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can see running stacks with the following command:

::

   $ heat stack-list
   +----+------------+--------------+---------------+
   | id | stack_name | stack_status | creation_time |
   +----+------------+--------------+---------------+
   +----+------------+--------------+---------------+

A ``stack`` is cloud resources that you use with your selected Heat Template. If
you deployed 5 VM instances with 2 floating IP addresses and 1 security group,
all of these resources fall into a single stack on OpenStack.

Stack Creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need a template first. Save a sample template above in a YAML file, e.g.
``openstack_heat_ex1.yaml`` It will create a new VM instance with a ``Ubuntu
14.04`` image, ``albert-india-key`` SSH keypair and a ``m1.small`` flavor.  You
have to **REPLACE** ``albert-india-key`` with your registered keyname.

If you are ready to create a new stack, run a following command:

::

  heat stack-create --template-file openstack_heat_ex1.yaml heat-tutorial-$OS_USERNAME

* You started a stack with a parameter for a template file ``--template-file``.
* ``heat-tutorial-$OS_USERNAME`` is a your stack name, you can use other names.

.. note:: If you have a template file on the web, you can use a URL with
          ``--template-url`` parameter.

The sample output is::

  +--------------------------------------+------------+--------------------+----------------------+
  | id                                   | stack_name | stack_status       | creation_time        |
  +--------------------------------------+------------+--------------------+----------------------+
  | a6c98d15-f569-426b-a364-46bcca831049 | heat-tut...| CREATE_IN_PROGRESS | 2015-04-02T06:15:56Z |
  +--------------------------------------+------------+--------------------+----------------------+

As you can see your stack is being processed. You can see more details with the following command::

  heat stack-show heat-tutorial-$OS_USERNAME
  
The output looks like::

  +----------------------+----------------------------------------------------------------------------+
  | Property             | Value                                                                      |
  +----------------------+----------------------------------------------------------------------------+
  | capabilities         | []                                                                         |
  | creation_time        | 2015-04-02T06:15:56Z                                                       |
  | description          | Simple template to deploy a single compute instance on FutureSystems       |
  | disable_rollback     | True                                                                       |
  | id                   | a6c98d15-f569-426b-a364-46bcca83104                                        |
  | links                | http://xxx.futuregrid.org:xxx/v1/.../stacks/../.. (self)                   |
  | notification_topics  | []                                                                         |
  | parameters           | {                                                                          |
  |                      |   "OS::stack_id": "a6c98d15-f569-426b-a364-46bcca83104",                   |
  |                      |   "OS::stack_name": "heat-tutorial-albert",                                |
  |                      |   "instance_type": "m1.small",                                             |
  |                      |   "image_id": "futuresystems/ubuntu-14.04",                                |
  |                      |   "key_name": "albert-india-key"                                           |
  |                      | }                                                                          |
  | parent               | None                                                                       |
  | stack_name           | heat-tutorial-albert                                                       |
  | stack_owner          | albert                                                                     |
  | stack_status         | CREATE_COMPLETE                                                            |
  | stack_status_reason  | Stack CREATE completed successfully                                        |
  | template_description | Simple template to deploy a single compute instance on FutureSystems       |
  | updated_time         | None                                                                       |
  +----------------------+----------------------------------------------------------------------------+

Stack List
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:: 

  heat stack-list [STACK_NAME]

If you have VM instances in your stack, you can see running instances.

::

  nova list


Stack Deletion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::
 
  heat stack-delete [STACK_NAME]

Samples of Heat Templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can find examples of the Heat templates.

https://github.com/openstack/heat-templates/blob/master/hot/


.. _ref-class-lesson-devops-openstack-heat-exercises:

Exercises
----------------------------------------------------------------------

Exercise I
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Try to create a two VM instances with the following conditions:

  - futuresystems/ubuntu14.04
  - m1.small
  - Port 22, 80, and 443 are open

  - Save your OpenStack Heat template in ``$USERNAME_heat_ex1.yaml``

  .. tip::

     The following documents will be useful:

     - `Heat Orchestration Template (HOT) Specification <http://docs.openstack.org/developer/heat/template_guide/hot_spec.html#hot-spec>`_
     - `Heat Orchestration (HOT) Guide <http://docs.openstack.org/developer/heat/template_guide/hot_guide.html>`_
     - `OpenStack Researce Types <http://docs.openstack.org/hot-reference/content/openstack-resource-types.html>`_

       - `OS::Neutron::SecurityGroup <http://docs.openstack.org/hot-reference/content/OS__Neutron__SecurityGroup.html>`_
       - `OS::Neutron::Port <http://docs.openstack.org/hot-reference/content/OS__Neutron__Port.html>`_

     - `Sample Heat template <https://github.com/futuresystems/class-bigdata-technology-spring-2015/blob/master/heat-template.yaml>`_

Exercise II
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Start a WordPress web service using Heat template on the web. The required
  conditions are:

  - Use `Template for WordPress on Fedora21 <https://raw.githubusercontent.com/cloudmesh/cloudmesh/dev2.0/heat-templates/fedora-21/wordpress.yaml>`_
  - Make sure to specify your key using the ``key_name`` parameter
  - Once you successfully created a WordPress stack, checkout the index page.
    ``curl -L http://[IP ADDRESS]/wordpress`` produces the index page in a text mode.
  - If your web browser opens the page properly, your WordPress is created successfully.

  .. tip::

     Examine the documentation for the ``heat`` subcommands
     ``stack-create`` and ``stack-show`` like so::

       $ heat help <subcommand>

     replacing ``<subcommand>`` as appropriate.

  .. tip::

     The IP address of your instance is listed as an output
     value. Make sure to examine your stack to get the location of the
     instance.


* Submission

  You will need to turn in a typescript of your terminal session.
  Do so by executing::

    $ script heat_ex2_$OS_USERNAME.typescript

  and then proceed with this exercise. Upon completion, make sure to
  type ``exit`` to end the typescripting. The contents of the session
  will be found in the ``heat_ex2_$OS_USERNAME.typescript`` file.



* If you'd like to use Horizon web dashboard, you need to find "Orchestration >
  Stacks" menu.

  - Make a screenshot of the page at ``Stacks > Topology``
  - Make a screenshot of the page at ``Stacks > Overview``
  - Make a screenshot of the page at ``Stacks > Resources``
  - Make a screenshot of the page at ``Stacks > Events``
  - Submit your screen shots.

Reference
-------------------------------------------------------------------------------

If you'd like to learn more about OpenStack Heat? Please follow the links
below:

* Heat Documentation: http://docs.openstack.org/developer/heat/
* Heat Template Guide:
  http://docs.openstack.org/developer/heat/template_guide/index.html

Glossary
-------------------------------------------------------------------------------

* Stack: A collection of instantiated resources that are defined in a single
  template.

* Template: An orchestration document that details everything needed to carry
  out an orchestration.

* Orchestration:
  Arrange or direct the elements of a situation to produce a desired effect.

* Resource:
  An element of OpenStack infrastructure instantiated from a particular
  resource provider.

More glossary are:
http://docs.openstack.org/developer/heat/glossary.html

Next Step
-------------------------------------------------------------------------------

In the next page, Ubuntu Juju will be discussed.

:ref:`Ubuntu Juju <ref-class-lesson-devops-juju>`
