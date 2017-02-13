Installing Cloudmesh Client on Ubuntu 16.04
===========================================

First install cloudmesh client using pip and make sure you
install the latest updates. 

Step 1 : Installation Cloudmesh Client
--------------------------------------
Install cloudmesh client using pip ::
   
  pip install -U cloudmesh_client

In order to make sure cloudmesh is running properly, enter cm in your command line.
It will show a terminal in the following way. 

::
   
   cm> 

Step 2 : Setting Up Profile
---------------------------

Now cloudmesh is installed locally. In order to run a virtual
machine in chameleon cloud, there are few configurations that
has to be done. 

You can find the configuration information in the following
location.

http://cloudmesh.github.io/client/configuration.html

After setting up cloudmesh client locally, the yaml file 
can be opened by running the following command. You can use
vim or vi instead of emacs to run this. ::

  emacs ~/.cloudmesh/cloudmesh.yaml

examples : 
::
   vim ~/.cloudmesh/cloudmesh.yaml
   vi ~/.cloudmesh/cloudmesh.yaml
   gedit ~/.cloudmesh/cloudmesh.yaml

First the profile section must be updated as follows. 
::
   
   profile:
          firstname: TBD
          lastname: TBD
          email: TBD
          user: TBD


example configuration
::

   profile:
        firstname: Vibhatha	
        lastname: Abeykoon
        email: vibhatha@gmail.com
        user: vibhatha

This must be filled when working on Cloudmesh set up.
And this can be found in the configuration file in cm- yaml file.


Step 3 :Setting Up Chamellion Cloud
-----------------------------------

In the cloudmesh.yaml file, set chameleon cloud as the active cloud
as shown below. Locate the attribute value in the 
::
   
   active:
    - chameleon

Go to the following link and you can find the information regarding,
the chameleon cloud setup. 

http://cloudmesh.github.io/client/configuration.html#chameleon-cloud

The following parameters has to be replaced with correspoding values.
::
   
   OS_PASSWORD: TBD
   OS_TENANT_NAME: TBD
   OS_TENANT_ID: TBD
   OS_PROJECT_NAME: TBD
   OS_USERNAME: TBD


example configuration
::
   OS_PASSWORD: NOTMYPASSWORD
   OS_TENANT_NAME: CH-818664
   OS_TENANT_ID: CH-818664
   OS_PROJECT_NAME: CH-818664
   OS_USERNAME: vibhatha


Make sure the TENANT_NAME: CH-818664.
You must be a member of the project in the Chameleon cloud, in order to 
gain access to the virtual machines. 

Note : Replace all TBD values with correct values (only in profile section and chameleon cloud section).


http://cloudmesh.github.io/client/configuration.html#chameleon-cloud

Make sure you are following the above url.
And after replacing all the TBD values, the confiuguration should look like
as follows.


Step 4 : Setting Up Virtual Machine
-----------------------------------

Run the following commands one by one.

First set up chameleon as the default cloud.
::
$ cm default cloud=chameleon

Information about the configurations can be retrieved by the following command. 
::
$cm info

Then add the ssh key to the cloudmesh database by running the following command.
And make sure, you have already generated a ssh key and the same ssh key will be
added to the database.
::
$ cm key add --ssh

Upload the key to the chameleon cloud.
::
$ cm key upload

Upload the security group to the chameleon cloud.
::
$ cm secgroup upload


Step 5 : Boot Virtual Machine
-----------------------------

Run the following command to boot the virtual machine. 
::
$ cm vm boot


Additional Info:
You can run the following commands to view the security groups
and virtual machines running. 
::
$ cm secgroup list
$ cm vm list


Step 6 : Run Virtual Machine
----------------------------

Execute the following command to run the virtual machine.
First assign a floating ip.
::
$ cm vm ip assign

Run the virtual machine.
::
$ cm vm ssh

After a successful launch it will show a similar console as shown below.
::
cc@hostname$-


Step 7 : Remove Virtual Machine

To delete a virtual machine, run the following command.
::
$ cm vm delete <name_of_vm>

Example :
::
$ cm vm delete vibhatha-001

Note :

No inside directories, just create everythin in the home directory.
Or a work directory in the home directory. Make sure work in the same
directory when executing commands. And make sure you are in the right directory 
when you are executing commands. We do this in order to minimize complications 
and add the correct cloudmesh.yaml file for the task.You should edit the right way.
(never use cd when doing this)

