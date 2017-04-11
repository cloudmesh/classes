.. _single_public_ip_:

Use only one public IP address on Chameleon cloud
=================================================

Chameleon cloud has relatively limited public IP addresses. In order to avoid consuming all, we require you to use only one ``head`` virtual machine, which will have a public IP associated with. All other nodes needed for your project will be non-floating IP nodes, meaning that that don't have a public accessible IP address. You can only access these nodes from your ``head`` node.

Essentially, you just need to migrate the VirtualBox vm that you have used on your laptop to Chameleon cloud. Instead of have cloudmesh_client up and running on your VirtualBox vm, you re-setup everything on a public accessible (and the only) Chameleon node. From here, you execute all your script to configure your cluster. Because this ``head`` node is inside Chameleon cloud, those local IP addresses e.g. 192.168.x.x can be used to communicate.

Step 0. Remove all your cluster virtual machines from Chameleon
---------------------------------------------------------------

Make sure your terminate all your previously allocated resources.

Step 1. Create a single vm on Chameleon cloud
---------------------------------------------
::

    $ cm vm boot

Step 2. Assign a public IP address to this virtual machine
----------------------------------------------------------
::

    $ cm vm ip assign

Step 3. Configure this public accessible vm
-------------------------------------------
::

    $ cm vm ssh

Basically, you just repeat what you have done on your laptop, including:

    * sudo apt-get update
    * install supporting packages like: python-dev, libffi-dev, libssl-dev...
    * install tools like: pip, git and virtual environment
    * activate virtualenv
       
Step 4. Install cloudmesh_client
--------------------------------
Consult to earlier chapters to install cloudmesh_client again with ``git pull`` from your repo. Remember to:

    * upload your keys to home folder
    * update cloudmesh.yaml accordingly to set cloud, key and user

Step 5. Bring up your cluster in a private IP environment
-------------------------------------------------------
Consult to earlier chapters to once again set your cluster up. The outline is::

    $ cm cluster define --count 3 --no-floating-ip
    $ cm cluster allocate
    $ cm cluster nodes <your cluster name>
    $ cm vm ssh <node-name>

So now you can refer your nodes with their names, not the public IP addresses.