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

Submission
----------

To submit your peer review, simply find the section of `refs.bib`
belonging to the student you are reviewing and **add your review as a
comment**.

For example, if student *S17-TS-0006* was reviewing *S17-TS-0007*'s entry::

  % S17-TS-0007
  @Book{nagios-book,
    Title =	 {Nagios: Building Enterprise-Grade Monitoring
                  Infrastructures for Systems and Networks},
    Author =	 {Josephsen, David},
    Publisher =	 {Prentice Hall Press},
    Year =	 2013,
    Address =	 {Upper Saddle River, NJ, USA},
    Edition =	 {2nd},
    ISBN =	 {013313573X, 9780133135732},
    Owner =	 {S17-TS-0007}
  }

  @Misc{www-nagios,
    Title =	 {{Nagios} components},

  ...

they could update `refs.bib` as follows::


  % S17-TS-0007
  
  % Peer review by S17-TS-0006

  % www-nagios, 1: You used the RST citation command in the
  abstract. All such commands should be removed since they introduce
  RST syntax in a BibTex file, and are circular references.
  
  % www-nagios, 2: ...

  @Book{nagios-book,
    Title =	 {Nagios: Building Enterprise-Grade Monitoring
                  Infrastructures for Systems and Networks},
    Author =	 {Josephsen, David},
    Publisher =	 {Prentice Hall Press},
    Year =	 2013,
    Address =	 {Upper Saddle River, NJ, USA},
    Edition =	 {2nd},
    ISBN =	 {013313573X, 9780133135732},
    Owner =	 {S17-TS-0007}
  }
  
  @Misc{www-nagios,
    Title =	 {{Nagios} components},

  ...
    
That is, add your comments and identify which reference they refer to. If your comment is relevant to all references or some, use *all* or *some* respectively::

  ...
  % www-nagios, 1: ...
  % www-nagios, 2: ...
  % nagios-book, 1: ...
  % some, 1: ...
  % some, 2: ...
  % all, 1: ...
  % all, 2: ...
  % all, 3: ...
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
