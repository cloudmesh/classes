Bibliography Management
=======================

.. note:: Students are actively encouraged to improve this page.

.. todo:: Saber, integrate some of the lesseons and examples we have
          in i524 piazza into this page. Search for bibtex and als for
          "Open Discussion:"

.. todo:: Saber, make all keys in bibtex entries lower case

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
----------------------

We will learn how to cite a source code from a publicly hosted
repository. Such repositories are frequently used and include, for
example github, bitbucket, sourcefore, or your Universities code
repository as long as it is publicly reachable.  As changes can occur
on these repositories, it is important that the date ov access is
listed in the entry or even the release version of the source code.

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

In this case the key field can be removed as the entry has an author
field entry. If there was no author field, we could use key to specify
the alphabetical ordering based on the specified key. Note that a key
is not the label. In fact in our original entry the key field was
wrongly used and the student did not understand that the key is used
for sorting. 

 
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

As we do not yet typically an accessed field, we simply include it in
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


Researching proper bibtex entries
----------------------------------------


Article in a journal
^^^^^^^^^^^^^^^^^^^^

Many online bibtex entries are wrong or incomplete.  Often you may find via google a bibtex entry that may need some more reserach. Lets assume your first google quesry returns a publication and you cite it such as this::


  @Unpublished{unpublished-google-sawzall,
      Title = {{Interpreting the Data: Parallel Analysis with Sawzall}},
      Author = {{Rob Pike, Sean Dorward, Robert Griesemer, Sean Quinlan}},
      Note = {accessed 2017-01-28},
      Month = {October},
      Year = {2005},
      Owner = {for the purpose of this discussion removed},
      Timestamp = {2017.01.31}
  }

Could we improve this entry to achieve your best? We oberve:

1. The author field has a wrong entry as the , is to be replaced by an and.

2. The author feild  has authors and thus must not have a {{ }}

3. The url is missing, as the simple google search actually finds a PDF document. 

Let us investigate a bit more while searching for the title. We find

 
A) https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0ahUKEwj_ytSA-PDRAhUH8IMKHaomC-oQFggaMAA&url=https%3A%2F%2Fresearch.google.com%2Farchive%2Fsawzall-sciprog.pdf&usg=AFQjCNHSSfKBwbxVAVPQ0td4rTjitKucpA&sig2=vbiVzi36B3gGFjIzlUKBDA&bvm=bv.146073913,d.amc

B) https://research.google.com/pubs/pub61.html
 
C) http://dl.acm.org/citation.cfm?id=1239658

 
Let us look at A)

As you can see from the url this is actualy some redirection to a
google web page which probably is replaced by B as its from google
research. So let us look at B)

Now when you look at the link we find the url
https://research.google.com/archive/sawzall-sciprog.pdf which
redirects you to the PDF paper.
 
When we go to B) we find surprisingly a bibtex entry as follows::

  @article{61,
    title = {Interpreting the Data: Parallel Analysis with Sawzall},
    author = {Rob Pike and Sean Dorward and Robert Griesemer and Sean Quinlan},
    year = 2005,
    URL = {https://research.google.com/archive/sawzall.html},
    journal = {Scientific Programming Journal},
    pages = {277--298},
    volume = {13}
  }


Now we could say lets be satisfied, but C) seems to be even more
interesting as its from a major publisher. So lats just make sure we
look at C)

