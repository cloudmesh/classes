What is the entry for a book
============================

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
