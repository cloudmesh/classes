reStructuredText
================

reStructuredText (RST) pur[pose is to provide an easy-to-read,
what-you-see-is-what-you-get plaintext markup syntax and parser
system. With its help you can develop documentation not only for stand
aone documentation, simple web pages, an in-line program documentation
(such as Python). RST is extensible and new features can be added. It
is used in sphinx as one of its supported formats.

Links
-----

* RST Sphinx documentation: http://www.sphinx-doc.org/en/stable/rest.html
* RST Syntax: http://docutils.sourceforge.net/rst.html
* Important extensions: http://sphinx-doc.org/ext/todo.html

Cheatcheat:
   * http://github.com/ralsina/rst-cheatsheet/raw/master/rst-cheatsheet.pdf
   * http://docutils.sourceforge.net/docs/ref/rst/directives.html


Source
------

The source for this page is located at

* https://raw.githubusercontent.com/cloudmesh/classes/master/docs/source/lesson/doc/rst.rst

This way you can look at the source on how we create this page.

Sections
--------


# with overline, for parts
* with overline, for chapters
=, for sections
-, for subsections
^, for subsubsections
", for paragraphs

RST allows to specify a number of sections. You can do this with the
various underlines::

      *********************
      Chapter
      *********************
      Section
      =====================
      Subsection
      ---------------------
      Subsubsection
      ^^^^^^^^^^^^^^^^^^^^^
      Paragraph
      ~~~~~~~~~~~~~~~~~~~~~

Listtable
---------

::

   .. csv-table:: Eye colors
      :header: "Name", "Firstname", "eyes"
      :widths: 20, 20, 10

      "von Laszewski", "Gregor", "gray"

.. csv-table:: a title
   :header: "Name", "Firstname", "eyes"
   :widths: 20, 20, 10

   "von Laszewski", "Gregor", "gray"


Exceltable
----------

we have integrated Excel table from
http://pythonhosted.org//sphinxcontrib-exceltable/ intou our sphinx
allowing the definition of more elaborate tables specified in
excel. Howere the most convenient way may be to use list-tables. The
documentation to list tables can be found at
http://docutils.sourceforge.net/docs/ref/rst/directives.html#list-table

Boxes
-----

Seealso
^^^^^^^

::

  .. seealso:: This is a simple **seealso** note. 


.. seealso:: This is a simple **seealso** note. 

Note
^^^^

.. note::  This is a **note** box.

::

    .. note::  This is a **note** box.

Warning
^^^^^^^

.. warning:: note the space between the directive and the text

::

    .. warning:: note the space between the directive and the text

Others
^^^^^^


.. attention:: This is an **attention** box.

::

    .. attention:: This is an **attention** box.


.. caution:: This is a **caution** box.

::

    .. caution:: This is a **caution** box.


.. danger:: This is a **danger** box.

::

    .. danger:: This is a **danger** box.


.. error:: This is a **error** box.

::

    .. error:: This is a **error** box.


.. hint:: This is a **hint** box.

::

    .. hint:: This is a **hint** box.


.. important:: This is an **important** box.

::

    .. important:: This is an **important** box.


.. tip:: This is a **tip** box.

::

    .. tip:: This is a **tip** box.




Sidebar directive
-----------------

It is possible to create sidebar using the following code::

    .. sidebar:: Sidebar Title
        :subtitle: Optional Sidebar Subtitle

        Subsequent indented lines comprise
        the body of the sidebar, and are
        interpreted as body elements.


.. sidebar:: Sidebar Title
    :subtitle: Optional Sidebar Subtitle

    Subsequent indented lines comprise
    the body of the sidebar, and are
    interpreted as body elements.

Sphinx Prompt
-------------

::

   .. prompt:: bash, cloudmesh$

      wget -O cm-setup.sh http://bit.ly/cloudmesh-client-xenial
      sh cm-setup.sh

.. prompt:: bash, cloudmesh$

    wget -O cm-setup.sh http://bit.ly/cloudmesh-client-xenial
    sh cm-setup.sh
    
    
Programm examples
-----------------

You can include code examples and bash commands with two colons.

This is an example for python::

  print ("Hallo World")


This is an example for a shell command::

  $ ls -lisa


..
   COMMENT
   Autorun
   -------

   .. warning:: This feature may not be enabled on the Web Page.

   Autorun is an extension for Sphinx_ that can execute the code from a
   runblock directive and attach the output of the execution to the document. 

   For example::

       .. runblock:: pycon

	   >>> for i in range(3):
	   ...    print i

   Produces

   .. runblock:: pycon

       >>> for i in range(3):
       ...    print i


   Another example::

       .. runblock:: console

	   $ date

   Produces

   .. runblock:: console

      $ date 

   However, when it comes to excersises we do preferthe use of ipython
   notebooks as this allows us to present them also to users as self
   contained excersises.

Hyperlinks
----------------------------------------------------------------------

Direct links to html pages can ve done with::

   `This is a link to an html page <hadoop.html>`_
  
Note that this page could be generated from an rst page


Links to the FG portal need to be formulated with the portal tag::

  :portal:`List to FG projects </projects/all>`
  
In case a subsection has a link declared you can use :ref: (this is
the prefered way as it can be used to point even to subsections::

  :ref:`Connecting private network VMs  clusters <_s_vpn>` 

A html link can be created anywhere in the document but must be
unique. for example if you place::

  .. _s_vpn:

in the text it will create a target to which the above link points
when you click on it


Todo
----------------------------------------------------------------------
 
::
      
      .. todo:: an example

.. image:: ../../images/todo.png


