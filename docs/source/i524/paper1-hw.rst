.. _paper1-hw:

Paper 1 Homework
=================================

In this homework you will write a short paper on one of the
technologies that was assigned to you in the :ref:`TechList homework
<techs-exercise>`. In the process, you will learn how to write a basic
`LaTeX <https://www.latex-project.org/>`_ document. LaTeX is a
document type setting environment used for writing scientific papers in
many fields, and it is what we will use to write all papers in the
class. Even if you are not planning to work in academia, LaTeX is a
very powerful tool and can be useful for typesetting other types of
documents, such as magazine articles, CVs, resumes, books and so on.

To complete the homework you will need to do the following.

1. Pick a technology you're interested in from the ones assigned to
   you. You can check your assignments in `this Piazza thread
   <https://piazza.com/class/ix39m27czn5uw?cid=31>`_ (and if you don't
   remember it, `find your HID in this thread
   <https://piazza.com/class/ix39m27czn5uw?cid=33>`_).

2. Decide on a LaTeX implementation you will use. Depending on the
   environment you want to work in (Windows, OSX, Linux, online) you
   will use a different LaTeX implementation. You can find more
   information about existing implementations here:
   https://www.latex-project.org/get/. We discuss the choice of LaTeX
   environment a little more below.

3. Fork the homework repository, which can be found at
   https://github.com/cloudmesh/sp17-i524. The forking process is the
   same as the one described in the video for the TechList homework
   and in the `README in the class repo
   <https://github.com/cloudmesh/classes>`_: You will need to clone
   your fork, add the upstream remote, and make sure you keep your
   fork synchronized with the upstream.

4. Follow the `instructions on using the paper template
   <https://github.com/cloudmesh/sp17-i524/tree/master/paper_template>`_:
   You will need to create a folder named after your HID in the
   *paper1* folder of the repository and copy the provided paper
   template there.

5. Write your paper committing changes as you write.

6. Push the final version of your paper to your fork.

7. Generate a pull request to merge your submission in the upstream
   like you did in the first assignment.

Choosing a LaTeX Environment
----------------------------------

You will either want to choose a LaTeX implementation for your OS, or
one available online. The advantage of installing a LaTeX environment
on your system is that you will be able to use the *Makefile* provided
with the paper template to easily compile your LaTeX document. In an
online LaTeX environment, you will need to copy the files from the
template to it, and use whatever mechanism the environment provides
for compiling.

A locally installed LaTeX environment also gives you more control to
install packages. This is a more advanced use case, but it is
something to keep in mind, if you plan to use LaTeX beyond this class.

We can recommend and support `TeXLive <http://www.tug.org/texlive>`_
for Linux, `MacTeX <http://www.tug.org/mactex/>`_ for OSX, `TexLive
<http://www.tug.org/texlive>`_ for Windows and `ShareLaTeX
<https://www.sharelatex.com/>`_ online.

Writing the Paper
--------------
For the actual content of the paper, you need to write a two page
overview of one of the technologies assigned to you in the TechList
assignment. Your intended audience should be someone who might not
have specific technical background in the area of the technology, but
who is a rigorous thinker and whose problem domain might benefit from
it. Thus, the paper should provide context about the technology such
as:

* Summarize the technology briefly
* What kind of problems has it been applied to successfully?
* What kind of infrastructure does it need?
* How does this technology relate to big data?
* What major big data projects have used this technology?
* If I were to be new to the technology, what resources exist to learn
  about it?
* What is the status and popularity of the tool?  Provide evidence, do
  not copy *advertisement* terms from the project..
* What other things are important that you came across? 
* What are alternatives and how does the technology compare to them in
  terms of features, support, performance, etc.
* Make sure you have sufficient references (You need at least one, but
  as you may point to projects using the technology and learning
  material you probably have more, determine the most important once).

Document Structure
^^^^^^^^^^^^^^^^^^
Your paper should have an introduction and a conclusion, and use
sections in the middle portion as needed to be easy to understand.

Writing Style
^^^^^^^^^^^^
Treat this as a scientific paper, so you should aim to inform and give
a well-rounded overview of the subject matter. Do not use superlatives
or adjectives that are more appropriate for an advertisement, such as
*very*, *best*, *cutting-edge*, etc.

In addition, non-trivial statements of fact or quantitative statements
should be supported by other parts of your paper or by citations. For
example, if you are asserting that tech A has more features than tech
B, you can support this by including a table of features that you
create or citing a paper that compared these technologies.

For your citations, use the original source of a finding whenever
possible. That is, if paper A states something and cites paper B as a
source, and paper B cites paper C for the same claim, you need to look
at paper C to make sure the claim is accurate and cite that paper.

  
Submission
----------
Submission of this assignment will be in Github as outlined
above. Please, start early and raise any questions about the above
process on Piazza and in the online office hours. Depending on how
students are doing and what issues they are encountering, we will
provide further resources to help you be successful in this
assignment.
