.. _S12:

Web Search and Text Mining
--------------------------

This section starts with an overview of data mining and puts our study
of classification, clustering and exploration methods in context. We
examine the problem to be solved in web and text search and note the
relevance of history with libraries, catalogs and concordances. An
overview of web search is given describing the continued evolution of
search engines and the relation to the field of Information
Retrieval. The importance of recall, precision and diversity is
discussed. The important Bag of Words model is introduced and both
Boolean queries and the more general fuzzy indices. The important
vector space model and revisiting the Cosine Similarity as a distance
in this bag follows. The basic TF-IDF approach is dis
cussed. Relevance is discussed with a probabilistic model while the
distinction between Bayesian and frequency views of probability
distribution completes this unit.

We start with an overview of the different steps (data
analytics) in web search and then goes key steps in detail starting
with document preparation. An inverted index is described and then how
it is prepared for web search. The Boolean and Vector Space approach
to query processing follow. This is followed by Link Structure
Analysis including Hubs, Authorities and PageRank. The application of
PageRank ideas as reputation outside web search is covered. The web
graph structure, crawling it and issues in web advertising and search
follow. The use of clustering and topic models completes section




Web Search and Text Mining I
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


The unit starts with the web with its size, shape (coming from the
mutual linkage of pages by URL's) and universal power laws for number
of pages with particular number of URL's linking out or in to
page. Information retrieval is introduced and compared to web
search. A comparison is given between semantic searches as in
databases and the full text search that is base of Web search. The
origin of web search in libraries, catalogs and concordances is
summarized. DIKW -- Data Information Knowledge Wisdom -- model for web
search is discussed. Then features of documents, collections and the
important Bag of Words representation. Queries are presented in
context of an Information Retrieval architecture. The method of
judging quality of results including recall, precision and diversity
is described. A time line for evolution of search engines is given.

Boolean and Vector Space models for query including the cosine
similarity are introduced. Web Crawlers are discussed and then the
steps needed to analyze data from Web and produce a set of
terms. Building and accessing an inverted index is followed by the
importance of term specificity and how it is captured in TF-IDF. We
note how frequencies are converted into belief and relevance.

.. i523/public/videos/web/lecture-26.pptx

* Slides: `PPT <https://drive.google.com/file/d/0B1Of61fJF7WseW5oNW5KY0g5dEk/view?usp=sharing>`_



Web and Document/Text Search: The Problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This lesson starts with the web with its size, shape (coming from the
mutual linkage of pages by URL's) and universal power laws for number
of pages with particular number of URL's linking out or in to page.


          
* Video:https://drive.google.com/file/d/0B1Of61fJF7WscTdYUUVHNW9uRUU/view?usp=sharing



Information Retrieval leading to Web Search
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Information retrieval is introduced A comparison is given between
semantic searches as in databases and the full text search that is
base of Web search. The ACM classification illustrates potential
complexity of ontologies. Some differences between web search and
information retrieval are given.

          
* Video: https://youtu.be/KtWhk2cdRa4


History behind Web Search
^^^^^^^^^^^^^^^^^^^^^^^^^

The origin of web search in libraries, catalogs and concordances is
summarized.

* Video: https://youtu.be/J7D61uH5gVM



Key Fundamental Principles behind Web Search
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This lesson describes the DIKW -- Data Information Knowledge Wisdom --
model for web search. Then it discusses documents, collections and the
important Bag of Words representation.
         
* Video: https://youtu.be/yPFi6xFnDHE


Information Retrieval (Web Search) Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


This describes queries in context of an Information Retrieval
architecture. The method of judging quality of results including
recall, precision and diversity is described.

* Video: https://youtu.be/EGsnonXgb3Y


Search Engines
^^^^^^^^^^^^^^

This short lesson describes a time line for evolution of search
engines. The first web search approaches were directly built on
Information retrieval but in 1998 the field was changed when Google
was founded and showed the importance of URL structure as exemplified
by PageRank.

* Video: https://youtu.be/kBV-99N6f7k


Boolean and Vector Space Models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This lesson describes the Boolean and Vector Space models for query
including the cosine similarity.

* Video: https://youtu.be/JzGBA0OhsIk



Web crawling and Document Preparation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This describes a Web Crawler and then the steps needed to analyze data
from Web and produce a set of terms.

          
* Video: https://youtu.be/Wv-r-PJ9lro


          
Indices
^^^^^^^

This lesson describes both building and accessing an inverted
index. It describes how phrases are treated and gives details of query
structure from some early logs.

* Video: https://youtu.be/NY2SmrHoBVM


TF-IDF and Probabilistic Models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It describes the importance of term specificity and how it is captured
in TF-IDF. It notes how frequencies are converted into belief and
relevance.

* Video: https://youtu.be/9P_HUmpselU



Resources
^^^^^^^^^

* http://saedsayad.com/data_mining_map.htm
* http://webcourse.cs.technion.ac.il/236621/Winter2011-2012/en/ho_Lectures.html

* The Web Graph: an Overview Jean-Loup Guillaume and Matthieu Latapy
  https://hal.archives-ouvertes.fr/file/index/docid/54458/filename/webgraph.pdf
* Constructing a reliable Web graph with information on browsing behavior, Yiqun Liu, Yufei Xue, Danqing Xu, Rongwei Cen, Min Zhang, Shaoping Ma, Liyun Ru
  http://www.sciencedirect.com/science/article/pii/S0167923612001844

* http://www.ifis.cs.tu-bs.de/teaching/ss-11/irws

Web Search and Text Mining II
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



We start with an overview of the different steps (data analytics) in
web search. This is followed by Link Structure Analysis including
Hubs, Authorities and PageRank. The application of PageRank ideas as
reputation outside web search is covered. Issues in web advertising
and search follow. his leads to emerging field of computational
advertising. The use of clustering and topic models completes unit
with Google News as an example.


.. i523/public/videos/web/lecture-27.pptx

* Slides: `PPT <https://drive.google.com/file/d/0B1Of61fJF7WsaW44NnU5YXptUkU/view?usp=sharing>`_


Data Analytics for Web Search
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This short lesson describes the different steps needed in web search
including: Get the digital data (from web or from scanning); Crawl
web; Preprocess data to get searchable things (words, positions); Form
Inverted Index mapping words to documents; Rank relevance of documents
with potentially sophisticated techniques; and integrate technology to
support advertising and ways to allow or stop pages artificially
enhancing relevance.

          
* Video: https://drive.google.com/file/d/0B1Of61fJF7WsNEJxbWVRQ2lnc1U/view?usp=sharing


Link Structure Analysis including PageRank
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The value of links and the concepts of Hubs and Authorities are
discussed. This leads to definition of PageRank with
examples. Extensions of PageRank viewed as a reputation are discussed
with journal rankings and university department rankings as
examples. There are many extension of these ideas which are not
discussed here although topic models are covered briefly in a later
lesson.



* Video: https://drive.google.com/file/d/0B1Of61fJF7WseFFsUk9ZNXRURGM/view?usp=sharing
          



Web Advertising and Search
^^^^^^^^^^^^^^^^^^^^^^^^^^

Internet and mobile advertising is growing fast and can be
personalized more than for traditional media. There are several
advertising types Sponsored search, Contextual ads, Display ads and
different models: Cost per viewing, cost per clicking and cost per
action. This leads to emerging field of computational advertising.

          
* Video:https://drive.google.com/file/d/0B1Of61fJF7WsbjZMNDlvemNZNUk/view?usp=sharing



Clustering and Topic Models
^^^^^^^^^^^^^^^^^^^^^^^^^^^

We discuss briefly approaches to defining groups of documents. We
illustrate this for Google News and give an example that this can give
different answers from word-based analyses. We mention some work at
Indiana University on a Latent Semantic Indexing model.

          
* Video: https://youtu.be/95cHMyZ-TUs


Resources
^^^^^^^^^

* http://www.ifis.cs.tu-bs.de/teaching/ss-11/irws
* https://en.wikipedia.org/wiki/PageRank
* http://webcourse.cs.technion.ac.il/236621/Winter2011-2012/en/ho_Lectures.html
* Meeker/Wu May 29 2013 Internet Trends D11 Conference http://www.slideshare.net/kleinerperkins/kpcb-internet-trends-2013
