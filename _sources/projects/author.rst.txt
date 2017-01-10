.. _authordisambiguity_b:

Author Disambiguty Problem
========================================

Deployment
----------

Setup a virtual cluster with a NoSQL distributed database. Create
ansible scripts for the deployment and management of the database
while resuing cloudmesh. Develop new commandline tools with the help
of docopts while integrting them into cloudmesh either as pulgin or
simply as standalone command with `cm-*` as commandname.


Analysis
--------

Given millions of publications how do we identify if an author of
paper a with the name Will Smith is the sam as the author of paper 2
with the name Will Smith, or William Smith, or W. Smith. AUthor
databases are either provided in bibtex format, or a database that can
not be shared outside of this class. You may have to add additional
information from IEEE explorer, rsearch gate, ISI, or other online
databases.

Identify further issues and discuss solutions to them. Example, an
author name changes, the author changes the institution.

Do a comprehensive literature review

Some ideas:

* Develop a graph view application in JS that showcases dependencies
  between coauthors, institutions

* Derive probabilities for the publications written by an auther given
  they are the same
* Utilize dependency graphs as given by online databases
* Utilize the and or topic/abstarct/full text to identify similarity
* Utilize keywords in the title
* Utilize refernces of the paper
* Prepare some vizualization of your result
* Prepare som interactive vizualization
* A possible good start is a previous project published at

* https://github.com/scienceimpact/bibliometric

There are also some screenshots available:

* https://github.com/scienceimpact/bibliometric/blob/master/Project%20Screenshots/Relationship_Authors_Publications.PNG

* https://github.com/scienceimpact/bibliometric/blob/master/Project%20Screenshots/Relationship_Authors_Publications2_Clusters.PNG

.. image:: /images/author_relation.png
  
