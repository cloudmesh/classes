Contributing
============

.. note:: We assume you are using a Linux or OSX operating system. If
          you use WIndows, you can use virtual box and install for
          example ubuntu 16.04.
   
Contributing content to this web page is easy. First, you have to **fork**
the repository while going to the link:

* https://github.com/cloudmesh/classes

And press the fork icon. Now you can clone or directly manipulate your
fork from the web browser. If you clone, you need to make sure you
clone from your fork.

We assume you use Python 3.6.2. If not please find instructions on how
to install it. We recommend that you use pyenv so yo ucan install
multiole python environments.

Next, you can cd to the `classes` directory and make the
modifications. Check them locally with::

  pip install -r requirements.txt
  make
  make view

To change things you can simply edit files in the docs/source
directory. Commit the changes and push them into your **local fork**. Now
you can create on the web page for the classes a pull request.

If accepted the request will be merged and you will be credited via
your github account. Make sure you use git config to set your name and
e-mail. Please remember that pull requests are merged by a human and
it will take time. This is not an instantemeous action.


Exercise
--------

Contrib.1:
   Identify a spelling error on the web page or another item
   to improve. Fork the Web page, fix the error and create a pull request.

Contrib.2:
   Identify a section that is not covered by this material, but could
   be useful. Add such a section and create a pull request so your
   contribution can be added. Work with others that review your
   section before submitting so we make sure no one else is working on
   this already. If they do we bring you in contact with them.

Contrib.3:
   How do you clone from your fork? What is the difference betweem
   your fork and the main repository? How do you identify it is your
   fork you clone from?
   
Contrib.4:
   We use the creation of the class Web site on your computer to
   benchmark your machine. This benchmark will be used as part of some
   class assignments. To do so execute the follwoing and write
   down/copy the times you get::

     make clean
     time make

   You will see something like::

     real	2m36.662s
     user	2m34.473s
     sys	0m1.467s

   Now we want you to run it again after you touched a file::

     touch docs/source/faq.rst

   Now rerun the timed make. You will see an output such as::

     real	0m27.853s
     user	0m27.394s
     sys	0m0.334s

   The only thing we are interested in is the time behind real, as
   well as some information about your computer, e.g.::

     computer: MacBook Pro, 15-in, 2016, 2.9GHz, 16GB, 2133Mhz, LPDDR3
     make clean: 2m36.662s
     make update: 0m27.853s
     python: 3.6.2

   We will post a form in which you can enter your information. We
   found that we can use this information to check if you may have an
   issue with your computer or your setup.



   
   
