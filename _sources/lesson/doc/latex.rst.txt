LaTeX
=====

Introduction
------------

Mastering a text processing system is an essential part of a researchers
life. Not knowing how to use a text processing system can slow down the
productivity of research drastically.

The information provided here is not intended to replace one of the many
text books available about LaTeX. For the beginning you might be just
fine with the documentation provided here. For serious users I recommend
to purchase a book. Examples for books include

-  LaTeX Users and Reference Guide, by Leslie Lamport
-  LaTeX an Introduction, by Helmut Kopka
-  The LaTeX Companion, by Frank Mittelbach

If you do not want to buy a book you can find a lot of useful
information in the LaTeX reference manual.

LaTeX vs. X
-----------

We will refrain from providing a detailed analysis on why we use LaTeX
in many cases versus other technologies. In general we find that LaTeX:

* is incredible stable
* produces high quality output
* is platform independent
* has lots of templates
* has been around for many years so it works well
* removes you form the pain of figure placements
* focusses you on content rather tan the appearance of the paper
* integrates well with code repositories such as git to write
  collaborative papers.
* has superior bibliography integration
* has a rich set of tools that make using LaTeX easier
* authors do not play with layouts much so papers in a format are uniform

In case you need a graphical view to edit LaTeX or LateX exportable
files you also find AucTeX and Lyx.

Word
^^^^

Word is arguably available to many, but if you work on Linux you may
be out of luck. Also Word often focusses not on structure of the text
but on look. Many students abuse Word and the documents in Word become
a pain to edit with multiple users. Recently Microsoft has offered
online services to collaborate on writing documents in groups which
work well. Integration with bibliography managers such as endnote or
Mendeley is possible.

However we ran into issues whenever we use word:

* Word tends sometimes to crash for unknown reasons and we lost a lot
  of work
* Word has some issues with the bibliography managers and tends to
  crash sometimes for unknown reasons.
* Word is slow with integration to large bibliographies.
* Figure placement in Word in some formats is a disaster and you will
  spend many hours to correct things just to find out that if you make
  small changes you have to spend additional many hours to get used
  to the new placement. We have not yet experienced a word version
  where we have not lost images. Maybe that has changed, so let us
  know

However we highly recommend the collaborative editing features of Word
that work on a paragraph and not letter level. Thus saving is
essential so you do not block other people from editing the paragraph.

Google Docs
^^^^^^^^^^^

Unfortunately many useful features got lost in the new google
docs. However it is great to collaborate quickly online, share
thoughts and even write your latex documents together if you like
(just copy your work in a file offline and use latex to compile it ;-)
)

