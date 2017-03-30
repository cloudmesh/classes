Improving Your Technology Papers
================================

Below, you will find some examples of some more common issues we found
with your submissions for paper 1. These are simply examples that
demonstrate a larger theme we've seen. You've you see your own writing
here, this doesn't mean you did better or worse than your peers.

As you consider the examples shown here, please take a few moments to
think for yourself about how they can be improved before reading our
notes on them.

Abstracts
---------

Let's start with an example of an abstract:

  This paper gives an overview of Apache Lucene. We will go through
  the basic architecture and functionality of the library. We will see
  the advantages and downfalls of Lucene and conclude on its
  implementation.

How can it be improved?

The abstract is the part of the paper that the most people will read,
and will often use to determine whether to read the rest of the
paper. Thus, the abstract should give a basic idea of what the
technology is about. This of it as an elevator pitch for that
technology. How can you most succinctly summarize what is important
about the technology?

The above example's main issue is that it is `about the paper`, not
`about the technology`. Anyone reading it would have not idea what
Apache Lucene is. This is why during lectures and office hours we
emphasize that you should avoid phrases like `This paper...` or `In
this paper, we...`. You need to focus on the technology and what is
most important about it, not the paper itself. Here is an example that
accomplishes this:

  RabbitMQ provides simple yet powerful messaging platform which
  allows applications pass messages in a reliable and fault tolerant
  way. RabbitMQ implements Advanced Message Queuing Protocol (AMQP)
  and is written in Erlang programming language. It runs on all major
  operating systems and supports SDK in all major programming
  languages[1] including objective-C, swift and node.js. When we look
  for messaging, we look for certain features: asynchronous messaging,
  large scale, reliability, clustering, multi-protocol, highly
  available, fault tolerant. RabbitMQ[2] fulfills these requirements
  and provides a distributed, persistent, highly available, fault
  tolerant messaging system which can scale as data grows.

This is a better abstract, but it can be improved as well. How?

The Good
~~~~~~~~

The good thing about this abstract is it gets to the main point right
away and gives a good idea about what RabbitMQ is and why readers
should care about it.

Neutral
~~~~~~~

The abstract is on the long site, but it is still reasonable. The
first abstract about Apache Lucene we saw was too short. While there
isn't a hard rule about length and you might be able to summarize your
technology in three sentences, most of the time you will need a little
more. However, you still need to keep everything succinct and focused
on the most important aspects of the technology.

Can improve
~~~~~~~~~~~

There are a couple things the RabbitMQ abstract can improve. First,
the references in it are not necessary. In general, citations in an
abstract are OK (though not all journals/conference proceedings allow
them), but they need to be reserved for something very specific and
crucial to the statements being made in the abstract. In this case, we
have two references that are quite general and are better included in
the main body of the paper.

In addition, there are some minor reference formatting and grammar
issues that we would have highlighted. We highlight grammar, term,
spelling and citation issues briefly, so if you need further details
from your graded about what they meant, don't hesitate to contact
them. You can either send a message to `Instructors` on Piazza, or
open a ticket under the `sp17-i524` repository where you can initiate
a discussion with your grader.

References
----------

Now, let's look at some common mistakes when putting references in
your papers.

`As noted in...`, `According to...` and similar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How can we improve this reference?

  As noted in [1], the current RDBMS systems were architected more
  than 25 years ago, when hardware characteristics were much different
  than today.

As discussed earlier, your paper should focus on the technology rather
than making direct statement about your paper, other papers, or the
people who wrote them. The above sentences can be rewritten as follows
to improve the flow of the paper:

  Current RDBMS systems were architected more than 25 years ago when
  hardware characteristics were much different than today [1].

Positioning of references
~~~~~~~~~~~~~~~~~~~~~~~~~

How can we improve this reference?

  [4]At high level, producer publishes the message to the
  broker. Consumer consumes...

We've made these points during lectures, office hours and on Piazza, but to summarize:

References should...

* go after the statement that refers to them.
* go before any punctuation.
* have a space between them and other text.
  
Thus, it's better to rewrite the above as:

  In general, a producer publishes the message to the broker [4]. The
  consumer consumes...

You need to add citations for figures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now let's look at the following references in the caption of a figure.

  Fig. 1. CoreOS container layout. [1]

According to the guidelines given earlier, the reference should be
positioned before the period:

  Fig. 1. CoreOS container layout [1].

But this reference does something well that is worth mentioning: If you include a figure in your paper that you did not create yourself, you need to add a reference to the original source for the figure.

Referring to figures
~~~~~~~~~~~~~~~~~~~~

What can be improved about this reference?

  Network File System throughput was done using iozone and results are
  shown in Figure 2:

There are a couple things to note here. If this was the LaTeX source,
the figure number should not have been hard-coded. You should always
use `... are shown in Figure~\ref{fig:arch}.` or something similar
rather than `... are shown in Figure 2.`

