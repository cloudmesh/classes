.. _reports:

Report Format
=============

Although we provide **trivial** but detailed report format
requirements, we observed over the years that some students still
asked us can I make my report shorter, or can i use a different format?
The answer to these questions is **no**. Furthermore, we observed that
the same students than went ahead and played with the formating and
introduced empty lines, increased tables or figures, or worse modified the
fontsize to circumvent the page limit requirement.

Thus we have adopted a much simpler approach that is easy to summarize

1. We provide you with a **high quality** report template format that you
   must not change and is used by millions of researchers.
2. All references must be managed with jabref as reference management tool and
   must be provided in addition to the document.
3. If your document does not follow the format or we find that you
   have modified the style of the template we provide will return the document
   without review. 
4. It is in the students responsibility to use the template format
   from the beginning on. In fact, our assignments will use the
   template for all assignments and not just your term paper or term
   report. 

The template for the report is available from:

* https://github.com/cloudmesh/classes/tree/master/docs/source/format/report

Convenient compressed files are available at

* https://github.com/cloudmesh/classes/tree/master/docs/source/format/report.tar.gz
* https://github.com/cloudmesh/classes/tree/master/docs/source/format/report.zip


You have two choices. A good one and a bad one.

The good choice is to use the LaTeX template and write your document
in LaTeX. The bad one is to use the Word template and write the
document in Word. Both templates are included in our git repository.

.. warning: Over the years, we have not yet found **ANY** student that
   has written a better report in Word than students that use
   LaTeX. This is based on the fact that students useing LaTeX focus
   on writing content and students using Word focus on making their
   reports pretty and focus less on content. We also found that
   including images into papers in Word is inferior to the mechanisms
   that LaTeX provides.

Hence, it is in your best interest to use LaTeX. The good news is that
we have made it simple for you to use it. Furthermore, you are allowed to use
online services. An example report in PDF format is available:

* `report.pdf <https://github.com/cloudmesh/classes/blob/master/docs/source/format/report/latex/report.pdf>`_
  
We provide a very simple `Makefile
<https://github.com/cloudmesh/classes/blob/master/docs/source/format/report/latex/Makefile>`_
that allows you to do editing with immediate preview as documented in
the LaTeX lesson.  Due to LaTeX being a **trivial** ASCII based format
and having a superior bibliography management you will save yourself
many hours of work that you will face while fighting with Word. We got feedback from
those that tried it and they thanked us later.  Furthermore, in case
you are in a team, you can use either git while collaboratively
developing the LaTeX document, use sharelatex, or overleaf.

However, we allow you to use word under the following conditions:

1. You accept the risk that Word may crash and you may find yourself
   in last minute in the situation that you lost your work and your
   document is broken. We will not be sympathetic to this situation as
   we recommended that you use LaTeX.
2. You must use not only Endnote, but also jabref when managing your
   references, so you have to do the management of references
   twice. This is so that your document could be converted to LaTeX in
   case we think it suitable for publication in a conference or
   workshop.
3. You do not modify the theme.
4. All images and tables are placed at the end of the paper.
5. Git wil be used to submit all documents with regular updates.
   
For LaTeX you will encounter a much more smooth experience.

1. Your final document must be committed in git and as LaTeX is ASCII
   based you can do thous throughout the semester and have backups via
   git.
2. You will be using jabref to manage your bibliography and as LaTeX
   has build in support for bibliography management there is not much
   you need to pay attention to, all Format of the references is done
   for you in case you entered them correctly
3. You do not modify our theme.
4. All images and tables are placed at the end of the paper.   
5. Git wil be used to submit all documents.   
6. You are allowed to use sharelatex or overleave so you do not have
   to install LaTeX on your computer, but see 5. and the next paragraph.

Whatever format you use, your final submission must be in **the
class** git. We will not review any documents stored on sharelatex or
overleaf or in any git repository not belonging to the class. Your
final submission will include the bibliography file(s) as a separate
document(s). All images must be placed in an images folder and submitted
in your repository with the originals. When using sharelatex or
overleaf you must replicate the directory layout carefully from our
template and include your final documents in git with a Makefile that
can recreate the document. It is in your responsibility that this
works. We will regenerate the document from source before we grade
it. Thus it is not sufficient to just check in the final PDF. 
The report must be spell checked.

.. warning:: There will be **NO EXCEPTION** to this. We will not
             review your report if its submission is incomplete.

             
  
Report Checklist
----------------

This partiald list may serve as a way to check if you follow the rules

#. Have you written the report in the specified format?
#. Have you included an acknowledgement section?
#. Have you included the report in git?
#. Have you specified the HID, names, and e-mails of all team members in
   your report. E.g. the Real Names that are registered in Canvas?
#. Have you included the project number in the report?
#. Have you included all images in native and PDF format in git in
   the images folder?
#. Have you added the bibliography file that you managed with jabref
#. In case you used word have you also provided the endnote file
#. Have you added an appendix describing who did what in the project
   or report?
#. Have you spellchecked the paper?
#. Have you made sure you do not plagiarize?
#. Have you not used phrases such as shown in the Figure below, but
   instead used as shown in Figure 3 when referring to the 3rd
   figure?
#. Have you capitalized "Figure 3", "Table 1", ... ?
#. Any figure that is not referred to explicitly in the text must be
   removed.
#. Are the figure captions bellow the figures and not on top. (Do
   not include the titles of the figures in the figure itself but instead use the caption
   or that information?
#. When using tables have you put the table caption on top?
#. Make the figures large enough so we can read the details. If needed
   make the figure over two columns?
#. Do not worry about the figure placement if they are at a different
   location than you think. Figures are allowed to float. If you want
   you can place all figures at the end of the report?
#. Are all figures and tables at the end?
#. Do not use the word "I"?
#. Do not artificially inflate your report if you are bellow the page
   limit and have nothing to say anymore.
#. If your paper limit is 12 pages but you want to hand in 120 pages,
   please check first with an instructor ;-)
#. Check in your current work of the report on a weekly basis to show
   consistent progress.
#. Is in your report directory a README.rst file in it as shown in the
   example project that we introduced you to?

If you observe something missing let us know.

README.rst
----------

In the directory that containes the report, please include the
following README.rst file. Without this file we will not review your document::

   Title: The title of your paper (one line)

   Author: The author s of the paper (one line)

   HID: The HID of the authors in the order as specified in authors (one line)

   PID: The PID of the paper (there will be exactly one)

   E-mail: The e-mails of the authors in the order of the author list (one line)

   Format: latex or word (specify one)
   
Please note that all information has an empty line between them and
all information is stored in one line

This information is used to autogenerate the class proceedings.



Exercise
--------

Report.1:
  Install latex and jabref on your system

Report.2:
  Check out the report example directory. Create a PDF and view
  it. Modify and recompile.

Report.4:
  Learn about the different bibliographic entry formats in bibtex

Report.5:
  What is an article in a magazine? Is it really an Article or a Misc?

Report.6:
  What is an InProceedings and how does it differ from Conference?

Report.7:  
  What is a Misc?

Report.8:
  Why are spaces, underscores in directory names
  problematic and why should you avoid using them for your projects

Report.9:
  Write an objective report about the advantages and disadvantages of
  programs to write reports.

Report.10:
  Why is it advantageous that directories are lowercase have no
  underscore or space in the name?







		   