The biggest issue we have with Google Docs is that it does not allow
the support of 2 column formats, that the bibliography integration is
non existent and that paste and copy from web pages and images
encourages unintended plagiarism when collecting information without
annotations (LaTeX and Word are prone to this too, but we found from
experience that it tends to happen more with Google docs users.

A Place for Each
^^^^^^^^^^^^^^^^

When looking at the tools we find a place for each:

Google docs:
   short meeting notes, small documents, quick online collaborations
   to develop documents collaboratively at the same time

Word:
   available to many, supports 2 column format, supports paragraph
   based collaborative editing, Integrates with bibliography managers.

LaTeX:
   reduce failures, great offline editing, superior bibliography
   management, superior image placement, runs everywhere. Great
   collaborative editing with sharelatex, allows easy generation of
   proceedings written by hundreds of people with shared index.

The best choice for your class:
   LaTeX

Editing
-------

Emacs
^^^^^

The text editor emacs provides a great basis for editing TeX and LaTeX
documents. Both modes are supported. In addition there exists a color
highlight module enabling the color display of LaTeX and TeX commands.
On OSX aquaemacs and carbon emacs have build in support for LaTeX. Spell
checking is done with flyspell in emacs.

Vi/Vim
^^^^^^

Another popular editor is vi or vim. It is less feature rich but many
programmers ar using it. As it can edit ASCII text you can edit LaTeX.
With the LaTeX add ons to vim, vim becomes similar powreful while
offering help and syntax highlighting for LaTeX as emacs does. (The
authors still prefer emacs)


TeXshop
^^^^^^^

Other editors such as TeXshop are available which provide a more
integrated experience. However, we find them at times to stringent and
prefer editors such as emacs/


LyX
~~~

We have made very good experiences with Lyx. You must assure that the
team you work with uses it consistently and that you all use the same version.

Using the ACM templates is documented here:

* https://wiki.lyx.org/Examples/AcmSiggraph

On OSX it is important that you have a new version of LaTeX and Lyx
installed. As it takes up quite some space, you ma want to delete
older versions. The new version of LyX comes with the acmsigplan
template included. However on OSX and other platforms the .cls file is
not included by default. However the above link clearly documents how
to fix this.

WYSIWYG locally
--------------

We have found that editors such as Lyx and Auctex provide very good
WYSIWYG alike features. However, we found an even easier way while
using `skim`, a pdf previewer, in conjunction with `emacs` and
`latexmk`. This can be achieved while using the following command
assuming your latex file is called `report.tex`::


  latexmk -pvc -view=pdf report

This command will update your pdf previewer (make sure to use skim)
whenever you edit the file report.tex and save it. It will maintain
via skim the current position, thus you have a real great way of
editing in one window, while seeing the results in the other.

.. note::
   Skim can be found at: http://skim-app.sourceforge.net/

Installation
-----------

Local Install
^^^^^^^^^^^^^

Installing LaTeX is trivial, but requires sufficient space and time as
it is a large environment. In addition to LaTeX we recommend that you
install `jabref` and use it for bibliography management.

Thus you will have the most of them on your system.

-  pdflatex: the latex program producing pdf
-  bibtex: to create bibliographies
-  jabref: less fancy GUI to bibtex files

Make sure you check that these programs are there, for example with
the linux commands::

   which pdflatex
   which bibtex
   which jabref (on OSX you may have an icon for it)

If these commands are missing, please instal them.

Online Services
^^^^^^^^^^^^^^^

Sharelatex
~~~~~~~~~~

Those that like to use latex, but do not have it installed on their
computers may want to look at the following video: 

Video: https://youtu.be/PfhSOjuQk8Y

Video with cc: https://www.youtube.com/watch?v=8IDCGTFXoBs

ShareLaTeX not only allows you to edit online, but allows you to share
your documents in a group of up to three. Licenses are available if
you need more than three people in a team.

Overleaf
~~~~~~~~

Overleaf.com is a collaborative latex editor. In its free version it
has a very limited disk space. However it comes with a Rich text mode
that allows you to edit the document in a preview mode. The free templates
provided do not include ACM template, put you are allowed to use the
OSA template.

Features of overleaf are documented at: https://www.overleaf.com/benefits


   
The LaTeX Cycle
---------------

To create a PDF file from latex yo need to generate it following a
simple development and improvement cycle.

First, Create/edit ASCII source file with ``file.tex`` file:

::

    emacs file.tex 

Create/edit bibliography file:

::

    jabref refs.bib

Create the PDF:

::

    pdflatex file
    bibtex file 
    pdflatex file
    pdflatex file

View the PDF:

::

    open file

A great example is provided at:

* https://gitlab.com/cloudmesh/project-000/tree/master/report

It not only showcases you an example file in ACM 2 column format, but
also integrates with a bibliography. Furthermore, it provides a
sample Makefile that you can use to generate view and recompile, or
even autogenerate. A compilation would look like::

  make
  make view

If however you want to do things on change in the tex file you can do
this automatically simply with::

  make watch

.. note:: for make watch its best to use skim as pdf previewer



Generating Images
-----------------

To produce high quality images the programs PowerPoint and omnigraffle
on OSX are recommended. When using powerpoint please keep the image
ratio to 4x3 as they produce nice size graphics which you also can use in
your presentations. When using other rations they may not fit in
presentations and thus you may increase unnecessarily your work. We do
not recommend vizio as it is not universally available and produces
images that in case you have to present them in a slide presentation
does not easily reformat if you do not use 4x3 aspect ratio.

Naturally graphics should be provided in SVG or PDF format so they can
scale well when we look at the final PDF. Including PNG, gif, or jpeg
files often do not result in the necessary resolution or the files
become real big. For this reason we for example can also not recommend
tools such as tablaeu as they do not provide proper exports to high
quality publication formats. For interactive display such tool may be
good, but for publications it produces inferior formatted images.



Bibliographies
--------------

LaTeX integrates very well with bibtex. There are several preformatted
styles available. It includes also styles for ACM and IEEE
bibliographies. For the ACM style we recommend that you replace
abbrv.bst with abbrvurl.bst, add hyperref to your usepackages so you
can also display urls in your citations:

::

    \bibliographystyle{IEEEtran}
    \bibliography{references.bib}

Than you have to run latex and bibtex in the following order:

::

    latex  file
    bibtex file
    latex  file
    latex  file

or simply call `make` from our `makefile`.
    
The reason for the multiple execution of the latex program is to update
all cross-references correctly. In case you are not interested in
updating the library every time in the writing progress just postpone it
till the end. Missing citations are viewed as [?].

Two programs stand out when managing bibliographies: emacs and jabref:

*  http://www.jabref.org/

Other programs such as mendeley, Zotero, and even endnote integrate
with bibtex. However their support is limited, so we recommend that
you just use jabref. Furthermore its free and runs on all platforms.

   
jabref
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Jabref is a very simple to use bibliography manager for LaTeX and
other systems. It cand create a multitude of bibliography file formats
and allows upload in other online bibliography managers.

Video: https://youtu.be/cMtYOHCHZ3k

Video with cc: https://www.youtube.com/watch?v=QVbifcLgMic


jabref and MSWord
^^^^^^^^^^^^^^^^^

Accordung to others it is possible to integrate jabref
references directly into MSWord. This has been conducted so far
however only on a Windows computer.

.. note::

   We have not tried this ourselves, but give it as a potential
   option. 

Here are the steps the need to be done:

 
1. Create the Jabref bibliography just like in presented in the Jabref video
2. After finishing adding your sources in Jabref, click `File -> export`
3. Name your bibliography and choose MS Office 2007(*.xml) as the file
   format. Remember the location of where you saved your file.
4. Open up your word document.  If you are using the ACM template, go
   ahead and remove the template references listed under
   `Section 7. References`
5. In the MS Word ribbon choose 'References'
6. Choose 'Manage Sources'
7. Click 'Browse' and locate/select your Jabref xml file
8. You should now see your references appear in the left side window.
   Select the references you want to add to your document and click
   the 'copy' button to move them from the left side window to the
   right window.
9. Click the 'Close' button
10. In the MS Word Ribbon, select 'Bibliography' under the References
    tab
11. Click 'Insert Bibliography' and your references should appear in
    the document
12. Ensure references are of Style: IEEE.  Styles are located in the
    References tab under 'Manage Sources'
 
As you can see there is significant effort involve, so we do recommend you
use LaTeX as you can focus there on content rather than dealing with
complex layout decisions. This is especially true, if your papers has
figures or tables, or you need to add references.

Other Reference Managers
^^^^^^^^^^^^^^^^^^^^^^^^

Please note that you should first decide which reference manager you
like to use. In case you for example install zotero and mendeley, that
may not work with word or other programs.

	  
Endnote
~~~~~~~~

Endnote os a reference manager that works with Windows. Many people
use endnote. However, in the past endnote has lead to complications
when dealing with collaborative management of references. Its price is
considerable. We have lost many hours of work because endnote being in
some cases instable. As student you may be able to use endnote for
free at Indiana University.

* http://endnote.com/


Mendeley
~~~~~~~~~

Mendeley is a free reference manager compatible with Windows Word 2013,
Mac Word 2011, LibreOffice, BibTeX. Videos on how to use it are
available at:

* https://community.mendeley.com/guides/videos

Installation instructions are available at

https://www.mendeley.com/features/reference-manager/

When dealing with large databases we found Mendeleys integration into
word slow.

Zotero
~~~~~~

Zotero is a free tool to help you collect, organize, cite, and share
your research sources.  Documentation is available at

* https://www.zotero.org/support/

The download link is available from

* https://www.zotero.org/

We have limited experience with zotero


Slides
----------------------

Slides are best produced with the seminar package:

::

    \documentclass{seminar}

    \begin{slide}

        Hello World on slide 1

    \end{slide}

    The text between slides is ignored

    \begin{slide}

        Hello World on slide 2

    \end{slide}

However, in case you need to have a slide presentation we recommend
you use ppt. Just paste and copy content from your PDF or your LaTeX
source file into the ppt.

    
.. _sharelatex:




Links
-----

-  The `LaTeX Reference
   Manual <http://texdoc.net/texmf-dist/doc/latex/latex2e-help-texinfo/latex2e.pdf>`__
   provides a good introduction to Latex.

LaTeX is available on all modern computer systems. A very good
installation for OSX is available at:

-  https://tug.org/mactex/

However, if you have older versions on your systems you may have to
first completely uninstall them.

Tips
----

Including figures over two columns:

* http://tex.stackexchange.com/questions/30985/displaying-a-wide-figure-in-a-two-column-document

* positioning figures with \textwidth and \columnwidth
  https://www.sharelatex.com/learn/Positioning_images_and_tables

* An organization as author. Assume the author is National Institute
  of Health and want  to have the author show up, please do::
 
    key= {National Institute of Health},
    author= {{National Institute of Health}},
 
  Please note the {{ }}

* words containing 'fi' or 'ffi' showing blank places like below after recompiling it:
  find as  nd efficiency as e   ciency

  You copied from word or PDF ff which is actually not an ff, but a
  condensed character, change it to ff and ffi, you may find other
  such examples such as any non ASCII character. A degree is for
  example another common issue in data science.

* do not use | & and other latex characters in bibtex references,
  instead use , and the word and

* If you need to use _ it is \_ but if you use urls leave them as is

* We do recommend that you use sharelatex and jabref for writing
  papers. This is the easiest solution and beats in many cases MSWord
  as you can focus on writing and not on formatting.