In addition, the colon `:` implies that there is an expectation the
figure will appear right underneath the statement that refers to
it. This is not always the case.  Some journals and conferences have
formats that put all figures at the end. In addition, LaTeX has some
limitations for positioning figures, which means you are not always
guaranteed where the figure will appear on the page. Thus, don’t use
colons like this, but simply refer to the figure without assuming
where it will appear on the page:

  Network File System throughput was done using iozone and results are
  shown in Figure 2.

When references are needed
~~~~~~~~~~~~~~~~~~~~~~~~~~

Take a look at this sentence and think about what can be improved
about it:

  Tree Architecture has enable Dremel to dispatch queries and collect
  results across tens of thousands of machines in a matter of seconds
  by using the Tree architecture.

There are some grammar issues, but more importantly this is a specific
quantitative claim. How do we know it’s true? It needs a reference!
(unless it was previously discussed in the paper, of course)

Other Areas of Improvement
--------------------------

Clarity
~~~~~~~

How can the clarity of this introduction be improved

  H-Store is a parallel, row-storage relational DBMS that runs on a
  cluster of shared-nothing, main memory executor nodes.

  A single H-Store instance is a cluster of two or more computational
  nodes deployed within the same domain…”

In general, you should assume that your audience that your audience
has basic grounding in Computer Science, but won't be familiar with
the specific technology, or the relevant subfield of CS, or
distributed systems.

In the example above, there are some keywords that can serve to
confuse rather than help understanding: `row-storage`,
`shared-nothing`, `executor nodes` Ask yourself, if the reader is not
already familiar with this area/topic, would they understand your
paper?  An example like this can be OK, if the relevant terms are
explained shortly after being introduced, but in this case they
weren't.

Scope
~~~~~

Take a look at this `Use Cases` section about H-Store. What could you
improve about it?

  Big Data is data at rest. Big Data describes data’s volume –
  petabytes to exabytes - and variety: structured, semi-structured and
  unstructured data that has the potential to be analyzed for
  information. Big Data systems facilitate the exploration and
  analysis of stored, large data sets. Big data is often created by
  data that is generated at incredible speeds, such as click-stream
  data, financial ticker data, log aggregation, or sensor data. Often
  these events occur thousands to tens of thousands of times per
  second. The benefits of big data are lost if fresh, fast-moving data
  from real time sources is dumped into HDFS, an analytic RDBMS, or
  even flat files, because the ability to act or alert right now, as
  things are happening, is lost.

  So this data stream which is the source for big data is called Fast
  Data. For Fast Data...

The problem here is with scope. These paragraphs don't describe or
discuss use cases, so their inclusion in this section is not
appropriate. More generally, however, this kind of description of `Big
Data` and `Fast Data` is not appropriate for a paper where you need to
focus more narrowly on one technology.

When you write and need to decide if something you wrote is in scope,
keep the following in mind:

* You have little space to give an overview of your technology, so use
  it wisely.
* Any background information should be there to illuminate a
  particular aspect of the technology, and should be introduced
  succinctly.
* You should still provide plenty of context to help understanding,
  just do it with good reason and succinctly.
* As mentioned earlier, put yourself in the shoes of a rigorous reader
  with some background in CS, but no expertise in the technology you
  are writing about or that subfield.

Voice
~~~~~

Next, what do you think can be improved with this paragraph?

  Although query and process large volume of data in any system is a
  challenging task, especially in the big data ecosystem due to vast
  expense of option available, Dremel has been standing out as the
  right model for process and storing data with a lot of benefits as
  well as fitting as part of an entire big data stack which can be
  used against raw data, like log data.

Phrases like `Dremel has been standing out as the right model for ...`
and `with a lot of benefits` are subjective or unspecific and are more
appropriate for an advertisement or a press release, but not a neutral
paper. The goal of your paper is to inform and give context, rather
than make big pronouncements about the technology and should be
written in a neutral voice and make specific, verifiable claims.

For a similar example, see this paragraph and think about how you
could rewrite it.

  Dremel can even execute a complex regular expression text matching
  on a huge logging table that consists of about 35 billion rows and
  20 TB, in merely tens of seconds. This is the power of Dremel; it
  has super high scalability and most of the time it returns results
  within seconds or tens of seconds no matter how big the queried
  dataset is. Why Dremel can be as drastically fast as the examples
  show?

Here, the first sentence is a specific quantitative claim and as
mentioned earlier when discussing citations, it needs to be backed up
by a reference. In addition, words and phrases like `merely`, `this is
the power of Dremel`, `super high scalability`, `drastically fast` are
subjective or not specific enough and should be avoided.

Conclusion
----------

There are only some of the common issues we have seen in your papers,
but please keep them in mind as you do your revisions for papers 1
and 2. If you don't understand any of your feedback, please work with
your grader by either contacting them on Piazza, or opening an issue
on the `sp17-i524` repository and assigning it to your grader. We
imagine that most of you will have questions, so don't hesitate to
reach out.

Last, but not least important, keep in mind that all the feedback you
receive should be viewed as an opportunity to improve your writing
and achieve your best in the class!
