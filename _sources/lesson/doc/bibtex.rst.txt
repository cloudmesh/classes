Bibliography Management
======================

.. warning:: THis page is under active development and students are
	     encouraged to contribute
	     

In this section we will explain how to find and properly generate
bibliographic entries. We are using bibtex for this as it is easy to
use and generates reasonable entries that can be included in
papers. What we like to achieve in this section is not to just show
you a final entry, but to document the process on how that entry was
derived. This will allow you to replicate or learn from the process to
apply to your own entries.

We will address a number of important entry types which includes:

* wikipedia entries
* github entries
* books
* articles in a scientific journal
* articles in a conference
* articles in magazines (non scientific)
* blogs

  
  
Source code References
---------------------

In this section we will learn how to cite a source code from a
publicly hosted repository. Such repositories are frequently used
and include, for example github, bitbucket, sourcefore, or your
Universities code repository as long as it is publicly reachable.
As changes can occur on these repositories, it is important that the
date ov access is listed in the entry or even the release version of
the source code.

Let us without bias chose a random source dode entry that has been
contributed by a student as follows::
  
  @Misc{gonzalez_2015,
    Title =	 {Buildstep},
    Author =	 {Gonzalez, Jose and Lindsay,Jeff},
    HowPublished = {Web Page},
    Month =	 {Jul},
    Note =	 {Accessed: 2017-1-24},
    Year =	 2015,
    Key =        {www-buildstep},
    Url =        {https://github.com/progrium/buildstep}
  }

Is this entry correct? Let us analyse.

Entry type Misc
^^^^^^^^^^^^^^^

First, it seems appropriate to use a *@misc* entry.  We correctly
identify this is a misc entry as it is online available. More recent
version of bibtex include also the type *@online* for it. However, in
order to maintain compatibility to older formats we chose simply Misc
here and if we really would need to we could replace it easily


Label
^^^^^

Typically the Label should contain 3 letters from an author name,
short year and the short name of the publication to provide maximum
information regarding the publication. Underscores need to be replaced
by dashes or removed. However as this is a github repository it is
better to integrate this into the label. Hence, we simply use the
github-projectname (in our case github-buildstep, out of convention we
only use lower case letters.

 
Author
^^^^^^

Unless the last name contains spaces, it should be first name followed
by the last name with multiple authors separated with "and". 
 
Key
^^^

Field can be removed as the entry has an author field entry. If there
was no author field, we could use key to specify the ordering based on
a defined attribute. Note that a key is not the label. IN fact in our
original entry the key field was wrongly used and the student did not
understand that the key is used for sorting, but not for referencing
to this entry. To reference this entry one must be using the label that
is defined in the line with the @Misc

 
Howpublished
^^^^^^^^^^^^

Since the source is a github project repository, the howpublished
field shall hold the value {Code Repository} rather than a web
page. If the url specified was a normal webpage, the {Web Page} entry
would be valid. 
 
Month
^^^^^

The lowercase month is, used for international notation since months
are not capitalized in some other languages.
 
Owner
^^^^^

In class we introduced the convention to put the student HID in it. If
multiple students contributed, add them with space separation.

 
Accessed
^^^^^^^^

as we do not yet typically an accessed field, we simply include it in
the note field. This is absolutely essential as code can change and
when we read the code we looked at a particular snapshot in time. In
addition it is often necessary to record the actual version of the
code. Typically this can also be done with the month and year field
while relying on a release date


Final Entry
^^^^^^^^^^^

Filling out as many fields as possible with information for this entry
we get::

  @Misc{github-buildstep,
    Title =	 {Buildstep},
    Author =	 {Jose Gonzalez and Jeff Lindsay},
    HowPublished = {Code Repository},
    Year =	 {2015},
    Month =	 jul,
    Note =	 {Accessed: 2017-1-24},
    Url =	 {https://github.com/progrium/buildstep},
    Owner =	 {S17-IO-3025},
  }

We are using the release date in the year and month field as this
project uses this for organizing releases. However, other project may
have release versions so you would have in addition to using the data
also to include the version in the note field such as::

      Note =	 {Version: 1.2.3, Accessed: 2017-1-24},


.. note:: All those that helped should add your HID to this entry with
	  a space separated from each other 

Wikipedia Entry
---------------

Please fill out

Web Page
--------

Please fill out

InProceedings
-------------

Please fill out

TechReport
----------

Please fill out

Article
-------

Please fill out

Proceedings
-----------

Please fill out


