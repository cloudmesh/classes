How to copy your image from Havana to Juno
=====================================

Description
-----------

The steps to copy your image from Havana to Juno goes like this;

- **Step 1.** Setup OpenStack Havana environment
- **Step 2.** Download image
- **Step 3.** Setup OpenStack Juno environment
- **Step 4.** Upload image

Step 1. Setup OpenStack Havana environment
-----------------------------------------

Load ``openstack-havana`` module::

    $ module load openstack-havana

Set environment variables for OpenStack Havana::

    $ source ~/.futuregrid/openstack_havana/novarc

Step 2. Download image
----------------------

Check the list of images by the following command, and find the name or id of
the image you want to copy to Juno.::

    $ nova image-list
    +--------------------------------------+-------------------------------------+--------+--------------+
    | ID                                   | Name                                | Status | Server       |
    +--------------------------------------+-------------------------------------+--------+--------------+
    | aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee | normanrockwell/custom-ubuntu-14.04  | ACTIVE | xxxxxxx-.... |
    | ffffffff-gggg-eeee-hhhh-iiiiiiiiiiii | normanrockwell/custom-centos-6.5    | ACTIVE | yyyyyyy-.... |
    +--------------------------------------+-------------------------------------+--------+--------------+

I'll pick ``normanrockwell/custom-ubuntu-14.04`` as an example, so the command to
download the image is like this::

    $ glance download-image normanrockwell/custom-ubuntu-14.04 \
        --file custom-ubuntu-14.04.img

Make sure your image is downloaded successfully::

    $ ls -lh custom-ubuntu-14.04.img
    -rw-r--r-- 1 nrockwell users 1.5G Apr  3 11:45 custom-ubuntu-14.04.img

Step 3. Setup OpenStack Juno environment
----------------------------------------

Load ``openstack`` (Juno) module::

    $ module load openstack

Setup environment variables for OpenStack Juno::

    $ source ~/.cloudmesh/clouds/india/juno/openrc.sh

Step 4. Upload image
--------------------

Upload the image with this::

    $ glance image-create \
        --name="normanrockwell/custom-ubuntu-14.04" \
        --disk-format qcow2 \
        --container-format bare \
        --file custom-ubuntu-14.04.img

::

    +------------------+--------------------------------------+
    | Property         | Value                                |
    +------------------+--------------------------------------+
    | checksum         | 7287f3cee8be2f153bda74eb01185ccb     |
    | container_format | bare                                 |
    | created_at       | 2015-04-03T17:24:21                  |
    | deleted          | False                                |
    | deleted_at       | None                                 |
    | disk_format      | qcow2                                |
    | id               | c22a81a1-5476-41a6-843f-7eebd33614ed |
    | is_public        | False                                |
    | min_disk         | 0                                    |
    | min_ram          | 0                                    |
    | name             | normanrockwell/custom-ubuntu-14.04   |
    | owner            | 8c251fab06b84ba3a62607194f4abff9     |
    | protected        | False                                |
    | size             | 1609629696                           |
    | status           | active                               |
    | updated_at       | 2015-04-03T17:24:35                  |
    +------------------+--------------------------------------+

Make sure the image is on the list::

    $ nova image-list|grep normanrockwell/custom-ubuntu-14.04
    | xxxxxxxx-yyyy-zzzz-wwww-zzzzzzzzzzzz | normanrockwell/custom-ubuntu-14.04 | ACTIVE |       |

You should `try the image <http://cloudmesh.github.io/introduction_to_cloud_computing/iaas/openstack.html#booting-an-image>`_,
and if everything looks good, then delete the image file::

    $ rm custom-ubuntu-14.04.img
