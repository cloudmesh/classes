.. _ref-class-lesson-devops-saltstack-ex1-output:  

Full Message of ``salt-call`` Execution
-------------------------------------------------------------------------------

::

  [INFO    ] Loading fresh modules for state activity
  [INFO    ] Fetching file from saltenv 'base', ** done ** 'top.sls'
  [INFO    ] Creating module dir '/var/cache/salt/minion/extmods/modules'
  [INFO    ] Syncing modules for environment 'base'
  [INFO    ] Loading cache from salt://_modules, for base)
  [INFO    ] Caching directory '_modules/' for environment 'base'
  [INFO    ] Creating module dir '/var/cache/salt/minion/extmods/states'
  [INFO    ] Syncing states for environment 'base'
  [INFO    ] Loading cache from salt://_states, for base)
  [INFO    ] Caching directory '_states/' for environment 'base'
  [INFO    ] Creating module dir '/var/cache/salt/minion/extmods/grains'
  [INFO    ] Syncing grains for environment 'base'
  [INFO    ] Loading cache from salt://_grains, for base)
  [INFO    ] Caching directory '_grains/' for environment 'base'
  [INFO    ] Creating module dir '/var/cache/salt/minion/extmods/renderers'
  [INFO    ] Syncing renderers for environment 'base'
  [INFO    ] Loading cache from salt://_renderers, for base)
  [INFO    ] Caching directory '_renderers/' for environment 'base'
  [INFO    ] Creating module dir '/var/cache/salt/minion/extmods/returners'
  [INFO    ] Syncing returners for environment 'base'
  [INFO    ] Loading cache from salt://_returners, for base)
  [INFO    ] Caching directory '_returners/' for environment 'base'
  [INFO    ] Creating module dir '/var/cache/salt/minion/extmods/outputters'
  [INFO    ] Syncing outputters for environment 'base'
  [INFO    ] Loading cache from salt://_outputters, for base)
  [INFO    ] Caching directory '_outputters/' for environment 'base'
  [INFO    ] Creating module dir '/var/cache/salt/minion/extmods/utils'
  [INFO    ] Syncing utils for environment 'base'
  [INFO    ] Loading cache from salt://_utils, for base)
  [INFO    ] Caching directory '_utils/' for environment 'base'
  [INFO    ] Loading fresh modules for state activity
  [INFO    ] Fetching file from saltenv 'base', ** done ** 'webserver.sls'
  [INFO    ] Running state [apache2] at time 18:40:25.136294
  [INFO    ] Executing state pkg.installed for apache2
  [INFO    ] Executing command ['dpkg-query', '--showformat', '${Status} ${Package} ${Version} ${Architecture}\n', '-W'] in directory '/home/ubuntu'
  [INFO    ] Executing command 'apt-get -q update' in directory '/home/ubuntu'
  [INFO    ] Executing command ['apt-get', '-q', '-y', '-o', 'DPkg::Options::=--force-confold', '-o', 'DPkg::Options::=--force-confdef', 'install', 'apache2'] in directory '/home/ubuntu'

  [INFO    ] Executing command ['dpkg-query', '--showformat', '${Status} ${Package} ${Version} ${Architecture}\n', '-W'] in directory '/home/ubuntu'
  [INFO    ] Installed Packages:
  httpd changed from absent to 1
  libapr1 changed from absent to 1.5.0-1
  libaprutil1-ldap changed from absent to 1.5.3-1
  apache2-api-20120211 changed from absent to 1
  libaprutil1 changed from absent to 1.5.3-1
  apache2-data changed from absent to 2.4.7-1ubuntu4.4
  apache2 changed from absent to 2.4.7-1ubuntu4.4
  libaprutil1-dbd-sqlite3 changed from absent to 1.5.3-1
  httpd-cgi changed from absent to 1
  ssl-cert changed from absent to 1.0.33
  apache2-bin changed from absent to 2.4.7-1ubuntu4.4

  [INFO    ] Loading fresh modules for state activity
  [INFO    ] Completed state [apache2] at time 18:41:23.121157
  local:
  ----------
  ID: apache2
  Function: pkg.installed
  Result: True
  Comment: The following packages were installed/updated: apache2.
  Started: 18:40:25.136294
  Duration: 57984.863 ms
  Changes:
  ----------
  apache2:
  ----------
  new:
  2.4.7-1ubuntu4.4
  old:

  apache2-api-20120211:
  ----------
  new:
  1
  old:

  apache2-bin:
  ----------
  new:
  2.4.7-1ubuntu4.4
  old:

  apache2-data:
  ----------
  new:
  2.4.7-1ubuntu4.4
  old:

  httpd:
  ----------
  new:
  1
  old:

  httpd-cgi:
  ----------
  new:
  1
  old:

  libapr1:
  ----------
  new:
  1.5.0-1
  old:

  libaprutil1:
  ----------
  new:
  1.5.3-1
  old:

  libaprutil1-dbd-sqlite3:
  ----------
  new:
  1.5.3-1
  old:

  libaprutil1-ldap:
  ----------
  new:
  1.5.3-1
  old:

  ssl-cert:
  ----------
  new:
  1.0.33
  old:


  Summary
  ------------
  Succeeded: 1 (changed=1)
  Failed:    0
  ------------
  Total states run:     1
