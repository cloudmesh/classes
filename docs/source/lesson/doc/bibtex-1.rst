What is the entry for a Blog
============================

I like to issue an open discussion on what the entry for 
 
http://dataconomy.com/2014/08/google-cloud-dataflow/
 
looks like. Please, work on the answer in the discussion and summarize the result in the student answer. Provide a reasoning for that entry.

A Misc entry has the following fields -
 
@Misc{label,
  OPTkey =            {},
  OPTauthor =     {},
  OPTtitle =           {},
  OPThowpublished = {},
  OPTmonth =     {},
  OPTyear =          {},
  OPTnote =          {},
  OPTannote =     {},
  url = {},
  owner = {}
}
 
To start with we go to the blog URL. From the blog we get the details for author, title, month, year,publisher and URL. The howpublished field we add blog, since it is a blog post.

@Misc{www-google-cloud-dataflow,
author = {Eileen McNulty},
title = {Understanding Big Data: What is Google Cloud Dataflow?},
publisher = {Dataconomy.com},
month = aug,
year = {2014},
howpublished = {Blog},
url = {http://dataconomy.com/2014/08/google-cloud-dataflow},
key = {Dataconomy},
owner = {S17-IR-2006 S17-IR-2026 S17-IR-2035},
note = {Accessed: 13-Feb-2017}
}
 
Misc: Misc type is used when nothing else fits the type of entry. For a Misc entry we have do not have any required fields
Optional fields: author, title, howpublished, month, year, note.
Since this is blog we use the misc entry. Online entry type is also available but in order to maintain compatibility with older formats we choose the Misc.
 
Key:
When the author and editor information is missing we use the key field for alphabetizing, cross-referencing, and creating a label. One should not confuse the key with the label that appears in the \cite command and at the beginning of the database entry. 
key = {organisation}
 
Label:  The label field is should contain 3 letters from[auth] an author name, short year and the short name of the publication to provide maximum information regarding the publication. Underscores need to be replaced by dashes or removed. Here since this is an online reference we use www- since it allows us to quickly search through a paper that we write and identifying online references, to judge if we should replace them with articles in journals or proceedings.
 
Author:   This field should include all the authors for your entry. Author names should be separated using “and”. We can write the author names in two forms as below –
Example 1: Type 1 -- Donald E. Knuth
        Type 2 -- Knuth, Donald E.
Example 2: Type 1 -- Eddie van Halen
        Type 2 -- van Halen, Eddie
The second type should be used for authors with more than two names to differentiate between middle name and last names.
  
Title: This is the title of the work. The capitalization depends on the bibliography style and the language used. For words that have to be capitalized (such as a proper noun), enclose the word (or its first letter) in braces.
 
Howpublished: Since the source is a blog, the howpublished field shall hold the value {Blog} rather than a web page. If the url specified was a normal webpage, the {Web Page} entry would be valid.
 
Month: It's best to use the three-letter abbreviations for the month, rather than spelling out the month yourself. This lets the bibliography style be consistent, since month in not capitalized in some languages. And if you want to include information for the day of the month, the month field is usually the best place. Example: month = aug # "~10,"  
 
Owner: the HID mapping each student and their technologies
