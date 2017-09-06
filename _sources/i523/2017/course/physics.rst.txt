.. _S6:

Physics Case Study
------------------


This section starts by describing the LHC accelerator at CERN and
evidence found by the experiments suggesting existence of a Higgs
Boson. The huge number of authors on a paper, remarks on histograms
and Feynman diagrams is followed by an accelerator picture
gallery. The next unit is devoted to Python experiments looking at
histograms of Higgs Boson production with various forms of shape of
signal and various background and with various event totals. Then
random variables and some simple principles of statistics are
introduced with explanation as to why they are relevant to Physics
counting experiments. The unit introduces Gaussian (normal)
distributions and explains why they seen so often in natural
phenomena. Several Python illustrations are given. Random Numbers with
their Generators and Seeds lead to a discussion of Binomial and
Poisson Distribution. Monte-Carlo and accept-reject methods. The
Central Limit Theorem concludes discussion.


Looking for Higgs Particles, Bumps in Histograms, Experiments and Accelerators (Part 1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This unit is devoted to Python and Java experiments looking at
histograms of Higgs Boson production with various forms of shape of
signal and various background and with various event totals. The
lectures use Python but use of Java is described.

.. i523/public/videos/physics/lecture-8.pptx


* Slides: `PPT <https://drive.google.com/file/d/0B1Of61fJF7WsV3ZPNXlyWmhVeFE/view?usp=sharing>`_


Files: :download:`HiggsClassI-Sloping.py </files/python/physics/mr_higgs/higgs_classI_sloping.py>`

Looking for Higgs Particle and Counting Introduction
""""""""""""""""""""""""""""""""""""""""""""""""""""

We return to particle case with slides used in introduction and stress
that particles often manifested as bumps in histograms and those bumps
need to be large enough to stand out from background in a
statistically significant fashion.


* Video: https://drive.google.com/file/d/0B5plU-u0wqMoTDdKYUxPRHFFV3M/view?usp=sharing


We give a few details on one LHC experiment ATLAS. Experimental
physics papers have a staggering number of authors and quite big
budgets. Feynman diagrams describe processes in a fundamental
fashion.

*        Video: http://youtu.be/UAMzmOgjj7I


Physics-Informatics Looking for Higgs Particle Experiments
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

We give a few details on one LHC experiment ATLAS. Experimental
physics papers have a staggering number of authors and quite big
budgets. Feynman diagrams describe processes in a fundamental
fashion.

*        Video: http://youtu.be/BW12d780qT8


Accelerator Picture Gallery of Big Science
""""""""""""""""""""""""""""""""""""""""""

This lesson gives a small picture gallery of
accelerators. Accelerators, detection chambers and magnets in tunnels
and a large underground laboratory used fpr experiments where you need
to be shielded from background like cosmic rays.

*        Video: http://youtu.be/WLJIxWWMYi8


Resources
"""""""""

* http://grids.ucs.indiana.edu/ptliupages/publications/Where%20does%20all%20the%20data%20come%20from%20v7.pdf
* http://www.sciencedirect.com/science/article/pii/S037026931200857X
* http://www.nature.com/news/specials/lhc/interactive.html

.. comment::

        * http://www.interactions.org/cms/?pid=6002
        * http://www.interactions.org/cms/?pid=1032811
        * http://biologos.org/blog/what-is-the-higgs-boson
        * http://www.atlas.ch/pdf/ATLAS_fact_sheets.pdf

Looking for Higgs Particles: Python Event Counting for Signal and Background (Part 2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This unit is devoted to Python experiments looking at
histograms of Higgs Boson production with various forms of shape of
signal and various background and with various event totals.

.. adobe presnter source, found in box in folder ....
   
.. adobe presnter source, found in googledocs in folder ....

.. adobe presenter, no where found, ask sidd and wiggum
   

.. i523/public/videos/physics/lecture-9.pptx


* Slides: `PPT <https://drive.google.com/file/d/0B1Of61fJF7WsMURyUUYyUnJueGc/view?usp=sharing>`_

Files:

* :download:`HiggsClassI-Sloping.py </files/python/physics/mr_higgs/higgs_classI_sloping.py>`
* :download:`HiggsClassIII.py </files/python/physics/number_theory/higgs_classIII.py>`
* :download:`HiggsClassIIUniform.py </files/python/physics/mr_higgs/higgs_classII_uniform.py>`


Physics Use Case II 1: Class Software
"""""""""""""""""""""""""""""""""""""

We discuss how this unit uses Java and Python on both a backend server
(FutureGrid) or a local client. WE point out useful book on Python for
data analysis. This builds on technology training in Section 3.


 * Video: https://drive.google.com/file/d/0B1Of61fJF7WsMm12eG5HQVNHUms/view?usp=sharing
   

This video contains Java information, but we are no longer using Java in this class.



Physics Use Case II 2: Event Counting
"""""""""""""""""""""""""""""""""""""

We define ''event counting'' data collection environments. We discuss
the python and Java code to generate events according to a particular
scenario (the important idea of Monte Carlo data). Here a sloping
background plus either a Higgs particle generated similarly to LHC
observation or one observed with better resolution (smaller
measurement error).

*          Video: http://youtu.be/h8-szCeFugQ


Physics Use Case II 3: With Python examples of Signal plus Background
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This uses Monte Carlo data both to generate data like the experimental
observations and explore effect of changing amount of data and
changing measurement resolution for Higgs.

*          Video: http://youtu.be/bl2f0tAzLj4



Physics Use Case II 4: Change shape of background & num of Higgs Particles
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This lesson continues the examination of Monte Carlo data looking at
effect of change in number of Higgs particles produced and in change
in shape of background.

*          Video: http://youtu.be/bw3fd5cfQhk


Resources
"""""""""

* Python for Data Analysis: Agile Tools for Real World Data By Wes
  McKinney, Publisher: O'Reilly Media, Released: October 2012,
  Pages: 472.

* http://jwork.org/scavis/api/
* https://en.wikipedia.org/wiki/DataMelt


Looking for Higgs Particles: Random Variables, Physics and Normal Distributions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We introduce random variables and some simple principles of
statistics and explains why they are relevant to Physics counting
experiments. The unit introduces Gaussian (normal) distributions and
explains why they seen so often in natural phenomena. Several Python
illustrations are given. Java is currently not available in this
unit.


.. i523/public/videos/physics/lecture-10.pptx


* Slides: `PPT <https://drive.google.com/file/d/0B1Of61fJF7WsN1FIdTBOQUx3VFE/view?usp=sharing>`_

:download:`HiggsClassIII.py </files/python/physics/number_theory/higgs_classIII.py>`


Statistics Overview and Fundamental Idea: Random Variables
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

We go through the many different areas of statistics covered in the
Physics unit. We define the statistics concept of a random variable.



* Video: https://drive.google.com/file/d/0B1Of61fJF7WsV0VxQldFQzFuUTQ/view?usp=sharing


Physics and Random Variables
""""""""""""""""""""""""""""

We describe the DIKW pipeline for the analysis of this type of physics
experiment and go through details of analysis pipeline for the LHC
ATLAS experiment. We give examples of event displays showing the final
state particles seen in a few events. We illustrate how physicists
decide whats going on with a plot of expected Higgs production
experimental cross sections (probabilities) for signal and background.


* Video A: http://youtu.be/Tn3GBxgplxg


* Video B: http://youtu.be/qWEjp0OtvdA



Statistics of Events with Normal Distributions
""""""""""""""""""""""""""""""""""""""""""""""

We introduce Poisson and Binomial distributions and define independent
identically distributed (IID) random variables. We give the law of
large numbers defining the errors in counting and leading to Gaussian
distributions for many things. We demonstrate this in Python
experiments.

*          Video: http://youtu.be/LMBtpWOOQLo


Gaussian Distributions
""""""""""""""""""""""

We introduce the Gaussian distribution and give Python examples of the
fluctuations in counting Gaussian distributions.

*          Video: http://youtu.be/LWIbPa-P5W0



Using Statistics
""""""""""""""""

We discuss the significance of a standard deviation and role of biases
and insufficient statistics with a Python example in getting incorrect
answers.

*          Video: http://youtu.be/n4jlUrGwgic


Resources
"""""""""

* http://indico.cern.ch/event/20453/session/6/contribution/15?materialId=slides
* http://www.atlas.ch/photos/events.html
* https://cms.cern/

Looking for Higgs Particles: Random Numbers, Distributions and Central Limit Theorem (Part 3)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


We discuss Random Numbers with their Generators and Seeds. It
introduces Binomial and Poisson Distribution. Monte-Carlo and
accept-reject methods are discussed. The Central Limit Theorem and
Bayes law concludes discussion. Python and Java (for student - not
reviewed in class) examples and Physics applications are given.


.. i523/public/videos/physics/lecture-11.pptx

* Slides: `PPT <https://drive.google.com/file/d/0B1Of61fJF7WseU1ZWEVhR0FpR2M/view?usp=sharing>`_


Files:

* :download:`HiggsClassIII.py </files/python/physics/calculated_dice_roll/higgs_classIV_seeds.py>`

Generators and Seeds
""""""""""""""""""""

We define random numbers and describe how to generate them on the
computer giving Python examples. We define the seed used to define to
specify how to start generation.


* Video: https://drive.google.com/file/d/0B1Of61fJF7WsTEM0em1YYW83RnM/view?usp=sharing

*          Video: http://youtu.be/9QY5qkQj2Ag


Binomial Distribution
"""""""""""""""""""""

We define binomial distribution and give LHC data as an example of
where this distribution valid.

*          Video: http://youtu.be/DPd-eVI_twQ


Accept-Reject
"""""""""""""

We introduce an advanced method **accept/reject** for generating
random variables with arbitrary distributions.

*          Video: http://youtu.be/GfshkKMKCj8



Monte Carlo Method
""""""""""""""""""


We define Monte Carlo method which usually uses accept/reject method
in typical case for distribution.

*          Video: http://youtu.be/kIQ-BTyDfOQ




Poisson Distribution
""""""""""""""""""""

We extend the Binomial to the Poisson distribution and give a set of
amusing examples from Wikipedia.

*          Video: http://youtu.be/WFvgsVo-k4s



Central Limit Theorem
"""""""""""""""""""""

We introduce Central Limit Theorem and give examples from Wikipedia.

*          Video: http://youtu.be/ZO53iKlPn7c



Interpretation of Probability: Bayes v. Frequency
"""""""""""""""""""""""""""""""""""""""""""""""""

This lesson describes difference between Bayes and frequency views of
probability. Bayes's law of conditional probability is derived and
applied to Higgs example to enable information about Higgs from
multiple channels and multiple experiments to be accumulated.

*          Video: http://youtu.be/jzDkExAQI9M



Resources
"""""""""

* https://en.wikipedia.org/wiki/Pseudorandom_number_generator
* https://en.wikipedia.org/wiki/Mersenne_Twister
* https://en.wikipedia.org/wiki/Mersenne_prime
* CMS-PAS-HIG-12-041 Updated results on the new boson discovered in
  the search for the standard model Higgs boson in the ZZ to 4 leptons
  channel in pp collisions at sqrt(s) = 7 and 8 TeV
  http://cds.cern.ch/record/1494488?ln=en
* https://en.wikipedia.org/wiki/Poisson_distribution
* https://en.wikipedia.org/wiki/Central_limit_theorem
* http://jwork.org/scavis/api/
* https://en.wikipedia.org/wiki/DataMelt
