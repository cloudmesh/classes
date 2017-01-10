Vagrant
======================================================================

.. sidebar:: Page Contents

   .. contents::
      :local:


What is Vagrant?
----------------------------------------------------------------------

Vagrant is an important tool for software development: it provides
reproducible environments in which to develop, test, and run software.

How it works
----------------------------------------------------------------------

Vagrant uses a file call ``Vagrantfile`` in the local directory to
control the installation and configuration of machines. Upon execution
of the ``vagrant up`` command, Vagrant initializes a virtual machine
based on the provided box, applies any specified provisioning, and
configures SSH for access.

As an example, consider the following `Vagrantfile
<https://github.com/cloudmesh/cloudmesh/blob/master/vagrant/Vagrantfile>`_
which is part of the cloudmesh repository.

::
    
     # IMPORTANT
     #
     # In order for this configuration to properly work you need to set
     # environmental variables:
     #
     # - PORTALNAME: your username on FutureSystems
     # - PROJECTID: the project you are associated with
     ##
     # Make sure that ssh-agent is running properly in order to access
     # futuresystems.
     # $ eval `ssh-agent`
     # $ ssh-add ~/.ssh/id_rsa
     # $ echo $SSH_AGENT_PID # check that this is set
     #
     # Example usage:
     # $ export PORTALNAME=albert
     # $ export PROJECTID=fg101
     # $ eval `ssh-agent`
     # $ ssh-add ~/.ssh/id_rsa
     # $ vagrant up
     
     PORTALNAME = ENV['PORTALNAME']
     PROJECTID  = ENV['PROJECTID']
     
     $script = <<SCRIPT
     
     set -o xtrace  # trace commands
     set -o errexit # stop if something fails
     
     # parameters for install, configure, start scripts
     export portalname=#{PORTALNAME}
     export projectid=#{PROJECTID}
     export venv=$HOME/ENV
     
     # install system deps and cloudmesh
     curl -s https://raw.githubusercontent.com/cloudmesh/get/master/cloudmesh/ubuntu/14.04.sh | bash
     
     # make sure to activate virtualenv
     source $venv/bin/activate
     
     # configure
     curl -s https://raw.githubusercontent.com/cloudmesh/get/master/cloudmesh/configure.sh | bash
     
     # start
     curl -s https://raw.githubusercontent.com/cloudmesh/get/master/cloudmesh/start.sh | bash
     
     # update bashrc
     echo "" >>~/.bashrc
     echo "source $venv/bin/activate" >>~/.bashrc
     
     SCRIPT
     
     VAGRANTFILE_API_VERSION = "2"
     
     Vagrant.configure(2) do |config|
       config.vm.box = "ubuntu/trusty64"
       config.vm.box_check_update = true
       config.vm.network "private_network", ip: "192.168.33.10"
       config.vm.provision "shell", privileged: false, inline: $script
     
       # Forward ssh-agent so that `cm-iu fetch` will work without needing
       # to copy the ssh keypair onto the VM
       # In order for this to work you need to:
       # $ eval `ssh-agent`
       # $ ssh-add ~/.ssh_id
       config.ssh.forward_agent = true;
     
     end


Let us look at what it does.  Comments begin with the ``#`` symbol and
are for documentation purposes only.  In this case, the instructions
tell us the setup that needs to be done before running ``vagrant up``.

Next, the environmental variables ``PORTALNAME`` and ``PROJECTID`` are
retrieved and injected into a provisioning shell script defined and
stored in ``$script``.

The rest of the file is fairly straightforward:

- use the ``ubuntu/trusty64`` box as the base system to run
- we want to make sure that the most up-to-date box is used so we
  enable automatic update checks
- the machine should not be accessible from the network (though it
  does have network access) to we set the IP address in a private
  network.
- the provisioning shell script is specified and will run as an
  unpriviledged user
- finally, use the ssh-agent forwarding system. This way the ssh
  keypairs for futuresystems access do not need to be copied into from
  the host machine into the workstation.

At this point running ``vagrant up`` will download the
``ubuntu/trusty64`` box if it is not already present, boot the
machine, and execute the provisioning script. The user can then run
``vagrant ssh`` to log into the machine and run any desired tests.
  

Boxes
----------------------------------------------------------------------

We have seen the use of the Ubuntu 14.04 (``ubuntu/trusty64``) box as
a base image for Vagrant to use. Many other options for boxes are
`publicly available
<https://atlas.hashicorp.com/boxes/search?provider=virtualbox>`_.


Provisioners
----------------------------------------------------------------------

Additionally, there are other options for provisioning the machines
managed by Vagrant. In addition to shell, Ansible and many others are
supported (see the `provisioning index
<https://docs.vagrantup.com/v2/provisioning/index.html>`_)


Providers
----------------------------------------------------------------------

By default, Vagrant uses VirtualBox to manage machines. Other options
are available such as VMWare or Docker.  Additionally, the design of
Vagrant's software architecture allows plugins to be built to support
alternative custom providers.  For instance, plugins for `Amazon Web
Services <https://github.com/mitchellh/vagrant-aws>`_, as well as
`OpenStack <https://github.com/cloudbau/vagrant-openstack-plugin>`_
are available to install.


How to get it
----------------------------------------------------------------------

Visit `Installing Vagrant <https://docs.vagrantup.com/v2/installation/index.html>`_.
