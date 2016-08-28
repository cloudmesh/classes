LaTeX
=====

.. _sharelatex:

Sharelatex
----------------------------------------------------------------------

Those that like to use latex, but do not have it installed on their
computers may want to look at the following video: 

Video: https://youtu.be/PfhSOjuQk8Y

Video with cc: https://www.youtube.com/watch?v=8IDCGTFXoBs

Overleaf
----------------------------------------------------------------------

Overleaf.com is a collaborative latex editor. In its free version it
has a very limited disk space. However it comes with a Rich text mode
that allows you to edit the document in a preview mode. The free templates
provided do not include ACM template, put you are allowed to use the
OSA template.

Features of overleaf are documented at: https://www.overleaf.com/benefits


jabref
----------------------------------------------------------------------

Jabref is a very simple to use bibliography manager for LaTeX and
other systems. It cand create a multitude of bibliography file formats
and allows upload in other online bibliography managers.

Video: https://youtu.be/cMtYOHCHZ3k

Video with cc: TBD


References
----------

-  The `LaTeX Reference
   Manual <http://texdoc.net/texmf-dist/doc/latex/latex2e-help-texinfo/latex2e.pdf>`__
   provides a good intriduction to Latex.

LaTeX is available on all modern computer systems. A very good
instalation for OSX is available at:

-  https://tug.org/mactex/

However, if you have older versions on your systems you may have to
first completely uninstall them.

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
information in the LaTeX refrence manual.

Manual pages and programs
-------------------------

Following programs are useful for using LaTeX. To most of them you will
find also manual pages:

-  pdflatex: the latex program producing pdf
-  bibtex: to create bibliographies
-  jabref: less fancy GUI to bibtex files

The LaTeX Cycle
---------------

Create/edit ASCII source file with ``file.tex`` file:

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

On OSX the best PDF viewer for LaTeX is skim:

-  http://skim-app.sourceforge.net/

Generating Images
-----------------

To produce high quality images the programs PowerPoint and omnigraffle
on OSX are recommended. When using powerpoint please keep the image
ratio to 4x3 as they produce nice sze graphics whoch you also can use in
your presentations. When using other rations they may not fit in
presentations and thus you may increase unnecessarily your work. We do
not recommend vizio as it is not universally available.

Editing LaTeX
-------------

The text editor emacs provides a good basis for editing TeX and LaTex
documents. Both modes are supported. In addition there exists a color
highlight module enableling the color display of LaTeX and TeX commands.
On OSX aquaemacs and carbon emacs have build in support for LaTeX. Spell
checking is done with flyspell in emacs.

Other editors such as TeXshop are available which provide a more
integrated experience.

However when using skim in conjunction with imacs and latexmk your PDF
view will be automatically updated once you save the file in emacs. This
provides a very good quasy WYSIWYG environment.

LyX
~~~

I have made very good experiences with Lyx, however it is not widespread
and you must assure that the team you work with uses it consistently and
that you all use the same version.

Using the ACM templates

http://jack-kelly.com/getting_latex_and_lyx_to_use_acm_sig_class_file
\*\ https://wiki.lyx.org/Examples/AcmSiggraph

How to edit Bibliographies?
---------------------------

It is a waste of your time to edit bibliographies with the bibitem
environment. There are several preformated styles available. It includes
also styles for ACM and IEEE bibliographies. For the ACM style we
recommend that you replace abbrv.bst with abbrvurl.bst, add hyperref to
your usepackages so you can also display urls in your citations:

::

    \bibliographystyle{abbrvurl}
    \bibliography{references.bib}

Than you have to run latex and bibtex in the following order:

::

    latex  file
    bibtex file
    latex  file
    latex  file

The reason for the multiple execution of the latex program is to update
all cross-references correctly. In case you are not interested in
updating the library every time in the writing progress just postpone it
till the end. Missing citations are viewed as [?].

Two programs stand out when manageing bibliographies: emacs and jabref:

-  http://www.jabref.org/

How to produce Slides?
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
