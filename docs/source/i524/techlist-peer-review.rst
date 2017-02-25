Peer Review for TechList References
===================================

.. contents::

Introduction
------------

For this assignment, you need to review the contributions one of your
peers made as part of the :ref:`TechList exercise <techs-exercise>`
and give them feedback on the quality of their references.

A mapping of reviewer HIDs is included below. Everyone with entries in
`refs.bib` as of 3pm on Mon, Feb 20 has been assigned a peer
review. If you haven't yet submitted anything, please focus on adding
entries to your technologies, since you are running out of time.

In your feedback, please be constructive. Your goal is not so much to
find errors as to help your fellow student understand how to do better
references in the future. Imagine you will work with that student
extensively on a project; what would you like them to know and do to
be a good contributor? How would you like them to write and format
their contributions so that the whole project has a consistent feel?

For more information on how to properly use BibTex references, please
see the :doc:`BibTex lesson <../lesson/doc/bibtex>` or one of the 11
*Open Discussion* threads about TechList on Piazza.

Submission
----------

To submit your peer review, simply find the section of `refs.bib`
belonging to the student you are reviewing and **add your comments to
the Review field of each reference**. The *Review* field has already
been added by us, you just need to put in your comments.

For example, if student *S17-TS-0006* was reviewing *S17-TS-0007*'s
entry::
  
  % S17-TS-0007
  ...
  @Misc{www-nagios,
    review =     {}
    Title =	 {{Nagios} components},
    HowPublished = {Web Page},
    Note =	 {Accessed: 2017-1-11},
    Abstract =	 {Nagios is a platform, which provides a set of
                  software for network infrastructure monitoring. It
                  also offers administrative tools to diagnose when
                  failure events happen, and to notify operators when
                  hardware issues are detected. Specifically,
                  :cite:`www-nagios` illustrates that Nagios is
  ...

they could update `refs.bib` as follows::

  % S17-TS-0007
  ...
  @Misc{www-nagios,
    review =     {You used the RST citation command in the abstract. All
                  such commands should be removed since they introduce
                  RST syntax in a BibTex file, and are circular
                  references. In addition, ...}
    Title =	 {{Nagios} components},
    HowPublished = {Web Page},
    Note =	 {Accessed: 2017-1-11},
    Abstract =	 {Nagios is a platform, which provides a set of
                  software for network infrastructure monitoring. It
                  also offers administrative tools to diagnose when
                  failure events happen, and to notify operators when
                  hardware issues are detected. Specifically,
                  :cite:`www-nagios` illustrates that Nagios is
  ...
    
If there are any general comments about the student's entries, add them as a paragraph in the beginning of their section in `refs.bib`, right below their HID::

  % S17-TS-0007
  % Review by S17-TS-0006: Please, make sure...
  ...
  
**Please, do not change the actual entries by the student you are reviewing.**

**Once you receive the review of your references, it is up to you to update them.**

Due Date
--------

For **residential students**, this is due at the beginning of class on **Monday, February 27th**.

For **online students**, this is due on **Monday, March 20th**. 

Reviewers
---------

.. csv-table::
   :header-rows: 1
   :widths: 70, 70
   :file: techlist-peer-review.csv
