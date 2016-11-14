.. _openstack_horizon_lesson:

OpenStack Horizion Web Dashboard
===============================================================================

On FutureSystems, we have a web interface for OpenStack cloud management,
OpenStack Horizon. It supports most functionality that you can use to manage
cloud resources via commannd line tools such as Nova Compute CLI with graphical
illustration.

Overview
-------------------------------------------------------------------------------

OpenStack Horizon is a GUI for managing OpenStack cloud. It is mainly developed
by a open source web application framework, Django and Python. Some of the
JavasScript and CSS libraries are also included such as, jQuery, AngularJS, D3,
Font-Awesome, Jasmine, Qunit, Rickshaw, etc.

Source code of Horizon (GitHub)
-------------------------------------------------------------------------------

If you are interested in Horizon Source code, visit:
GitHub: https://github.com/openstack/horizon

Horizon on FutureSystems
-------------------------------------------------------------------------------

.. list-table:: Horizon endpoints
   :header-rows: 1
   :widths: 10,10,10,10,30

   * - Image
     - Version
     - Machine
     - Protocol
     - Description
   * - |image-horizon| 
     - Kilo
     - India_OpenStack_Kilo_
     - Native OpenStack
     - GUI for OpenStack

Getting Started
-------------------------------------------------------------------------------

* Open the following URL:
  India_OpenStack_Kilo_

* Use ``OS_USERNAME`` and ``OS_PASSWORD`` as a User Name and Password on Horizon.
  You can find your ``OS_USERNAME`` and ``OS_PASSWORD`` in the
  ``~/.cloudmesh/clouds/india/kilo/openrc.sh``

.. note:: If you are using other versions of OpenStack on FutureSystems,
          try to find your identity file with the following pattern of the path.
          ``$HOME/.cloudmesh/clouds/[cloud host]/[openstack version]/[openrc.sh or novarc.sh]``

:: 

   $ cat ~/.cloudmesh/clouds/india/kilo/openrc.sh
   export OS_USERNAME=albert
   export OS_PASSWORD=**********
   export OS_TENANT_NAME=fg465
   export OS_AUTH_URL=https://i5r.idp.iu.futuregrid.org:5000/v2.0
   export OS_CACERT=~/.cloudmesh/clouds/india/kilo/cacert.pem

* Select a project that you would like to use at the project selection link at
  the top left-hand corder of the page next to the OpenStack title image.

* Choose a component that you would like to use among Compute, Network, or
  Orchestration.

Usage Summary
-------------------------------------------------------------------------------

The Overview page in the Compute tab shows current usage of OpenStack cloud
resources on your account.  You can also have a summary reports for a certain
period to see resource utilization, for example, how many VM instances were
being used, or how many IP addresses were allocated.

Exercises
-------------------------------------------------------------------------------

* Try other features on Horizon.
   - See detailed information of your virtual server.
   - Attach a floating ip address to your virtual server and confirm it is
     accessible.

.. important::

   To find your password, find the ``OS_PASSWORD`` field in your openrc.sh.
   See the comment above for details.


.. _India_OpenStack_Kilo: https://openstack.futuresystems.org/horizon


.. |image-horizon| image:: /images/fg-horizon.png 
   :width: 100px 

