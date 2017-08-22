Singularity
===========

::

    [USER@comet-dev ~]$ cat /etc/issue
    CentOS release 6.9 (Final)
    Kernel \r on an \m

    [USER@comet-dev ~]$ python --version
    Python 2.6.6

    [USER@comet-dev ~]$ module load singularity
    [USER@comet-dev ~]$ mkdir /dev/shm/cloudmesh
    [USER@comet-dev ~]$ cd /dev/shm/cloudmesh

    [USER@comet-dev cloudmesh]$ singularity pull docker://python:2.7.13
    Initializing Singularity image subsystem
    Opening image file: python-2.7.13.img
    Creating 1283MiB image
    Binding image to loop
    Creating file system within image
    Image is done: python-2.7.13.img
    Docker image path: index.docker.io/library/python:2.7.13
    Cache folder set to /home/USER/.singularity/docker
    Importing: base Singularity environment
    Importing: /home/USER/.singularity/docker/sha256:aghkjg....tar.gz
    Importing: /home/USER/.singularity/docker/sha256:bghkjg....tar.gz
    Importing: /home/USER/.singularity/docker/sha256:cghkjg....tar.gz
    Importing: /home/USER/.singularity/docker/sha256:dghkjg....tar.gz
    Importing: /home/USER/.singularity/docker/sha256:eghkjg....tar.gz
    Importing: /home/USER/.singularity/docker/sha256:fghkjg....tar.gz
    Importing: /home/USER/.singularity/docker/sha256:gghkjg....tar.gz
    Importing: /home/USER/.singularity/docker/sha256:hghkjg....tar.gz
    Importing: /home/USER/.singularity/metadata/sha256:ighkjg....tar.gz
    Done. Container is at: python-2.7.13.img


    [USER@comet-dev cloudmesh]$ sudo su
    [root@comet-dev cloudmesh]# module load singularity
    [root@comet-dev cloudmesh]# singularity exec --writable ./python-2.7.13.img pip install cloudmesh_client
    Collecting cloudmesh_client
     Using cached cloudmesh_client-4.7.2-py2.py3-none-any.whl
    Collecting python-novaclient==7.1.0 (from cloudmesh_client)
     Using cached python_novaclient-7.1.0-py2.py3-none-any.whl
    Collecting python-hostlist==1.17 (from cloudmesh_client)
    Collecting pyreadline==2.1 (from cloudmesh_client)
    Collecting azure-servicebus==0.20.1 (from cloudmesh_client)
     Using cached azure_servicebus-0.20.1-py2.py3-none-any.whl
    Collecting azure-mgmt-resource==0.20.1 (from cloudmesh_client)
     Using cached azure_mgmt_resource-0.20.1-py2.py3-none-any.whl
    Collecting enum34==1.1.6 (from cloudmesh_client)
     Using cached enum34-1.1.6-py2-none-any.whl
    Collecting pyparsing==2.1.10 (from cloudmesh_client)
     Using cached pyparsing-2.1.10-py2.py3-none-any.whl
    Collecting oslo.utils==3.22.0 (from cloudmesh_client)
     Using cached oslo.utils-3.22.0-py2.py3-none-any.whl
    Collecting pytz==2016.10 (from cloudmesh_client)
     Using cached pytz-2016.10-py2.py3-none-any.whl
    Collecting python-keystoneclient==3.10.0 (from cloudmesh_client)
     Using cached python_keystoneclient-3.10.0-py2.py3-none-any.whl
    Collecting humanize==0.5.1 (from cloudmesh_client)
    Collecting httpsig==1.1.2 (from cloudmesh_client)
     Using cached httpsig-1.1.2-py2.py3-none-any.whl
    Collecting azure-servicemanagement-legacy==0.20.2 (from cloudmesh_client)
     Using cached azure_servicemanagement_legacy-0.20.2-py2.py3-none-any.whl
    Collecting idna==2.2 (from cloudmesh_client)
     Using cached idna-2.2-py2.py3-none-any.whl
    Collecting azure-mgmt-network==0.20.1 (from cloudmesh_client)
     Using cached azure_mgmt_network-0.20.1-py2.py3-none-any.whl
    Collecting cryptography==1.7.2 (from cloudmesh_client)
    Collecting azure-mgmt-compute==0.20.1 (from cloudmesh_client)
     Using cached azure_mgmt_compute-0.20.1-py2.py3-none-any.whl
    Collecting apache-libcloud==1.5.0 (from cloudmesh_client)
     Using cached apache_libcloud-1.5.0-py2.py3-none-any.whl
    Collecting pyasn1==0.1.9 (from cloudmesh_client)
     Using cached pyasn1-0.1.9-py2.py3-none-any.whl
    Collecting Jinja2==2.8.1 (from cloudmesh_client)
     Using cached Jinja2-2.8.1-py2.py3-none-any.whl
    Collecting netifaces==0.10.5 (from cloudmesh_client)
    Collecting azure-nspkg==1.0.0 (from cloudmesh_client)
     Using cached azure_nspkg-1.0.0-py2.py3-none-any.whl
    Collecting oslo.serialization==2.16.0 (from cloudmesh_client)
     Using cached oslo.serialization-2.16.0-py2.py3-none-any.whl
    Collecting appdirs==1.4.0 (from cloudmesh_client)
     Using cached appdirs-1.4.0-py2.py3-none-any.whl
    Collecting azure-storage==0.20.3 (from cloudmesh_client)
     Using cached azure_storage-0.20.3-py2-none-any.whl
    Collecting MarkupSafe==0.23 (from cloudmesh_client)
    Collecting azure-mgmt==0.20.2 (from cloudmesh_client)
    Collecting functools32==3.2.3.post2 (from cloudmesh_client)
    Collecting pycparser==2.17 (from cloudmesh_client)
    Collecting nose==1.3.7 (from cloudmesh_client)
     Using cached nose-1.3.7-py2-none-any.whl
    Collecting azure-mgmt-storage==0.20.0 (from cloudmesh_client)
     Using cached azure_mgmt_storage-0.20.0-py2.py3-none-any.whl
    Collecting PyYAML==3.12 (from cloudmesh_client)
    Collecting msgpack-python==0.4.8 (from cloudmesh_client)
    Collecting pycrypto==2.6.1 (from cloudmesh_client)
    Collecting azure-mgmt-common==0.20.0 (from cloudmesh_client)
     Using cached azure_mgmt_common-0.20.0-py2.py3-none-any.whl
    Collecting ansible==2.2.1.0 (from cloudmesh_client)
    Collecting six==1.10.0 (from cloudmesh_client)
     Using cached six-1.10.0-py2.py3-none-any.whl
    Collecting colorama==0.3.7 (from cloudmesh_client)
     Using cached colorama-0.3.7-py2.py3-none-any.whl
    Collecting azure==1.0.3 (from cloudmesh_client)
    Collecting python-dateutil==2.6.0 (from cloudmesh_client)
     Using cached python_dateutil-2.6.0-py2.py3-none-any.whl
    Collecting requests==2.13.0 (from cloudmesh_client)
     Using cached requests-2.13.0-py2.py3-none-any.whl
    Collecting debtcollector==1.11.0 (from cloudmesh_client)
     Using cached debtcollector-1.11.0-py2.py3-none-any.whl
    Collecting pytest==3.0.6 (from cloudmesh_client)
     Using cached pytest-3.0.6-py2.py3-none-any.whl
    Collecting gitchangelog==2.4.1 (from cloudmesh_client)
    Collecting click==6.7 (from cloudmesh_client)
     Using cached click-6.7-py2.py3-none-any.whl
    Collecting wrapt==1.10.8 (from cloudmesh_client)
    Collecting funcsigs==1.0.2 (from cloudmesh_client)
     Using cached funcsigs-1.0.2-py2.py3-none-any.whl
    Collecting paramiko==2.1.1 (from cloudmesh_client)
     Using cached paramiko-2.1.1-py2.py3-none-any.whl
    Collecting SQLAlchemy==1.1.5 (from cloudmesh_client)
    Collecting sandman==0.9.8 (from cloudmesh_client)
     Using cached sandman-0.9.8-py2-none-any.whl
    Collecting Babel==2.3.4 (from cloudmesh_client)
     Using cached Babel-2.3.4-py2.py3-none-any.whl
    Collecting azure-common==1.1.4 (from cloudmesh_client)
     Using cached azure_common-1.1.4-py2.py3-none-any.whl
    Collecting pyaml==16.12.2 (from cloudmesh_client)
     Using cached pyaml-16.12.2-py2.py3-none-any.whl
    Collecting pbr==1.10.0 (from cloudmesh_client)
     Using cached pbr-1.10.0-py2.py3-none-any.whl
    Collecting simplejson==3.10.0 (from cloudmesh_client)
    Collecting cloudmesh-timestring==1.6.2.1 (from cloudmesh_client)
    Collecting packaging==16.8 (from cloudmesh_client)
     Using cached packaging-16.8-py2.py3-none-any.whl
    Collecting ipaddress==1.0.18 (from cloudmesh_client)
     Using cached ipaddress-1.0.18-py2-none-any.whl
    Collecting Flask==0.12 (from cloudmesh_client)
     Using cached Flask-0.12-py2.py3-none-any.whl
    Collecting future==0.16.0 (from cloudmesh_client)
    Collecting oslo.config==3.22.0 (from cloudmesh_client)
     Using cached oslo.config-3.22.0-py2.py3-none-any.whl
    Collecting netaddr==0.7.19 (from cloudmesh_client)
     Using cached netaddr-0.7.19-py2.py3-none-any.whl
    Collecting Flask-SQLAlchemy==2.1 (from cloudmesh_client)
    Collecting Flask-HTTPAuth==3.2.2 (from cloudmesh_client)
    Collecting prettytable==0.7.2 (from cloudmesh_client)
    Collecting positional==1.1.1 (from cloudmesh_client)
    Collecting docopt==0.6.2 (from cloudmesh_client)
    Collecting WTForms==2.1 (from cloudmesh_client)
    Collecting urllib3==1.20 (from cloudmesh_client)
     Using cached urllib3-1.20-py2.py3-none-any.whl
    Collecting Flask-Admin==1.4.2 (from cloudmesh_client)
    Collecting Werkzeug==0.11.15 (from cloudmesh_client)
     Using cached Werkzeug-0.11.15-py2.py3-none-any.whl
    Collecting cffi==1.9.1 (from cloudmesh_client)
     Using cached cffi-1.9.1-cp27-cp27mu-manylinux1_x86_64.whl
    Collecting futures==3.0.5 (from cloudmesh_client)
     Using cached futures-3.0.5-py2-none-any.whl
    Collecting monotonic==1.2 (from cloudmesh_client)
     Using cached monotonic-1.2-py2.py3-none-any.whl
    Collecting rfc3986==0.4.1 (from cloudmesh_client)
     Using cached rfc3986-0.4.1-py2.py3-none-any.whl
    Collecting iso8601==0.1.11 (from cloudmesh_client)
     Using cached iso8601-0.1.11-py2.py3-none-any.whl
    Collecting oslo.i18n==3.12.0 (from cloudmesh_client)
     Using cached oslo.i18n-3.12.0-py2.py3-none-any.whl
    Collecting py==1.4.32 (from cloudmesh_client)
     Using cached py-1.4.32-py2.py3-none-any.whl
    Collecting azure-mgmt-nspkg==1.0.0 (from cloudmesh_client)
     Using cached azure_mgmt_nspkg-1.0.0-py2.py3-none-any.whl
    Collecting jsonschema==2.5.1 (from cloudmesh_client)
     Using cached jsonschema-2.5.1-py2.py3-none-any.whl
    Collecting stevedore==1.20.0 (from cloudmesh_client)
     Using cached stevedore-1.20.0-py2.py3-none-any.whl
    Collecting itsdangerous==0.24 (from cloudmesh_client)
    Collecting keystoneauth1==2.18.0 (from cloudmesh_client)
     Using cached keystoneauth1-2.18.0-py2.py3-none-any.whl

     Requirement already satisfied: setuptools>=11.3 in
       /usr/local/lib/python2.7/site-packages (from
       cryptography==1.7.2->cloudmesh_client)

    Installing collected packages: pytz, Babel, pbr, six, oslo.i18n,
    wrapt, funcsigs, debtcollector, iso8601, netifaces, monotonic,
    netaddr, pyparsing, oslo.utils, msgpack-python,
    oslo.serialization, positional, requests, stevedore,
    keystoneauth1, prettytable, simplejson, python-novaclient,
    python-hostlist, pyreadline, azure-nspkg, azure-common,
    azure-servicebus, azure-mgmt-nspkg, azure-mgmt-common,
    azure-mgmt-resource, enum34, rfc3986, oslo.config,
    python-keystoneclient, humanize, pycrypto, httpsig,
    azure-servicemanagement-legacy, idna, azure-mgmt-network,
    ipaddress, pyasn1, pycparser, cffi, cryptography,
    azure-mgmt-compute, apache-libcloud, MarkupSafe, Jinja2, appdirs,
    futures, python-dateutil, azure-storage, azure-mgmt-storage,
    azure-mgmt, functools32, nose, PyYAML, paramiko, ansible,
    colorama, azure, py, pytest, gitchangelog, click, SQLAlchemy,
    docopt, itsdangerous, Werkzeug, Flask, WTForms, Flask-Admin,
    Flask-SQLAlchemy, Flask-HTTPAuth, sandman, pyaml,
    cloudmesh-timestring, packaging, future, urllib3, jsonschema,
    cloudmesh-client

    Successfully installed Babel-2.3.4 Flask-0.12 Flask-Admin-1.4.2
    Flask-HTTPAuth-3.2.2 Flask-SQLAlchemy-2.1 Jinja2-2.8.1
    MarkupSafe-0.23 PyYAML-3.12 SQLAlchemy-1.1.5 WTForms-2.1
    Werkzeug-0.11.15 ansible-2.2.1.0 apache-libcloud-1.5.0
    appdirs-1.4.0 azure-1.0.3 azure-common-1.1.4 azure-mgmt-0.20.2
    azure-mgmt-common-0.20.0 azure-mgmt-compute-0.20.1
    azure-mgmt-network-0.20.1 azure-mgmt-nspkg-1.0.0
    azure-mgmt-resource-0.20.1 azure-mgmt-storage-0.20.0
    azure-nspkg-1.0.0 azure-servicebus-0.20.1
    azure-servicemanagement-legacy-0.20.2 azure-storage-0.20.3
    cffi-1.9.1 click-6.7 cloudmesh-client-4.7.2
    cloudmesh-timestring-1.6.2.1 colorama-0.3.7 cryptography-1.7.2
    debtcollector-1.11.0 docopt-0.6.2 enum34-1.1.6 funcsigs-1.0.2
    functools32-3.2.3.post2 future-0.16.0 futures-3.0.5
    gitchangelog-2.4.1 httpsig-1.1.2 humanize-0.5.1 idna-2.2
    ipaddress-1.0.18 iso8601-0.1.11 itsdangerous-0.24 jsonschema-2.5.1
    keystoneauth1-2.18.0 monotonic-1.2 msgpack-python-0.4.8
    netaddr-0.7.19 netifaces-0.10.5 nose-1.3.7 oslo.config-3.22.0
    oslo.i18n-3.12.0 oslo.serialization-2.16.0 oslo.utils-3.22.0
    packaging-16.8 paramiko-2.1.1 pbr-1.10.0 positional-1.1.1
    prettytable-0.7.2 py-1.4.32 pyaml-16.12.2 pyasn1-0.1.9
    pycparser-2.17 pycrypto-2.6.1 pyparsing-2.1.10 pyreadline-2.1
    pytest-3.0.6 python-dateutil-2.6.0 python-hostlist-1.17
    python-keystoneclient-3.10.0 python-novaclient-7.1.0 pytz-2016.10
    requests-2.13.0 rfc3986-0.4.1 sandman-0.9.8 simplejson-3.10.0
    six-1.10.0 stevedore-1.20.0 urllib3-1.20 wrapt-1.10.8


    [root@comet-dev cloudmesh]# exit
    exit


    [USER@comet-dev cloudmesh]$ mv python-2.7.13.img cloudmesh_client-4.7.2.img
    [USER@comet-dev ~]$ ls -lh /dev/shm/cloudmesh/cloudmesh_client-4.7.2.img
    -rwxr-xr-x 1 USER USER 1.3G Jun  9 21:07 /dev/shm/cloudmesh/cloudmesh_client-4.7.2.img


    [USER@comet-dev ~]$ singularity exec /dev/shm/cloudmesh/cloudmesh_client-4.7.2.img cat /etc/issue
    Debian GNU/Linux 8 \n \l


    [USER@comet-dev ~]$ singularity exec /dev/shm/cloudmesh/cloudmesh_client-4.7.2.img python --version
    Python 2.7.13


    [USER@comet-dev ~]$ singularity exec /dev/shm/cloudmesh/cloudmesh_client-4.7.2.img cm version
    ~/.cloudmesh/cloudmesh.yaml created
    Model created
    ERROR: Please define a key first, e.g.: cm key add --ssh <keyname>
    +------------------+---------+
    | name             | version |
    +------------------+---------+
    | python           | 2.7.13  |
    | pip              | 8.1.2   |
    | cloudmesh_client | 4.7.2   |
    | git hash         |         |
    +------------------+---------+
    You are running a supported version of python: 2.7.13
    You are running a supported version of pip: 8.1.2


    [USER@comet-dev ~]$ singularity exec /dev/shm/cloudmesh/cloudmesh_client-4.7.2.img cm comet init
    Initializing the comet configuration file...
    Set a default username (RETURN to skip):
    Set the active service endpoint to use. The availalbe endpoints are - dev/production [dev]:
    Set the base url for the nucleus dev service [https://comet-nucleus-dev.sdsc.edu/nucleus]:
    Set the api version for the nucleus dev service [v1]:
    Authenticating to the nucleus dev service and obtaining the apikey...
    Comet nucleus username [TBD]: USER
    Password:
    api key retrieval and set was successful!


    [USER@comet-dev ~]$ singularity exec /dev/shm/cloudmesh/cloudmesh_client-4.7.2.img cm comet ll
    +-------+---------+-------+------------------+---------------+---------------+-----------+-------------+-------------+
    | Name  | Project | Count | Nodes            | Frontend (Fe) | State (Fe)    | Type (Fe) | allocations | Description |
    +-------+---------+-------+------------------+---------------+---------------+-----------+-------------+-------------+
    | vc8   | ddp280  | 0     |                  | vc8           | nostate-error | VM        | ddp280      |             |
    | vct03 | ddp280  | 4     | vm-vct03-[00-03] | vct03         | nostate-error | VM        | ddp280      |             |
    | k8s   | sys200  | 16    | vm-k8s-[00-15]   | k8s           | nostate-error | VM        | sys200      |             |
    | vct06 | sys200  | 7     | vm-vct06-[00-06] | vct06         | nostate-error | VM        | sys200      |             |
    | vct01 | ddp280  | 2     | vm-vct01-[00-01] | vct01         | nostate-error | VM        | ddp280      |             |
    |       |         |       |                  |               |               |           | sds166      |             |
    +-------+---------+-------+------------------+---------------+---------------+-----------+-------------+-------------+


This is faster than installing a new Python version, setuptools and
pip then creating a virtualenv to pip install cloudmesh_client into
and not a bad way to build/test with arbitrary OS support/Python
versions.