If you go to C, you find under the colored box entitled Tools and
Resources a link called **bibtex**. Thus it seems a good idea to click
on it. This will give you::

 

  @article{Pike:2005:IDP:1239655.1239658,
      author = {Pike, Rob and Dorward, Sean and Griesemer, Robert and Quinlan, Sean},
      title = {Interpreting the Data: Parallel Analysis with Sawzall},
      journal = {Sci. Program.},
      issue_date = {October 2005},
      volume = {13},
      number = {4},
      month = oct,
      year = {2005},
      issn = {1058-9244},
      pages = {277--298},
      numpages = {22},
      url = {http://dx.doi.org/10.1155/2005/962135},
      doi = {10.1155/2005/962135},
      acmid = {1239658},
      publisher = {IOS Press},
      address = {Amsterdam, The Netherlands, The Netherlands},
  }
 
Now we seem to be at a position to combine our search result as neither entry is sufficient. As the doi number properly specifies a paper (look
up what a doi is) we can replace the url with one that we find online,
such as the one we found in A) Next we see that all field sin B are
already coverd in C, so we take C) and add the url. Now as the label
is graet and uniform for ACM, but for us a bit less convenient as its
difficult to remember, we just change it while for example using
authors, title, and year information. lets also make sure to do mostly
lowercase in the label just as a convention. Thus our entry looks
like::

  @article{pike05swazall,
      author = {Pike, Rob and Dorward, Sean and Griesemer, Robert and Quinlan, Sean},
      title = {Interpreting the Data: Parallel Analysis with Sawzall},
      journal = {Sci. Program.},
      issue_date = {October 2005},
      volume = {13},
      number = {4},
      month = oct,
      year = {2005},
      issn = {1058-9244},
      pages = {277--298},
      numpages = {22},
      url = {https://research.google.com/archive/sawzall-sciprog.pdf},
      doi = {10.1155/2005/962135},
      acmid = {1239658},
      publisher = {IOS Press},
      address = {Amsterdam, The Netherlands, The Netherlands},
  }
 
As you can see properly specifying a refernce takes multiple google quesries and merging of the results you find from various returms. As you still have time to correct things I advise that you check your refernces and correct them. If the original refernce would have been graded it would have been graded with a "fail" instead of a "pass".

 
Article in a conference proceedings
-----------------------------------

Lets look at a second obvious example that needs improvement::

  
  @InProceedings{wettinger-any2api,
    Title                    = {Any2API - Automated APIfication},
    Author                   = {Wettinger, Johannes and
                                Uwe Breitenb{\"u}cher
                                and Frank Leymann},
    Booktitle                = {Proceedings of the 5th International
                                Conference on Cloud Computing and
				Services Science},
    Year                     = {2015},
    Pages                    = {475­486},
    Publisher                = {SciTePress},

    ISSN                     = {2326-7550},
    Owner                    = {S17-IO-3005},
    Url                      = {https://pdfs.semanticscholar.org/1cd4/4b87be8cf68ea5c4c642d38678a7b40a86de.pdf}
  }

As you can see this entry seems to define all required fields, so we
could be tempted to stop here. But its good to double check. Lets do
some queries against ACM, . and google scholar, so we jst type in
the title, and if this is in a proceedings they should return hopeflly
a predefined bibtex record for us.

Lets query::

  google: googlescholar Any2API Automated APIfication

We get:

* https://scholar.google.de/citations?view_op=view_citation&hl=en&user=j6lIXt0AAAAJ&citation_for_view=j6lIXt0AAAAJ:8k81kl-MbHgC

On that page we see `Cite
<https://scholar.google.com/scholar_lookup?title=Automated+drug+dispensing+system+reduces+medication+errors+in+an+intensive+care+setting&author=Chapuis&publication_year=2010#>`_

So we find a PDF at
https://pdfs.semanticscholar.org/1cd4/4b87be8cf68ea5c4c642d38678a7b40a86de.pdf

Lets click on this and the document incldes a bibtex entry such as::

  @inproceedings{Wettinger2015,	
    author= {Johannes Wettinger and Uwe Breitenb{\"u}cher and Frank
	     Leymann},
    title = {Any2API - Automated APIfication},
    booktitle = {Proceedings of the 5th International Conference on Cloud
		 Computing and Service Science (CLOSER)},
    year = {2015},
    pages = {475--486},
    publisher = {SciTePress}
  }	

Now lets add the URL and owner::

  @inproceedings{Wettinger2015,	
    author= {Johannes Wettinger and Uwe Breitenb{\"u}cher and Frank
	     Leymann},
    title = {Any2API - Automated APIfication},
    booktitle = {Proceedings of the 5th International Conference on Cloud
		 Computing and Service Science (CLOSER)},
    year = {2015},
    pages = {475--486},
    publisher = {SciTePress},
    url ={https://pdfs.semanticscholar.org/1cd4/4b87be8cf68ea5c4c642d38678a7b40a86de.pdf},
    owner = {S17-IO-3005},
  }	

Should we be satisfied? No, even our original information we gathere
provided more information. So lets continue. Lets googlesearch
different queries with ACM or IEEE and the title. When doing the IEEE
in the example we find an entry called

`dlp: Frank Leyman <http%3A%2F%2Fdblp.uni-trier.de%2Fpers%2Fl%2FLeymann%3AFrank&usg=AFQjCNHCu-66qxWH0zRlPLr4DA8jIo5V-g&sig2=1vYdnGOEiMcLBEMpbeBA7g>`_ 

Lets look at it and we find two entries::

  @inproceedings{DBLP:conf/closer/WettingerBL15,
    author    = {Johannes Wettinger and
		 Uwe Breitenb{\"{u}}cher and
		 Frank Leymann},
    title     = {{ANY2API} - Automated APIfication - Generating APIs for Executables
		 to Ease their Integration and Orchestration for Cloud Application
		 Deployment Automation},
    booktitle = {{CLOSER} 2015 - Proceedings of the 5th International Conference on
		 Cloud Computing and Services Science, Lisbon, Portugal, 20-22 May,
		 2015.},
    pages     = {475--486},
    year      = {2015},
    crossref  = {DBLP:conf/closer/2015},
    url       = {http://dx.doi.org/10.5220/0005472704750486},
    doi       = {10.5220/0005472704750486},
    timestamp = {Tue, 04 Aug 2015 09:28:21 +0200},
    biburl    = {http://dblp.uni-trier.de/rec/bib/conf/closer/WettingerBL15},
    bibsource = {dblp computer science bibliography, http://dblp.org}
  }

  @proceedings{DBLP:conf/closer/2015,
    editor    = {Markus Helfert and
		 Donald Ferguson and
		 V{\'{\i}}ctor M{\'{e}}ndez Mu{\-{n}}oz},
    title     = {{CLOSER 2015 - Proceedings of the 5th International Conference on
		 Cloud Computing and Services Science, Lisbon, Portugal, 20-22 May,
		 2015}},
    publisher = {SciTePress},
    year      = {2015},
    isbn      = {978-989-758-104-5},
    timestamp = {Tue, 04 Aug 2015 09:17:34 +0200},
    biburl    = {http://dblp.uni-trier.de/rec/bib/conf/closer/2015},
    bibsource = {dblp computer science bibliography, http://dblp.org}
  }

So lets look at the entry and see how to get a better one for our
purpose to combine them. When using jabref, you see optional and
required fields, we want to add as many as possible, regardless if
optional or required, so Lets do that (I I write here in ASCII as
easier to document::
  


    @InProceedings{,
      author = 	 {},
      title = 	 {},
      OPTcrossref =  {},
      OPTkey = 	 {},
      OPTbooktitle = {},
      OPTyear = 	 {},
      OPTeditor = 	 {},
      OPTvolume = 	 {},
      OPTnumber = 	 {},
      OPTseries = 	 {},
      OPTpages = 	 {},
      OPTmonth = 	 {},
      OPTaddress = 	 {},
      OPTorganization = {},
      OPTpublisher = {},
      OPTnote = 	 {},
      OPTannote = 	 {},
      url = {}
    }

So lets copy and fill out the **form** from our various searches::

    @InProceedings{Wettinger2015any2api,	
      author    = {Johannes Wettinger and
  		 Uwe Breitenb{\"{u}}cher and
  		 Frank Leymann},
      title     = {{ANY2API - Automated APIfication - Generating APIs for Executables
		 to Ease their Integration and Orchestration for Cloud Application
		 Deployment Automation}},
      booktitle = {{CLOSER 2015 - Proceedings of the 5th International Conference on
  		   Cloud Computing and Services Science}},
      year = 	 {2015},
      editor    = {Markus Helfert and
 		   Donald Ferguson and
		   V{\'{\i}}ctor M{\'{e}}ndez Mu{\-{n}}oz},
      publisher = {SciTePress},
      isbn      = {978-989-758-104-5},
      pages = {475--486},
      month = {20-22 May},
      address = 	 {Lisbon, Portugal},
      doi       = {10.5220/0005472704750486},
      url ={https://pdfs.semanticscholar.org/1cd4/4b87be8cf68ea5c4c642d38678a7b40a86de.pdf},
      owner = {S17-IO-3005},
    }

What are the differnt entry types and fields
--------------------------------------------


We were asked what are the different entry types and fields, so we did
a google query and found the following useful information. please
remember that we also have fields such as doi, owner, we will add
status ={pass/fail} at time of grading to indicate if the refernce
passes or fails. We may assign this to you so you get familiar with
the identification if a referncei is ok or not.

Please see https://en.wikipedia.org/wiki/BibTeX 

    
InProceedings
-------------


Please fill out

::

  @InProceedings{,
    author =       {},
    title =        {},
    OPTcrossref =  {},
    OPTkey =       {},
    OPTbooktitle = {},
    OPTyear =      {},
    OPTeditor =    {},
    OPTvolume =    {},
    OPTnumber =    {},
    OPTseries =    {},
    OPTpages =     {},
    OPTmonth =     {},
    OPTaddress =   {},
    OPTorganization = {},
    OPTpublisher = {},
    OPTnote =      {},
    OPTannote =    {},
    url = {}
  }

::

  @inproceedings{vonLaszewski15tas,
    author =	 {DeLeon, Robert L. and Furlani, Thomas R. and Gallo,
                    Steven M. and White, Joseph P. and Jones, Matthew
                    D. and Patra, Abani and Innus, Martins and Yearke,
                    Thomas and Palmer, Jeffrey T. and Sperhac, Jeanette
                    M. and Rathsam, Ryan and Simakov, Nikolay and von
                    Laszewski, Gregor and Wang, Fugang},
    title =	 {{TAS View of XSEDE Users and Usage}},
    booktitle =	 {Proceedings of the 2015 XSEDE Conference: Scientific
                    Advancements Enabled by Enhanced
                    Cyberinfrastructure},
    series =	 {XSEDE '15},
    year =	 2015,
    isbn =	 {978-1-4503-3720-5},
    location =	 {St. Louis, Missouri},
    pages =	 {21:1--21:8},
    articleno =	 21,
    numpages =	 8,
    url =		 {http://doi.acm.org/10.1145/2792745.2792766},
    doi =		 {10.1145/2792745.2792766},
    acmid =	 2792766,
    publisher =	 {ACM},
    address =	 {New York, NY, USA},
    keywords =	 {HPC, SUPReMM, TAS, XDMoD, XSEDE usage, XSEDE users},
  }

TechReport
----------

Please fill out

::

  @TechReport{,
    author =       {},
    title =        {},
    institution =  {},
    year =         {},
    OPTkey =       {},
    OPTtype =      {},
    OPTnumber =    {},
    OPTaddress =   {},
    OPTmonth =     {},
    OPTnote =      {},
    OPTannote =    {},
    url = {}    
  }

::

  @TechReport{las05exp,
    title =	 {{The Java CoG Kit Experiment Manager}},
    Author =	 {von Laszewski, Gregor},
    Institution =	 {Argonne National Laboratory},
    Year =	 2005,
    Month =	 jun,
    Number =	 {P1259},
    url = {https://laszewski.github.io/papers/vonLaszewski-exp.pdf}
  }
 
Article
-------

Please fill out

::

  @Article{,
    author =       {},
    title =        {},
    journal =      {},
    year =         {},
    OPTkey =       {},
    OPTvolume =    {},
    OPTnumber =    {},
    OPTpages =     {},
    OPTmonth =     {},
    OPTnote =      {},
    OPTannote =    {},,
    url = {}
  }

::

  @Article{las05gridhistory,
    title =	 {{The Grid-Idea and Its Evolution}},
    author =	 {von Laszewski, Gregor},
    journal =	 {Journal of Information Technology},
    year =	 2005,
    month =	 jun,
    number =	 6,
    pages =	 {319-329},
    volume =	 47,
    doi =		 {10.1524/itit.2005.47.6.319},
    url = {https://laszewski.github.io/papers/vonLaszewski-grid-idea.pdf}
  }

Proceedings
-----------

Please fill out


::

  @Proceedings{,
    title =        {},
    year =         {},
    OPTkey =       {},
    OPTbooktitle = {},
    OPTeditor =    {},
    OPTvolume =    {},
    OPTnumber =    {},
    OPTseries =    {},
    OPTaddress =   {},
    OPTmonth =     {},
    OPTorganization = {},
    OPTpublisher = {},
    OPTnote =      {},
    OPTannote =    {},
    url = {}
  }

::
 
  @Proceedings{las12fedcloud-proc,
    title =	 {{FederatedClouds '12: Proceedings of the 2012
                    Workshop on Cloud Services, Federation, and the 8th
                    Open Cirrus Summit}},
    year =	 2012,
    address =	 {New York, NY, USA},
    editor =	 {vonLaszewski, Gregor and Robert Grossman and Michael
                    Kozuchand Rick McGeerand Dejan Milojicic},
    publisher =	 {ACM},
    iSBN =	 {978-1-4503-1754-2},
    location =	 {San Jose, California, USA},
    url =
                    {http://dl.acm.org/citation.cfm?id=2378975&picked=prox&cfid=389635474&cftoken=32712991}
  }

Wikipedia Entry
---------------

Please fill out


::

  @Misc{,
    OPTkey =       {},
    OPTauthor =    {},
    OPTtitle =     {},
    OPThowpublished = {},
    OPTmonth =     {},
    OPTyear =      {},
    OPTnote =      {},
    OPTannote =    {},
    url = {}
  }

::

  @Misc{www-ode-wikipedia,
    Title =	 {Apache ODE},
    HowPublished = {Web Page},
    Note =	 {Accessed: 2017-2-11},
    Key =		 {Apache ODE},
    Url =		 {https://en.wikipedia.org/wiki/Apache_ODE}
  }
  
Blogs
---------------

Please fill out

::

  @Misc{,
    OPTkey =       {},
    OPTauthor =    {},
    OPTtitle =     {},
    OPThowpublished = {},
    OPTmonth =     {},
    OPTyear =      {},
    OPTnote =      {},
    OPTannote =    {},
    OPTurl = {}
  }

::

  @Misc{www-clarridge-discoproject-blog,
    title =	 {Disco - A Powerful Erlang and Python Map/Reduce
                    Framework},
    uthor =	 {Clarridge, Tait},
    howpublished = {Blog},
    month =	 may,
    note =	 {Accessed: 25-feb-2017},
    year =	 2014,
    url =  {http://www.taitclarridge.com/techlog/2014/05/disco-a-powerful-erlang-and-python-mapreduce-framework.html}
  }

Web Page
--------

Please fill out


::

  @Misc{, 
    OPTkey =       {}, 
    OPTauthor =    {}, 
    OPTtitle =     {}, 
    OPThowpublished = {}, 
    OPTmonth =     {}, 
    OPTyear =      {}, 
    OPTnote =      {},
    OPTannote =    {},
    url = {}
  }

::

  @Misc{www-cloudmesh-classes,
    OPTkey =       {},
    author =    {von Laszewski, Gregor},
    title =     {Cloudmesh Classes},
    howpublished = {Web Page},
    OPTmonth =     {},
    OPTyear =      {},
    OPTnote =      {},
    OPTannote =    {},
    url = {https://cloudmesh.github.io/classes/}
  }

::

  @Misc{www-awslambda,
    title =	 {AWS Lambda},
    author =	 {{Amazon}},
    key =		 {AWS Lambda},
    howpublished = {Web Page},
    url =		 {https://aws.amazon.com/lambda/faqs/}
  }


Book
----------------------------

Given the following entry. What is the proper entry for this book.
Provide rationale::
 
  @Book{netty-book,
      Title = {Netty in Action},
      Author = {Maurer, Norman and Wolfthal, Marvin},
      Publisher = {Manning Publications},
      Year = {2016},
  }
 

To obtain the record of a book you can look at many information
sources. The can include:
 
* https://www.manning.com/books/netty-in-action 
* https://www.amazon.com/Netty-Action-Norman-Maurer/dp/1617291471 
* http://www.barnesandnoble.com/w/netty-in-action-norman-maurer/1117342155?ean=9781617291470#productInfoTabs 
* http://www.powells.com/book/netty-in-action-9781617291470/1-0 

Furtheromore wee need to consider the entry of a book, we simply look
it up in emacs where we find the following but add the owner and the
url field::

  @Book{,
    ALTauthor = 	 {},
    ALTeditor = 	 {},
    title = 	 {},
    publisher = 	 {},
    year = 	 {},
    OPTkey = 	 {},
    OPTvolume = 	 {},
    OPTnumber = 	 {},
    OPTseries = 	 {},
    OPTaddress = 	 {},
    OPTedition = 	 {},
    OPTmonth = 	 {},
    OPTnote = 	 {},
    OPTannote = 	 {},
    ownwer =       {},
    url = {}
  }

In summary we find the following fields:
 
Required fields:
   author/editor, title, publisher, year

Optional fields:
   volume/number, series, address, edition, month, note, key

We apply the following to fill out the fields.

address:
  The address is the Publisher's address. Usually just the city, but can
  be the full address for lesser-known publishers.

author:
  The name(s) of the author(s) (in the case of more than one author, separated by and)
  Names can be written in one of two forms: Donald E. Knuth or Knuth,
  Donald E. or van Halen, Eddie. Please note that Eddie van Halen
  would result in a wrong name. For our purpose we keep nobelity
  titles part of the last name.
  
edition:
  The edition of a book, long form (such as "First" or "Second")

editor:
  The name(s) of the editor(s)

key:
  A hidden field used for specifying or overriding the alphabetical
  order of entries (when the "author" and "editor" fields are missing).
  Note that this is very different from the key that is used to cite or
  cross-reference the entry.

label:
  The label field should contain three letters from the auth field, a
  short year reference and a short name of the publication to provide
  the maximum information regarding the
  publication.  Underscores should be replaced with dashes or removed completely.  

month:
  The month of publication or, if unpublished, the month of creation.
  Use three-letter abbreviations for this field in order to account
  for languages that do not capitalize month names.
  Additional information for the day can be included as follows: aug #"~10,"

publisher:
  The publisher's name

series:
  The series of books the book was published in (e.g. "The Hardy Boys"
  or "Lecture Notes in Computer Science")

title:
  The title of the work. As the capitalization depends on the
  bibliography style and the language used we typically use camel case.
  To force caitalization of a word or its first letter you can use the
  curly braces, '{ }'.
  To keep the title in camel case simple use title = {{My Title}}
  
type:
  The field overriding the default type of publication (e.g. "Research
  Note" for techreport, "{PhD} dissertation" for phdthesis, "Section"
  for inbook/incollection) volume The volume of a journal or
  multi-volume book year The year of publication (or, if unpublished,
  the year of creation)
 

While applying the above rules and tips we summarize what we have done
for this entry:

1. Search for the book by title/Author on ACM (http://dl.acm.org/) or Amazon or
   barnesandnoble or upcitemdb (http://upcitemdb.com). These services
   return bibtex entrie that you can improve.

2. Hence one option is t get the ISBN of the book. For "Mesos in
   action" from upcitemdb we
   got the ISBN as "9781617 292927". This is the 13 digit ISBN. The first
   3 digits (GS1 code) can be skipped.
   Using the rest of 10 digits "1617 292927", Add in JabRef in Optional
   Fields->ISBN.

   However it is fine to youst specify the full number.

   We can also return a bibtex entry generated while using 
   Click on the "Get BibTex from ISBN".

   Now we get more information on this book entry from ISBN. We can
   opt either the original or newly searched entry for the below
   bibtex fields or merge as appropriate. URL may not match from where we
   initially read the book, however there is option to put your original
   url or newly searched url. EAN, Edition, Pages,url,published date etc. 
   Do a search on amazon for "ASIN". Can skip if not available. Sometime
   we get ASIN for a different publication, maybe a paperback
   ASIN={B01MT311CU} We can add it as it becomes easier to search

doi:
   If you can find a doi numer you should also add it. IN this case we
   could not locate one.
   
As a result we obtain the entry::

  @Book{netty-book,
    title = {Netty in Action},
    publisher = {Manning Publications Co.},
    year = {2015},
    author = {Maurer, Norman and Wolfthal, Marvin Allen},
    address = {Greenwich, CT, USA},
    edition = {1st},
    isbn = {1617291471},
    asin = {1617291471},
    date = {2015-12-23},
    ean = {9781617291470},
    owner = {S17-IO-3022 S17-IO-3010 S17-IO-3012},
    pages = {296},
    url = {http://www.ebook.de/de/product/21687528/norman_maurer_netty_in_action.html},
  }

Bibtex import to MSWord
------------------------

XML import
^^^^^^^^^^

Plaease respond back to us if you have used this and give feedback.

1. In JabRef, export the bibliography in MS Word 2008 xml format
2. Name the file Sources.xml (case sensitive)
3. In OSX with MS Word 2015: Go to ~/Library/Containers/com.microsoft.word/Data/Library/Application Support/Microsoft/Office.
4. Rename the original Sources.xml file to Sources.xml.bak
5. Copy the generated Sources.xml in this folder
6. Restart MS Word.

We do not know what needs to be done in case you need to make changes
to the refernces. Please report back your experiences. To avoid issues
we recommend that you use LaTeX. and not MSWord.


BibTex4Word
^^^^^^^^^^^

We have not tried this:

* http://www.ee.ic.ac.uk/hp/staff/dmb/perl/index.html
