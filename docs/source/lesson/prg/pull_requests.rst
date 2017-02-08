Pull Requests
=============

A Pull Request is a way to propagate changes to an upstream repository.

.. graphviz::

   digraph PR {

     rankdir=LR;
     center=true;
     edge[spines=curved];

     "origin" -> "copy" [label="fork"];
     "copy" -> "copy" [label="commit changes"];
     "copy" -> "origin" [label="pull request"];

   }


Given an orign repository, and changes commited to the copy.
After some time, one may wish to propagate those change back to the origin.
By creating a Pull Request, the owner of the origin repository can view the changes, and can comment and ask for additional changes if necessary.


Procedure
---------

#. Go to the GitHub page of the origin repository
#. Fork it to your account
#. Clone your fork
#. Commit your changes
#. Synchronize any changes to the origin
#. Push to your fork
#. Create a pull request

Resources
---------


See GitHub's documentation for submitting pull requests `here
<https://help.github.com/categories/collaborating-with-issues-and-pull-requests/>`_.

In particular, pay attention to the following sections:

* `About forks <https://help.github.com/articles/about-forks>`_
* `Syncing a fork <https://help.github.com/articles/syncing-a-fork>`_
* `About Pull Requests <https://help.github.com/articles/about-pull-requests/>`_
* `Creating a pull request from a fork <https://help.github.com/articles/creating-a-pull-request-from-a-fork/>`_
