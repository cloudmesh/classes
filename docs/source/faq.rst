.. contents:: :depth: 2


FAQ
===============================================================================


How to ask a question
-------------------------------------------------------------------------------

When submitting a questions please:

#. copy/paste directly from the terminal into the email message.
   Do not send text files, zipfiles, or other attachments as they may be not be opened.
   Screen grabs *may* be acceptable if you annotate the relevant parts using an image editor, or they are integral to showing the problem.

#. use the mailing list (bdosspcoursehelp@googlegroups.com) to direct questions as all support staff are subscribed.
   Direct message via Slack is discouraged.

#. describe the specific step you are trying to accomplish, include the actions you took and the results.
   Ensure that you can reproduce your problem by executing only the steps present in your email.
   Also include:

   - your futuresystems username
   - the output of ``nova show MY_VM`` (replacing ``MY_VM`` appropriately)

   For example:

   ::

      I cannot ssh into my VM due to permission denied errors:

      $ ssh user@machine
      Permission denied (publickey,hostbased).

      I tried following the steps in the FAQ as defined here: https://...
      <SHOW THE COMMANDS AND THEIR OUTPUT> 


      Relvant information is:

      Username: albert
      $ nova show MY_VM
      +--------------------------------------+----------------------------------------------------------+
      | Property                             | Value                                                    |
      +--------------------------------------+----------------------------------------------------------+
      | accessIPv4                           |                                                          |
      | accessIPv6                           |                                                          |
      | config_drive                         |                                                          |
      | created                              | 2016-03-29T19:35:41Z                                     |
      | fg491-net network                    | 10.0.5.22, 149.165.159.241                               |
      | flavor                               | m1.large (4)                                             |
      | hostId                               | 683eed6c03fcc23879620b6042eaaa22149d915bfcd4ec9e5feab7c5 |
      | id                                   | 60dc4420-e5c0-4897-9a58-2cd48d6521b0                     |
      | image                                | CentOS7 (dc5c041f-7881-441e-af91-e9620efde901)           |
      | key_name                             | india                                                    |
      | metadata                             | {}                                                       |
      | name                                 | $USER-myvmname                                           |
      | os-extended-volumes:volumes_attached | []                                                       |
      | progress                             | 0                                                        |
      | security_groups                      | default                                                  |
      | status                               | ACTIVE                                                   |
      | tenant_id                            | 74e411d6d99e4497901d4c4e2b159f41                         |
      | updated                              | 2016-03-29T19:35:56Z                                     |
      | user_id                              | 090ea72e85c94c49ad8cc8133627fa1a                         |
      +--------------------------------------+----------------------------------------------------------+




Why can't I ``ssh`` into my VM?
-------------------------------------------------------------------------------

#. Make sure to boot using on the internal network **first**. Once the node is up, **then** attach the floating ip.

   ::

      $ NET_ID=$(nova net-list | grep $OS_PROJECT_NAME | cut -d' ' -f2)
      $ nova boot --nic net-id=$NET_ID      # ... etc
      $ nova floating-ip-list | grep ' - '  # find an available floating ip.
      $ # create a floating ip with nova floating-ip-create if there are no floating ips available
      $ nova floating-ip-associate          # ... etc

#. If your VM is on the 10.1.x.y it is accessible:

   - from outside the subnet with a floating ip only
   - from inside the 10.1.x.y subnet

   Check ip of your VM(s) with

   ::

      $ nova show $USER-myvmname | grep network

#. Make sure you can ping your VM:

   ::

      $ ping -c 5 $IP

#. Make sure that the machine have finished boot by checking that ssh daemon is listening on port 22:

   ::

      $ nc -zv $IP 22
      Connection to 149.165.158.1 22 port [tcp/ssh] succeeded!

#. Make sure you are trying to log in with the correct username.
   For Ubuntu VMs, the username is ``ubuntu``; for CentOS use ``centos``.

   For example, to log into an Ubuntu VM:

   ::

      $ ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ubuntu@$IP

#. If you are still unable to ssh, try a hard reboot a few times:

   ::

      $ nova reboot --hard $USER-myvmname

#. Check that you have an ssh key registered with openstack using ``nova keypair-list`` and make note of the fingerprint:

   ::

      $ nova keypair list
      +----------------+-------------------------------------------------+
      | Name           | Fingerprint                                     |
      +----------------+-------------------------------------------------+
      | india          | 41:29:20:a2:51:25:5d:66:71:02:15:b6:cd:e2:36:06 |
      +----------------+-------------------------------------------------+

#. Check that the correct key name was passed to ``nova boot`` when starting the VM by using ``nova show``:

   ::

      $ nova show $USER-myvmname
      +--------------------------------------+----------------------+
      | Property                             | Value                |
      +--------------------------------------+----------------------+
      # ...
      | key_name                             | india                |
      # ...
      +--------------------------------------+----------------------+

#. Ensure that the fingerprint matches:

   ::

      $ ssh-keygen -lf ~/.ssh/id_rsa
      2048 41:29:20:a2:51:25:5d:66:71:02:15:b6:cd:e2:36:06 ~/.ssh/id_rsa.pub

#. Make sure that the key was injected into the VM during the startup by grabbing the console log and searching for your fingerprint. Make sure to wait for a few minutes after ``nova boot`` to allow the node start up:

  ::

     $ nova console-log $USER-myvmname | grep -A 2 -B 4 '41:29:20:a2:51:25:5d:66:71:02:15:b6:cd:e2:36:06'
     ci-info: ++++++Authorized keys from /home/centos/.ssh/authorized_keys for user centos+++++++
     ci-info: +---------+-------------------------------------------------+---------+-----------+
     ci-info: | Keytype |                Fingerprint (md5)                | Options |  Comment  |
     ci-info: +---------+-------------------------------------------------+---------+-----------+
     ci-info: | ssh-rsa | 41:29:20:a2:51:25:5d:66:71:02:15:b6:cd:e2:36:06 |    -    |           |
     ci-info: +---------+-------------------------------------------------+---------+-----------+

If, after going through these steps, you are still unable to access the VM, delete the VM and try again two or three times, waiting a few minutes between each attempt.
OpenStack is a collection of many distributed systems, and the nature of distributed systems is that they can be prone to random failure.

If you are still unable to log in, please contact us and indicate that you have gone through these steps, and show the output of the above commands.

Why can't I modify my ``~/.ssh/authorized_keys`` file?
-------------------------------------------------------------------------------

You can not manually manage your ``authorized_keys`` file on ``india`` for security reasons.
If you need to change your ssh key, do so via the ``SSH keys`` tab on your `Web Portal Account <https://portal.futuresystems.org/user>`_.

Why does my MongoDB deployment fail?
-------------------------------------------------------------------------------

In this case: mongodb is installed successfully, but the service cannot be started.
Solving this is the goal of the assignment, which is demonstrating an important aspect of many development processes: namely the affects of changing infrastructure.

To put this in context: Ubuntu for many years (through the 14.04 LTS release) used the `Upstart`_ init daemon.
As of 15.04, this is switched to `systemd`_.
However, the mongodb installation expects to use Upstart to run the service, which therefore fails.

There are many solutions to this type of problem:

#. add the system service file by hand

#. rollback the OS from Ubuntu 15.04 to 14.04

#. use a different repository which includes the systemd service file

For the purposes of this homework, the first option is taken, and the service file is provided in the repository.
As the `hw instructions say <https://github.iu.edu/bdossp-sp16/assignments/tree/hw5#hw5-tasks>`_ place the `provided service file <https://github.iu.edu/bdossp-sp16/assignments/blob/hw5/mongodb.service.j2>`_ in the appropriate location.

If, after deploying the service file you are still unable to start the mongodb service, please include the contents of ``/lib/systemd/system/mongodb.service`` in your email.


.. _Upstart: http://upstart.ubuntu.com/
.. _systemd: https://freedesktop.org/wiki/Software/systemd/


One common issue is the user the mongodb service runs as: you should make sure that the username in the service file matches the user account created for mongodb.

- Check the username in the service file by looking at the ``User`` value.
- Check the username on the system by ``grep -i mongo /etc/passwd``

If these two values do not match, adjust your ansible deployment.



Using Chameleon Cloud
--------------------------------------------------------------------------------

You can find documentation on how to migrate from India (Futuresystems) OpenStack to Chameleon cloud here:
https://github.com/futuresystems/class-admin-tools/blob/master/chameleon/big-data-stack.org

Make sure you follow these instructions.

Regarding some common questions about switching to and using Chameleon, here are some tips if you are having trouble:

General
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. there is so far **no** evidence that chameleon is experiencing the same load problems that india is
#. make sure you **don't** source **anything** under ``~/.cloudmesh/``
#. make sure you **do** source the ``CH-817724-openrc.sh`` file
#. make sure you enter your password in correctly
#. make sure that running ``nova list`` works as a sanity check (if not, try steps 2, 3 again)
     As there is **no confirmation or denial** that your password is entered correctly or incorrectly, you should test using ``nova list`` to ensure authentication is possible. Make sure you have **not** sourced **anything** under ``~/.cloudmesh/clouds/...`` as this will corrupt the environment nova uses to authenticate to chameleon.

Differences between Chameleon and India:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. the username to log into the VM is different: use ``cc`` instead of ``ubuntu``
#. you cannot log into the internal IP address (192.X.Y.Z). You **must** associate a floating ip address first
#. the ubuntu image is called ``CC-Ubuntu14.04`` instead of ``Ubuntu-14.04-64``.

BDS on Chameleon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are using the `Big Data Stack <https://github.com/futuresystems/big-data-stack>`_, you need to make the following changes as well to tell BDS to use the Chameleon-specific environment instead of india:


#. update ``.cluster.py`` to use the ``CC-Ubuntu14.04`` image (as per `here <https://github.com/futuresystems/class-admin-tools/blob/master/chameleon/big-data-stack.org#setup-instructions>`_)
#. set "create_floating_ip" to "True" in .cluster.py (as per `here <https://github.com/futuresystems/class-admin-tools/blob/master/chameleon/big-data-stack.org#setup-instructions>`_)
#. set the user to ``cc`` in ``ansible.cfg`` (as per `here <https://github.com/futuresystems/class-admin-tools/blob/master/chameleon/big-data-stack.org#setup-instructions>`_)

SSH problems with Chameleon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you experience trouble ssh-ing into a Chameleon instance, make sure that the fingerprint of the key injected into the instance (get it with ``nova console-log $VM_NAME``) matches the one you are using (default is ``~/.ssh/id_rsa`, use ``ssh-keygen -lf $PATH_TO_KEY`` to see it).

